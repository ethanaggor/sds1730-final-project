# GPT 5.4 Pro Extended Thinking: Raw Predict (Split 0)

**Model:** GPT 5.4 Pro (extended thinking, 28 min)
**Harness:** Raw Predict (no tools, no REPL, no sub-LLM)
**Split:** 0 (40 train / 11 held-out)
**RMSE:** 3.84
**Score:** 0.8080

## Comparison (Split 0)

| Method | RMSE |
|--------|------|
| OLS Regression | 5.45 |
| RLM, median (Gemini 3 Flash) | 5.85 |
| Predict (Gemini 3 Flash) | 4.21 |
| Tools (GPT 5.4 Heavy) | 4.11 |
| Predict (Gemini 3.1 Pro) | 3.87 |
| **Predict (GPT 5.4 Pro)** | **3.84** |
| Predict (GPT 5.4 Heavy) | 3.28 |
| Predict (Claude Opus 4.6) | 3.16 |

## Per-State Results

| State | Predicted | Actual | Error |
|-------|-----------|--------|-------|
| UT | -15.70 | -21.93 | +6.23 |
| SD | -3.00 | 0.00 | -3.00 |
| WA | -21.00 | -25.19 | +4.19 |
| IL | -14.50 | -21.81 | +7.31 |
| MO | -7.00 | -10.97 | +3.97 |
| NY | -18.00 | -14.02 | -3.98 |
| LA | -6.00 | -4.21 | -1.79 |
| NC | -11.50 | -13.06 | +1.56 |
| AR | -8.50 | -6.70 | -1.80 |
| NM | -15.50 | -15.68 | +0.18 |
| IN | -9.00 | -7.30 | -1.70 |

## Model Response

The model spent 28 minutes in extended thinking, cycling through multiple estimate revisions per state. It described its approach as anchoring to the closest training-state analogues on appreciation, labor market, income, and population growth, then adjusting for speculation and oversupply risk.

The thinking trace shows repeated self-correction: for Utah, estimates ranged from -12.7 to -15.7 across different reasoning passes; for Illinois, from -14 to -17; for New York, from -15.7 to -18.3. The final predictions generally landed in the middle of these ranges. The result is over-smoothed estimates that systematically underpredict the hardest-hit states.

**UT (+6.23 error):** Compared to CO, ID, GA. Recognized the low unemployment and fast population growth as overbuilding risk but concluded "still much less severe than ID/AZ/NV." Underpredicted by anchoring too heavily on moderate appreciation (23%) without weighting the speculative growth dynamics.

**IL (+7.31 error):** The worst single-state error in the comparison table. Compared to WI, MN, MA, PA and noted "moderate appreciation plus a large metro/condo exposure pushes it into a mid-teens decline." Like every other model, missed Chicago's subprime severity, but the extended thinking actually pushed the estimate further from the truth: earlier passes had -17, which the model revised down to -14.5.

**NM (+0.18 error):** Nearly perfect. The model correctly placed NM as "not enough to justify an Arizona/Nevada-style crash" with a Southwest adjustment from the MT/ID/WY cluster.

**WA (+4.19 error):** Used OR as the primary comp and adjusted for income and tech resilience. Same reasoning as Claude Opus but with a less aggressive estimate.

## Observations

GPT 5.4 Pro with extended thinking (3.84) scored worse than GPT 5.4 Heavy with standard reasoning (3.28) despite spending 7x longer thinking. The extended thinking trace shows why: the model repeatedly revised estimates toward moderate values, hedging between upper and lower bounds rather than committing. The result is over-smoothed predictions.

The IL prediction is the clearest example. The model's early reasoning passes produced -17 (closer to the actual -21.81), but further deliberation pushed the estimate down to -14.5. More thinking produced a worse answer because the model hedged away from its initial, more accurate instinct.

The GPT 5.4 family comparison is instructive: Heavy (4 min thinking, RMSE 3.28) beats Pro (28 min thinking, RMSE 3.84). The consumer-tier "extended thinking" model is not the same as the Heavy model with shorter reasoning. Pro's extended deliberation introduces noise rather than signal on this task.
