#!/usr/bin/env python3
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
from dotenv import load_dotenv
from gepa.strategies.instruction_proposal import InstructionProposalSignature

from data_utils import build_dataset, make_examples
from local_interpreter import LocalInterpreter
from metric import crash_metric, set_event_log
from signatures import CrashPredictorBase

PROJECT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_DIR.parent.parent / ".env")

TRACES_DIR = Path("traces")

PROFILES = {
    "gpt": {
        "student": "openai/gpt-5.4-mini",
        "teacher": "openai/gpt-5.4",
        "sub": "openai/gpt-5.4-mini",
        "api_key_env": "OPENAI_API_KEY",
        "reasoning_effort": "xhigh",
        "max_tokens": 65000,
    },
    "gemini": {
        "student": "gemini/gemini-3-flash-preview",
        "teacher": "gemini/gemini-3.1-pro-preview",
        "sub": "gemini/gemini-3-flash-preview",
        "api_key_env": "GEMINI_API_KEY",
        "reasoning_effort": "high",
        "max_tokens": 65000,
    },
}
DEFAULT_PROFILE = "gpt"


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


def make_constrained_proposer(template: str, lm, event_log):
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
            event_log.emit({
                "type": "proposed_instruction",
                "component": name,
                "iteration": _iter[0],
                "instruction": results[name][:5000],
            })
        return results

    return proposer


class EventLog:
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

    profile_name = os.environ.get("MODEL_PROFILE", DEFAULT_PROFILE)
    resume_id = None
    for arg in sys.argv[1:]:
        if arg.startswith("--profile="):
            profile_name = arg.split("=", 1)[1]
        elif not arg.startswith("--"):
            resume_id = arg

    if profile_name not in PROFILES:
        sys.exit(f"Unknown profile: {profile_name!r}. Choose from: {', '.join(PROFILES)}")
    profile = PROFILES[profile_name]

    print("Loading dataset...")
    df = build_dataset()
    examples = make_examples(df, n_splits=20, seed=42)
    print(f"Built {len(examples)} cross-validation examples (51 states, 11 held out per split)")

    api_key = os.environ[profile["api_key_env"]]
    lm_kwargs = {"api_key": api_key, "reasoning_effort": profile["reasoning_effort"], "cache": False}
    if profile["max_tokens"] is not None:
        lm_kwargs["max_tokens"] = profile["max_tokens"]

    student_lm = dspy.LM(profile["student"], **lm_kwargs)
    teacher_lm = dspy.LM(profile["teacher"], **lm_kwargs)
    sub_lm = dspy.LM(profile["sub"], **lm_kwargs)

    prompt_text = (PROJECT_DIR / "prompts" / "rlm.md").read_text()
    CrashPredictor = CrashPredictorBase.with_instructions(prompt_text)

    reflection_template = (PROJECT_DIR / "prompts" / "GEPA_reflection_template.md").read_text()

    interpreter = LocalInterpreter()
    predictor = dspy.RLM(
        CrashPredictor,
        max_iterations=20,
        max_llm_calls=50,
        sub_lm=sub_lm,
        interpreter=interpreter,
    )

    dspy.configure(lm=student_lm)

    run_id = resume_id or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")
    run_dir = TRACES_DIR / "runs" / run_id
    if not resume_id:
        run_dir.mkdir(parents=True, exist_ok=True)
    print(f"{'Resuming' if resume_id else 'Run'} directory: {run_dir}")

    event_log = EventLog(run_dir / "events.jsonl")
    set_event_log(event_log)

    event_log.emit({
        "type": "optimization_start",
        "profile": profile_name,
        "student_model": profile["student"],
        "teacher_model": profile["teacher"],
        "sub_model": profile["sub"],
        "reasoning_effort": profile["reasoning_effort"],
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
    print(f"Phase 2: starting GEPA optimization (profile={profile_name}, auto=light)...")
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

    results = getattr(optimized, "detailed_results", None)
    if results:
        for i, (cand, score, parent, evals) in enumerate(zip(
            results.candidates, results.val_aggregate_scores,
            results.parents, results.discovery_eval_counts,
        )):
            instruction = list(cand.values())[0] if isinstance(cand, dict) and cand else ""
            event_log.emit({
                "type": "candidate",
                "idx": i,
                "score": score,
                "parents": parent,
                "instruction": instruction[:5000],
                "eval_count_at_discovery": evals,
            })

    optimized_instructions = None
    for _, pred in optimized.named_predictors():
        optimized_instructions = getattr(pred.signature, "instructions", None)
        if optimized_instructions:
            break

    if optimized_instructions:
        out_path = PROJECT_DIR / "prompts" / "optimized.md"
        out_path.write_text(optimized_instructions)
        print(f"Saved optimized prompt to {out_path}")

    lm_roles = {
        "student": (profile["student"], student_lm),
        "teacher": (profile["teacher"], teacher_lm),
        "sub": (profile["sub"], sub_lm),
    }
    stats = {role: _lm_stats(lm) for role, (_, lm) in lm_roles.items()}
    total_cost = round(sum(s["cost_usd"] for s in stats.values()), 4)

    manifest = {
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(elapsed, 1),
        "total_cost_usd": total_cost,
        "profile": profile_name,
        "gepa_auto": "light",
        **{role: {"model": model, "reasoning": profile["reasoning_effort"], **stats[role]} for role, (model, _) in lm_roles.items()},
    }

    manifest_path = run_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"Manifest written to {manifest_path}")

    event_log.emit({
        "type": "optimization_complete",
        "elapsed_seconds": round(elapsed, 1),
        "total_cost_usd": total_cost,
        **stats,
    })
    event_log.close()


if __name__ == "__main__":
    main()
