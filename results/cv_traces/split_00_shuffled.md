## Analysis Approach

I'll identify comparable training states for each prediction, focusing on: (1) appreciation as a bubble signal, (2) unemployment as labor market vulnerability, (3) income as a buffer, (4) population growth as fundamental vs. speculative demand. The training data is noisy (e.g., NV at 0.00 despite 80% appreciation; AL at -46.01 with only 18% appreciation), so I'll use a comparative approach over any simple formula.

Training median crash: approximately -13.0%. Training mean: approximately -16.6%.

---

## State-by-State Reasoning

### UT (Utah)
**Features:** appreciation 23.39, ur 2.87, pcpi 31107, pop_growth 7.01

Utah has the lowest unemployment of any state in the dataset (2.87) and strong population growth (7.01), both protective factors. Appreciation is moderate at 23.39. Income is low (31107), which adds some vulnerability.

**Comparables:**
- CO (11.88, ur 4.25, pcpi 39869, pop 4.23) → -4.97: Lower appreciation and higher income, but similar western economy
- ND (22.30, ur 3.12, pcpi 33120, pop 1.66) → -2.88: Near-identical appreciation and ur, but much lower pop growth
- TX (11.68, ur 4.98, pcpi 35422, pop 6.03) → -4.45: Similar pop growth, lower appreciation
- ID (39.45, ur 3.39, pcpi 31244, pop 7.72) → -24.38: Very similar income and pop growth, but much higher appreciation

UT's low ur and high pop growth pull it toward the CO/ND/TX cluster, but its low income and slightly higher appreciation add risk relative to those. Not as exposed as ID.

**Prediction: -9.0**

---

### SD (South Dakota)
**Features:** appreciation 17.95, ur 3.01, pcpi 34983, pop_growth 2.53

Classic plains state profile: low appreciation, low unemployment, moderate income, modest population growth. Very similar to its northern neighbor.

**Comparables:**
- ND (22.30, ur 3.12, pcpi 33120, pop 1.66) → -2.88: Nearly identical profile, slightly higher appreciation
- KS (12.49, ur 4.42, pcpi 35411, pop 1.47) → -7.26: Similar income, lower appreciation, higher ur
- IA (13.29, ur 3.69, pcpi 34197, pop 1.38) → -10.06: Similar income and geography
- OK (14.28, ur 3.91, pcpi 34650, pop 2.54) → -11.93: Very similar pop growth and income

SD is closest to ND, with slightly lower appreciation but modestly higher pop growth. Plains and energy states generally weathered the crisis well due to minimal speculative activity.

**Prediction: -6.0**

---

### WA (Washington)
**Features:** appreciation 42.91, ur 4.99, pcpi 39744, pop_growth 4.37

Pacific Northwest state with moderate-high appreciation driven by Seattle's tech economy. Moderate unemployment and income provide some buffer.

**Comparables:**
- OR (44.87, ur 5.39, pcpi 34488, pop 3.48) → -13.02: Geographic neighbor, nearly identical appreciation, but WA has higher income and lower ur
- DE (45.63, ur 3.58, pcpi 40736, pop 5.04) → -26.95: Similar appreciation and income, but much worse outcome
- VT (41.92, ur 3.68, pcpi 36609, pop 0.81) → -6.55: Similar appreciation, lower pop growth
- CT (36.58, ur 4.42, pcpi 53224, pop 0.95) → -7.70: Similar appreciation, much higher income

Oregon is the most natural comparison. WA's higher income (39744 vs. 34488) and lower ur (4.99 vs. 5.39) provide modest protection, but the large spread in outcomes for similar-appreciation states (VT -6.55 to DE -26.95) introduces uncertainty.

**Prediction: -13.0**

---

### IL (Illinois)
**Features:** appreciation 25.87, ur 4.62, pcpi 40021, pop_growth 0.70

Moderate appreciation with near-stagnant population growth. Chicago's housing market had meaningful subprime exposure. The combination of moderate appreciation with very low pop growth suggests that demand was not fundamentals-driven.

**Comparables:**
- MN (24.94, ur 4.06, pcpi 39362, pop 2.18) → -22.13: Nearly identical appreciation and income
- PA (34.06, ur 4.73, pcpi 37803, pop 1.10) → -17.39: Similar ur and low pop growth
- NJ (48.76, ur 4.69, pcpi 47366, pop 0.70) → -18.48: Identical pop growth, similar ur
- WI (22.65, ur 4.69, pcpi 36047, pop 1.80) → -3.57: Similar appreciation and ur, but dramatically different outcome (the MN/WI split at similar features is the most confounding pattern in this dataset)

IL's very low pop growth (0.70) and moderate appreciation align it more with the PA/NJ cluster than with WI. Chicago's size, subprime exposure, and labor market dynamics push this toward the more negative end.

**Prediction: -17.0**

---

### MO (Missouri)
**Features:** appreciation 18.82, ur 4.89, pcpi 33860, pop_growth 2.33

Low-moderate appreciation with moderate economic indicators across the board. Typical heartland profile without extreme bubble dynamics.

**Comparables:**
- TN (17.18, ur 5.22, pcpi 32878, pop 4.12) → -17.56: Nearly identical appreciation, similar income, but higher pop growth
- OK (14.28, ur 3.91, pcpi 34650, pop 2.54) → -11.93: Very similar pop growth and income
- IA (13.29, ur 3.69, pcpi 34197, pop 1.38) → -10.06: Similar income, lower appreciation
- GA (15.17, ur 4.66, pcpi 34574, pop 6.18) → -10.14: Similar ur and income

MO sits between TN's worse outcome and the OK/IA/GA cluster. Its pop growth (2.33) is lower than TN and GA, which limits the fundamental demand buffer. Moderate ur (4.89) is a mild negative.

**Prediction: -12.0**

---

### NY (New York)
**Features:** appreciation 40.29, ur 4.50, pcpi 43760, pop_growth -0.37

High appreciation with high income but negative population growth. NYC's economy provided insulation, but negative pop growth signals that appreciation was not demand-driven. The market bifurcation (resilient Manhattan vs. weaker outer boroughs and upstate) is reflected in moderate features.

**Comparables:**
- CT (36.58, ur 4.42, pcpi 53224, pop 0.95) → -7.70: Similar appreciation and ur, but much higher income
- MA (28.21, ur 4.69, pcpi 47311, pop -0.19) → -4.15: Negative pop growth and high income, but lower appreciation
- NJ (48.76, ur 4.69, pcpi 47366, pop 0.70) → -18.48: Higher appreciation and income
- RI (48.54, ur 5.26, pcpi 38719, pop -0.77) → -29.40: Negative pop growth with lower income, much worse outcome

NY's high income (43760) puts it in the CT/MA/NJ bracket, which is protective. But negative pop growth combined with 40% appreciation is a bearish signal (compare MA's lower appreciation with similar pop dynamics). NY splits between the insulated high-income cluster (CT/MA) and the more exposed Northeast corridor (NJ/RI).

**Prediction: -14.0**

---

### LA (Louisiana)
**Features:** appreciation 22.89, ur 4.14, pcpi 33627, pop_growth -4.83

The extreme negative pop growth (-4.83) is unique in the dataset and almost certainly driven by Hurricane Katrina (2005) displacement. This makes standard pop-growth interpretation unreliable: the negative figure reflects diaspora, not economic decline. Katrina simultaneously destroyed housing supply and displaced demand, while rebuilding generated significant construction activity that supported prices.

**Comparables:**
- OK (14.28, ur 3.91, pcpi 34650, pop 2.54) → -11.93: Similar income and ur, ignoring pop distortion
- ND (22.30, ur 3.12, pcpi 33120, pop 1.66) → -2.88: Similar appreciation and income
- KY (14.25, ur 5.73, pcpi 30476, pop 2.48) → -9.38: Similar southern economy
- MS (16.40, ur 6.38, pcpi 27827, pop 1.28) → -11.81: Gulf neighbor, also Katrina-affected

If I discount the pop growth signal as Katrina noise, LA's fundamentals (moderate appreciation, moderate ur, moderate-low income) suggest a moderate decline. The rebuilding demand likely provided some price support.

**Prediction: -10.0**

---

### NC (North Carolina)
**Features:** appreciation 16.94, ur 4.73, pcpi 34189, pop_growth 5.87

Low appreciation with strong population growth and moderate economic indicators. The Southeast sunbelt migration story, but without the bubble-level appreciation seen in FL or AZ.

**Comparables:**
- GA (15.17, ur 4.66, pcpi 34574, pop 6.18) → -10.14: Extremely similar on all four features; geographic neighbor
- TX (11.68, ur 4.98, pcpi 35422, pop 6.03) → -4.45: Similar pop growth, lower appreciation
- TN (17.18, ur 5.22, pcpi 32878, pop 4.12) → -17.56: Similar appreciation but lower pop growth and higher ur
- OK (14.28, ur 3.91, pcpi 34650, pop 2.54) → -11.93: Similar appreciation and income

NC is nearly a clone of GA (15.17 appreciation, 4.66 ur, 34574 pcpi, 6.18 pop). Slightly higher appreciation (16.94 vs 15.17) is essentially neutral. High pop growth (5.87) reflects genuine migration demand, which should partially support prices.

**Prediction: -11.0**

---

### AR (Arkansas)
**Features:** appreciation 20.02, ur 5.23, pcpi 29376, pop_growth 3.56

Low-moderate appreciation with the highest ur in the held-out set and the lowest income (29376). This vulnerability profile resembles the lower-income southern states that performed poorly.

**Comparables:**
- KY (14.25, ur 5.73, pcpi 30476, pop 2.48) → -9.38: Similar ur and income
- TN (17.18, ur 5.22, pcpi 32878, pop 4.12) → -17.56: Nearly identical ur and pop growth
- WV (25.64, ur 4.77, pcpi 28528, pop 0.86) → -20.44: Similar income, higher appreciation
- MS (16.40, ur 6.38, pcpi 27827, pop 1.28) → -11.81: Similar income and geography

AR's ur (5.23) closely matches TN (5.22), and its pop growth (3.56) is close to TN's (4.12). But AR's income is significantly lower (29376 vs. 32878), adding vulnerability. The very low income parallels WV's, but AR has much better pop growth (3.56 vs. 0.86).

**Prediction: -14.0**

---

### NM (New Mexico)
**Features:** appreciation 32.57, ur 4.23, pcpi 30433, pop_growth 4.50

Moderate appreciation with low income (30433), a mountain/western state. The appreciation is meaningfully higher than the low-growth heartland but below the bubble states.

**Comparables:**
- MT (36.61, ur 3.37, pcpi 31870, pop 3.60) → 0.00: Similar income and pop growth, slightly higher appreciation but much lower ur
- WY (34.89, ur 3.07, pcpi 43805, pop 3.82) → -8.67: Similar appreciation and pop, but much higher income
- ID (39.45, ur 3.39, pcpi 31244, pop 7.72) → -24.38: Similar income, higher appreciation and pop growth
- OR (44.87, ur 5.39, pcpi 34488, pop 3.48) → -13.02: Higher appreciation and ur

NM falls between MT (0.00) and ID (-24.38) among mountain states. NM's ur (4.23) is notably higher than MT (3.37), WY (3.07), or ID (3.39), and its income (30433) is the lowest in this peer group. These factors push NM away from MT's insulation and toward a moderate decline.

**Prediction: -12.0**

---

### IN (Indiana)
**Features:** appreciation 8.68, ur 5.02, pcpi 32905, pop_growth 2.20

The lowest appreciation in the held-out set (8.68), indicating virtually no bubble. However, Indiana's manufacturing-dependent economy makes it vulnerable through job losses rather than bubble deflation. A "vulnerability crash" rather than a "bubble crash."

**Comparables:**
- OH (9.43, ur 5.43, pcpi 33976, pop 0.41) → -18.76: Rust Belt neighbor, nearly identical appreciation, similar ur and income
- MI (8.86, ur 6.87, pcpi 33563, pop -0.05) → -19.98: Closest match on appreciation, but much worse ur and pop growth
- IA (13.29, ur 3.69, pcpi 34197, pop 1.38) → -10.06: Midwest but less manufacturing-dependent
- KY (14.25, ur 5.73, pcpi 30476, pop 2.48) → -9.38: Similar ur and pop growth

IN is squarely in the Rust Belt orbit of OH (-18.76) and MI (-19.98), but with better ur (5.02 vs. 5.43/6.87) and better pop growth (2.20 vs. 0.41/-0.05). These are meaningful protective factors. IN's outcome should be less severe than OH/MI but worse than the stable heartland (IA/KS).

**Prediction: -15.0**

---

## Final Predictions

```json
[
  {"state": "UT", "predicted_crash_pct": -9.00},
  {"state": "SD", "predicted_crash_pct": -6.00},
  {"state": "WA", "predicted_crash_pct": -13.00},
  {"state": "IL", "predicted_crash_pct": -17.00},
  {"state": "MO", "predicted_crash_pct": -12.00},
  {"state": "NY", "predicted_crash_pct": -14.00},
  {"state": "LA", "predicted_crash_pct": -10.00},
  {"state": "NC", "predicted_crash_pct": -11.00},
  {"state": "AR", "predicted_crash_pct": -14.00},
  {"state": "NM", "predicted_crash_pct": -12.00},
  {"state": "IN", "predicted_crash_pct": -15.00}
]
```
