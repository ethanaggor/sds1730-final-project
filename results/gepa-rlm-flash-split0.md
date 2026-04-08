# GEPA RLM (Gemini 3 Flash): Split 0

**Model:** gemini/gemini-3-flash-preview (reasoning: high)
**Harness:** RLM with Python REPL (numpy, pandas) and llm_query(), unoptimized seed prompt
**Split:** 0 (40 train / 11 held-out)
**Median RMSE:** 5.85 (5 evals)
**Mean RMSE:** 5.19

## Comparison (Split 0)

| Method | RMSE |
|--------|------|
| OLS Regression | 5.45 |
| RLM, median (Gemini 3 Flash) | 5.85 |
| Predict (Gemini 3 Flash) | 4.21 |
| Tools (GPT 5.4 Heavy) | 4.11 |
| Predict (Gemini 3.1 Pro) | 3.87 |
| Predict (GPT 5.4 Heavy) | 3.28 |
| Predict (Claude Opus 4.6) | 3.16 |

## Split 0 Eval Distribution

All 5 evals use the identical seed prompt (GEPA accepted zero mutations in run 2). The only source of variation is stochastic RLM reasoning.

| Eval | RMSE | Score | Iterations |
|------|------|-------|------------|
| 0 | 5.85 | 0.7077 | 8 |
| 1 | 2.48 | 0.8761 | 11 |
| 2 | 7.92 | 0.6039 | 8 |
| 3 | 3.09 | 0.8454 | 9 |
| 4 | 6.60 | 0.6702 | 20 |

**Median:** 5.85, **Mean:** 5.19, **Min:** 2.48, **Max:** 7.92, **Spread:** 5.44

## Observations

The 5.44 pp spread across 5 evals on the same split with the same prompt is the defining result. The RLM harness with Gemini 3 Flash produces wildly variable outputs: the best run (2.48) would be the top result in the entire comparison, while the worst (7.92) would be below OLS. This variance is pure reasoning stochasticity, not prompt or data variation.

Eval 4 hit the 20-iteration cap (the SUBMIT bug caused looping; see gepa-run-2-constrained-teacher.md). Eval 1 (the best) ran 11 iterations and likely made effective use of `llm_query` for domain context.

The median (5.85) is worse than OLS (5.45) on this split, and worse than every Predict method. The RLM harness with Gemini Flash does not reliably outperform simpler methods on a per-split basis, despite occasionally producing excellent results. The high variance makes it unsuitable for single-shot evaluation; its value, if any, lies in the best-of-N regime or with a stronger base model.

## Source

Data from GEPA run 2 (`2026-04-07T21-06-58`, label: `constrained-teacher-flash-loops`). Events extracted from `events.jsonl`, filtered to split 0.
