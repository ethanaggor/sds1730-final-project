## Analysis and Predictions

### Key Patterns in the Training Data

Before predicting, I'll identify the core relationships:

1. **Appreciation is the primary driver** — states with >60% appreciation (NV, AZ, FL) had the worst crashes (-44% to -56%). States under 15% appreciation rarely exceeded -10%.
2. **Population growth amplifies bubbles** — among high-appreciation states, crash severity scales with pop growth (NV at 12.18% pop → -55.69; FL at 6.84% → -44.73; MD at 2.39% → -25.30). High pop growth signals speculative overbuilding.
3. **Economic fundamentals provide a floor** — high PCPI and stable employment dampen crashes (DC: 70% appreciation but only -11.93% crash due to government employment; HI: 81% appreciation but only -18.48% crash due to supply constraints).
4. **Industrial distress creates crashes without bubbles** — MI crashed -29.40% with only 8.86% appreciation, driven by auto sector collapse.
5. **States with no crash (0.00%)** — AK, IA, ND, SD — share resource-based economies (oil, agriculture) and conservative lending environments.

---

### Predictions

**OK (Oklahoma): -5.0%**

Low appreciation (14.28%), healthy labor market (3.91% ur), energy-based economy. Oklahoma's oil and gas sector provided employment stability through the crisis, and conservative lending norms limited subprime exposure. Nearly identical profile to KS (12.49% appr → -4.97) and KY (14.25% appr → -4.45). Slightly higher appreciation than NE (-2.88) but slightly weaker income.

**VA (Virginia): -21.0%**

Significant bubble (53.63% appreciation) concentrated in Northern Virginia's DC suburbs. Appreciation sits between NJ (48.76% → -22.13) and MD (65.16% → -25.30). VA has the best unemployment in this group (3.08%), reflecting government/defense sector stability (Pentagon, defense contractors, federal agencies). Pop growth of 4.16% indicates NoVA sprawl, adding some overbuilding risk. A weighted interpolation between NJ and MD by appreciation gives roughly -23%, adjusted upward by ~2 points for VA's government employment buffer and superior labor market.

**SC (South Carolina): -12.0%**

Low-moderate appreciation (19.42%) limits downside, but high unemployment (6.35%) and low income ($30,789) signal economic vulnerability. NC (16.94% appr, 4.73% ur → -13.06) is the best geographic and economic comp. SC has slightly more appreciation but meaningfully worse unemployment and income. Unlike GA (-24.38%), SC lacks an Atlanta-scale subprime/sprawl epicenter. TN (17.18% appr, 5.22% ur → -8.92) and AL (18.37% appr → -9.90) are also comparable. SC falls on the worse end of this Southern cluster due to its labor market weakness.

**DE (Delaware): -24.0%**

High appreciation (45.63%) places DE squarely in the 40-50% cluster: NJ (48.76% → -22.13), OR (44.87% → -25.98), WA (42.91% → -25.19). DE has the best unemployment (3.58%) in this group, but the highest pop growth (5.04%), suggesting meaningful new construction. Wilmington's financial sector concentration (credit card companies, banking) created direct job-loss exposure when the financial crisis hit. Very close to WA on most dimensions; slightly higher appreciation but better fundamentals, with financial sector vulnerability as a headwind. Net effect lands near OR/WA levels.

**MA (Massachusetts): -14.0%**

Moderate appreciation (28.21%) with high income ($47,311, above NY's $43,760) and negative pop growth (-0.19%). The best comp is NY (40.29% appr, -0.37% pop → -14.02): both are high-income Northeast states with flat/declining populations and appreciation driven by existing demand rather than migration. MA's appreciation is 12 points lower than NY, suggesting a milder crash. But MA had significant subprime exposure in Springfield and Worcester, while Boston's biotech/healthcare/education sectors provided stability. CT (-18.76) and NH (-19.98) had higher appreciation; ME (-13.11) and PA (-9.38) had lower crashes. MA lands just below NY's level.

**TX (Texas): -4.0%**

The hallmark of Texas is elastic housing supply: 6.03% population growth produced only 11.68% appreciation. This supply-demand balance is the signature of strong regulatory framework (strict lending rules, efficient permitting, abundant land). No meaningful bubble formed, so there was minimal overshoot to correct. Comparable to NE (11.88% appr → -2.88), KS (12.49% → -4.97), and CO (11.88% → -10.14). TX's diversified economy (energy, tech, healthcare, military) and absence of speculative overbuilding make it one of the most resilient states. Not 0.00% because even non-bubble states experienced modest price softening from the credit contraction.

**VT (Vermont): -15.0%**

High appreciation (41.92%) but in a small, rural market driven partly by vacation/second-home demand (ski country). Low pop growth (0.81%) and low unemployment (3.68%) limit overbuilding and provide stability. NY (40.29% → -14.02) is the closest appreciation comp with similarly flat population. MT (36.61%, 3.60% pop → -10.06) is a comp as a rural/resort state, but VT's appreciation is higher. Vacation home markets can be volatile because demand is discretionary, but VT's limited construction activity tempers this. Moderate income ($36,609) offers less cushion than NY. Slightly worse than NY due to lower income and vacation-market fragility.

**AR (Arkansas): -9.0%**

Low-moderate appreciation (20.02%), weak fundamentals (5.23% ur, $29,376 pcpi), moderate pop growth. AR fits squarely in the Southern/border-state cluster: TN (17.18% appr, 5.22% ur → -8.92), AL (18.37% appr → -9.90), MO (18.82% appr → -10.97), MS (16.40% appr → -8.67). AR has slightly higher appreciation than these comps but the lowest income. No major metro with extreme subprime dynamics. The combination lands near the cluster mean.

**RI (Rhode Island): -27.0%**

High appreciation (48.54%) nearly identical to NJ (48.76% → -22.13), but every fundamental is worse: higher unemployment (5.26% vs 4.69%), lower income ($38,719 vs $47,366), negative pop growth (-0.77% vs +0.70%). The negative population growth means the appreciation was not supported by migration-driven demand; it was purely credit/speculation-driven, making the correction sharper. RI's small, concentrated economy had limited capacity to absorb losses. Adjusting NJ's crash for worse unemployment (~1-2%), lower income (~1-2%), and negative pop growth (~2-3%) yields roughly -26 to -29%. Similar to OR (-25.98) which had comparable appreciation and unemployment but positive pop growth.

**LA (Louisiana): -8.0%**

Louisiana's profile is shaped by Hurricane Katrina (2005). The -4.83% pop growth is Katrina displacement, not economic decline. The 22.89% appreciation largely reflects post-Katrina supply destruction and rebuilding costs, not speculative demand. This means the "bubble" was fundamentally different: supply-driven appreciation doesn't create the same crash dynamics as speculation-driven appreciation. Federal rebuilding money provided counter-cyclical economic stimulus through the crisis. Oil/gas industry remained strong. Training comps by appreciation: WI (22.65% → -11.81), ND (22.30% → 0.00). ND's energy economy avoided any crash; Louisiana's energy sector is similarly stabilizing but the state is economically weaker (lower income). Predicting milder than WI given Katrina's structural, non-speculative nature.

**CA (California): -40.0%**

California was the epicenter of the subprime lending crisis (Countrywide, IndyMac, WaMu all headquartered there). Appreciation of 73.96% is virtually identical to AZ (73.44% → -46.01) and FL (74.37% → -44.73). The key moderating factor: CA's pop growth (2.18%) is far below AZ (9.41%) and FL (6.84%), indicating less speculative overbuilding statewide. Fitting a linear model to the NV/AZ/FL "Sand States" cluster yields -40.0 for CA. California's higher PCPI ($41,454) provides modest cushion vs AZ/FL, but the state's Inland Empire and Central Valley had Sand State-level crashes (50-60%). Coastal markets (SF, West LA) held up better. The statewide average blends these extremes. MD (65.16% appr, 2.39% pop → -25.30) provides a lower bound for a high-appreciation, low-pop-growth state, but CA's far greater subprime exposure and larger absolute bubble push well beyond MD.

---

### Final Predictions

```json
[
  {"state": "OK", "predicted_crash_pct": -5.00},
  {"state": "VA", "predicted_crash_pct": -21.00},
  {"state": "SC", "predicted_crash_pct": -12.00},
  {"state": "DE", "predicted_crash_pct": -24.00},
  {"state": "MA", "predicted_crash_pct": -14.00},
  {"state": "TX", "predicted_crash_pct": -4.00},
  {"state": "VT", "predicted_crash_pct": -15.00},
  {"state": "AR", "predicted_crash_pct": -9.00},
  {"state": "RI", "predicted_crash_pct": -27.00},
  {"state": "LA", "predicted_crash_pct": -8.00},
  {"state": "CA", "predicted_crash_pct": -40.00}
]
```
