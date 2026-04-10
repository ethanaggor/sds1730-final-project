#!/usr/bin/env python3
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import dspy
import numpy as np
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

from data_utils import build_dataset, make_examples
from local_interpreter import LocalInterpreter
from optimize import _lm_stats
from signatures import CrashPredictorBase, STATE_NAMES

STUDENT_MODEL = "gemini/gemini-3-flash-preview"
SUB_MODEL = "gemini/gemini-3-flash-preview"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "results"
PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "rlm.md"


def build_transcript(result, example, elapsed, student_lm, sub_lm) -> str:
    lines = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    s = _lm_stats(student_lm)
    sub = _lm_stats(sub_lm)

    lines.append(f"# Smoke Test: {STUDENT_MODEL} (high) -- RLM")
    lines.append(f"**Time**: {elapsed:.1f}s")
    lines.append(f"**Root** ({STUDENT_MODEL}): {s['input_tokens']:,} in ({s['cached_tokens']:,} cached) / {s['output_tokens']:,} out / ${s['cost_usd']:.4f} / {s['calls']} calls")
    lines.append(f"**Sub** ({SUB_MODEL}): {sub['input_tokens']:,} in ({sub['cached_tokens']:,} cached) / {sub['output_tokens']:,} out / ${sub['cost_usd']:.4f} / {sub['calls']} calls")
    lines.append(f"**Total cost**: ${s['cost_usd'] + sub['cost_usd']:.4f}")
    lines.append(f"**Timestamp**: {now}")
    lines.append("")

    trajectory = getattr(result, "trajectory", [])
    if not trajectory:
        lines.append("## No trajectory recorded")
    else:
        for i, entry in enumerate(trajectory):
            lines.append(f"## Iteration {i + 1}")
            lines.append("")

            reasoning = entry.get("reasoning", "")
            if reasoning:
                lines.append("### Reasoning")
                lines.append(reasoning)
                lines.append("")

            code = entry.get("code", "")
            if code:
                lines.append("### Code")
                lines.append("```python")
                lines.append(code)
                lines.append("```")
                lines.append("")

            output = entry.get("output", "")
            if output:
                lines.append("### Output")
                lines.append("```")
                lines.append(output[:3000])
                lines.append("```")
                lines.append("")

    final_reasoning = getattr(result, "final_reasoning", "")
    if final_reasoning and (not trajectory or final_reasoning != trajectory[-1].get("reasoning", "")):
        lines.append("## Final Reasoning")
        lines.append(final_reasoning)
        lines.append("")

    lines.append("## Final Predictions")
    lines.append("")
    lines.append("| State | Predicted | Actual | Error |")
    lines.append("|-------|-----------|--------|-------|")

    actual = np.array(example.actual_values)
    test_states = example.test_states

    try:
        preds_dict = {p.state: p.predicted_crash_pct for p in result.predictions}
    except Exception as e:
        lines.append(f"Failed to parse predictions: {e}")
        lines.append("")
        lines.append(f"Raw predictions field: {getattr(result, 'predictions', 'MISSING')}")
        return "\n".join(lines)

    pred_values = []
    for st, act in zip(test_states, actual):
        p = preds_dict.get(st, float("nan"))
        pred_values.append(p)
        err = p - act if not np.isnan(p) else float("nan")
        lines.append(f"| {STATE_NAMES.get(st, st)} ({st}) | {p:.1f} | {act:.1f} | {err:+.1f} |")

    pred_arr = np.array(pred_values)
    valid = ~np.isnan(pred_arr)
    if valid.any():
        rmse = float(np.sqrt(np.nanmean((actual - pred_arr) ** 2)))
        lines.append("")
        lines.append(f"**RMSE: {rmse:.2f}**")

    return "\n".join(lines)


def main():
    print("Loading dataset...")
    df = build_dataset()
    examples = make_examples(df, n_splits=20, seed=42)
    example = examples[0]

    student_lm = dspy.LM(STUDENT_MODEL, api_key=os.environ["GEMINI_API_KEY"], reasoning_effort="high", cache=False)
    sub_lm = dspy.LM(SUB_MODEL, api_key=os.environ["GEMINI_API_KEY"], reasoning_effort="high", cache=False)
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
    print(f"Root: {STUDENT_MODEL} (high) | Sub: {SUB_MODEL} (high)")
    t0 = time.time()

    result = predictor(
        train_df=example.train_df,
        test_df=example.test_df,
    )

    elapsed = time.time() - t0
    print(f"Done in {elapsed:.1f}s")

    transcript = build_transcript(result, example, elapsed, student_lm, sub_lm)

    out_path = OUTPUT_DIR / "smoke_test_rlm.md"
    out_path.write_text(transcript)
    print(f"Transcript saved to {out_path}")


if __name__ == "__main__":
    main()
