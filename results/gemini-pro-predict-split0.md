# Gemini 3.1 Pro: Raw Predict (Split 0)

**Model:** gemini/gemini-3.1-pro-preview
**Harness:** Predict (no tools, no REPL, no sub-LLM)
**Split:** 0 (40 train / 11 held-out)
**RMSE:** 3.87
**Score:** 0.8066

## Comparison (Split 0)

| Method | RMSE |
|--------|------|
| OLS Regression | 5.45 |
| Predict (Gemini 3 Flash) | 4.21 |
| **Predict (Gemini 3.1 Pro)** | **3.87** |
| GEPA Baseline RLM (Gemini 3 Flash) | 5.85 |
| GEPA Best Mutation RLM (Gemini 3 Flash) | 2.48 |

## Per-State Results

| State | Predicted | Actual | Error |
|-------|-----------|--------|-------|
| UT | -16.50 | -21.93 | +5.43 |
| SD | -1.50 | 0.00 | -1.50 |
| WA | -24.80 | -25.19 | +0.39 |
| IL | -15.20 | -21.81 | +6.61 |
| MO | -9.00 | -10.97 | +1.97 |
| NY | -19.80 | -14.02 | -5.78 |
| LA | -5.50 | -4.21 | -1.29 |
| NC | -13.00 | -13.06 | +0.06 |
| AR | -8.50 | -6.70 | -1.80 |
| NM | -9.80 | -15.68 | +5.88 |
| IN | -10.80 | -7.30 | -3.50 |

## Model Response

To predict the housing crash severity for the held-out states, we can analyze the relationships in the training data using the economic indicators provided. The 2008 housing crash was largely driven by the unraveling of speculative bubbles, making pre-crash appreciation (appreciation_03_06) the strongest predictor. Population growth (pop_growth_03_06) acts as an amplifier: rapid growth fueled overbuilding (as seen in AZ, FL, NV), which worsened the crash. Meanwhile, weak local economies (high ur_2006) struggled more when the bubble burst, particularly in the Rust Belt (e.g., MI, OH).

Here is the economic rationale for each held-out state based on comparable training states:

**WA (Washington):** Very similar profile to Oregon (appreciation ~44.8%, pop_growth ~3.4%). The Pacific Northwest had a pronounced bubble and a significant subsequent correction. Expect a crash similarly deep to OR (-25.98%).

**NY (New York):** Closely resembles neighboring Tri-State and Northeast areas like NJ (crash -22.13%) and CT (crash -18.76%). With an appreciation of 40.29% and slight population decline, it sits squarely between them.

**UT (Utah):** Experienced moderate-high appreciation (23.39%) and high population growth (7.01%). Its metrics place it between Colorado (crash -10.14%) and Idaho (crash -26.95%).

**IL (Illinois):** Fits the profile of Midwest states with medium appreciation and low population growth (like MN, WI, PA). The deep crash in the Chicago metro pulls the state average down.

**NC (North Carolina):** Metrics align well with neighbors SC (crash -13.02%) and TN (crash -8.92%). It did not suffer the massive overbuilding seen in Georgia (-24.38%).

**IN (Indiana):** A classic Rust Belt profile similar to Ohio (crash -12.93%), but with slightly better unemployment and lower appreciation, pointing to a slightly milder correction than OH and far milder than MI.

**NM (New Mexico):** Best compared to states with similar rural-to-urban population dynamics and appreciation spikes like Montana (crash -10.06%) and Wyoming (crash -7.70%).

**MO (Missouri) & AR (Arkansas):** Both display moderate appreciation (18-20%) and standard unemployment/income. They benchmark well against Tennessee, Oklahoma, and Kansas, which saw mild, single-digit corrections.

**LA (Louisiana):** Anomalous due to Hurricane Katrina in 2005 (hence the -4.83% population drop). Its housing market was buoyed by post-storm rebuilding and a booming oil industry through 2008, sparing it from a massive crash, similar to Texas and Mississippi.

**SD (South Dakota):** Aligns with Great Plains states like North Dakota (crash 0.00%), Iowa (crash 0.00%), and Nebraska (crash -2.88%), where the housing bubble virtually never existed.

## Predictions

```json
[
  {"state": "UT", "predicted_crash_pct": -16.50},
  {"state": "SD", "predicted_crash_pct": -1.50},
  {"state": "WA", "predicted_crash_pct": -24.80},
  {"state": "IL", "predicted_crash_pct": -15.20},
  {"state": "MO", "predicted_crash_pct": -9.00},
  {"state": "NY", "predicted_crash_pct": -19.80},
  {"state": "LA", "predicted_crash_pct": -5.50},
  {"state": "NC", "predicted_crash_pct": -13.00},
  {"state": "AR", "predicted_crash_pct": -8.50},
  {"state": "NM", "predicted_crash_pct": -9.80},
  {"state": "IN", "predicted_crash_pct": -10.80}
]
```

## Observations

The model's reasoning is explicit and well-structured. It identifies comparable training states for each held-out state, references specific crash values from the training data, and accounts for idiosyncratic factors (Katrina for LA, auto industry for Rust Belt). No tools or code needed; the model mentally computes nearest-neighbor comparisons and interpolates.

Largest errors: IL (+6.61, underpredicted the crash) and NM (+5.88). Both are states where local economic structure diverges from the comparison group the model chose. IL's Chicago metro drove a deeper crash than Midwest peers suggest. NM's appreciation (32.6%) warranted a heavier crash than MT/WY comparisons imply.

This is a single split. A 20-split evaluation would be needed to compare fairly against the other methods.
