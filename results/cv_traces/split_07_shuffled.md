## Analysis and Predictions

### Identifying Patterns in the Training Data

The training data is noisy. The mean crash is roughly -17%, the median around -13 to -14%. Critically, no single feature is a strong predictor: states with similar appreciation levels show wildly different outcomes (e.g., appreciation ~35%: CT at 0.00, WY at -41.04). This means I need to triangulate across multiple features and use comparable states rather than relying on any one dimension.

Key structural observations from the training data:
- **Appreciation alone is weakly predictive.** High-bubble states like FL (-4.97) and HI (-9.38) fared much better than lower-appreciation states like KS (-29.40) and SD (-27.60).
- **Low/negative population growth correlates with worse outcomes**: RI (-0.77% pop, -21.83 crash), NY (-0.37%, -26.95), MI (-0.05%, -17.39) all above-average severity.
- **Low income is a risk factor but not deterministic**: MS (27827, -55.69) vs WV (28528, -6.70).
- **Extreme outliers** (MS, DE, WA, WY) appear driven by idiosyncratic or unobservable factors.

---

### State-by-State Reasoning

**MT (Montana)** — appreciation: 36.61, UR: 3.37, income: 31870, pop: 3.60

Mountain west state, not a speculative hotspot. Closest comparable: **ID** (39.45 appreciation, 3.39 UR, 31244 income → -3.57) and **VT** (41.92, 3.68, 36609 → -6.55). Both share low UR, moderate appreciation, and modest income. ME (34.89 → -24.38) and WY (34.89 → -41.04) have similar appreciation but crashed far harder, reflecting idiosyncratic risk in the 30-40% appreciation band. Montana's strong labor market and moderate pop growth favor the milder end.

**Prediction: -9.0**

---

**TN (Tennessee)** — appreciation: 17.18, UR: 5.22, income: 32878, pop: 4.12

Low appreciation, slightly above-average UR, moderate income. Southeastern state with a diversified economy (Nashville, Memphis). Closest comparables: **NC** (16.94, 4.73 → -7.26), **AR** (20.02, 5.23 → -8.67). Both are similar southern states with low appreciation and moderate economic profiles. MO (18.82 → -25.30) and SC (19.42 → -25.19) had similar appreciation but crashed much harder, likely due to specific local dynamics. TN's moderate pop growth (4.12) and urban economic centers pull it toward the NC/AR cluster.

**Prediction: -11.0**

---

**WI (Wisconsin)** — appreciation: 22.65, UR: 4.69, income: 36047, pop: 1.80

Midwest state with moderate fundamentals across all dimensions. Natural comparables: **MN** (24.94, 4.06, 39362 → -10.97), **IL** (25.87, 4.62, 40021 → -18.48), **ND** (22.30, 3.12, 33120 → -13.02). WI sits squarely between MN and IL in economic profile. Higher UR than MN but lower than IL's effective labor market stress. The average of the three Midwest comps is -14.2; WI's fundamentals place it near that centroid.

**Prediction: -13.0**

---

**KY (Kentucky)** — appreciation: 14.25, UR: 5.73, income: 30476, pop: 2.48

Low appreciation, above-average UR, low income. Appalachian/industrial profile. **OK** (14.28 appreciation → -20.44) is the closest appreciation match but had lower UR. **IN** (8.68, 5.02, 32905 → -12.93) shares the industrial Midwest/Appalachian character. **AR** (20.02, 5.23, 29376 → -8.67) has similar income and UR. The higher UR (5.73) is a risk factor; states above 5.5% UR averaged around -18 in the training data (excluding AK's oil-economy anomaly). But the very low appreciation limits bubble exposure. Balancing these: slightly worse than IN.

**Prediction: -13.0**

---

**IA (Iowa)** — appreciation: 13.29, UR: 3.69, income: 34197, pop: 1.38

Low appreciation, low UR, moderate income, low pop growth. Stable Midwest agricultural economy. **NE** (11.88, 3.04, 35718 → -7.30) is the closest comparable: similar appreciation, low UR, moderate income, both stable agricultural economies. **CO** (11.88, 4.25 → -13.06) shares the appreciation but has a more volatile economy. Iowa's fundamentals point strongly toward the NE cluster.

**Prediction: -9.0**

---

**MA (Massachusetts)** — appreciation: 28.21, UR: 4.69, income: 47311, pop: -0.19

Moderate appreciation, moderate UR, high income, negative pop growth. Northeast knowledge economy. Within the Northeast cluster: **CT** (36.58, 53224 → 0.00), **NH** (31.83, 42866 → -19.98), **RI** (48.54, 38719 → -21.83), **NY** (40.29, 43760 → -26.95), **PA** (34.06, 37803 → -13.11). MA's appreciation is lower than all of these except PA. The negative pop growth aligns with NY and RI, which both crashed significantly. But MA's high income and lower appreciation provide some buffer. The Northeast's correction was broad-based, so MA likely falls in the middle of the pack.

**Prediction: -15.0**

---

**NJ (New Jersey)** — appreciation: 48.76, UR: 4.69, income: 47366, pop: 0.70

High appreciation, moderate UR, high income, low pop growth. **RI** (48.54, 5.26, 38719, -0.77 → -21.83) is the nearest appreciation match and shares the dense, coastal Northeast profile. **MD** (65.16, 45293 → -21.81) is a high-appreciation/high-income comp with nearly identical crash severity. **DC** (70.23, 55384 → -18.76) had even higher appreciation but only -18.76. NJ's high income provides some resilience, but the combination of high appreciation, low pop growth, and Northeast correction dynamics pushes this toward the -20 range. RI's near-identical appreciation is the strongest anchor.

**Prediction: -20.0**

---

**LA (Louisiana)** — appreciation: 22.89, UR: 4.14, income: 33627, pop: -4.83

The extreme outlier feature here is population growth at -4.83%, reflecting post-Katrina displacement. This is 4 percentage points below the worst training state (RI at -0.77%). In the training data, all three negative pop-growth states had above-average crashes: RI (-21.83), NY (-26.95), MI (-17.39). Massive population loss directly reduces housing demand. However, LA's other fundamentals are moderate (decent UR, moderate appreciation), and post-Katrina reconstruction spending partially offset demand collapse. The appreciation is moderate enough that there wasn't a huge speculative bubble to unwind. This places LA in a severe-but-not-extreme range: worse than the typical moderate-fundamentals state, but not approaching MS (-55.69).

**Prediction: -18.0**

---

**AL (Alabama)** — appreciation: 18.37, UR: 4.01, income: 31264, pop: 2.79

Low-moderate appreciation, decent UR, low income, moderate pop growth. Southern state. Closest comparables: **NC** (16.94, 4.73, 34189 → -7.26), **AR** (20.02, 5.23, 29376 → -8.67), **GA** (15.17, 4.66, 34574 → 0.00). AL's UR (4.01) is better than NC, AR, and GA. Its income is lower, but the low appreciation limits bubble exposure. GA at 0.00 seems like a positive outlier. AL should fall between GA's 0 and AR's -8.67, but pulled slightly lower by its income vulnerability and toward the cluster of southern moderate states.

**Prediction: -11.0**

---

**UT (Utah)** — appreciation: 23.39, UR: 2.87, income: 31107, pop: 7.01

Moderate appreciation, very low UR (lowest in held-out set), low income, high pop growth. Strong economic fundamentals. **ID** (39.45, 3.39, 31244, 7.72 → -3.57) is the best comparable: nearly identical income and pop growth, similar low UR, both mountain west growth states. ID had higher appreciation (39.45 vs 23.39) yet only crashed -3.57. **FL** (74.37, 3.28, 38009, 6.84 → -4.97) had much higher appreciation but similar pop growth and low UR with a mild crash. Utah's combination of the lowest UR, strong pop growth, and only moderate appreciation makes it one of the most resilient profiles. Similar to the ID/FL low-UR/high-growth cluster.

**Prediction: -6.0**

---

**NM (New Mexico)** — appreciation: 32.57, UR: 4.23, income: 30433, pop: 4.50

Moderate appreciation, moderate UR, low income, moderate pop growth. Sun Belt state. The 30-37% appreciation band is the most volatile in the training data: CT (0.00), AK (-2.88), ID (-3.57), VT (-6.55), PA (-13.11), ME (-24.38), WY (-41.04). NM's low income (30433) is a risk factor, similar to SC (30789 → -25.19), but NM has much lower UR (4.23 vs 6.35) and better pop growth. **ID** (39.45, 3.39, 31244 → -3.57) has similar income but lower UR and higher pop growth. **PA** (34.06, 4.73, 37803 → -13.11) has similar appreciation and UR but higher income. NM's low income pushes it worse than ID but its decent UR and pop growth keep it from the ME/WY zone.

**Prediction: -13.0**

---

### Final Predictions

```json
[
  {"state": "MT", "predicted_crash_pct": -9.00},
  {"state": "TN", "predicted_crash_pct": -11.00},
  {"state": "WI", "predicted_crash_pct": -13.00},
  {"state": "KY", "predicted_crash_pct": -13.00},
  {"state": "IA", "predicted_crash_pct": -9.00},
  {"state": "MA", "predicted_crash_pct": -15.00},
  {"state": "NJ", "predicted_crash_pct": -20.00},
  {"state": "LA", "predicted_crash_pct": -18.00},
  {"state": "AL", "predicted_crash_pct": -11.00},
  {"state": "UT", "predicted_crash_pct": -6.00},
  {"state": "NM", "predicted_crash_pct": -13.00}
]
```
