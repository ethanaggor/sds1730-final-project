## Analysis Framework

Before predicting, I need to extract the key patterns from the 40 training states. The main drivers of crash severity in this data are:

1. **Appreciation (bubble size)**: Generally correlated with worse crashes, but with enormous variance. NV (79.74 appreciation) crashed -55.69, while FL (74.37) crashed only -11.93.
2. **Population growth**: Amplifies crashes by proxying speculative/construction demand. NV's 12.18 pop growth vs FL's 6.84 helps explain the gap above.
3. **Per-capita income**: Strong buffer. States above ~$43K (DC, NJ, WY, AK, NY) cluster at the mild end. DC (55384 income, 70.23 appreciation) crashed only -4.45.
4. **Unemployment**: Higher pre-crisis unemployment means more economic fragility and subprime exposure.

Key benchmarks from the training data:

| Profile | Representative States | Crash Range |
|---|---|---|
| Very high appreciation + high pop growth | NV (-55.69), AZ (-17.56) | Severe |
| High appreciation + high income | DC (-4.45), NJ (-3.57) | Mild |
| Moderate appreciation + stable economy | KS (-7.30), SD (-7.26), CO (-4.15) | Mild |
| Low appreciation + high unemployment | OH (-12.93), IN (-8.67) | Moderate |
| High pop growth + low/mod appreciation | TX (-21.93), NC (-15.68) | Moderate-severe |

---

## State-by-State Predictions

### GA (appreciation 15.17, ur 4.66, pcpi 34574, pop 6.18)

**Best comparable: NC** (16.94, 4.73, 34189, 5.87) at -15.68. GA and NC are strikingly similar across all four features: moderate appreciation, moderate unemployment, nearly identical income, and high population growth. GA has slightly less appreciation and slightly more pop growth. Atlanta was a major foreclosure hotspot with significant subprime exposure and suburban sprawl, making it at least as vulnerable as NC.

Among high-pop-growth states (>5%), the average crash is about -21.4, but GA's low appreciation keeps it from the extreme end. TX (11.68, 6.03 pop) at -21.93 is also comparable but has lower appreciation.

**Prediction: -16.0**

---

### IA (appreciation 13.29, ur 3.69, pcpi 34197, pop 1.38)

**Best comparables: KS** (12.49, 4.42, 35411, 1.47) at -7.30; **SD** (17.95, 3.01, 34983, 2.53) at -7.26; **OK** (14.28, 3.91, 34650, 2.54) at -6.55.

Iowa is a textbook stable agricultural state. Low appreciation (no bubble), low unemployment (strong labor market), moderate income, and low population growth (no speculative inflow). It clusters with the stable Plains/Midwest states that largely avoided the crisis. CO (11.88 appreciation) at -4.15 is also comparable but has higher income and pop growth.

**Prediction: -6.5**

---

### AR (appreciation 20.02, ur 5.23, pcpi 29376, pop 3.56)

**Best comparables: SC** (19.42, 6.35, 30789, 5.00) at -10.06; **WV** (25.64, 4.77, 28528, 0.86) at -10.14; **MS** (16.40, 6.38, 27827, 1.28) at -13.06.

AR has the lowest income in either dataset (29376), making it economically vulnerable. However, appreciation was moderate (20.02) and the state wasn't a major speculative market. It closely resembles SC in appreciation and income bracket, though with better unemployment (5.23 vs 6.35). KY (14.25, 5.73, 30476) at -4.21 is also in the low-income group but had much less appreciation.

The low-income / moderate-appreciation cluster (SC, WV, MS) consistently lands around -10 to -13. AR's slightly better unemployment offsets its slightly lower income relative to SC.

**Prediction: -9.5**

---

### OR (appreciation 44.87, ur 5.39, pcpi 34488, pop 3.48)

**Best comparable: WA** (42.91, 4.99, 39744, 4.37) at -8.92. Geographic neighbor with similar appreciation. But OR has meaningfully worse unemployment (+0.40) and much lower income (-$5,256), both indicating greater economic vulnerability.

Also comparable: **ID** (39.45, 3.39, 31244, 7.72) at -13.11; **MT** (36.61, 3.37, 31870, 3.60) at -11.81; **RI** (48.54, 5.26, 38719, -0.77) at -10.97. OR's unemployment and income profile push it notably worse than WA, toward the ID/MT/RI range.

Portland had significant appreciation but the state lacked the extreme speculative pop growth of NV/AZ. The Pacific Northwest tech economy provided some resilience, but OR's weaker economic fundamentals compared to WA warrant a meaningfully worse outcome.

**Prediction: -12.5**

---

### HI (appreciation 80.67, ur 2.57, pcpi 38315, pop 4.68)

The highest appreciation in either dataset. Comparable high-appreciation training states:
- **NV** (79.74) at -55.69: Nearly identical appreciation, but NV had extreme pop growth (12.18 vs 4.68) and higher unemployment (4.17 vs 2.57). NV's crash was driven by massive speculative construction.
- **FL** (74.37) at -11.93: Similar income (38009 vs 38315), lower unemployment (3.28 vs 2.57 in HI's favor), higher pop growth (6.84 vs 4.68).
- **AZ** (73.44) at -17.56: Lower income (34460), higher unemployment (4.27), much higher pop growth (9.41).

Hawaii has critical structural buffers: island geography constraining supply, a tourism/military economic base providing employment stability, and the lowest unemployment in the entire dataset (2.57). The extreme appreciation reflects scarcity-driven pricing more than speculative overbuilding.

HI's pop growth (4.68) is well below the speculative states (NV 12.18, AZ 9.41, FL 6.84). Following the pattern where lower pop growth among high-appreciation states predicts milder crashes, HI should be comparable to or slightly worse than FL, given higher appreciation offset by lower pop growth and better unemployment.

**Prediction: -14.0**

---

### NE (appreciation 11.88, ur 3.04, pcpi 35718, pop 1.96)

**Best comparable: CO** (11.88, 4.25, 39869, 4.23) at -4.15. Identical appreciation. NE has lower unemployment (better) but lower income and lower pop growth. Also comparable: **KS** (12.49, 4.42, 35411, 1.47) at -7.30 and **SD** (17.95, 3.01, 34983, 2.53) at -7.26.

Nebraska is a stable agricultural state with no bubble dynamics. Very low unemployment (3.04) indicates a resilient labor market. The profile is almost interchangeable with the stable Plains cluster (KS, SD, OK). Slightly less severe than KS/SD due to lower appreciation and better unemployment, but slightly worse than CO due to lower income.

**Prediction: -5.5**

---

### VA (appreciation 53.63, ur 3.08, pcpi 42164, pop 4.16)

Key comparables bracket VA:
- **NJ** (48.76, 4.69, 47366, 0.70) at -3.57: Lower appreciation, higher income, higher unemployment, much less pop growth.
- **MD** (65.16, 3.85, 45293, 2.39) at -13.02: Higher appreciation, higher income, higher unemployment, less pop growth.

Interpolating on appreciation, VA (53.63) sits about 30% of the way from NJ to MD, suggesting a baseline around -6.4. But VA has lower income than both (-$5,200 vs NJ, -$3,100 vs MD), which worsens the outlook by roughly 1.5-2 points. VA's higher pop growth (4.16 vs NJ 0.70, MD 2.39) adds another 1-2 points of severity. However, VA's very low unemployment (3.08, lower than both) claws back 1-2 points.

Virginia benefits from Northern Virginia's government/military employment stability and Hampton Roads' naval base economy, providing genuine demand and employment resilience during the downturn.

**Prediction: -10.0**

---

### CA (appreciation 73.96, ur 4.89, pcpi 41454, pop 2.18)

The crucial comparison:
- **FL** (74.37, 3.28, 38009, 6.84) at -11.93: Nearly identical appreciation. CA has worse unemployment (+1.61), higher income (+$3,445), and much less pop growth (-4.66).
- **AZ** (73.44, 4.27, 34460, 9.41) at -17.56: Nearly identical appreciation. CA has worse unemployment (+0.62), much higher income (+$6,994), and much less pop growth (-7.23).
- **NV** (79.74, 4.17, 39437, 12.18) at -55.69: Extreme outlier driven by extreme pop growth.

CA's low pop growth (2.18) is the key differentiator. In the training data, pop growth is the main factor separating NV's catastrophe from FL's moderate decline. CA's pop growth is the lowest among all high-appreciation states by a wide margin.

However, CA's unemployment (4.89) is the highest among high-appreciation states (excluding DC, which has extreme income). Higher unemployment means more subprime exposure and more defaults. California's Inland Empire and Central Valley had massive subprime penetration.

Net assessment: CA sits between FL and AZ, with lower pop growth pulling toward FL but higher unemployment pulling toward AZ. Income (41454) provides a modest buffer over AZ but doesn't reach the NJ/DC "safe" zone.

**Prediction: -16.0**

---

### MI (appreciation 8.86, ur 6.87, pcpi 33563, pop -0.05)

**Best comparables: IN** (8.68, 5.02, 32905, 2.20) at -8.67; **OH** (9.43, 5.43, 33976, 0.41) at -12.93.

MI shares the Rust Belt profile of IN/OH (very low appreciation, moderate income), but its fundamentals are dramatically worse. MI's unemployment (6.87) is the highest in either dataset, reflecting the auto industry collapse that was already underway pre-crisis. Negative pop growth (-0.05) indicates outmigration and demand destruction.

This is a fundamentals-driven crash, not a bubble crash. Low appreciation means there was no speculative excess to unwind, but severe economic distress means homeowners defaulted at high rates and demand collapsed.

OH (-12.93) with 5.43 unemployment provides the best anchor. MI's 1.44 additional unemployment points (representing dramatically worse economic conditions) warrant a meaningfully worse outcome. Among high-unemployment states, only AK (6.62 ur, 0.00 crash) escaped, and AK had $7,450 more income plus a resource economy boom.

**Prediction: -15.0**

---

### DE (appreciation 45.63, ur 3.58, pcpi 40736, pop 5.04)

Key comparables:
- **NJ** (48.76, 4.69, 47366, 0.70) at -3.57: Similar appreciation, higher income, higher unemployment, much less pop growth.
- **RI** (48.54, 5.26, 38719, -0.77) at -10.97: Similar appreciation, lower income, higher unemployment, negative pop growth.

Income interpolation between NJ and RI: DE's income (40736) is 39.8% of the way from RI (38719) to NJ (47366), suggesting a crash around -8.0 before adjustments. DE's low unemployment (3.58, better than both) helps, but its high pop growth (5.04, much higher than NJ at 0.70 or RI at -0.77) is a risk factor.

Delaware is a small state tied to the Philadelphia metro area with some mid-Atlantic suburban bubble dynamics. The pop growth suggests speculative demand that could amplify the downturn.

**Prediction: -10.0**

---

### CT (appreciation 36.58, ur 4.42, pcpi 53224, pop 0.95)

CT's defining feature is its very high income (53224), second only to DC (55384) in either dataset. High-income states in the training data consistently show milder crashes:

| State | Income | Appreciation | Crash |
|---|---|---|---|
| DC | 55384 | 70.23 | -4.45 |
| NJ | 47366 | 48.76 | -3.57 |
| MA | 47311 | 28.21 | -14.02 |
| WY | 43805 | 34.89 | 0.00 |
| NY | 43760 | 40.29 | -9.38 |

CT (53224 income, 36.58 appreciation) has more income than any training state except DC, and less appreciation than DC, NJ, or NY. By the pattern where income buffers crashes, CT should land in the mild category.

MA at -14.02 is the counterexample of a high-income state crashing harder, but CT has $5,913 more income and lower unemployment (4.42 vs 4.69). CT's Fairfield County hedge fund economy was exposed to the financial crisis, but the overwhelming income buffer and moderate appreciation keep this manageable.

**Prediction: -7.5**

---

## Final Predictions

```json
[
  {"state": "GA", "predicted_crash_pct": -16.00},
  {"state": "IA", "predicted_crash_pct": -6.50},
  {"state": "AR", "predicted_crash_pct": -9.50},
  {"state": "OR", "predicted_crash_pct": -12.50},
  {"state": "HI", "predicted_crash_pct": -14.00},
  {"state": "NE", "predicted_crash_pct": -5.50},
  {"state": "VA", "predicted_crash_pct": -10.00},
  {"state": "CA", "predicted_crash_pct": -16.00},
  {"state": "MI", "predicted_crash_pct": -15.00},
  {"state": "DE", "predicted_crash_pct": -10.00},
  {"state": "CT", "predicted_crash_pct": -7.50}
]
```
