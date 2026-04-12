## Approach

I'll analyze the training data patterns, identify comparable states for each prediction target, and combine pattern-matching with structural economic reasoning. Key relationships I'll track:

1. **Appreciation vs. crash** -- not linear; high-appreciation states range from 0.00 (DC, NY) to -55.69 (FL)
2. **Income as a buffer** -- high-pcpi states with high appreciation tend to crash less (DC, MD, VA, NY all > -12)
3. **Pop growth as demand support** -- among high-bubble states, higher pop growth correlates with milder crashes (NV 12.18% growth, only -4.21; FL 6.84%, crashed -55.69)
4. **Regional/structural factors** -- New England manufacturing states crashed harder; resource/government economies were more insulated

Training mean crash: roughly -16.2%.

---

## State-by-State Reasoning

### WY (Wyoming)
**Profile**: Moderate appreciation (34.89), very low unemployment (3.07), high income (43,805), moderate pop growth (3.82). Energy-driven economy (coal, oil, natural gas).

**Comparables**:
- **MT** (appreciation 36.61, pcpi 31,870, pop 3.60) → -18.76 -- geographically closest, but WY income is ~$12K higher
- **VA** (appreciation 53.63, pcpi 42,164, pop 4.16) → -6.55 -- similar income and pop growth, but much higher appreciation
- **WA** (appreciation 42.91, pcpi 39,744, pop 4.37) → -8.92 -- similar profile but higher appreciation

WY's high income (driven by energy-sector wages) provides a strong buffer. Energy commodities were still rising through 2007-2008, insulating WY's economy longer. However, WY lacks the economic diversification of VA/WA, so it won't be as resilient. Between the MT comp (-18.76, with much lower income) and the VA/WA comps (-6 to -9, with more diversified economies).

**Prediction: -11.0**

---

### ME (Maine)
**Profile**: Moderate appreciation (34.89), moderate unemployment (4.71), moderate income (34,168), low pop growth (1.31). New England economy with tourism, fishing, aging demographics.

**Comparables**:
- **PA** (appreciation 34.06, ur 4.73, pcpi 37,803, pop 1.10) → -15.68 -- nearly identical profile, best single comp
- **VT** (appreciation 41.92, pcpi 36,609, pop 0.81) → -14.02 -- New England peer, higher appreciation but also higher income
- **NH** (appreciation 31.83, pcpi 42,866) → -26.95 -- New England peer but much higher income yet still crashed hard

PA is the tightest comp across all four features. ME has ~$3,600 lower income than PA, suggesting slightly more vulnerability. New England states have a pattern of manufacturing decline and aging demographics that amplified the downturn. ME's low pop growth (1.31%) means weak fundamental demand support.

**Prediction: -17.0**

---

### CO (Colorado)
**Profile**: Low appreciation (11.88), moderate unemployment (4.25), high income (39,869), moderate pop growth (4.23). Diversified economy: tech (Boulder/Denver corridor), military, energy, tourism.

**Comparables**:
- **IL** (appreciation 25.87, pcpi 40,021, pop 0.70) → -10.06 -- similar high income, but CO has much lower appreciation AND higher pop growth
- **OK** (appreciation 14.28, pcpi 34,650, pop 2.54) → -3.57 -- similar low appreciation, energy component, but CO has much higher income and pop growth
- **NE** (appreciation 11.88 -- exact match!, pcpi 35,718, pop 1.96) → -21.81 -- identical appreciation but CO has ~$4K higher income and double the pop growth

CO's very low appreciation means there was minimal bubble to pop. The high income and diversified economy (Colorado was not dependent on housing or manufacturing) provided resilience. CO's pop growth (4.23%) is stronger than most low-appreciation peers. Colorado also notably had a tech-sector expansion in the 2000s that provided alternative economic support.

**Prediction: -9.0**

---

### WI (Wisconsin)
**Profile**: Moderate appreciation (22.65), moderate unemployment (4.69), moderate income (36,047), low pop growth (1.80). Manufacturing, agriculture, services economy.

**Comparables**:
- **IL** (appreciation 25.87, pcpi 40,021, pop 0.70) → -10.06 -- Midwest peer, but IL has ~$4K higher income
- **ND** (appreciation 22.30, pcpi 33,120, pop 1.66) → -22.13 -- very similar appreciation and pop growth, lower income
- **MO** (appreciation 18.82, pcpi 33,860, pop 2.33) → -8.67 -- nearby state, lower appreciation

WI sits between the IL comp (-10.06, higher income) and the ND comp (-22.13, lower income). WI's manufacturing sector (paper, machinery, food processing) was vulnerable to the broader recession that followed the housing crash. Low pop growth (1.80%) provides minimal demand buffer. The Midwest shows high variance in this dataset (MO at -8.67 vs IA at -46.01), but WI's more diversified economy and moderate income put it in the middle tier.

**Prediction: -16.0**

---

### KY (Kentucky)
**Profile**: Low appreciation (14.25), high unemployment (5.73), low income (30,476), low pop growth (2.48). Coal/tobacco/manufacturing economy, Appalachian structural challenges.

**Comparables**:
- **AR** (appreciation 20.02, ur 5.23, pcpi 29,376, pop 3.56) → -10.97 -- closest overall match; similar low-income, higher-unemployment Southern state
- **OK** (appreciation 14.28, ur 3.91, pcpi 34,650, pop 2.54) → -3.57 -- nearly identical appreciation and pop growth, but much lower unemployment and higher income
- **MS** (appreciation 16.40, ur 6.38, pcpi 27,827, pop 1.28) → -19.98 -- similar high unemployment and low income

KY's low appreciation means minimal bubble. But the high unemployment (5.73%, second only to MI and MS in training data) and low income create vulnerability to the broader economic downturn. AR is the best single comp; KY has lower appreciation (slightly better) but higher unemployment (slightly worse) and similar income.

**Prediction: -11.0**

---

### MN (Minnesota)
**Profile**: Moderate appreciation (24.94), low unemployment (4.06), high income (39,362), low-moderate pop growth (2.18). Diversified economy: Fortune 500 headquarters (Target, UnitedHealth, 3M, General Mills), finance, healthcare.

**Comparables**:
- **IL** (appreciation 25.87, ur 4.62, pcpi 40,021, pop 0.70) → -10.06 -- best single comp; nearly identical appreciation and income
- **WA** (appreciation 42.91, pcpi 39,744, pop 4.37) → -8.92 -- similar income, higher appreciation
- **ND** (appreciation 22.30, pcpi 33,120, pop 1.66) → -22.13 -- geographic neighbor but much lower income

MN is anchored by the IL comp. MN's corporate economy is highly diversified; Minneapolis-St. Paul's white-collar employment base is structurally similar to Chicago's. MN has slightly better unemployment (4.06 vs 4.62) and better pop growth (2.18 vs 0.70), but fractionally lower income. On balance, MN should be close to IL but possibly slightly worse due to more seasonally volatile housing markets in the Upper Midwest.

**Prediction: -12.0**

---

### CA (California)
**Profile**: Very high appreciation (73.96), moderate unemployment (4.89), moderate-high income (41,454), low pop growth (2.18). Massive, diverse economy but with extreme housing speculation in Inland Empire, Central Valley, and exurban LA/Sacramento.

**Comparables**:
- **AZ** (appreciation 73.44, pcpi 34,460, pop 9.41) → -25.19 -- near-identical appreciation, but CA has much higher income AND much lower pop growth
- **FL** (appreciation 74.37, pcpi 38,009, pop 6.84) → -55.69 -- near-identical appreciation, CA has higher income but much lower pop growth
- **NV** (appreciation 79.74, pcpi 39,437, pop 12.18) → -4.21 -- similar appreciation, but NV's pop growth (12.18) dwarfs CA's (2.18)
- **MD** (appreciation 65.16, pcpi 45,293, pop 2.39) → -7.26 -- similar income and pop growth, but lower appreciation

Among the high-appreciation sand states, pop growth appears to provide demand support: NV (12.18% growth, mild crash) vs FL (6.84%, catastrophic crash). CA's very low pop growth (2.18%) is a major red flag; it means the 74% appreciation was overwhelmingly speculative rather than migration-driven.

However, CA's income ($41,454) is meaningfully higher than FL ($38,009) and AZ ($34,460). The high-income, high-appreciation group (DC, MD, VA, NJ, NY) all had relatively mild crashes. CA sits at the intersection: extreme bubble like FL/AZ, but income level closer to the DC/MD/VA group.

CA's inland subprime markets (Stockton, Bakersfield, Riverside) were devastated, but coastal markets (SF, parts of LA) had stronger income support. The state-level average reflects this mix. I place CA near AZ (-25.19), where CA's higher income roughly offsets its lower pop growth.

**Prediction: -25.0**

---

### GA (Georgia)
**Profile**: Low appreciation (15.17), moderate unemployment (4.66), moderate income (34,574), high pop growth (6.18). Metro Atlanta drives the economy; services, logistics (Hartsfield-Jackson), military.

**Comparables**:
- **NC** (appreciation 16.94, ur 4.73, pcpi 34,189, pop 5.87) → -4.97 -- best single comp; nearly identical across all features
- **TN** (appreciation 17.18, ur 5.22, pcpi 32,878, pop 4.12) → -6.70 -- similar Southern state
- **SC** (appreciation 19.42, ur 6.35, pcpi 30,789, pop 5.00) → 0.00 -- similar region, higher appreciation, yet no crash
- **AL** (appreciation 18.37, ur 4.01, pcpi 31,264, pop 2.79) → -7.30 -- nearby state

GA is almost a carbon copy of NC across all four features. NC was -4.97. GA's pop growth is slightly higher (6.18 vs 5.87, positive for demand), but metro Atlanta had more speculative suburban/exurban development than the Research Triangle, which adds some downside risk. The broader Southern pattern with low appreciation and high pop growth is consistently mild (SC: 0.00, NC: -4.97, TN: -6.70).

**Prediction: -7.0**

---

### TX (Texas)
**Profile**: Very low appreciation (11.68), moderate unemployment (4.98), moderate income (35,422), high pop growth (6.03). Energy, tech, agriculture, defense. Strict home equity lending laws, abundant land supply.

**Comparables**:
- **OK** (appreciation 14.28, ur 3.91, pcpi 34,650, pop 2.54) → -3.57 -- fellow energy state, similar low appreciation and income
- **NC** (appreciation 16.94, ur 4.73, pcpi 34,189, pop 5.87) → -4.97 -- similar pop growth and income

TX has the lowest appreciation of any held-out state (11.68%). Texas was widely cited as the counter-example to the housing crisis, thanks to Section 50(a)(6) of the Texas Constitution limiting cash-out refinancing, plus elastic housing supply from abundant land. Its diversified economy (energy, tech in Austin, defense, healthcare in Houston) and strong in-migration provided fundamental demand support. OK, the closest energy-state comp, was only -3.57.

**Prediction: -3.5**

---

### HI (Hawaii)
**Profile**: Highest appreciation of all states (80.67), lowest unemployment (2.57), moderate income (38,315), moderate pop growth (4.68). Island economy: tourism, military (Pearl Harbor, multiple bases), constrained land supply.

**Comparables**:
- **NV** (appreciation 79.74, ur 4.17, pcpi 39,437, pop 12.18) → -4.21 -- closest in appreciation, but NV has 3x the pop growth
- **DC** (appreciation 70.23, ur 5.83, pcpi 55,384, pop 0.38) → 0.00 -- unique economy with stable government demand, much higher income
- **FL** (appreciation 74.37, ur 3.28, pcpi 38,009, pop 6.84) → -55.69 -- similar appreciation and income, but very different economic structure

HI is structurally unique. Island geography creates a hard supply constraint that supports prices even during downturns; you cannot build new land. Military bases provide recession-resistant employment. Tourism, while cyclical, benefits from HI being an irreplaceable destination. The extremely low unemployment (2.57%) reflects a tight, supply-constrained labor market.

HI's income (38,315) is lower than NV's (39,437), and pop growth (4.68) is far below NV's (12.18). But HI's supply constraint acts as a structural price floor that mainland states lack. I discount the FL comparison due to FL's elastic supply (massive spec building in Cape Coral, Port St. Lucie, etc.) which HI cannot replicate.

**Prediction: -10.0**

---

### AK (Alaska)
**Profile**: Moderate-high appreciation (36.14), high unemployment (6.62), high income (41,013), moderate pop growth (4.15). Resource economy: oil (Prudhoe Bay, Trans-Alaska Pipeline), fishing, federal spending.

**Comparables**:
- **MT** (appreciation 36.61, ur 3.37, pcpi 31,870, pop 3.60) → -18.76 -- nearly identical appreciation and pop growth, but MT has much lower income
- **WA** (appreciation 42.91, ur 4.99, pcpi 39,744, pop 4.37) → -8.92 -- similar income and pop growth, higher appreciation
- **PA** (appreciation 34.06, ur 4.73, pcpi 37,803, pop 1.10) → -15.68 -- similar appreciation, lower income

AK's high unemployment (6.62%) is structural, driven by seasonal industries (fishing, construction in summer months) and remote geography, not economic weakness. Oil revenues fund the Permanent Fund Dividend, providing a unique economic cushion. High income ($41,013) is in the WA/VA tier, which tends to buffer crashes.

Between the MT comp (-18.76, much lower income) and the WA comp (-8.92, higher appreciation but similar income), AK's unique economic structure (oil-dependent but with Permanent Fund backstop) places it in the middle.

**Prediction: -12.0**

---

## Final Predictions

```json
[
  {"state": "WY", "predicted_crash_pct": -11.00},
  {"state": "ME", "predicted_crash_pct": -17.00},
  {"state": "CO", "predicted_crash_pct": -9.00},
  {"state": "WI", "predicted_crash_pct": -16.00},
  {"state": "KY", "predicted_crash_pct": -11.00},
  {"state": "MN", "predicted_crash_pct": -12.00},
  {"state": "CA", "predicted_crash_pct": -25.00},
  {"state": "GA", "predicted_crash_pct": -7.00},
  {"state": "TX", "predicted_crash_pct": -3.50},
  {"state": "HI", "predicted_crash_pct": -10.00},
  {"state": "AK", "predicted_crash_pct": -12.00}
]
```
