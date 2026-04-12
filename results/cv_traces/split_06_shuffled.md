## Analysis Framework

Before predicting, let me identify the key patterns in the training data.

**Overall mean crash: ~-15.1%**

### Key patterns observed

**1. High appreciation does NOT predict worse crashes in this data.** States with appreciation >60% (AZ -4.97, NV -9.90, CA -13.06, HI -15.68, DC -10.14) average only -10.8. The worst crashes occur at *moderate-low* appreciation levels (TN -55.69 at 17%, OK -46.01 at 14%, UT -41.04 at 23%).

**2. Low unemployment correlates with worse outcomes.** States with ur < 3.5 average -20.4 (UT -41.04, SD -29.40, NE -18.76, NH -25.30, MT -17.39, etc.), while states with ur > 5.5 average only -7.2 (MI -4.45, MS -4.15, SC -7.26).

**3. Low/negative population growth is strongly protective.** States with pop_growth < 1% average -7.7 (RI 0.00, IL 0.00, NY -3.57, MI -4.45, NJ -7.70). States with pop_growth > 5% average -17.8.

**4. High per-capita income + low pop growth is the most protective combination** (NY -3.57, IL 0.00, NJ -7.70).

---

## State-by-State Predictions

### AK (appreciation 36.14, ur 6.62, pcpi 41013, pop_growth 4.15)

Alaska's defining feature is its **very high unemployment rate (6.62)**, the highest in the test set. In the training data, high-ur states crash mildly: MI (6.87, -4.45), MS (6.38, -4.15), SC (6.35, -7.26), averaging -5.3. Alaska's high pcpi (41013) provides additional resilience, comparable to CO (-10.06, pcpi 39869). The moderate appreciation (36.14) is similar to MT (-17.39) and CT (-18.48), but those states had much lower unemployment. The high ur should dominate here.

**Prediction: -8.0**

---

### WA (appreciation 42.91, ur 4.99, pcpi 39744, pop_growth 4.37)

Washington matches well against several moderate-appreciation, high-pcpi states. The closest comparables by appreciation: VT (41.92, -8.92), NY (40.29, -3.57). By pcpi and pop_growth: CO (39869, -10.06), VA (42164, -8.67), NV (39437, -9.90). WA's moderate ur (4.99) is unremarkable, and its pop_growth (4.37) is slightly higher than most of these comparables, adding modest downward pressure. The tech-driven economy (Seattle) parallels the diversified economic bases of the -8 to -10 cohort.

**Prediction: -10.0**

---

### GA (appreciation 15.17, ur 4.66, pcpi 34574, pop_growth 6.18)

Georgia is an extremely strong match to NC across all four features:

| Feature | GA | NC (-21.93) | TX (-21.83) |
|---|---|---|---|
| appreciation | 15.17 | 16.94 | 11.68 |
| ur | 4.66 | 4.73 | 4.98 |
| pcpi | 34574 | 34189 | 35422 |
| pop_growth | 6.18 | 5.87 | 6.03 |

NC and TX are nearly identical on all features and both crashed ~-21.9. AL (18.37, -21.81) is also close. This low-appreciation, high-pop-growth, moderate-income profile represents states with sprawling suburban development (Atlanta suburbs, Research Triangle, Dallas-Fort Worth) where demand was migration-driven but fundamentals were fragile.

**Prediction: -21.5**

---

### AR (appreciation 20.02, ur 5.23, pcpi 29376, pop_growth 3.56)

Arkansas has the **lowest pcpi in the test set** (29376). Low-income comparables: MS (27827, -4.15), WV (28528, -9.38), KY (30476, -13.11), NM (30433, -4.21). These average -7.7. By appreciation, SC (19.42, -7.26) and AL (18.37, -21.81) bracket the range. The moderate ur (5.23) is almost identical to TN (5.22, -55.69) and RI (5.26, 0.00), but these are extreme outliers in opposite directions and cancel out. AR's moderate pop_growth (3.56) is similar to MT (3.60, -17.39). The low pcpi limits both the size of the bubble and the severity of speculative overbuilding, but also limits economic resilience.

**Prediction: -12.0**

---

### DE (appreciation 45.63, ur 3.58, pcpi 40736, pop_growth 5.04)

Delaware has high appreciation comparable to NJ (48.76, -7.70) and RI (48.54, 0.00), but with a critically lower ur (3.58). That low ur matches NH (3.52, -25.30) and VT (3.68, -8.92), both of which fared worse than the high-appreciation mild-crash states. The high pcpi (40736) is similar to IL (40021, 0.00) and CA (41454, -13.06), which is protective. But DE's pop_growth (5.04) is much higher than NJ (0.70) or VT (0.81), indicating migration-driven demand that may have been partially speculative. The combination of low ur + elevated pop_growth pulls DE more negative than the pure high-appreciation comparables suggest.

**Prediction: -13.0**

---

### WI (appreciation 22.65, ur 4.69, pcpi 36047, pop_growth 1.80)

Wisconsin's closest comparable is **MN** (24.94, 4.06, 39362, 2.18), which crashed -12.93. Feature-by-feature, WI has slightly lower appreciation, slightly higher ur (which should moderate), slightly lower pcpi (which adds vulnerability), and similar pop_growth. These adjustments roughly cancel. Other Midwest comparables: IL (25.87, 0.00), ND (22.30, -19.98), LA (22.89, -10.97). ND crashed harder partly due to its very low ur (3.12), which WI doesn't share. WI's ur (4.69) is squarely in the middle-of-the-pack range.

**Prediction: -13.0**

---

### FL (appreciation 74.37, ur 3.28, pcpi 38009, pop_growth 6.84)

Florida's very high appreciation (74.37) places it squarely in the bubble-state cluster: AZ (73.44, -4.97), CA (73.96, -13.06), NV (79.74, -9.90), HI (80.67, -15.68). In this training data, these states average only -10.9. AZ is the nearest neighbor by appreciation and also had high pop_growth (9.41), yet crashed only -4.97.

However, FL has two features that pull it more negative than the bubble-state average: **very low ur (3.28)**, which in this data correlates with worse outcomes (low-ur group averages -20.4), and **high pop_growth (6.84)** pointing to speculative migration demand. HI is the best composite comparable (high appreciation + low ur + similar pcpi), and HI crashed -15.68.

Balancing the protective effect of high appreciation against the risk factors of low ur and high pop_growth:

**Prediction: -12.0**

---

### OR (appreciation 44.87, ur 5.39, pcpi 34488, pop_growth 3.48)

Oregon's moderate-high appreciation matches VT (41.92, -8.92) and NJ (48.76, -7.70). But OR has notably higher ur (5.39), closer to OH (5.43, -14.02) and TN (5.22, -55.69, an outlier). The pcpi (34488) is moderate-low, similar to ME (34168, -6.55) and NC (34189, -21.93). Pop_growth (3.48) is moderate, like MT (3.60, -17.39). Excluding the TN outlier, the nearest comparables average about -12: PA (-13.02), OH (-14.02), MT (-17.39), VT (-8.92), ME (-6.55).

**Prediction: -12.0**

---

### IA (appreciation 13.29, ur 3.69, pcpi 34197, pop_growth 1.38)

Iowa is a stable agricultural economy. The best single comparable is **KS** (12.49, 4.42, 35411, 1.47), which crashed -7.30 and matches on appreciation, pcpi, and pop_growth. NE (11.88, 3.04, 35718, 1.96) matches on appreciation and pop_growth but crashed -18.76, partly driven by its even lower ur (3.04). IA's ur (3.69) is higher than NE's, which should moderate the outcome. By ur, VT (3.68, -8.92) is nearly identical. CO (11.88, -10.06) also has similar appreciation. Low pop_growth (1.38) provides some stability.

**Prediction: -10.0**

---

### ID (appreciation 39.45, ur 3.39, pcpi 31244, pop_growth 7.72)

Idaho has a distinctive and risky profile. Three of its four features match **MT** (36.61, 3.37, 31870, 3.60) remarkably well: appreciation (39.45 vs 36.61), ur (3.39 vs 3.37), and pcpi (31244 vs 31870). MT crashed -17.39. But ID's pop_growth (7.72) is more than double MT's (3.60), which is a significant risk amplifier.

The closest match on pop_growth + pcpi is **UT** (23.39, 2.87, 31107, 7.01), which crashed -41.04. ID is a hybrid of MT (3 feature match) and UT (pop_growth + pcpi match). The low pcpi combined with very high pop_growth signals an overheated market in a low-income state, where speculative building can significantly overshoot fundamentals. ID's higher appreciation (39.45 vs UT's 23.39) may provide some buffer.

**Prediction: -20.0**

---

### MA (appreciation 28.21, ur 4.69, pcpi 47311, pop_growth -0.19)

Massachusetts has the **most protective profile** in the test set: very high pcpi (47311), negative pop_growth (-0.19), and moderate appreciation. The ur (4.69) and pcpi (47311) are nearly identical to **NJ** (4.69, 47366, -7.70). The negative pop_growth aligns with **NY** (-0.37, -3.57) and **RI** (-0.77, 0.00), both of which had very mild or no crashes.

States with pop_growth < 1% average only -7.7 in crash severity. States with both high pcpi (>40k) and low pop_growth (<1%): IL (0.00), NJ (-7.70), NY (-3.57), DC (-10.14). Average: -5.4. MA's negative pop_growth and high pcpi indicate a mature, income-rich market with no speculative migration demand, providing strong downside protection.

**Prediction: -5.0**

---

## Final Predictions

```json
[
  {"state": "AK", "predicted_crash_pct": -8.00},
  {"state": "WA", "predicted_crash_pct": -10.00},
  {"state": "GA", "predicted_crash_pct": -21.50},
  {"state": "AR", "predicted_crash_pct": -12.00},
  {"state": "DE", "predicted_crash_pct": -13.00},
  {"state": "WI", "predicted_crash_pct": -13.00},
  {"state": "FL", "predicted_crash_pct": -12.00},
  {"state": "OR", "predicted_crash_pct": -12.00},
  {"state": "IA", "predicted_crash_pct": -10.00},
  {"state": "ID", "predicted_crash_pct": -20.00},
  {"state": "MA", "predicted_crash_pct": -5.00}
]
```
