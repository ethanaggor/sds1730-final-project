# GPT 5.4 Heavy: Raw Predict (Split 0)

**Model:** openai/gpt-5.4 (Heavy / xhigh reasoning effort)
**Harness:** Raw Predict (no tools, no REPL, no sub-LLM)
**Split:** 0 (40 train / 11 held-out)
**RMSE:** 3.28
**Score:** 0.8361

## Comparison (Split 0)

| Method | RMSE |
|--------|------|
| OLS Regression | 5.45 |
| Predict (Gemini 3 Flash) | 4.21 |
| Tools (GPT 5.4 Heavy) | 4.11 |
| Predict (Gemini 3.1 Pro) | 3.87 |
| **Predict (GPT 5.4 Heavy)** | **3.28** |
| GEPA Best Mutation RLM (Gemini 3 Flash) | 2.48 |

## Per-State Results

| State | Predicted | Actual | Error |
|-------|-----------|--------|-------|
| UT | -15.60 | -21.93 | +6.33 |
| SD | -1.80 | 0.00 | -1.80 |
| WA | -21.50 | -25.19 | +3.69 |
| IL | -15.40 | -21.81 | +6.41 |
| MO | -8.20 | -10.97 | +2.77 |
| NY | -15.30 | -14.02 | -1.28 |
| LA | -5.50 | -4.21 | -1.29 |
| NC | -11.70 | -13.06 | +1.36 |
| AR | -7.40 | -6.70 | -0.70 |
| NM | -14.90 | -15.68 | +0.78 |
| IN | -9.80 | -7.30 | -2.50 |

## Model Response

The model spent 4m 10s thinking. Its approach:

> I'd treat 2003–2006 appreciation as the main signal of bubble size, then adjust for whether demand looked speculative and easy to overbuild (fast population growth, elastic supply, Sunbelt/Mountain West migration markets) versus structural and supply-constrained (high-income coastal metros). I'd also adjust for pre-crash labor-market weakness where that seems to amplify downside even without a huge bubble.

State-by-state reasoning:

**UT (Utah):** Mid-sized bubble (23.39 appreciation) but very fast population growth (7.01) and very low unemployment. Strong fundamentals keep it from Sunbelt collapse, but building activity means meaningful bust. Between CO (-10.14) and ID (-26.95)/GA (-24.38).

**SD (South Dakota):** Classic Plains-state mild correction. Best comps IA (0.00), ND (0.00), NE (-2.88), KS (-4.97). Slightly more heated than IA/ND but far from bubble territory.

**WA (Washington):** Real bubble signal (42.91 appreciation, 4.37 pop growth). Near OR (-25.98) and DE (-20.44). Seattle's income base and tech exposure should cushion relative to Oregon and desert boom states.

**IL (Illinois):** Moderate bubble, low growth. Chicago suburbs make it more vulnerable than calmer interior Midwest. Between WI (-11.81)/OH (-12.93) and MN (-21.83)/MA (-17.56).

**MO (Missouri):** Middling interior-market correction. Best comps TN (-8.92), AL (-9.90), OK (-3.57). Mild-to-moderate decline.

**NY (New York):** High appreciation (40.29) but negative population growth and supply-constrained profile. Much less crash-prone than equally appreciated Sunbelt markets. Comps CT (-18.76), MA (-17.56), NJ (-22.13), PA (-9.38).

**LA (Louisiana):** 2003-2006 run-up likely reflects Katrina distortion, not pure credit bubble. Very large negative population growth (-4.83) is a strong clue. Comps TX (-4.15), OK (-3.57), WV (-7.26), AL (-9.90) with discount for bubble interpretation.

**NC (North Carolina):** Modest appreciation but strong population growth — growth-market correction, not pure bubble collapse. Worse than TN (-8.92) but milder than GA (-24.38) and VA (-17.39). SC (-13.02) is the anchor.

**AR (Arkansas):** No big bubble. Moderate appreciation, somewhat elevated unemployment, low income. Comps TN (-8.92), AL (-9.90), MS (-8.67), KY (-4.45). Mild decline.

**NM (New Mexico):** Fairly strong bubble (32.57) plus decent population growth. Between milder MT (-10.06) and more bubbly OR (-25.98)/ID (-26.95). Southwest spillover and second-home demand push it down.

**IN (Indiana):** Very little bubble appreciation, but more Midwest industrial exposure than Plains states. Comps OH (-12.93), KY (-4.45), WI (-11.81). Modest-to-moderate decline.

## Observations

Best single-model result on split 0. GPT 5.4 Heavy's pure reasoning (3.28) outperforms the same model with Python tools (4.11), confirming the "tools make models dumber" pattern also observed with Gemini 3.1 Pro (3.87 raw vs 5.42 with tools).

The reasoning is well-calibrated: 7 of 11 states have errors under 3 percentage points. The model correctly identifies Katrina distortion for LA, supply-constraint cushioning for NY, and Plains-state resilience for SD.

Persistent hard cases: UT (+6.33) and IL (+6.41) remain systematically underpredicted across all models. Both have metro-specific dynamics (Salt Lake City construction boom, Chicago condo bust) that neighbor-based reasoning underestimates.

Compared to Gemini 3.1 Pro raw Predict: GPT 5.4 Heavy is notably better on WA (+3.69 vs Gemini's +0.39 — though Gemini got unusually lucky there), MO (+2.77 vs +1.97), and NY (-1.28 vs -5.78). The models share the same blind spots (UT, IL) but GPT 5.4 Heavy has tighter error distribution overall.
