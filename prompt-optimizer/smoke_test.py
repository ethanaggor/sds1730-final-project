#!/usr/bin/env python3
"""Single-split RLM evaluation using the active model profile."""
import os
import sys
import time
from pathlib import Path

import dspy
import numpy as np
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

from data_utils import build_dataset, make_examples
from local_interpreter import LocalInterpreter
from metric import crash_metric
from optimize import PROFILES, DEFAULT_PROFILE, _lm_stats
from signatures import CrashPredictorBase, STATE_NAMES

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "results"
PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "rlm.md"


def main():
    profile_name = os.environ.get("MODEL_PROFILE", DEFAULT_PROFILE)
    for arg in sys.argv[1:]:
        if arg.startswith("--profile="):
            profile_name = arg.split("=", 1)[1]

    if profile_name not in PROFILES:
        sys.exit(f"Unknown profile: {profile_name!r}. Choose from: {', '.join(PROFILES)}")
    profile = PROFILES[profile_name]

    print("Loading dataset...")
    df = build_dataset()
    examples = make_examples(df, n_splits=20, seed=42)
    example = examples[0]

    api_key = os.environ[profile["api_key_env"]]
    base_kwargs = {"api_key": api_key, "cache": False}
    if profile["max_tokens"] is not None:
        base_kwargs["max_tokens"] = profile["max_tokens"]

    student_lm = dspy.LM(profile["student"], reasoning_effort=profile["student_reasoning"], **base_kwargs)
    sub_lm = dspy.LM(profile["sub"], reasoning_effort=profile["student_reasoning"], **base_kwargs)
    dspy.configure(lm=student_lm)

    prompt_text = PROMPT_PATH.read_text()
    CrashPredictor = CrashPredictorBase.with_instructions(prompt_text)

    interpreter = LocalInterpreter()
    predictor = dspy.RLM(
        CrashPredictor,
        max_iterations=20,
        max_llm_calls=50,
        sub_lm=sub_lm,
        interpreter=interpreter,
    )

    print(f"Running RLM on split 0 ({len(example.test_states)} held-out states)...")
    print(f"Profile: {profile_name} | Student: {profile['student']} ({profile['student_reasoning']})")
    t0 = time.time()

    result = predictor(train_df=example.train_df, test_df=example.test_df)
    elapsed = time.time() - t0

    score_result = crash_metric(example, result)
    score = score_result.score if hasattr(score_result, "score") else float(score_result)
    feedback = getattr(score_result, "feedback", "")

    s = _lm_stats(student_lm)
    sub = _lm_stats(sub_lm)

    lines = [
        f"# Smoke Test: {profile['student']} ({profile['student_reasoning']}) -- RLM",
        f"**Profile**: {profile_name}",
        f"**Time**: {elapsed:.1f}s",
        f"**Score**: {score:.4f}",
        f"**Student** ({profile['student']}): {s['input_tokens']:,} in / {s['output_tokens']:,} out / ${s['cost_usd']:.4f} / {s['calls']} calls",
        f"**Sub** ({profile['sub']}): {sub['input_tokens']:,} in / {sub['output_tokens']:,} out / ${sub['cost_usd']:.4f} / {sub['calls']} calls",
        f"**Total cost**: ${s['cost_usd'] + sub['cost_usd']:.4f}",
        "",
    ]

    try:
        preds_dict = {p.state: p.predicted_crash_pct for p in result.predictions}
        actual = np.array(example.actual_values)
        pred_arr = np.array([preds_dict.get(st, float("nan")) for st in example.test_states])
        rmse = float(np.sqrt(np.nanmean((actual - pred_arr) ** 2)))

        lines.append("## Predictions")
        lines.append("")
        lines.append("| State | Predicted | Actual | Error |")
        lines.append("|-------|-----------|--------|-------|")
        for st, a in zip(example.test_states, actual):
            p = preds_dict.get(st, float("nan"))
            lines.append(f"| {STATE_NAMES.get(st, st)} ({st}) | {p:.1f} | {a:.1f} | {p - a:+.1f} |")
        lines.append("")
        lines.append(f"**RMSE: {rmse:.2f}**")
    except Exception as e:
        lines.append(f"Failed to parse predictions: {e}")
        lines.append(f"Raw: {getattr(result, 'predictions', 'MISSING')}")

    transcript = "\n".join(lines)
    print(f"\nDone in {elapsed:.1f}s | Score: {score:.4f}")

    out_path = OUTPUT_DIR / "smoke_test_rlm.md"
    out_path.write_text(transcript)
    print(f"Transcript saved to {out_path}")


if __name__ == "__main__":
    main()
