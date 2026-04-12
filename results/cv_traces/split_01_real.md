## Analysis Framework

Before predicting, I'll extract the key patterns from the training data.

**Primary driver: Appreciation (bubble size).** Grouping training states by appreciation band reveals a clear escalating pattern:

| Appreciation Band | Avg Crash | States |
|---|---|---|
| <20% | ~-7.3 | NE, KS, KY, OK, MS, TN, AL, MO, SC, AR |
| 20-35% | ~-16.7 | UT, MN, WV, IL, MA, NH, NM, WY |
| 35-50% | ~-21.0 | MT, ID, NY, OR, DE, RI, NJ |
| 70%+ | ~-46.9 | AZ, CA, FL, NV |

**Key modifiers identified in outliers:**
- **Government employment** buffers crashes heavily: DC (70% appreciation, only -12 crash)
- **Energy economies** resist entirely: AK (36% → 0.0), ND (22% → 0.0)
- **Manufacturing collapse** amplifies crashes independent of bubble: MI (9% appreciation, -29 crash), GA (15% → -24)
- **Population growth** amplifies via overbuilding: NV (12% pop growth, -56), AZ (9.4%, -46), FL (6.8%, -45)
- **High income** provides modest mortgage-servicing buffer but doesn't prevent crashes (NJ at $47k income still crashed -22)

---

## State-by-State Predictions

### NC (North Carolina)
**Features:** appreciation 16.94, ur 4.73, pcpi 34189, pop_growth 5.87

**Comparable states:**
- SC: appreciation 19.42, pop 5.00 → -13.02 (closest match: Southern, similar pop growth)
- AL: appreciation 18.37, pop 2.79 → -9.90
- TN: appreciation 17.18, pop 4.12 → -8.92
- GA: appreciation 15.17, pop 6.18 → -24.38 (outlier due to Atlanta exurban subprime exposure)

NC had modest appreciation in the low band, but the highest pop growth of any state in that band (5.87). SC with similar pop growth (5.00) and slightly higher appreciation crashed -13. GA is an outlier driven by Atlanta's massive exurban sprawl and subprime concentration; NC's economy was more diversified (Research Triangle tech, military at Bragg/Lejeune). Charlotte was vulnerable as a banking hub (Wachovia collapsed), but the Triangle and military regions provided stability.

**Prediction: -12.0**

---

### PA (Pennsylvania)
**Features:** appreciation 34.06, ur 4.73, pcpi 37803, pop_growth 1.10

**Comparable states:**
- NH: appreciation 31.83, pop 2.23 → -19.98
- NM: appreciation 32.57, pop 4.50 → -15.68
- NY: appreciation 40.29, pop -0.37 → -14.02
- MA: appreciation 28.21, pop -0.19 → -17.56

PA sits between MA and NY in appreciation. Low pop growth (1.10) limits overbuilding. The critical structural factor is that PA was two states in one: the Philadelphia metro and Lehigh Valley participated in the mid-Atlantic bubble, while Pittsburgh's housing market was famously stable (slow growth, no bubble). The state average blends a ~-20 crash in the east with ~-5 in the west. Moderate income and Northeast labor market dynamics apply.

**Prediction: -16.0**

---

### WI (Wisconsin)
**Features:** appreciation 22.65, ur 4.69, pcpi 36047, pop_growth 1.80

**Comparable states:**
- MN: appreciation 24.94, ur 4.06, pop 2.18 → -21.83 (closest: Upper Midwest neighbor)
- IL: appreciation 25.87, ur 4.62, pop 0.70 → -21.81
- UT: appreciation 23.39, ur 2.87, pop 7.01 → -21.93

MN and IL are the natural benchmarks: fellow Upper Midwest states with similar appreciation, both at -22. WI has 2-3 points less appreciation and a smaller, less overheated metro area (Milwaukee vs. Twin Cities/Chicago). WI's manufacturing sector was vulnerable, but the housing market was less speculative than its neighbors. The gap between MN/IL at -22 and WI's fundamentals justifies a modest discount.

**Prediction: -18.0**

---

### ME (Maine)
**Features:** appreciation 34.89, ur 4.71, pcpi 34168, pop_growth 1.31

**Comparable states:**
- NH: appreciation 31.83, ur 3.52, pcpi 42866, pop 2.23 → -19.98 (closest: New England neighbor)
- MA: appreciation 28.21, ur 4.69, pcpi 47311, pop -0.19 → -17.56
- VT: appreciation 41.92, ur 3.68, pcpi 36609, pop 0.81 → -6.55 (outlier: tiny, rural vacation-home market)
- WY: appreciation 34.89 (identical!), ur 3.07, pcpi 43805 → -7.70

ME has identical appreciation to WY but they are completely different markets. WY is a small, isolated energy/ranching state. ME's southern coast (Portland to Kittery) functions as a Boston exurb with full exposure to the New England bubble; the interior/north is more like VT's stable rural market. ME's income ($34k) is the lowest in New England, suggesting higher subprime exposure. Higher unemployment (4.71) than NH (3.52) adds vulnerability. Low pop growth moderates somewhat.

The New England trend: MA (28%) → -17.6, NH (32%) → -20.0 extrapolates ME (35%) to approximately -20 to -22. The large stable rural interior moderates toward -19.

**Prediction: -19.0**

---

### IA (Iowa)
**Features:** appreciation 13.29, ur 3.69, pcpi 34197, pop_growth 1.38

**Comparable states:**
- NE: appreciation 11.88, ur 3.04, pcpi 35718, pop 1.96 → -2.88
- KS: appreciation 12.49, ur 4.42, pcpi 35411, pop 1.47 → -4.97
- OK: appreciation 14.28, ur 3.91, pcpi 34650, pop 2.54 → -3.57
- KY: appreciation 14.25, ur 5.73, pcpi 30476, pop 2.48 → -4.45

IA is a textbook stable Plains state. Low appreciation driven by fundamentals, not speculation. Low unemployment signals a healthy agricultural economy. Income and pop growth are moderate. The Des Moines insurance/financial services hub was relatively conservative in lending practices. IA sits squarely among the -3 to -5 cluster of NE, KS, OK, KY.

**Prediction: -4.0**

---

### VA (Virginia)
**Features:** appreciation 53.63, ur 3.08, pcpi 42164, pop_growth 4.16

**Comparable states:**
- DC: appreciation 70.23, ur 5.83, pcpi 55384, pop 0.38 → -11.93 (government buffer benchmark)
- NJ: appreciation 48.76, ur 4.69, pcpi 47366, pop 0.70 → -22.13
- RI: appreciation 48.54, ur 5.26, pcpi 38719, pop -0.77 → -27.60
- DE: appreciation 45.63, ur 3.58, pcpi 40736, pop 5.04 → -20.44

VA sits in a gap in the training data (50-70% appreciation). The without-buffer baseline at 54% appreciation interpolates to roughly -27 to -30 (above DE/NJ/RI at 45-49%). But VA has a significant government employment buffer: Northern Virginia is deeply tied to the DC federal/contractor economy, and Hampton Roads has major military installations. VA's unemployment (3.08) is the lowest of any held-out state.

However, VA isn't DC. Prince William and Loudoun counties saw massive speculative exurban construction and significant subprime exposure. The government buffer reduces a potential -30 crash by roughly 20-25%.

**Prediction: -24.0**

---

### MD (Maryland)
**Features:** appreciation 65.16, ur 3.85, pcpi 45293, pop_growth 2.39

**Comparable states:**
- DC: appreciation 70.23, pop 0.38 → -11.93 (government buffer ceiling)
- CA: appreciation 73.96, pop 2.18 → -41.04 (no buffer floor)
- HI: appreciation 80.67, pop 4.68 → -18.48 (isolated market)
- NJ: appreciation 48.76, pop 0.70 → -22.13

MD had the highest appreciation of any held-out state, almost reaching the extreme bubble tier. It sits between DC and the sand states. The without-buffer interpolation between the 45-50% group (-23 average) and the 70+% group (-47 average) puts 65% appreciation at roughly -37 to -40.

MD benefits from a partial DC government buffer (Montgomery County, many federal workers live in MD). But it also carries two severe liabilities: Prince George's County had among the highest subprime exposure of any suburban county nationally, and Baltimore had structural economic weakness. Pop growth (2.39) is moderate but comparable to CA's (2.18, → -41).

The government buffer reduces the potential crash significantly but less than DC proper. High income ($45k) provides additional mortgage-servicing capacity.

**Prediction: -28.0**

---

### WA (Washington)
**Features:** appreciation 42.91, ur 4.99, pcpi 39744, pop_growth 4.37

**Comparable states:**
- OR: appreciation 44.87, ur 5.39, pcpi 34488, pop 3.48 → -25.98 (Pacific NW neighbor, closest match)
- DE: appreciation 45.63, ur 3.58, pcpi 40736, pop 5.04 → -20.44
- ID: appreciation 39.45, ur 3.39, pcpi 31244, pop 7.72 → -26.95

OR is the natural benchmark: Pacific Northwest neighbor with nearly identical appreciation. WA has slightly lower appreciation (-2 points), lower unemployment, higher income, and higher pop growth. The Seattle tech sector (Microsoft, early-growth Amazon) provided a meaningful employment buffer not present in Portland. Higher income means better mortgage servicing. But the exurbs and smaller cities (Tacoma, Spokane, Clark County) were hit hard.

Net effect: slightly less severe than OR due to tech employment buffer and higher income.

**Prediction: -23.0**

---

### CO (Colorado)
**Features:** appreciation 11.88, ur 4.25, pcpi 39869, pop_growth 4.23

**Comparable states:**
- NE: appreciation 11.88 (identical), ur 3.04, pcpi 35718, pop 1.96 → -2.88
- KS: appreciation 12.49, ur 4.42, pcpi 35411, pop 1.47 → -4.97
- IN: appreciation 8.68, ur 5.02, pcpi 32905, pop 2.20 → -7.30

CO has the same appreciation as NE but very different dynamics. The critical context: Colorado had its housing bubble earlier (late 1990s tech boom) and already corrected during 2001-2003. The 2003-2006 appreciation was recovery growth, not a new bubble. This fundamentally changes the interpretation of the 11.88% figure.

CO's higher pop growth (4.23) adds some risk from new construction, and unemployment is moderate. But the high income ($39.8k, highest among the low-appreciation held-out states), diversified economy (tech, energy, military, tourism), and absence of a bubble provide strong insulation. The GA cautionary tale (15%, pop 6.18 → -24) doesn't apply because GA's crash was driven by Atlanta-specific exurban subprime exposure.

**Prediction: -7.0**

---

### CT (Connecticut)
**Features:** appreciation 36.58, ur 4.42, pcpi 53224, pop_growth 0.95

**Comparable states:**
- NY: appreciation 40.29, ur 4.50, pcpi 43760, pop -0.37 → -14.02
- MT: appreciation 36.61 (nearly identical), ur 3.37, pcpi 31870, pop 3.60 → -10.06
- NJ: appreciation 48.76, ur 4.69, pcpi 47366, pop 0.70 → -22.13
- NH: appreciation 31.83, ur 3.52, pcpi 42866, pop 2.23 → -19.98

CT is a wealthy Northeast state ($53k income, second only to DC in the training data) with moderately high appreciation. Very low pop growth (0.95) limits overbuilding. But CT's economy was acutely exposed to the financial crisis: Fairfield County (hedge funds, GE Capital in Stamford), Hartford (insurance industry). This financial sector concentration acted as a crash amplifier through the employment channel.

CT's income is the highest of any held-out state, providing mortgage-servicing buffer. But the New England trend (MA → NH → ME all worsening with appreciation) places CT at approximately -20 to -22 before adjustments. The extreme income buffer pulls this back, but the financial sector vulnerability pushes it forward. Net: moderate offset.

**Prediction: -19.0**

---

### TX (Texas)
**Features:** appreciation 11.68, ur 4.98, pcpi 35422, pop_growth 6.03

**Comparable states:**
- OK: appreciation 14.28, ur 3.91, pcpi 34650, pop 2.54 → -3.57 (fellow energy state)
- NE: appreciation 11.88, ur 3.04, pcpi 35718, pop 1.96 → -2.88
- KS: appreciation 12.49, ur 4.42, pcpi 35411, pop 1.47 → -4.97

TX had the lowest appreciation of any held-out state despite the highest pop growth (6.03). This apparent paradox is explained by Texas's unique regulatory environment: the state constitution limited home equity lending and cash-out refinancing, effectively suppressing subprime speculation. Large land supply and permissive zoning kept housing affordable even with rapid population growth. The energy sector remained strong through 2008-2009 (oil prices stayed elevated until late 2008).

TX's pop growth (6.03) is a risk factor, but the 11.68% appreciation confirms that this growth was absorbed by new construction at stable prices, not price speculation. TX is structurally closer to OK (energy state, low appreciation) than to GA (high pop growth outlier crash).

**Prediction: -5.0**

---

## Final Predictions

```json
[
  {"state": "NC", "predicted_crash_pct": -12.00},
  {"state": "PA", "predicted_crash_pct": -16.00},
  {"state": "WI", "predicted_crash_pct": -18.00},
  {"state": "ME", "predicted_crash_pct": -19.00},
  {"state": "IA", "predicted_crash_pct": -4.00},
  {"state": "VA", "predicted_crash_pct": -24.00},
  {"state": "MD", "predicted_crash_pct": -28.00},
  {"state": "WA", "predicted_crash_pct": -23.00},
  {"state": "CO", "predicted_crash_pct": -7.00},
  {"state": "CT", "predicted_crash_pct": -19.00},
  {"state": "TX", "predicted_crash_pct": -5.00}
]
```
