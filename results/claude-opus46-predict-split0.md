# Claude Opus 4.6: Raw Predict (Split 0)

**Model:** claude-opus-4-6 (max reasoning)
**Harness:** Raw Predict (no tools, no REPL, no sub-LLM)
**Split:** 0 (40 train / 11 held-out)
**RMSE:** 3.16
**Score:** 0.8418

## Comparison (Split 0)

| Method | RMSE |
|--------|------|
| OLS Regression | 5.45 |
| Predict (Gemini 3 Flash) | 4.21 |
| Tools (GPT 5.4 Heavy) | 4.11 |
| Predict (Gemini 3.1 Pro) | 3.87 |
| Predict (GPT 5.4 Heavy) | 3.28 |
| **Predict (Claude Opus 4.6)** | **3.16** |
| GEPA Best Mutation RLM (Gemini 3 Flash)* | 2.48 |

*Cherry-picked from Pareto frontier across all evals in GEPA run 2.

## Per-State Results

| State | Predicted | Actual | Error |
|-------|-----------|--------|-------|
| UT | -17.00 | -21.93 | +4.93 |
| SD | -5.00 | 0.00 | -5.00 |
| WA | -21.00 | -25.19 | +4.19 |
| IL | -19.00 | -21.81 | +2.81 |
| MO | -10.00 | -10.97 | +0.97 |
| NY | -18.00 | -14.02 | -3.98 |
| LA | -6.00 | -4.21 | -1.79 |
| NC | -13.00 | -13.06 | +0.06 |
| AR | -9.00 | -6.70 | -2.30 |
| NM | -13.00 | -15.68 | +2.68 |
| IN | -9.00 | -7.30 | -1.70 |

## Model Response

The model identified five key patterns from the training data before predicting:

1. **Appreciation is the primary predictor, but not sufficient alone.** NV (80% to -56), AZ (73% to -46), FL (74% to -45), CA (74% to -41) form a clear cluster.
2. **Supply constraints buffer high appreciation.** HI (81% to -18), DC (70% to -12). Constrained geography limits overbuilding.
3. **Population growth amplifies bubbles.** NV (12%), AZ (9%), FL (7%), ID (8%) all had high pop growth and high appreciation, producing the worst crashes. TX (6% pop growth, 12% appreciation) was fine, so pop growth alone is not enough.
4. **Manufacturing collapse creates crashes without bubbles.** MI (9% appreciation to -29) and to a lesser extent OH (9% to -13). Weak labor markets drive foreclosures.
5. **Low-appreciation, stable economies are resilient.** IA (0.0), ND (0.0), NE (-2.9), KS (-5.0).

State-by-state reasoning highlights:

**UT:** Split the difference between GA-like overbuilding risk (high pop growth) and TX-like fundamental demand (low unemployment, demographic growth from birth rates). Identified that 7.01% pop growth is partly fundamental rather than speculative.

**SD:** Classic Great Plains profile. Placed between ND (0.0) and KS (-4.97). Overpredicted the crash at -5.00 (actual 0.00).

**WA:** Used OR (-25.98) as the near-perfect comp but adjusted upward for WA's higher income and tech sector cushion (Microsoft, Amazon).

**IL:** Closest comp MN (24.94 appreciation to -21.83). Recognized Chicago subprime exposure in south side and suburbs. Only model to get IL within 3 pp of actual.

**NY:** Identified supply constraints (NYC geography) and negative pop growth as crash moderators, but overpredicted severity at -18.00. The model noted Long Island and upstate vulnerability.

**LA:** Correctly identified Katrina as a supply-reducing event that paradoxically supported prices. Noted the -4.83% population loss destroyed housing stock, not just demand.

## Observations

Best single-model result on split 0 (RMSE 3.16). The error distribution is notably tight: no state exceeds 5 pp error, compared to 6-7 pp outliers for every other model.

The IL prediction (+2.81 error) is the standout. Every other model misses IL by 6+ pp. Claude Opus correctly weighted Chicago's subprime exposure and MN as the primary comp, arriving at -19.00 vs the actual -21.81. GPT 5.4 Heavy predicted -15.40 (+6.41 error), Gemini 3.1 Pro predicted -15.20 (+6.61 error).

The biggest miss is SD (-5.00 vs 0.00), where the model overpredicted the crash. This is a calibration issue at the mild end: the model hedged toward a small negative number rather than committing to zero crash for a Plains state.

NY (-3.98 error) is the other notable miss, where the model overweighted appreciation relative to supply constraints. GPT 5.4 Heavy was better here (-1.28 error) with a more aggressive supply-constraint discount.
