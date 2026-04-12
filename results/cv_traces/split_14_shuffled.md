## Analysis and Predictions

### Identifying Key Patterns in Training Data

The training data reveals several important dynamics:

1. **Regional clustering matters more than any single feature.** Northeast states (CT, ME, NH, NJ, NY, PA) consistently crash harder (-20% to -55%) regardless of appreciation level. Mountain/West states with similar appreciation levels (OR, WA, ID, NM, MT) crash much less or not at all.

2. **Appreciation alone is a weak predictor.** The highest-appreciation states (HI 80.67%, NV 79.74%) crash only moderately (-13.06%, -11.93%), while low-appreciation states (IN 8.68%, NE 11.88%) can crash severely (-44.73%, -21.81%). The relationship is noisy.

3. **Population growth is a resilience indicator.** States with strong pop growth tend to have milder crashes even with high appreciation (NV 12.18% pop → -11.93%; ID 7.72% → -4.97%; UT 7.01% → -9.38%), because growth signals real demand rather than pure speculation.

4. **Low income + high unemployment amplifies severity.** MS (pcpi 27827, ur 6.38%) crashed -25.98% despite only 16.40% appreciation. Economic fragility makes even modest corrections worse.

---

### State-by-State Predictions

**OK (Oklahoma)**
- Profile: Low appreciation (14.28%), healthy labor market (3.91% ur), moderate income, moderate pop growth.
- Oklahoma's energy-driven economy and minimal speculative building insulated it from the bubble. No exotic mortgage proliferation.
- Nearest comparables: KS (12.49% appr → -4.45%), MO (18.82% → 0.00%), NC (16.94% → -2.88%).
- **Prediction: -5.0%**

**VA (Virginia)**
- Profile: High appreciation (53.63%), very low unemployment (3.08%), high income, solid pop growth (4.16%).
- Northern Virginia is effectively the DC corridor. DC (70.23% appr → -15.68%) and MD (65.16% → -25.30%) bracket the regional dynamics. VA's lower appreciation than both, combined with government/military employment stability and the lowest unemployment in the held-out set, should moderate the decline. However, the mid-Atlantic bubble was real.
- **Prediction: -18.0%**

**SC (South Carolina)**
- Profile: Moderate appreciation (19.42%), high unemployment (6.35%), low income (30789), decent pop growth (5.00%).
- The high unemployment is SC's main vulnerability, approaching MS (6.38% ur → -25.98%) and MI (6.87% → -18.48%). But SC's stronger pop growth and Southeast comparables (GA -8.92%, NC -2.88%, AL -13.11%, KY -10.97%) anchor it. TN (5.22% ur, similar region → -21.93%) suggests the unemployment drag is real but tempered by population inflows.
- **Prediction: -13.0%**

**DE (Delaware)**
- Profile: Significant appreciation (45.63%), low unemployment (3.58%), high income (40736), strong pop growth (5.04%).
- DE sits in the mid-Atlantic corridor between PA (-46.01%) and NJ (-26.95%), but its profile is meaningfully different: 5.04% pop growth is far above NJ's 0.70% and PA's 1.10%, signaling genuine demand. Among high-appreciation states with strong pop growth, outcomes are milder (WA 42.91% appr, 4.37% pop → 0%; OR 44.87%, 3.48% → -9.90%). The regional pull is severe, but fundamentals provide a buffer.
- **Prediction: -17.0%**

**MA (Massachusetts)**
- Profile: Moderate appreciation (28.21%), moderate unemployment (4.69%), high income (47311), slightly negative pop growth (-0.19%).
- Firmly in the Northeast pattern, but MA's appreciation is the lowest among all NE training states (CT 36.58% → -19.98%, ME 34.89% → -25.19%, NY 40.29% → -22.13%). The negative pop growth and high income echo NY's profile (-0.37% pop → -22.13%). MA's lower appreciation should bring it below CT's -19.98%.
- **Prediction: -18.0%**

**TX (Texas)**
- Profile: Very low appreciation (11.68%), moderate unemployment (4.98%), moderate income, strong pop growth (6.03%).
- Texas was famously resilient due to state-level lending regulations that restricted exotic mortgages, combined with strong population-driven fundamental demand. The profile mirrors KS (12.49% appr → -4.45%) and CO (11.88% → -7.70%) on appreciation, with NC-like pop growth (5.87% → -2.88%) providing additional support.
- **Prediction: -4.0%**

**VT (Vermont)**
- Profile: Moderate-high appreciation (41.92%), low unemployment (3.68%), moderate income (36609), low pop growth (0.81%).
- VT is a small rural Northeast state. Its appreciation sits between CT (36.58% → -19.98%) and NJ (48.76% → -26.95%), and is most comparable to NY (40.29% → -22.13%). The low pop growth means limited fundamental demand to absorb the correction. While VT's lower income means less dollar exposure than CT or NY, the Northeast regional effect dominates.
- **Prediction: -21.0%**

**AR (Arkansas)**
- Profile: Moderate appreciation (20.02%), elevated unemployment (5.23%), low income (29376), moderate pop growth (3.56%).
- AR maps closely to the AL/KY/TN cluster. AL (18.37% appr, 4.01% ur → -13.11%) and KY (14.25%, 5.73% → -10.97%) are the tightest comparables. TN (17.18%, 5.22% ur → -21.93%) shares AR's unemployment level almost exactly, but AR's lower income and more rural character limit exposure. The average of AL, KY, and TN lands around -15%; AR's lower income and modest pop growth split the difference.
- **Prediction: -13.0%**

**RI (Rhode Island)**
- Profile: High appreciation (48.54%), elevated unemployment (5.26%), moderate income (38719), negative pop growth (-0.77%).
- RI's appreciation almost exactly matches NJ (48.76% → -26.95%). But RI has worse fundamentals across the board: higher unemployment (5.26% vs 4.69%), negative pop growth (-0.77% vs 0.70%), and lower income. Negative pop growth with high appreciation indicates speculation-driven bubble without fundamental demand support. RI was a classic overbuilt, over-leveraged small Northeast state.
- **Prediction: -28.0%**

**LA (Louisiana)**
- Profile: Moderate appreciation (22.89%), moderate unemployment (4.14%), moderate income, extreme negative pop growth (-4.83%).
- The -4.83% pop growth is Katrina-driven (August 2005), not economic decline. This complicates the analysis: population loss was accompanied by housing stock destruction, creating partially offsetting effects on prices. States with similar appreciation but normal demographics (MN 24.94% → -11.81%, WI 22.65% → -7.30%, SD 17.95% → -10.14%) cluster around -10%. Post-Katrina reconstruction spending provided some economic support, but disrupted markets add uncertainty.
- **Prediction: -11.0%**

**CA (California)**
- Profile: Very high appreciation (73.96%), moderate unemployment (4.89%), high income (41454), moderate pop growth (2.18%).
- California was a primary epicenter of subprime lending, particularly in the Central Valley and Inland Empire. FL (74.37% appr → -21.83%) is the closest match on appreciation. However, CA has weaker fundamentals than FL: lower pop growth (2.18% vs 6.84%), higher unemployment (4.89% vs 3.28%), and higher income (more dollar exposure). MD (65.16% appr, 2.39% pop → -25.30%) is a good comparison for the combination of high appreciation with moderate pop growth. CA should land between FL and MD.
- **Prediction: -22.0%**

---

### Final Predictions

```json
[
  {"state": "OK", "predicted_crash_pct": -5.00},
  {"state": "VA", "predicted_crash_pct": -18.00},
  {"state": "SC", "predicted_crash_pct": -13.00},
  {"state": "DE", "predicted_crash_pct": -17.00},
  {"state": "MA", "predicted_crash_pct": -18.00},
  {"state": "TX", "predicted_crash_pct": -4.00},
  {"state": "VT", "predicted_crash_pct": -21.00},
  {"state": "AR", "predicted_crash_pct": -13.00},
  {"state": "RI", "predicted_crash_pct": -28.00},
  {"state": "LA", "predicted_crash_pct": -11.00},
  {"state": "CA", "predicted_crash_pct": -22.00}
]
```
