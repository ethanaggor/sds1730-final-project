#!/usr/bin/env python3
"""GEPA prompt optimization for crash predictor using Gemini + RLM."""

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import dspy
import numpy as np
from dotenv import load_dotenv

from data_utils import build_dataset, make_examples
from local_interpreter import LocalInterpreter
from metric import crash_metric, set_event_log
from signatures import CrashPredictorBase

load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

TRACES_DIR = Path("traces")

STUDENT_MODEL = "openai/gpt-5.4-mini"
TEACHER_MODEL = "gemini/gemini-3.1-pro-preview"
SUB_MODEL = "gemini/gemini-3-flash-preview"


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

    print("Loading dataset...")
    df = build_dataset()
    examples = make_examples(df, n_splits=20, seed=42)
    print(f"Built {len(examples)} cross-validation examples (51 states, 11 held out per split)")

    gemini_key = os.environ["GEMINI_API_KEY"]
    student_lm = dspy.LM(STUDENT_MODEL, api_key=os.environ["OPENAI_API_KEY"], reasoning_effort="xhigh", cache=False)
    teacher_lm = dspy.LM(TEACHER_MODEL, api_key=gemini_key, reasoning_effort="high", cache=False)
    sub_lm = dspy.LM(SUB_MODEL, api_key=gemini_key, reasoning_effort="high", cache=False)

    prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "crash_predictor_rlm.md"
    prompt_text = prompt_path.read_text()
    CrashPredictor = CrashPredictorBase.with_instructions(prompt_text)

    interpreter = LocalInterpreter()
    predictor = dspy.RLM(
        CrashPredictor,
        max_iterations=20,
        max_llm_calls=50,
        sub_lm=sub_lm,
        interpreter=interpreter,
    )

    dspy.configure(lm=student_lm)

    event_log = EventLog(TRACES_DIR / "events.jsonl")
    set_event_log(event_log)

    event_log.emit({
        "type": "optimization_start",
        "student_model": STUDENT_MODEL,
        "student_reasoning": "xhigh",
        "teacher_model": TEACHER_MODEL,
        "teacher_reasoning": "high",
        "sub_model": SUB_MODEL,
        "sub_reasoning": "high",
        "n_examples": len(examples),
        "initial_prompt_length": len(prompt_text),
    })

    print("Starting GEPA optimization (auto=light, 6 candidates)...")
    t0 = time.time()

    gepa = GEPA(
        metric=crash_metric,
        reflection_lm=teacher_lm,
        auto="light",
        track_stats=True,
        log_dir=str(TRACES_DIR),
        num_threads=20,
        seed=42,
    )

    optimized = gepa.compile(student=predictor, trainset=examples)

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
        out_path = Path(__file__).resolve().parent.parent / "prompts" / "crash_predictor_optimized.md"
        out_path.write_text(optimized_instructions)
        print(f"Saved optimized prompt to {out_path}")

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

    stats_student = _lm_stats(student_lm)
    stats_teacher = _lm_stats(teacher_lm)
    stats_sub = _lm_stats(sub_lm)
    total_cost = stats_student["cost_usd"] + stats_teacher["cost_usd"] + stats_sub["cost_usd"]

    manifest = {
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(elapsed, 1),
        "total_cost_usd": round(total_cost, 4),
        "gepa_auto": "light",
        "student": {"model": STUDENT_MODEL, "reasoning": "xhigh", **stats_student},
        "teacher": {"model": TEACHER_MODEL, "reasoning": "high", **stats_teacher},
        "sub": {"model": SUB_MODEL, "reasoning": "high", **stats_sub},
    }

    manifest_path = TRACES_DIR / "manifest.json"
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
