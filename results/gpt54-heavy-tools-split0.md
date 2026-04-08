# GPT 5.4 Heavy: Tools (Split 0)

**Model:** openai/gpt-5.4 (Heavy / xhigh reasoning effort)
**Harness:** ChatGPT with Python tools (execute_python with numpy/pandas)
**Split:** 0 (40 train / 11 held-out)
**RMSE:** 4.11
**Score:** 0.7945

## Comparison (Split 0)

| Method | RMSE |
|--------|------|
| OLS Regression | 5.45 |
| Predict (Gemini 3 Flash) | 4.21 |
| **Tools (GPT 5.4 Heavy)** | **4.11** |
| Predict (Gemini 3.1 Pro) | 3.87 |
| GEPA Best Mutation RLM (Gemini 3 Flash) | 2.48 |

## Per-State Results

| State | Predicted | Actual | Error |
|-------|-----------|--------|-------|
| UT | -15.80 | -21.93 | +6.13 |
| SD | -2.90 | 0.00 | -2.90 |
| WA | -19.20 | -25.19 | +5.99 |
| IL | -14.20 | -21.81 | +7.61 |
| MO | -6.60 | -10.97 | +4.37 |
| NY | -17.80 | -14.02 | -3.78 |
| LA | -7.20 | -4.21 | -2.99 |
| NC | -13.10 | -13.06 | -0.04 |
| AR | -8.40 | -6.70 | -1.70 |
| NM | -14.80 | -15.68 | +0.88 |
| IN | -7.10 | -7.30 | +0.20 |

## Approach

The model spent 6m 14s of "thinking" and executed 15 Python code cells. Its strategy:

1. **Correlation analysis:** Confirmed appreciation (r = -0.68) and population growth (r = -0.52) as primary signals; unemployment near-zero correlation.
2. **Weighted kNN:** Tested 5 weight configurations across features, settled on appreciation (0.45) + population growth (0.35) + income (0.15) + unemployment (0.05).
3. **Regional segmentation:** Assigned states to Census regions (West, Midwest, Northeast, South), computed region-specific nearest neighbors.
4. **Combo model:** 60% overall kNN + 40% regional kNN, with manual domain adjustments for outliers (LA post-Katrina, WA tech sector).
5. **Tercile analysis:** Binned training states by appreciation and population growth terciles to verify nonlinear interaction (high appreciation + high growth = severe crash).

Excluded AK, HI, DC as analogs due to unique market dynamics.

## Observations

Despite extensive computational analysis (correlation matrices, multiple kNN variants, regional segmentation, tercile pivots), the model's predictions are only marginally better than Gemini 3 Flash's pure reasoning (4.21 vs 4.11) and worse than Gemini 3.1 Pro's raw Predict (3.87).

The same "tools make models dumber" pattern observed with Gemini 3.1 Pro + tools: computation anchors the model on neighbor averages rather than allowing domain judgment about bubble dynamics. The model correctly identified the key features but mechanically averaged neighbors instead of reasoning about why IL's Chicago metro or WA's coastal speculation would amplify beyond what neighbors suggest.

Largest errors: IL (+7.61, systematically underpredicted — kNN neighbors MN, WI, PA don't capture Chicago's severity) and WA (+5.99, nearest Western analogs OR/ID averaged down by MT/WY/CO). Near-perfect: NC (-0.04), IN (+0.20).

## Prompt

The model received the anti-regression prompt (banning statsmodels, sklearn, scipy.optimize, np.polyfit, np.linalg.lstsq) with the split 0 training data and `execute_python` tool definition. It was instructed to use domain reasoning and analytical methods rather than regression.
