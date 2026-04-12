## Analysis Framework

I'll extract key patterns from the training data, then apply them state by state.

### Key Patterns in the Training Data

**Pattern 1: High appreciation is *protective*, not risky.** This is the most counterintuitive finding. States with appreciation >60% almost uniformly had mild crashes: CA (74% → 0.00), NV (80% → -8.92), AZ (73% → -4.15), MD (65% → -2.88), HI (81% → -13.06). The lone exception is DE (46% → -55.69), which is a severe outlier.

**Pattern 2: Low income amplifies crash severity.** States with pcpi below ~32k cluster toward bad outcomes: MS (27.8k → -46.01), AR (29.4k → -24.38), AL (31.3k → -25.98), SC (30.8k → -22.13). High income (>42k) is protective: MA (-3.57), WY (-4.97), NY (-9.90), CA (0.00).

**Pattern 3: Low appreciation + low income is the worst combination.** Southern/lower-income states with modest appreciation averaged roughly -27%: MS, AL, GA, AR, SC, TN, IN.

**Pattern 4: Negative/near-zero population growth has a mild protective association.** NY (-0.37 → -9.90), MA (-0.19 → -3.57), MI (-0.05 → -7.70) all had mild crashes, possibly because less migration-driven speculation meant less bubble.

**Pattern 5: Significant noise exists.** IL (appreciation 26, pcpi 40k) → 0.00 vs MN (appreciation 25, pcpi 39k) → -44.73. Nearly identical features, ~45 points apart. This limits precision.

---

## State-by-State Predictions

### RI (appreciation 48.54, ur 5.26, pcpi 38,719, pop_growth -0.77)

**Closest comps:** NJ (48.76 → -18.48), VA (53.63 → -13.11), OR (44.87 → -6.70). Excluding the DE outlier, states in the 45-55 appreciation band average about -12.8.

RI has the highest ur among these comps (5.26), which is a risk factor, and lower income than NJ (38.7k vs 47.4k). However, its negative pop growth echoes MA (-0.19 → -3.57) and NY (-0.37 → -9.90), which were protective. Net: slightly milder than NJ, pulled toward mid-teens.

**Prediction: -13.0**

---

### CT (appreciation 36.58, ur 4.42, pcpi 53,224, pop_growth 0.95)

**Closest comps:** VT (41.92 → 0.00), MA (28.21 → -3.57), WY (34.89 → -4.97). CT has the second-highest income in the entire dataset (after DC), exceeding even MA. High-income states averaging >43k pcpi have mean crash around -6.5 (excluding NJ outlier).

CT dominates MA on nearly every dimension: higher income (53k vs 47k), higher appreciation (37 vs 28), lower ur (4.42 vs 4.69). Its New England neighbors VT and MA had extremely mild crashes. Low pop growth (0.95) matches IL (0.70 → 0.00) and VT (0.81 → 0.00).

**Prediction: -6.0**

---

### NM (appreciation 32.57, ur 4.23, pcpi 30,433, pop_growth 4.50)

**Closest comps:** WV (25.64, 28.5k → -17.56), ME (34.89, 34.2k → -10.06), SC (19.42, 30.8k → -22.13).

NM's low income (30.4k) places it squarely in the vulnerable tier with AR (29.4k → -24.38), KY (30.5k → -8.67), and SC (30.8k → -22.13). However, its moderate appreciation (32.57) is higher than most of these, which is somewhat protective. Its decent ur (4.23) helps relative to SC (6.35). WV at -17.56 with lower appreciation and income is a reasonable anchor, adjusted slightly worse for NM's higher pop growth (speculative demand risk).

**Prediction: -18.0**

---

### PA (appreciation 34.06, ur 4.73, pcpi 37,803, pop_growth 1.10)

**Closest comp:** ME (34.89, 4.71, 34.2k, 1.31 → -10.06). Nearly identical on every dimension. PA has slightly higher income (37.8k vs 34.2k) which is mildly protective, but otherwise the profiles are remarkably similar. WV (25.64, 4.77, 28.5k → -17.56) brackets the lower end; NY (40.29, 4.50, 43.8k → -9.90) brackets the upper end.

**Prediction: -11.0**

---

### CO (appreciation 11.88, ur 4.25, pcpi 39,869, pop_growth 4.23)

**Closest comps by appreciation:** NE (11.88 → -25.30), TX (11.68 → -7.26), KS (12.49 → -7.30), IA (13.29 → -6.55). These range from -6.55 to -25.30; TX/KS/IA cluster around -7, while NE is an outlier.

CO's defining advantage is its income: 39.9k is far above NE (35.7k), TX (35.4k), and KS (35.4k). In the high-income tier, this level sits near IL (40k → 0.00). However, CO's low appreciation (11.88) is a genuine risk factor in this dataset. Balancing the mild-crash cluster (TX/KS/IA ~-7) against NE's outlier, and giving credit for CO's income advantage, I anchor between these groups.

**Prediction: -10.0**

---

### WI (appreciation 22.65, ur 4.69, pcpi 36,047, pop_growth 1.80)

**Closest comp:** ND (22.30, 3.12, 33.1k, 1.66 → -13.02). Very similar appreciation and pop growth. WI has higher ur (4.69 vs 3.12), which is a negative, but also higher income (36k vs 33k).

The Midwest is wildly volatile in this data: IL (0.00), MN (-44.73), IA (-6.55), IN (-29.40), MO (-4.45). WI's moderate-in-every-way profile doesn't clearly signal either extreme. The higher ur relative to ND pushes worse; the higher income pulls milder. I weight toward ND's -13.02 but shade worse for the ur gap.

**Prediction: -16.0**

---

### NH (appreciation 31.83, ur 3.52, pcpi 42,866, pop_growth 2.23)

**Closest comps:** WY (34.89, 3.07, 43.8k, 3.82 → -4.97), VT (41.92, 3.68, 36.6k, 0.81 → 0.00), MA (28.21, 4.69, 47.3k, -0.19 → -3.57).

NH has strong fundamentals: high income (42.9k), low ur (3.52), moderate appreciation. It shares WY's profile of high income + low ur + moderate appreciation almost exactly. VT (New England neighbor) had zero crash. MA (New England, high income) had -3.57. The high-income, low-ur cluster averages around -3 to -5.

**Prediction: -5.0**

---

### OH (appreciation 9.43, ur 5.43, pcpi 33,976, pop_growth 0.41)

**Closest comps:** IN (8.68, 5.02, 32.9k, 2.20 → -29.40), MI (8.86, 6.87, 33.6k, -0.05 → -7.70). Nearly identical appreciation to both, and ur/income between them.

OH's very low pop growth (0.41) is much closer to MI (-0.05) than IN (2.20), which might favor a milder outcome. But MI's crash was mild partly despite having the highest ur in training (6.87), a quirk. OH's ur (5.43) sits between IN (5.02) and MI (6.87). Averaging IN and MI gives -18.55; adjusting toward MI for the pop growth similarity but hedging for the IN risk.

**Prediction: -17.0**

---

### UT (appreciation 23.39, ur 2.87, pcpi 31,107, pop_growth 7.01)

**Closest comp:** ID (39.45, 3.39, 31.2k, 7.72 → -17.39). Mountain West neighbor with nearly identical income and pop growth. ND (22.30 → -13.02) matches on appreciation.

UT has the lowest ur in the entire combined dataset (2.87), signaling exceptional labor market strength. HI, with the next-lowest ur (2.57), got -13.06. UT's high pop growth (7.01) is similar to ID and FL (-14.02). ID at -17.39 is the natural anchor, adjusted milder for UT's superior labor market. The very low ur should provide meaningful cushion.

**Prediction: -12.0**

---

### LA (appreciation 22.89, ur 4.14, pcpi 33,627, pop_growth -4.83)

**Closest comps by profile:** ND (22.30 → -13.02), TN (17.18, 5.22, 32.9k → -21.81), SC (19.42, 6.35, 30.8k → -22.13). By region (southern), the average crash is roughly -25.

LA's defining feature is extreme negative pop growth (-4.83), driven by Hurricane Katrina. This is far below any training state (next-worst is NY at -0.37). The population loss simultaneously destroyed housing stock (reducing supply) and eliminated demand. The net effect on prices is ambiguous, but the massive economic disruption and uncertainty about rebuilding and future disasters likely dominated. Comparable southern states (AL -25.98, TN -21.81, SC -22.13, AR -24.38) anchor the regional baseline. I shade slightly milder than this average because LA's appreciation (22.89) is a bit higher and ur (4.14) is lower than most of these comps.

**Prediction: -22.0**

---

### WA (appreciation 42.91, ur 4.99, pcpi 39,744, pop_growth 4.37)

**Closest comp:** OR (44.87, 5.39, 34.5k, 3.48 → -6.70). Pacific Northwest neighbor with very similar appreciation. NY (40.29 → -9.90) is another comp by appreciation.

WA has substantially higher income than OR (39.7k vs 34.5k), which is protective. Its appreciation (42.91) places it in the moderate-high band where VT (41.92 → 0.00), NY (40.29 → -9.90), and OR (44.87 → -6.70) cluster. The average of these three is -5.53. WA's slightly higher ur (4.99) offsets some of the income advantage over OR. I anchor near OR at -6.70 and shade slightly worse for the higher ur.

**Prediction: -9.0**

---

## Final Predictions

```json
[
  {"state": "RI", "predicted_crash_pct": -13.0},
  {"state": "CT", "predicted_crash_pct": -6.0},
  {"state": "NM", "predicted_crash_pct": -18.0},
  {"state": "PA", "predicted_crash_pct": -11.0},
  {"state": "CO", "predicted_crash_pct": -10.0},
  {"state": "WI", "predicted_crash_pct": -16.0},
  {"state": "NH", "predicted_crash_pct": -5.0},
  {"state": "OH", "predicted_crash_pct": -17.0},
  {"state": "UT", "predicted_crash_pct": -12.0},
  {"state": "LA", "predicted_crash_pct": -22.0},
  {"state": "WA", "predicted_crash_pct": -9.0}
]
```
