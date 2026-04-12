## Analysis Framework

I'll work through this by identifying the strongest signals in the training data, finding the most comparable states for each prediction, and applying domain knowledge about the 2008 crisis.

### Key Patterns in the Training Data

**Unemployment is the strongest predictor.** States with ur > 5.0 averaged about -25.4% crash vs -10.6% for states with ur < 3.5. This makes economic sense: weak labor markets mean more foreclosures, distressed sales, and reduced buying capacity.

**Low per-capita income amplifies vulnerability.** The worst crashes in low-appreciation states (AR -44.73, MS -41.04) combined high unemployment with very low pcpi. Households with less income buffer are more sensitive to economic shocks.

**Appreciation alone is a weak predictor.** High-appreciation states ranged from -4.21 (MD) to -46.01 (DC). Low-appreciation states ranged from 0 (KY) to -55.69 (TX). The bubble size matters, but other factors determine whether it pops hard.

**Population growth provides mixed signals.** Negative pop growth states averaged about -19.5% (declining demand), while moderate growth (1-3%) states averaged about -11.7%.

---

## State-by-State Predictions

### HI (appreciation 80.67, ur 2.57, pcpi 38315, pop_growth 4.68)

Hawaii has the highest appreciation in the entire dataset and the lowest unemployment. These factors push in opposite directions. Comparable high-appreciation states: NV (79.74 → -13.06), FL (74.37 → -9.90), CA (73.96 → -26.95), AZ (73.44 → -24.38). Among these, FL (ur 3.28) and NV (ur 4.17) had milder crashes; CA (ur 4.89) and DC (ur 5.83) had worse ones. The ur gradient matters.

Hawaii's island geography fundamentally constrains housing supply, limiting overbuilding even during a speculative boom. The 2.57% unemployment rate (lowest in either dataset) signals a healthy underlying economy. While 80.67% appreciation indicates a significant bubble, much of Hawaii's price growth reflects genuine scarcity rather than purely speculative excess. Comparable to NV/FL on appreciation but with stronger labor market fundamentals.

**Prediction: -13.0**

### WI (appreciation 22.65, ur 4.69, pcpi 36047, pop_growth 1.80)

Wisconsin is a textbook Midwest moderate. Closest comparisons: MN (24.94 appreciation, ur 4.06 → -15.68), IL (25.87, ur 4.62 → -7.26), IA (13.29, ur 3.69 → -8.67), KS (12.49, ur 4.42 → -10.97), MO (18.82, ur 4.89 → -4.97). WI's appreciation falls between IA and MN. Its ur (4.69) is between IL and MO. pcpi at 36047 is moderate.

Wisconsin's economy is diversified (manufacturing, agriculture, services) without extreme exposure to speculative housing. No major bubble inflated, and labor markets were middling. The range of comparable Midwest states is -4.97 to -15.68. WI falls in the middle.

**Prediction: -10.0**

### NE (appreciation 11.88, ur 3.04, pcpi 35718, pop_growth 1.96)

Nebraska has exactly the same appreciation as CO (11.88 → -13.11) but much lower unemployment (3.04 vs 4.25). Other comparables: IA (13.29, ur 3.69 → -8.67), KS (12.49, ur 4.42 → -10.97), ND (22.30, ur 3.12 → -6.70). All Great Plains states with similar economic structures.

Low appreciation means minimal bubble risk. Very low unemployment signals economic resilience. Nebraska's agricultural and insurance-based economy was relatively insulated from mortgage-driven speculation. The IA/ND comparison (similar region, similar ur, similar pcpi) centers predictions around -7 to -9.

**Prediction: -8.0**

### SD (appreciation 17.95, ur 3.01, pcpi 34983, pop_growth 2.53)

South Dakota's closest match is its neighbor ND (22.30, ur 3.12, pcpi 33120 → -6.70). Very similar unemployment, similar pcpi, similar region. SD has lower appreciation, which means even less bubble to deflate. Also comparable to IA (-8.67) but with lower ur.

The very low unemployment (3.01) places SD firmly in the protected category. No speculative excesses, stable Plains economy, and genuine (if slow) population growth.

**Prediction: -7.0**

### SC (appreciation 19.42, ur 6.35, pcpi 30789, pop_growth 5.00)

This is the most concerning profile among the held-out states. The 6.35% unemployment rate is the second-highest in the held-out set and matches MS (6.38 → -41.04) almost exactly. pcpi at 30789 is in the vulnerable low-income range, similar to NM (30433 → -29.40) and AL (31264 → -25.19).

Key comparisons among high-ur states: MS (6.38 → -41.04), AK (6.62 → -25.98), MI (6.87 → -17.56). The critical difference between SC and MS is population growth: 5.00 vs 1.28. SC was attracting genuine migration-driven demand (retirement, lower cost of living), which provides a demand floor that MS lacked. SC's pcpi is also meaningfully higher than MS's 27827.

SC's profile resembles AK (-25.98) in the ur/pop-growth combination, but with lower pcpi. The high ur + low pcpi combination signals significant household financial fragility, leading to elevated foreclosure rates.

**Prediction: -23.0**

### TN (appreciation 17.18, ur 5.22, pcpi 32878, pop_growth 4.12)

Tennessee sits between two clear comparables: IN (8.68 appreciation, ur 5.02, pcpi 32905 → -18.76) and NC (16.94, ur 4.73, pcpi 34189 → -14.02). TN's ur (5.22) is between these, and pcpi (32878) is nearly identical to IN's (32905). The appreciation level (17.18) is close to NC's (16.94).

TN has worse ur than NC but better pop growth than IN. The moderately high unemployment in a moderate-income state creates foreclosure pressure, but nothing extreme. AR (ur 5.23 → -44.73) has nearly identical unemployment but crashed far worse due to much lower pcpi (29376). TN's extra ~3500 in pcpi provides meaningful buffer.

Average of IN and NC: about -16.4.

**Prediction: -17.0**

### NJ (appreciation 48.76, ur 4.69, pcpi 47366, pop_growth 0.70)

New Jersey is a high-appreciation, high-income Northeast state. The most striking comparable is MA (ur 4.69, pcpi 47311 → -19.98), which has almost identical ur and pcpi. MA crashed about -20% with only 28.21% appreciation. NJ's much higher appreciation (48.76) suggests a larger bubble.

Other Northeast comparisons: NY (40.29, ur 4.50, pcpi 43760 → -21.83), CT (36.58, ur 4.42, pcpi 53224 → -7.70). CT's much milder crash likely reflects its significantly higher pcpi providing a buffer. NJ's pcpi (47366) is between MA and CT.

NJ also resembles DE (45.63, ur 3.58 → -20.44) in appreciation level, though DE has lower ur. NJ's low pop growth (0.70) limits demand-side support but is at least positive (unlike MA and NY's negative growth).

Balancing the high appreciation risk against high income and non-negative growth, NJ should be in the MA/NY range but possibly slightly milder.

**Prediction: -18.0**

### VT (appreciation 41.92, ur 3.68, pcpi 36609, pop_growth 0.81)

Vermont is a small New England state with moderate-high appreciation and low unemployment. Closest comparisons: WA (42.91, ur 4.99 → -11.93) has nearly identical appreciation but higher ur. ME (34.89, ur 4.71 → -4.45) and PA (34.06, ur 4.73 → -4.15) are milder but have lower appreciation. NH (31.83, ur 3.52 → -21.81) is a geographic neighbor with lower appreciation but a surprisingly severe crash.

The NH result is concerning, but VT and NH have different market structures. VT is more rural with less suburban commuter-driven speculation. VT's ur (3.68) is slightly higher than NH's (3.52), but VT's pop growth (0.81) is lower than NH's (2.23).

WA (-11.93) is the best appreciation match and seems like a reasonable anchor, adjusted slightly for VT's lower pcpi and pop growth.

**Prediction: -12.0**

### OK (appreciation 14.28, ur 3.91, pcpi 34650, pop_growth 2.54)

Oklahoma has strikingly similar appreciation to KY (14.25 → 0.00), but KY's 0% crash is likely an anomaly. More useful comparables: IA (13.29, ur 3.69 → -8.67), KS (12.49, ur 4.42 → -10.97), CO (11.88, ur 4.25 → -13.11).

Oklahoma's energy-dependent economy provides countercyclical support: oil prices remained elevated through much of the crisis period, supporting employment and income. Low appreciation signals minimal speculative building. The ur of 3.91 is moderate, and pcpi is in line with Plains peers.

Average of IA (-8.67) and KS (-10.97): about -9.8. OK's lower ur than KS suggests slightly milder.

**Prediction: -9.0**

### RI (appreciation 48.54, ur 5.26, pcpi 38719, pop_growth -0.77)

Rhode Island has the most troubling feature combination among the held-out states: high appreciation (bubble), high unemployment (weak labor market), and negative population growth (shrinking demand). This triple threat is rare in the training data.

Closest comparisons: MA (28.21, ur 4.69, pcpi 47311, pop -0.19 → -19.98) and NY (40.29, ur 4.50, pcpi 43760, pop -0.37 → -21.83). RI has higher appreciation than both, higher unemployment than both, lower pcpi than both, and more negative pop growth than both. Every factor points to a worse outcome.

Among high-ur states, AR (ur 5.23 → -44.73) and OR (ur 5.39 → -9.38) show how much other factors matter. RI's high appreciation + negative pop growth + lower income position it worse than MA/NY but better than the extreme cases (AR, DC).

RI was heavily exposed to subprime lending and manufacturing job losses, with no population growth to absorb housing inventory.

**Prediction: -24.0**

### OH (appreciation 9.43, ur 5.43, pcpi 33976, pop_growth 0.41)

Ohio is a Rust Belt state with the lowest appreciation in the held-out set. Direct comparables: MI (8.86, ur 6.87, pcpi 33563 → -17.56) and IN (8.68, ur 5.02, pcpi 32905 → -18.76). OH's appreciation, ur, and pcpi all fall between these two states.

OH has lower ur than MI (5.43 vs 6.87) but higher ur than IN (5.02). Pop growth (0.41) is between MI (-0.05) and IN (2.20). The minimal appreciation means the crash isn't about a bubble popping but rather about economic weakness: manufacturing decline, job losses, and foreclosure pressure in an already stagnant market.

Average of MI and IN: -18.16. OH's slightly better ur vs MI and slightly better pop growth suggest a modestly milder outcome.

**Prediction: -16.0**

---

## Final Predictions

```json
[
  {"state": "HI", "predicted_crash_pct": -13.00},
  {"state": "WI", "predicted_crash_pct": -10.00},
  {"state": "NE", "predicted_crash_pct": -8.00},
  {"state": "SD", "predicted_crash_pct": -7.00},
  {"state": "SC", "predicted_crash_pct": -23.00},
  {"state": "TN", "predicted_crash_pct": -17.00},
  {"state": "NJ", "predicted_crash_pct": -18.00},
  {"state": "VT", "predicted_crash_pct": -12.00},
  {"state": "OK", "predicted_crash_pct": -9.00},
  {"state": "RI", "predicted_crash_pct": -24.00},
  {"state": "OH", "predicted_crash_pct": -16.00}
]
```
