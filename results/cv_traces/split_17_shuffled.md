## Approach

I'll analyze the training data for patterns, identify the most relevant comparable states for each held-out state, and combine data-driven inference with domain knowledge of the 2008 crisis.

### Key patterns in the training data

**Appreciation is not the sole driver.** High-appreciation states like NV (79.74 -> -55.69) and CA (73.96 -> -21.81) crashed hard, but NJ (48.76 -> 0.00) and NY (40.29 -> -2.88) barely declined despite large bubbles. Meanwhile, low-appreciation states like KS (12.49 -> -46.01) and SD (17.95 -> -44.73) had severe crashes, suggesting idiosyncratic factors the features don't fully capture.

**Wealthy Northeast states were insulated.** NJ (47366 income, 0.00 crash), MA (47311, -4.15), NY (43760, -2.88), IL (40021, -4.97) form a cluster where high income buffered price declines.

**The DC metro corridor crashed hard.** MD (-25.30) and DC (-26.95), both high-appreciation, high-income areas, had severe declines, distinguishing them from the NJ/NY/MA cluster.

**High unemployment alone doesn't predict severity.** MS (6.38 UR, 0.00) and SC (6.35, 0.00) had the highest unemployment and no crash, while TN (5.22, -41.04) collapsed. The interaction between labor markets and bubble dynamics matters more than either alone.

**Median crash: -13.04. Mean: -16.20.** The distribution has a heavy left tail driven by outliers (KS, SD, TN, NV).

---

## State-by-State Predictions

### KY (appreciation: 14.25, UR: 5.73, income: 30476, pop growth: 2.48)

Low appreciation and low income place KY in the non-bubble Southern/Appalachian tier. Closest comparables:
- **AL** (18.37, 4.01, 31264, 2.79) -> -13.06: geographic neighbor, similar income and pop growth
- **OK** (14.28, 3.91, 34650, 2.54) -> -14.02: nearly identical appreciation and pop growth
- **NC** (16.94, 4.73, 34189, 5.87) -> -9.38
- **IN** (8.68, 5.02, 32905, 2.20) -> -9.90: similar economic profile

KY's unemployment (5.73) is higher than all four comps, which adds labor market vulnerability. Kentucky's mixed economy (coal, bourbon, manufacturing, agriculture) lacked the speculative construction of Sun Belt states but was exposed to manufacturing decline. Average of comps: -11.59, adjusted slightly worse for unemployment.

**Prediction: -12.00**

---

### OH (appreciation: 9.43, UR: 5.43, income: 33976, pop growth: 0.41)

Rock-bottom appreciation (second lowest in all data) and near-zero population growth define Ohio as a Rust Belt state with no bubble to burst. The crash is demand-driven, not bubble-driven.

- **IN** (8.68, 5.02, 32905, 2.20) -> -9.90: nearest Rust Belt comp, nearly identical appreciation and income
- **MO** (18.82, 4.89, 33860, 2.33) -> -4.21: similar income
- **GA** (15.17, 4.66, 34574, 6.18) -> -10.06

OH has worse unemployment (5.43 vs IN 5.02) and much worse pop growth (0.41 vs IN 2.20), signaling structural economic decline. Manufacturing job losses dragged down housing demand. But the absence of a bubble limits the percentage decline from peak.

**Prediction: -10.00**

---

### WI (appreciation: 22.65, UR: 4.69, income: 36047, pop growth: 1.80)

Moderate Midwest state with modest bubble. The two nearest geographic comps diverge wildly:
- **MN** (24.94, 4.06, 39362, 2.18) -> -22.13: closest Midwest neighbor, similar appreciation
- **IL** (25.87, 4.62, 40021, 0.70) -> -4.97: similar appreciation and unemployment
- **ND** (22.30, 3.12, 33120, 1.66) -> -7.70: almost identical appreciation and pop growth
- **UT** (23.39, 2.87, 31107, 7.01) -> -8.92

MN's severity (-22.13) is puzzling given its moderate fundamentals; IL's mildness (-4.97) is equally surprising. WI sits between them economically. Wisconsin's diversified economy (agriculture, manufacturing, services) and moderate appreciation suggest a middle-ground outcome. Average of comps: -10.93, weighted toward MN as the geographic twin.

**Prediction: -12.00**

---

### OR (appreciation: 44.87, UR: 5.39, income: 34488, pop growth: 3.48)

The highest appreciation among held-out states outside VA. Oregon had genuine speculative activity in the Portland metro.

- **WA** (42.91, 4.99, 39744, 4.37) -> -6.55: Pacific NW neighbor, nearly identical appreciation
- **DE** (45.63, 3.58, 40736, 5.04) -> -15.68: almost identical appreciation
- **MT** (36.61, 3.37, 31870, 3.60) -> -7.30: similar region and pop growth
- **VT** (41.92, 3.68, 36609, 0.81) -> -21.93

WA is the strongest comp (same region, same appreciation level, similar economic structure), but OR has materially higher unemployment (5.39 vs 4.99) and lower income (34488 vs 39744). Oregon's timber and manufacturing sectors were more vulnerable to recession. These weaker fundamentals should produce a worse outcome than WA. Anchored to WA at -6.55, adjusted up for worse labor market.

**Prediction: -10.00**

---

### VA (appreciation: 53.63, UR: 3.08, income: 42164, pop growth: 4.16)

The DC metro bubble clearly extended into Northern Virginia. High appreciation signals genuine overvaluation.

- **MD** (65.16, 3.85, 45293, 2.39) -> -25.30: DC metro neighbor, the primary comp
- **DC** (70.23, 5.83, 55384, 0.38) -> -26.95: geographic anchor
- **NJ** (48.76, 4.69, 47366, 0.70) -> 0.00: similar appreciation, wealthy
- **RI** (48.54, 5.26, 38719, -0.77) -> -20.44
- **DE** (45.63, 3.58, 40736, 5.04) -> -15.68

The DC corridor (MD, DC) consistently shows a crash-to-appreciation ratio of about -0.38 to -0.39. Applying this to VA: 53.63 * 0.39 = -20.9. However, VA has the lowest unemployment in the held-out set (3.08), strong government/defense employment providing a floor, and better pop growth than MD. These fundamentals should moderate the crash below the raw ratio estimate. VA lands between the severe DC-metro crash and the insulated wealthy-Northeast pattern.

**Prediction: -18.00**

---

### AK (appreciation: 36.14, UR: 6.62, income: 41013, pop growth: 4.15)

Alaska is unique: resource-dependent (oil), geographically isolated, thin housing market, high cost of living reflected in elevated income.

- **WY** (34.89, 3.07, 43805, 3.82) -> -24.38: fellow resource state, similar appreciation and income
- **MT** (36.61, 3.37, 31870, 3.60) -> -7.30: nearly identical appreciation, Northern/rural
- **ME** (34.89, 4.71, 34168, 1.31) -> -13.02: similar appreciation

WY is the natural resource-state comp but had much lower unemployment (3.07 vs 6.62). Alaska's highest-in-dataset unemployment signals pre-existing economic weakness, but its resource income premium and geographic isolation constrain both speculation and price collapse. Oil prices crashed in late 2008, which would depress demand, but Alaska's housing market has limited inventory and low turnover. Splitting between MT (-7.30) and WY (-24.38), weighted toward the middle.

**Prediction: -13.00**

---

### WV (appreciation: 25.64, UR: 4.77, income: 28528, pop growth: 0.86)

The lowest income in the entire dataset signals a structurally weak economy with limited housing speculation. Thin markets with low prices don't attract speculators.

- **AR** (20.02, 5.23, 29376, 3.56) -> -6.70: closest in income
- **ND** (22.30, 3.12, 33120, 1.66) -> -7.70: similar appreciation and pop growth
- **IL** (25.87, 4.62, 40021, 0.70) -> -4.97: similar appreciation and pop growth
- **LA** (22.89, 4.14, 33627, -4.83) -> -10.97

WV's Appalachian economy (coal, services) was already stagnant. Low appreciation (25.64) reflects fundamental demand, not speculation. The absence of a bubble limits downside. Average of closest comps: -7.59.

**Prediction: -8.00**

---

### CT (appreciation: 36.58, UR: 4.42, income: 53224, pop growth: 0.95)

CT has the second-highest income in the entire dataset (only DC is higher). This places it firmly in the wealthy Northeast cluster.

- **NJ** (48.76, 4.69, 47366, 0.70) -> 0.00: wealthy Northeast
- **MA** (28.21, 4.69, 47311, -0.19) -> -4.15: wealthy Northeast
- **NY** (40.29, 4.50, 43760, -0.37) -> -2.88: wealthy Northeast
- **MT** (36.61, 3.37, 31870, 3.60) -> -7.30: nearly identical appreciation
- **PA** (34.06, 4.73, 37803, 1.10) -> -18.48: similar appreciation, nearby

The wealthy cluster (NJ/MA/NY) averaged -2.34 crash, suggesting strong income-based insulation. But CT has a critical differentiator: financial sector concentration (hedge funds in Fairfield County, insurance in Hartford). The 2008 crisis was a financial crisis, hitting CT's core industries harder than NJ's pharma or NY's diversified economy. AIG, headquartered in CT, required a federal bailout. This structural exposure to the financial sector pushes CT's crash beyond the typical wealthy-Northeast outcome, but the extreme income buffer keeps it moderate.

**Prediction: -10.00**

---

### CO (appreciation: 11.88, UR: 4.25, income: 39869, pop growth: 4.23)

CO's appreciation is identical to NE (11.88) and similar to TX (11.68), KS (12.49). This reflects Colorado's post-dot-com correction; the housing market had already deflated in 2001-2003, so 2003-2006 appreciation was catching up, not bubbling.

- **TX** (11.68, 4.98, 35422, 6.03) -> -13.11: nearly identical appreciation, diversified economy
- **OK** (14.28, 3.91, 34650, 2.54) -> -14.02: similar appreciation
- **NE** (11.88, 3.04, 35718, 1.96) -> -27.60: identical appreciation but very different outcome

TX is the best comp: similar low appreciation, diversified economy, good pop growth. CO has higher income (39869 vs 35422), lower unemployment (4.25 vs 4.98), and similarly strong pop growth. These better fundamentals should produce a slightly milder outcome than TX. NE's severe crash (-27.60) with identical appreciation seems driven by factors not captured in the features; CO's diversified urban economy (tech, aerospace, energy, military) is fundamentally different from Nebraska's agricultural base.

**Prediction: -10.00**

---

### MI (appreciation: 8.86, UR: 6.87, income: 33563, pop growth: -0.05)

Michigan has the worst combination of fundamentals in the entire dataset: highest unemployment, lowest appreciation, and the only state (alongside LA and NY) with negative/near-zero pop growth. The auto industry was already collapsing before the financial crisis hit.

- **IN** (8.68, 5.02, 32905, 2.20) -> -9.90: closest Rust Belt comp
- **MS** (16.40, 6.38, 27827, 1.28) -> 0.00: similar high unemployment
- **SC** (19.42, 6.35, 30789, 5.00) -> 0.00: similar high unemployment

IN is the anchor comp, but MI's fundamentals are dramatically worse: unemployment 6.87 vs 5.02, pop growth -0.05 vs 2.20. The auto bailout, GM and Chrysler bankruptcies, and cascading supplier failures created a demand collapse that drove foreclosures and price declines even in the absence of a bubble. MS and SC show that high unemployment alone doesn't cause a crash (their markets were already at equilibrium or too small to attract speculation), but Michigan's combination of manufacturing collapse, population flight, and foreclosure waves is qualitatively different.

**Prediction: -15.00**

---

### NH (appreciation: 31.83, UR: 3.52, income: 42866, pop growth: 2.23)

New Hampshire straddles two patterns: the New England speculative corridor (ME, VT) and the wealthy Northeast insulation cluster (MA, NJ).

- **ME** (34.89, 4.71, 34168, 1.31) -> -13.02: New England neighbor, similar appreciation
- **VT** (41.92, 3.68, 36609, 0.81) -> -21.93: New England, higher appreciation
- **MA** (28.21, 4.69, 47311, -0.19) -> -4.15: income peer, southern neighbor
- **PA** (34.06, 4.73, 37803, 1.10) -> -18.48: similar appreciation

NH's income (42866) is well above ME (34168) and VT (36609), approaching MA territory. Southern NH functions as a Boston exurb, benefiting from spillover demand and commuter fundamentals. Lower unemployment (3.52) than ME (4.71) signals economic strength. However, NH's appreciation (31.83) indicates real speculative activity, and exurban markets tend to be more volatile than urban cores. NH should do better than ME and VT (income buffer) but worse than MA (more speculation, less economic diversification). Anchored between ME (-13.02) and MA (-4.15).

**Prediction: -12.00**

---

## Final Predictions

```json
[
  {"state": "KY", "predicted_crash_pct": -12.00},
  {"state": "OH", "predicted_crash_pct": -10.00},
  {"state": "WI", "predicted_crash_pct": -12.00},
  {"state": "OR", "predicted_crash_pct": -10.00},
  {"state": "VA", "predicted_crash_pct": -18.00},
  {"state": "AK", "predicted_crash_pct": -13.00},
  {"state": "WV", "predicted_crash_pct": -8.00},
  {"state": "CT", "predicted_crash_pct": -10.00},
  {"state": "CO", "predicted_crash_pct": -10.00},
  {"state": "MI", "predicted_crash_pct": -15.00},
  {"state": "NH", "predicted_crash_pct": -12.00}
]
```
