## Analysis Framework

I'll work through this systematically: identify the dominant patterns in the training data, then apply those patterns along with crisis-specific domain knowledge to each held-out state.

### Key Patterns in Training Data

**1. Appreciation is the strongest predictor, but with critical moderators:**

| Appreciation Range | Typical Crash | Examples |
|---|---|---|
| >70% + high pop growth | -44% to -56% | NV, AZ, FL |
| >70% + supply-constrained | ~-18% | HI |
| 40-55% | -20% to -28% | NJ, RI, DE, OR, WA, ID |
| 20-40% | -7% to -22% (wide) | IL, MN, UT, NH, CT, VT, MT, PA |
| <20% | -3% to -13% | TX, KS, NE, AL, NC, TN |

**2. Population growth amplifies bubbles.** Among the extreme appreciation states, NV (12.18% pop growth, -55.69 crash) was far worse than FL (6.84%, -44.73). Migration-driven demand fed speculative construction.

**3. Supply constraints neutralize appreciation.** HI had the highest appreciation in the dataset (80.67%) but only -18.48% crash. Island geography caps construction. AK (36.14%, 0.00) is similar: isolated, constrained.

**4. Industry-specific shocks override fundamentals.** MI had only 8.86% appreciation but crashed -29.40% due to the auto industry collapse. Its pre-crisis unemployment (6.87%) was a leading indicator.

**5. Energy/agricultural economies are resilient.** ND (0.00), IA (0.00), AK (0.00) all avoided crashes. Commodity-driven economies with stable demand and limited speculation.

---

## State-by-State Predictions

### California (CA)
**Features:** 73.96% appreciation, 4.89% ur, $41,454 income, 2.18% pop growth

CA was the epicenter of the subprime crisis. The appreciation (73.96%) is nearly identical to AZ (73.44% → -46.01) and FL (74.37% → -44.73). However, CA's population growth (2.18%) is dramatically lower than AZ (9.41%) or FL (6.84%), indicating less migration-driven speculative construction on a statewide basis.

The moderating factors: coastal markets (San Francisco, parts of LA) are supply-constrained and held up better. The higher per-capita income ($41,454) provides some buffer. The aggravating factors: CA was ground zero for no-doc loans, option ARMs, and NINJA lending. The Inland Empire (Riverside-San Bernardino), Central Valley (Stockton, Bakersfield), and Sacramento metro were devastated with localized declines of 40-55%. The statewide HPI blends these severely hit inland markets with more resilient coastal ones.

Net effect: severe, but moderated ~5 points below AZ/FL by lower pop growth and partial supply constraints.

**Prediction: -40.00**

---

### Maryland (MD)
**Features:** 65.16% appreciation, 3.85% ur, $45,293 income, 2.39% pop growth

MD sits in an appreciation gap in the training data: above NJ (48.76% → -22.13) and RI (48.54% → -27.60) but below FL/AZ (73-74% → -45%). The bubble was concentrated in the DC exurbs and Baltimore metro. Prince George's County had among the highest foreclosure rates nationally, driven by subprime lending disproportionately targeting its communities. Baltimore's struggling economy added downward pressure.

Moderating factors: DC proximity means government-contractor employment provides a floor. Low unemployment (3.85%), high income ($45,293), moderate pop growth (2.39%). Montgomery County and other affluent areas were more resilient.

Extrapolating from NJ/RI at ~48-49% appreciation (-22 to -28%) upward by ~16 points of appreciation, adjusted for MD's strong fundamentals.

**Prediction: -25.50**

---

### Virginia (VA)
**Features:** 53.63% appreciation, 3.08% ur, $42,164 income, 4.16% pop growth

VA's appreciation (53.63%) sits between the NJ/RI/DE cluster (45-49%) and the extreme bubble states. Northern Virginia's exurbs (Prince William, Loudoun, Stafford counties) saw massive speculative construction and severe price collapses, with localized declines of 30-40%. But the government/defense sector in Fairfax/Arlington provided stability. Hampton Roads (military-driven) was moderate.

Closest comparables: NJ (48.76% → -22.13), DE (45.63% → -20.44). VA has higher appreciation, which pushes toward a worse outcome, but the lowest unemployment in the held-out set (3.08%) and substantial government-sector employment buffer the decline.

**Prediction: -22.50**

---

### District of Columbia (DC)
**Features:** 70.23% appreciation, 5.83% ur, $55,384 income, 0.38% pop growth

DC's appreciation (70.23%) is in the extreme range, but DC is structurally unique. It's a single city with severe supply constraints (small geographic area, building height limits, no suburban sprawl). The federal government was the dominant employer and actually expanded during the crisis (stimulus spending, regulatory growth under Dodd-Frank).

The closest analog in the training data is HI (80.67% → -18.48%): both are supply-constrained jurisdictions where high appreciation reflected genuine demand scarcity rather than speculative overbuilding. DC has the highest income in the entire dataset ($55,384) and the lowest pop growth (0.38%) among the held-out states, confirming demand was driven by price competition for scarce units, not migration-fueled construction.

The elevated unemployment (5.83%) reflects DC's structural inequality (NW vs SE/NE) rather than broad economic weakness. Adjusting slightly downward from HI for this factor.

**Prediction: -20.00**

---

### Maine (ME)
**Features:** 34.89% appreciation, 4.71% ur, $34,168 income, 1.31% pop growth

ME is a rural New England state with a mid-sized metro (Portland) and significant coastal second-home markets. Its appreciation (34.89%) is between NH (31.83% → -19.98) and CT (36.58% → -18.76). However, ME differs from NH and CT in critical ways: NH is essentially a Boston bedroom community, and CT's housing market is tied to the NYC commuter corridor. Both had more suburban speculative dynamics.

ME's rural character is more similar to VT (41.92% → -6.55), but ME has a real metro area and more coastal resort speculation. ME also has lower income ($34,168) than other New England states, meaning less buffer. Splitting the difference between the suburban-corridor New England states (~-19%) and rural VT (-6.55%), weighted toward the suburban comparables since Portland's market was meaningfully impacted.

**Prediction: -16.00**

---

### Massachusetts (MA)
**Features:** 28.21% appreciation, 4.69% ur, $47,311 income, -0.19% pop growth

MA has lower appreciation (28.21%) than CT (36.58% → -18.76) and NH (31.83% → -19.98), both of which are New England corridor states. The negative population growth (-0.19%) indicates no speculative migration pressure. The very high income ($47,311, second only to CT and DC-area states) provides a significant buffer. Boston's economy (healthcare, education, biotech, finance) is highly diversified.

The Boston metro had a genuine bubble in suburban areas, but the city core has persistent supply constraints (zoning, land scarcity). The statewide decline should be moderated by both the lower appreciation level and the structural economic strength. Less severe than CT/NH by roughly 3-4 points due to lower appreciation and negative pop growth.

**Prediction: -15.50**

---

### Wisconsin (WI)
**Features:** 22.65% appreciation, 4.69% ur, $36,047 income, 1.80% pop growth

WI sits between two clear Midwest anchors: MO (18.82% → -10.97) and MN (24.94% → -21.83). Linear interpolation yields approximately -17.8. WI's economy (manufacturing, agriculture, services) is similar to MN's, and Milwaukee's housing market exhibited moderate bubble characteristics.

However, WI lacks the Minneapolis/St. Paul tech and finance concentration that amplified MN's decline. WI's pop growth (1.80%) and unemployment (4.69%) are moderate. The state was affected by the broader Midwest downturn but wasn't as exposed to speculative dynamics. Adjusting slightly below the interpolation point.

**Prediction: -16.50**

---

### South Carolina (SC)
**Features:** 19.42% appreciation, 6.35% ur, $30,789 income, 5.00% pop growth

SC is a southeastern state with moderate appreciation. The closest comparable is NC (16.94% → -13.06), which has similar pop growth (5.87%) but lower unemployment (4.73%) and higher income ($34,189). SC's high unemployment (6.35%) and low income ($30,789) indicate greater economic vulnerability.

SC's coastal areas (Myrtle Beach, Hilton Head, Charleston) saw second-home and resort speculation, though not on the scale of FL. The combination of moderate appreciation, high pop growth, and high unemployment is a concerning trifecta. GA (15.17% → -24.38) shows how overbuilding with high pop growth can cause severe crashes even with low appreciation, but GA's Atlanta-specific dynamics (extreme suburban sprawl) are unique.

SC should be slightly worse than NC due to higher unemployment and lower income, but without GA's extreme overbuilding pattern.

**Prediction: -13.50**

---

### New York (NY)
**Features:** 40.29% appreciation, 4.50% ur, $43,760 income, -0.37% pop growth

NY has high appreciation (40.29%) but a massive structural buffer: NYC. The city's housing market is dominated by rentals, co-ops with strict board approvals, and condos. These barriers limited speculative purchasing. Manhattan and brownstone Brooklyn are among the most supply-constrained markets in the country.

States with 39-45% appreciation in the training data include WA (-25.19), OR (-25.98), ID (-26.95), and VT (-6.55). But those western states had 3.5-7.7% pop growth driving speculative construction. NY had negative pop growth (-0.37%). The statewide HPI blends NYC (resilient), Long Island (significant declines), Westchester (moderate declines), and upstate (flat to mild). NYC's dominance in the statewide average pulls it well below the western comparables.

High income ($43,760) and negative pop growth provide additional buffers.

**Prediction: -13.00**

---

### Wyoming (WY)
**Features:** 34.89% appreciation, 3.07% ur, $43,805 income, 3.82% pop growth

WY is a sparsely populated energy state (oil, gas, coal, mining). The training data shows energy states were highly resilient: AK (36.14% → 0.00), ND (22.30% → 0.00). MT (36.61% → -10.06) is the closest non-energy-boom comparable with similar appreciation.

WY has nearly identical appreciation to AK (36.14%) but a real economy rather than AK's extreme geographic isolation. WY's very low unemployment (3.07%) and high income ($43,805, energy-sector driven) indicate strong fundamentals. The energy sector sustained demand through the initial crisis phase, though the 2008-2009 oil price collapse eventually impacted the state.

WY should fall between AK (0.00) and MT (-10.06), closer to AK given the energy-sector buffer and strong income.

**Prediction: -7.00**

---

### South Dakota (SD)
**Features:** 17.95% appreciation, 3.01% ur, $34,983 income, 2.53% pop growth

SD is a Great Plains state with the lowest unemployment in the held-out set (3.01%). The training data shows Plains states were the most resilient: IA (0.00), ND (0.00), NE (-2.88), KS (-4.97). SD's appreciation (17.95%) is between IA (13.29%) and ND (22.30%), both of which had zero decline.

SD's economy (agriculture, financial services, tourism) is stable and non-cyclical. There was no speculative construction boom. The very low unemployment and moderate income indicate strong fundamentals. SD should be among the least-affected states, with a very mild decline similar to NE (-2.88) adjusted slightly for the higher appreciation.

**Prediction: -3.20**

---

## Final Predictions

```json
[
  {"state": "MA", "predicted_crash_pct": -15.50},
  {"state": "SC", "predicted_crash_pct": -13.50},
  {"state": "SD", "predicted_crash_pct": -3.20},
  {"state": "CA", "predicted_crash_pct": -40.00},
  {"state": "ME", "predicted_crash_pct": -16.00},
  {"state": "VA", "predicted_crash_pct": -22.50},
  {"state": "NY", "predicted_crash_pct": -13.00},
  {"state": "DC", "predicted_crash_pct": -20.00},
  {"state": "MD", "predicted_crash_pct": -25.50},
  {"state": "WI", "predicted_crash_pct": -16.50},
  {"state": "WY", "predicted_crash_pct": -7.00}
]
```
