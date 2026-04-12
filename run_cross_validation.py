#!/usr/bin/env python3
"""20-split cross-validation: Claude Opus 4.6 Predict via claude -p."""

import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

sys.path.insert(0, str(Path(__file__).parent / "prompt-optimizer"))
from data_utils import build_dataset

TRACE_DIR = Path("results/cv_traces")
RESULTS_PATH = Path("results/llm_experiment_results.json")
N_SPLITS = 20
SEED = 42
CONCURRENCY = 8
OLS_FORMULA = "crash_pct ~ appreciation_03_06 + ur_2006 + pcpi_2006 + pop_growth_03_06"

PROMPT_PREAMBLE = """\
You are an expert economic analyst specializing in the 2008 US housing crisis. \
You will be given economic indicators for 40 US states along with their actual \
housing crash severity (peak-to-trough decline in home prices, 2006-2012). You \
must predict the crash severity for 11 held-out states using only the training \
data and your domain knowledge.

You may not use the internet or search for any information online. Work only \
from the data provided and your own reasoning. Do not use any programmatic \
tools or tools to analyze the data. This is a pure reasoning task.

## Features

- **appreciation_03_06**: Home price appreciation 2003-2006 (%). Proxy for bubble size.
- **ur_2006**: Unemployment rate in 2006 (%). Pre-crash labor market health.
- **pcpi_2006**: Per-capita personal income in 2006 ($). Economic baseline.
- **pop_growth_03_06**: Population growth 2003-2006 (%). Migration-driven demand.
- **crash_pct**: Peak-to-trough home price decline 2006-2012 (%). This is the \
target variable. More negative = worse crash."""

PROMPT_INSTRUCTIONS = """\
## Instructions

For each held-out state, predict the crash_pct value. Use your understanding \
of the 2008 housing crisis, bubble dynamics, regional economic structure, \
speculative vs. fundamental demand, and labor market vulnerability, combined \
with patterns in the training data.

Explain your reasoning for each state, identifying comparable training states \
and the economic logic behind your prediction.

Return your final predictions as a JSON array:
```json
[
  {"state": "XX", "predicted_crash_pct": -0.00},
  ...
]
```"""

TRAIN_COLS = ["state", "crash_pct", "appreciation_03_06", "ur_2006", "pcpi_2006", "pop_growth_03_06"]
TEST_COLS = ["state", "appreciation_03_06", "ur_2006", "pcpi_2006", "pop_growth_03_06"]


def fmt_val(col, v):
    if col == "state":
        return str(v)
    if col == "pcpi_2006":
        return str(int(v))
    return f"{v:.2f}"


def make_table(df, columns):
    header = "| " + " | ".join(columns) + " |"
    sep = "|" + "|".join("---" for _ in columns) + "|"
    rows = []
    for _, row in df.iterrows():
        cells = " | ".join(fmt_val(c, row[c]) for c in columns)
        rows.append(f"| {cells} |")
    return "\n".join([header, sep] + rows)


def build_prompt(df_train, df_test_no_outcome):
    return "\n\n".join([
        PROMPT_PREAMBLE,
        f"## Training Data ({len(df_train)} states)\n\n{make_table(df_train, TRAIN_COLS)}",
        f"## Held-Out States (predict crash_pct)\n\n{make_table(df_test_no_outcome, TEST_COLS)}",
        PROMPT_INSTRUCTIONS,
    ])


def parse_predictions(text):
    match = re.search(r"```json?\s*\n(\[.*?\])\s*\n```", text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    matches = list(re.finditer(r'\[\s*\{[^]]*"state"[^]]*\}\s*\]', text, re.DOTALL))
    if matches:
        return json.loads(matches[-1].group(0))
    raise ValueError("No JSON predictions found in output")


def run_single(split_idx, condition, prompt, trace_path):
    if trace_path.exists():
        text = trace_path.read_text()
        try:
            preds = parse_predictions(text)
            if len(preds) >= 5:
                print(f"  [cached] split {split_idx} {condition}", flush=True)
                return preds
        except (ValueError, json.JSONDecodeError):
            pass

    print(f"  [running] split {split_idx} {condition}", flush=True)
    result = subprocess.run(
        ["claude", "-p", "--model", "opus", "--effort", "max",
         "--tools", "", "--no-session-persistence"],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=600,
    )

    if result.returncode != 0:
        raise RuntimeError(f"claude exited {result.returncode}: {result.stderr[:500]}")

    text = result.stdout
    trace_path.write_text(text)
    return parse_predictions(text)


def compute_rmse(preds_list, actual_values, test_states):
    preds_dict = {p["state"]: p["predicted_crash_pct"] for p in preds_list}
    pred_arr = np.array([preds_dict.get(st, np.nan) for st in test_states])
    return float(np.sqrt(np.nanmean((actual_values - pred_arr) ** 2)))


def main():
    df = build_dataset()
    TRACE_DIR.mkdir(parents=True, exist_ok=True)

    splits = []
    for i in range(N_SPLITS):
        rng = np.random.RandomState(SEED + i)
        test_idx = rng.choice(len(df), size=11, replace=False)
        train_idx = np.setdiff1d(np.arange(len(df)), test_idx)
        df_train = df.iloc[train_idx].reset_index(drop=True)
        df_test = df.iloc[test_idx].reset_index(drop=True)

        ols = smf.ols(OLS_FORMULA, data=df_train).fit()
        rmse_ols = float(np.sqrt(np.mean(
            (df_test["crash_pct"].values - ols.predict(df_test).values) ** 2
        )))

        df_train_shuf = df_train.assign(
            crash_pct=rng.permutation(df_train["crash_pct"].values)
        )
        df_test_no = df_test.drop(columns=["crash_pct"])

        splits.append({
            "i": i,
            "rmse_ols": rmse_ols,
            "actual": df_test["crash_pct"].values,
            "test_states": df_test["state"].values.tolist(),
            "prompt_real": build_prompt(df_train, df_test_no),
            "prompt_shuf": build_prompt(df_train_shuf, df_test_no),
        })

    futures = {}
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as pool:
        for s in splits:
            f_real = pool.submit(
                run_single, s["i"], "real",
                s["prompt_real"], TRACE_DIR / f"split_{s['i']:02d}_real.md",
            )
            f_shuf = pool.submit(
                run_single, s["i"], "shuffled",
                s["prompt_shuf"], TRACE_DIR / f"split_{s['i']:02d}_shuffled.md",
            )
            futures[s["i"]] = (f_real, f_shuf)

    results = []
    for s in splits:
        f_real, f_shuf = futures[s["i"]]

        try:
            rmse_real = compute_rmse(f_real.result(), s["actual"], s["test_states"])
        except Exception as e:
            print(f"  Split {s['i']} real FAILED: {e}", flush=True)
            rmse_real = float("nan")

        try:
            rmse_shuf = compute_rmse(f_shuf.result(), s["actual"], s["test_states"])
        except Exception as e:
            print(f"  Split {s['i']} shuffled FAILED: {e}", flush=True)
            rmse_shuf = float("nan")

        results.append({
            "split": s["i"],
            "rmse_ols": s["rmse_ols"],
            "rmse_llm_real": rmse_real,
            "rmse_llm_shuffled": rmse_shuf,
        })
        print(
            f"Split {s['i']+1}/{N_SPLITS}: "
            f"OLS={s['rmse_ols']:.2f}  LLM={rmse_real:.2f}  Shuffled={rmse_shuf:.2f}",
            flush=True,
        )

    with open(RESULTS_PATH, "w") as f:
        json.dump(results, f, indent=2)

    rdf = pd.DataFrame(results)
    print(f"\n{'='*50}")
    print(f"Mean RMSE - OLS:      {rdf['rmse_ols'].mean():.2f} (+/- {rdf['rmse_ols'].std():.2f})")
    print(f"Mean RMSE - LLM:      {rdf['rmse_llm_real'].mean():.2f} (+/- {rdf['rmse_llm_real'].std():.2f})")
    print(f"Mean RMSE - Shuffled: {rdf['rmse_llm_shuffled'].mean():.2f} (+/- {rdf['rmse_llm_shuffled'].std():.2f})")
    print(f"Win rate vs OLS:      {(rdf['rmse_llm_real'] < rdf['rmse_ols']).mean():.0%}")
    print(f"Contamination check:  {(rdf['rmse_llm_shuffled'] > rdf['rmse_llm_real']).mean():.0%}")
    print(f"\nResults: {RESULTS_PATH}")


if __name__ == "__main__":
    main()
