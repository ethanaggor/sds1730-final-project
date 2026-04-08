#!/usr/bin/env python3
"""GEPA prompt optimization for crash predictor using Gemini + RLM."""

import json
import os
import shutil
import sys
import threading
import time
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import dspy
import numpy as np
from dotenv import load_dotenv
from gepa.strategies.instruction_proposal import InstructionProposalSignature

from data_utils import build_dataset, make_examples
from local_interpreter import LocalInterpreter
from metric import crash_metric, set_event_log
from signatures import CrashPredictorBase

load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

TRACES_DIR = Path("traces")

STUDENT_MODEL = "gemini/gemini-3-flash-preview"
TEACHER_MODEL = "gemini/gemini-3.1-pro-preview"
SUB_MODEL = "gemini/gemini-3-flash-preview"


def _lm_stats(lm):
    inp = out = cached = 0
    cost = 0.0
    for h in lm.history:
        u = h.get("usage", {})
        inp += u.get("prompt_tokens", 0) if isinstance(u, dict) else getattr(u, "prompt_tokens", 0) or 0
        out += u.get("completion_tokens", 0) if isinstance(u, dict) else getattr(u, "completion_tokens", 0) or 0
        det = getattr(u, "prompt_tokens_details", None) if not isinstance(u, dict) else None
        cached += getattr(det, "cached_tokens", 0) if det else 0
        cost += h.get("cost") or 0.0
    return {"input_tokens": inp, "output_tokens": out, "cached_tokens": cached, "cost_usd": round(cost, 4), "calls": len(lm.history)}


class StatsEmitter:
    """Background thread that periodically emits LM usage stats to the event log."""

    def __init__(self, event_log, student_lm, teacher_lm, sub_lm, interval=10):
        self._event_log = event_log
        self._lms = {"student": student_lm, "teacher": teacher_lm, "sub": sub_lm}
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._run, args=(interval,), daemon=True)

    def start(self):
        self._thread.start()

    def stop(self):
        self._stop.set()
        self._thread.join(timeout=2)

    def _run(self, interval):
        while not self._stop.wait(interval):
            stats = {role: _lm_stats(lm) for role, lm in self._lms.items()}
            total = sum(s["cost_usd"] for s in stats.values())
            self._event_log.emit({"type": "stats", **stats, "total_cost_usd": round(total, 4)})


def make_constrained_proposer(template: str, lm, event_log) -> "ProposalFn":
    """Build a ProposalFn that injects a custom reflection template into InstructionProposalSignature."""
    _iter = [0]

    def _lm_call(prompt: str) -> str:
        raw_outputs = lm(prompt)
        for raw in raw_outputs:
            if isinstance(raw, str):
                return raw
            if isinstance(raw, dict):
                return raw["text"]
        raise TypeError("Unexpected output type from LM")

    def proposer(
        candidate: dict[str, str],
        reflective_dataset: Mapping[str, Sequence[Mapping[str, Any]]],
        components_to_update: list[str],
    ) -> dict[str, str]:
        _iter[0] += 1
        event_log.emit({"type": "iteration", "idx": _iter[0], "components": components_to_update})

        results = {}
        for name in components_to_update:
            results[name] = InstructionProposalSignature.run(
                lm=_lm_call,
                input_dict={
                    "current_instruction_doc": candidate[name],
                    "dataset_with_feedback": reflective_dataset[name],
                    "prompt_template": template,
                },
            )["new_instruction"]
        return results

    return proposer


class EventLog:
    """Append-only JSONL event log for dashboard consumption."""

    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._fh = open(path, "a")

    def emit(self, event: dict):
        event.setdefault("ts", datetime.now(timezone.utc).isoformat())
        self._fh.write(json.dumps(event) + "\n")
        self._fh.flush()

    def close(self):
        self._fh.close()


def main():
    from dspy.teleprompt.gepa import GEPA

    resume_id = sys.argv[1] if len(sys.argv) > 1 else None

    print("Loading dataset...")
    df = build_dataset()
    examples = make_examples(df, n_splits=20, seed=42)
    print(f"Built {len(examples)} cross-validation examples (51 states, 11 held out per split)")

    gemini_key = os.environ["GEMINI_API_KEY"]
    student_lm = dspy.LM(STUDENT_MODEL, api_key=gemini_key, reasoning_effort="high", cache=False)
    teacher_lm = dspy.LM(TEACHER_MODEL, api_key=gemini_key, reasoning_effort="high", cache=False)
    sub_lm = dspy.LM(SUB_MODEL, api_key=gemini_key, reasoning_effort="high", cache=False)

    prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "crash_predictor_rlm.md"
    prompt_text = prompt_path.read_text()
    CrashPredictor = CrashPredictorBase.with_instructions(prompt_text)

    reflection_template_path = Path(__file__).resolve().parent / "reflection_template.md"
    reflection_template = reflection_template_path.read_text()

    interpreter = LocalInterpreter()
    predictor = dspy.RLM(
        CrashPredictor,
        max_iterations=20,
        max_llm_calls=50,
        sub_lm=sub_lm,
        interpreter=interpreter,
    )

    dspy.configure(lm=student_lm)

    if resume_id:
        run_id = resume_id
        run_dir = TRACES_DIR / "runs" / run_id
        print(f"Resuming from: {run_dir}")
    else:
        run_id = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")
        run_dir = TRACES_DIR / "runs" / run_id
        run_dir.mkdir(parents=True, exist_ok=True)
    print(f"Run directory: {run_dir}")

    event_log = EventLog(run_dir / "events.jsonl")
    set_event_log(event_log)

    event_log.emit({
        "type": "optimization_start",
        "student_model": STUDENT_MODEL,
        "student_reasoning": "high",
        "teacher_model": TEACHER_MODEL,
        "teacher_reasoning": "high",
        "sub_model": SUB_MODEL,
        "sub_reasoning": "high",
        "n_examples": len(examples),
        "initial_prompt_length": len(prompt_text),
        "resumed": resume_id is not None,
    })

    stats_emitter = StatsEmitter(event_log, student_lm, teacher_lm, sub_lm, interval=10)

    t0 = time.time()
    stats_emitter.start()

    # Phase 1: baseline evaluation only
    if not resume_id:
        print("Phase 1: running baseline evaluation...")
        event_log.emit({"type": "phase", "phase": "baseline", "n_splits": len(examples)})
        gepa_baseline = GEPA(
            metric=crash_metric,
            reflection_lm=teacher_lm,
            max_metric_calls=len(examples),
            track_stats=True,
            log_dir=str(run_dir),
            num_threads=20,
            seed=42,
        )
        gepa_baseline.compile(student=predictor, trainset=examples)

        baseline_state = run_dir / "gepa_state_baseline.bin"
        shutil.copy(run_dir / "gepa_state.bin", baseline_state)
        print(f"Baseline checkpoint saved to {baseline_state}")

    # Phase 2: full optimization with constrained teacher
    print("Phase 2: starting GEPA optimization (auto=light, 6 candidates)...")
    event_log.emit({"type": "phase", "phase": "optimizing"})
    constrained_proposer = make_constrained_proposer(reflection_template, teacher_lm, event_log)
    gepa_full = GEPA(
        metric=crash_metric,
        reflection_lm=teacher_lm,
        instruction_proposer=constrained_proposer,
        auto="light",
        track_stats=True,
        log_dir=str(run_dir),
        num_threads=20,
        reflection_minibatch_size=5,
        seed=42,
    )

    try:
        optimized = gepa_full.compile(student=predictor, trainset=examples)
    finally:
        stats_emitter.stop()

    elapsed = time.time() - t0
    print(f"Optimization complete in {elapsed:.0f}s")

    # Emit candidate events from GEPA results
    results = getattr(optimized, "detailed_results", None)
    if results:
        candidates = getattr(results, "candidates", [])
        scores = getattr(results, "val_aggregate_scores", [])
        parents = getattr(results, "parents", [])
        discovery = getattr(results, "discovery_eval_counts", [])

        for i in range(len(candidates)):
            cand = candidates[i]
            instruction = ""
            if isinstance(cand, dict) and cand:
                instruction = list(cand.values())[0]
            else:
                try:
                    for _, pred in cand.named_predictors():
                        sig = pred.signature
                        if hasattr(sig, "instructions") and sig.instructions:
                            instruction = sig.instructions
                            break
                except Exception:
                    pass
            event_log.emit({
                "type": "candidate",
                "idx": i,
                "score": scores[i] if i < len(scores) else None,
                "parents": parents[i] if i < len(parents) else None,
                "instruction": instruction[:5000],
                "eval_count_at_discovery": discovery[i] if i < len(discovery) else None,
            })

    optimized_instructions = None
    for name, pred in optimized.named_predictors():
        sig = pred.signature
        if hasattr(sig, "instructions"):
            optimized_instructions = sig.instructions
            break

    if optimized_instructions:
        out_path = Path(__file__).resolve().parent.parent / "prompts" / "crash_predictor_reward_hacked.md"
        out_path.write_text(optimized_instructions)
        print(f"Saved optimized prompt to {out_path}")

    stats_student = _lm_stats(student_lm)
    stats_teacher = _lm_stats(teacher_lm)
    stats_sub = _lm_stats(sub_lm)
    total_cost = stats_student["cost_usd"] + stats_teacher["cost_usd"] + stats_sub["cost_usd"]

    manifest = {
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(elapsed, 1),
        "total_cost_usd": round(total_cost, 4),
        "gepa_auto": "light",
        "student": {"model": STUDENT_MODEL, "reasoning": "high", **stats_student},
        "teacher": {"model": TEACHER_MODEL, "reasoning": "high", **stats_teacher},
        "sub": {"model": SUB_MODEL, "reasoning": "high", **stats_sub},
    }

    manifest_path = run_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"Manifest written to {manifest_path}")

    event_log.emit({
        "type": "optimization_complete",
        "elapsed_seconds": round(elapsed, 1),
        "total_cost_usd": round(total_cost, 4),
        "student": stats_student,
        "teacher": stats_teacher,
        "sub": stats_sub,
    })
    event_log.close()


if __name__ == "__main__":
    main()
