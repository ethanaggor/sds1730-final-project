## Analysis Framework

Before predicting each state, I'll identify the key patterns from the training data:

**Pattern 1 - Appreciation is the primary driver, but not sufficient alone.** FL/CA (73-74% appreciation) crashed ~41-45%, while HI (81%) crashed only -18.5% and DC (70%) only -12%. Supply constraints, government employment, and high income moderate the effect.

**Pattern 2 - Population growth amplifies crashes via overbuilding.** FL (6.84% pop growth) crashed worse than CA (2.18% pop growth) despite similar appreciation. ID (7.72% pop growth) and UT (7.01%) crashed harder than their moderate appreciation would predict.

**Pattern 3 - Manufacturing exposure causes crashes independent of bubbles.** MI (8.86% appreciation) crashed -29.4% due to auto industry collapse. OH, IL, MN had moderate appreciation but -12 to -22% crashes from industrial decline.

**Pattern 4 - High income and stable employment sectors insulate.** DC (pcpi $55k, government jobs) and HI (tourism + military) resisted despite extreme appreciation. VT (41.9% appreciation) crashed only -6.6% with its small, rural, supply-constrained market.

**Pattern 5 - States with <15% appreciation and no structural economic weakness rarely crash more than -5%.** IA, ND, SD held at 0%; NE, OK, TX, KS stayed above -5%.

---

## State-by-State Predictions

### WI (Wisconsin) — Predicted: **-13.0%**

WI's appreciation (22.65%) sits between MO (18.82%, crash -10.97) and MN (24.94%, crash -21.83). WI is a Midwest manufacturing state (paper, machinery, food processing in Milwaukee and the Fox Valley corridor), giving it some of the structural vulnerability that hit MN and IL. However, WI's manufacturing base is less concentrated than MI's auto sector and its appreciation is lower than MN/IL (~25-26%). Low population growth (1.80%) means limited overbuilding. The Milwaukee metro would have driven the state's decline. Splitting between MO and MN, weighted toward the milder end given lower appreciation.

**Comparables:** MO (-10.97 at 18.82%), MN (-21.83 at 24.94%), IL (-21.81 at 25.87%)

---

### DE (Delaware) — Predicted: **-22.0%**

DE's appreciation (45.63%) is very close to NJ (48.76%, crash -22.13) and OR (44.87%, crash -25.98). DE sits in the Mid-Atlantic corridor with bubble dynamics similar to MD and NJ. Its pop growth (5.04%) is much higher than NJ's (0.70%), suggesting some overbuilding from migration (people seeking Delaware's tax advantages while commuting to Philadelphia, Wilmington, and Baltimore). However, DE's economy is anchored by financial services (credit card industry headquarters) and chemicals (DuPont), and its PCPI ($40,736) is relatively high. The high appreciation dominates, placing DE near NJ's outcome.

**Comparables:** NJ (-22.13 at 48.76%), OR (-25.98 at 44.87%), WA (-25.19 at 42.91%)

---

### AZ (Arizona) — Predicted: **-47.0%**

AZ is one of the clearest predictions. Its appreciation (73.44%) matches FL (74.37%, crash -44.73) and CA (73.96%, crash -41.04), and its pop growth (9.41%) is far higher than either (FL 6.84%, CA 2.18%). The Phoenix metro was a textbook speculative market: unconstrained desert land for development, massive investor-driven purchases, heavy subprime lending, and rapid construction of tract housing in exurban areas (Maricopa, Queen Creek, Buckeye). The combination of FL-level appreciation with even more overbuilding should produce a crash worse than FL. The spread between FL and CA (~3.7 points) corresponds roughly to FL's 4.66 points of additional pop growth; AZ's 2.57 points above FL suggests an additional ~2 points of severity.

**Comparables:** FL (-44.73 at 74.37%), CA (-41.04 at 73.96%)

---

### GA (Georgia) — Predicted: **-15.0%**

GA has low appreciation (15.17%) but very high pop growth (6.18%), making it structurally similar to NC (16.94% appreciation, 5.87% pop growth, crash -13.06). The Atlanta metro had significant suburban sprawl and was a major center for subprime lending activity, which amplified foreclosure rates beyond what appreciation alone would suggest. Outer-ring suburbs (Clayton, Henry, Rockdale counties) were devastated. GA's higher pop growth than NC and subprime exposure push it slightly below NC's outcome, but the low appreciation caps the overall severity.

**Comparables:** NC (-13.06 at 16.94%), SC (-13.02 at 19.42%), TN (-8.92 at 17.18%)

---

### CO (Colorado) — Predicted: **-5.0%**

CO has very low appreciation (11.88%), identical to NE (11.88%, crash -2.88) and similar to TX (11.68%, crash -4.15) and KS (12.49%, crash -4.97). Denver had already experienced a correction after the dot-com bust in 2001-2002, which suppressed bubble formation during the subsequent national run-up. CO's diversified economy (tech, energy, federal facilities, tourism) and relatively high income ($39,869) provide stability. Pop growth (4.23%) is higher than the low-appreciation comparables but didn't generate speculative overbuilding. CO's crash should be modest, slightly worse than NE/TX due to higher pop growth.

**Comparables:** NE (-2.88 at 11.88%), TX (-4.15 at 11.68%), KS (-4.97 at 12.49%)

---

### NH (New Hampshire) — Predicted: **-12.0%**

NH's appreciation (31.83%) is in the moderate range, comparable to PA (34.06%, crash -9.38), MT (36.61%, crash -10.06), and WY (34.89%, crash -7.70). NH is a New England state with two distinct dynamics: the southern tier (Nashua, Manchester) functions as a Boston commuter zone with bubble exposure, while the northern part is rural. Its New England peers diverge wildly: CT crashed -18.76 (NYC financial sector exposure) while VT crashed only -6.55 (rural, supply-constrained). NH falls between them. High income ($42,866) provides some buffer, but the Boston commuter market exposure pulls it worse than PA/MT/WY. Low population growth (2.23%) limits overbuilding.

**Comparables:** PA (-9.38 at 34.06%), CT (-18.76 at 36.58%), VT (-6.55 at 41.92%), MT (-10.06 at 36.61%)

---

### NV (Nevada) — Predicted: **-52.0%**

NV has the most extreme combination of features in the entire dataset (training + test): near-highest appreciation (79.74%) and by far the highest pop growth (12.18%). Las Vegas was the paradigmatic speculative market with unconstrained desert land, investor-driven condo conversions, rampant subprime lending, and massive tract development. NV's appreciation exceeds FL's (74.37%) by 5.4 points, and its pop growth exceeds FL's (6.84%) by 5.3 points. Only HI had comparable appreciation (80.67%), but HI is an island with severe supply constraints and military/tourism employment stability, factors completely absent in NV. Following the FL-to-CA relationship (where FL's extra 4.66 points of pop growth corresponded to ~3.7 points worse crash), NV's metrics should produce the worst crash in the combined dataset.

**Comparables:** FL (-44.73 at 74.37%), CA (-41.04 at 73.96%); anti-comparable HI (-18.48 at 80.67%, supply-constrained)

---

### RI (Rhode Island) — Predicted: **-23.0%**

RI's appreciation (48.54%) closely matches NJ (48.76%, crash -22.13). RI has weaker economic fundamentals: higher unemployment (5.26% vs NJ's 4.69%), lower income ($38,719 vs $47,366), and negative pop growth (-0.77%). The higher unemployment suggests greater labor market vulnerability to recession. However, negative pop growth implies less overbuilding, which partially offsets. RI's small, dense housing market and proximity to the Boston-Providence corridor created genuine bubble dynamics. The combination of NJ-level appreciation with weaker fundamentals pushes RI slightly below NJ's outcome.

**Comparables:** NJ (-22.13 at 48.76%), OR (-25.98 at 44.87%), MD (-25.30 at 65.16%)

---

### AL (Alabama) — Predicted: **-10.0%**

AL's appreciation (18.37%) is squarely between TN (17.18%, crash -8.92) and MO (18.82%, crash -10.97), and AL's fundamentals are similar to both: moderate unemployment, low-to-moderate income, moderate pop growth. AL's economy (auto manufacturing transplants, military, healthcare) was stable but not booming. The Birmingham metro had some foreclosure issues but nothing approaching the Sand States. AL didn't have significant speculative activity, and its housing market was driven by fundamental demand. Splitting between TN and MO.

**Comparables:** TN (-8.92 at 17.18%), MO (-10.97 at 18.82%), SC (-13.02 at 19.42%)

---

### MA (Massachusetts) — Predicted: **-13.0%**

MA has moderate appreciation (28.21%) combined with very high income ($47,311, second only to DC and CT in the training set) and slightly negative pop growth (-0.19%). The high-income pattern in the training data shows strong insulation: DC ($55k, 70% appreciation, only -11.9% crash), NY ($43.7k, 40.3% appreciation, -14.0% crash). MA's economy is anchored by education, healthcare, biotech, and financial services, all relatively recession-resistant sectors. Boston's housing market has supply constraints (restrictive zoning, older housing stock) that limit overbuilding. The negative pop growth confirms no excess construction. MA should crash less than NY (which had higher appreciation) but more than the rural/resource states. Its high income dampens the effect of its moderate appreciation.

**Comparables:** NY (-14.02 at 40.29%), CT (-18.76 at 36.58%), IL (-21.81 at 25.87% but manufacturing-exposed)

---

### ME (Maine) — Predicted: **-11.0%**

ME's appreciation (34.89%) is identical to WY (34.89%, crash -7.70) and similar to PA (34.06%, crash -9.38) and MT (36.61%, crash -10.06). ME is a rural New England state with some coastal resort/vacation home markets (Portland, Bar Harbor) that participated in the bubble. Its economy depends on tourism, healthcare, and light manufacturing. Low pop growth (1.31%) means minimal overbuilding. ME's moderate income ($34,168) provides no special buffer. Among New England peers, VT at higher appreciation (41.92%) crashed only -6.55, suggesting rural New England markets were somewhat insulated. However, ME's Portland metro is larger and more connected to Boston dynamics than VT, pulling it slightly worse. ME should fall near PA and MT.

**Comparables:** WY (-7.70 at 34.89%), PA (-9.38 at 34.06%), MT (-10.06 at 36.61%), VT (-6.55 at 41.92%)

---

## Final Predictions

```json
[
  {"state": "WI", "predicted_crash_pct": -13.00},
  {"state": "DE", "predicted_crash_pct": -22.00},
  {"state": "AZ", "predicted_crash_pct": -47.00},
  {"state": "GA", "predicted_crash_pct": -15.00},
  {"state": "CO", "predicted_crash_pct": -5.00},
  {"state": "NH", "predicted_crash_pct": -12.00},
  {"state": "NV", "predicted_crash_pct": -52.00},
  {"state": "RI", "predicted_crash_pct": -23.00},
  {"state": "AL", "predicted_crash_pct": -10.00},
  {"state": "MA", "predicted_crash_pct": -13.00},
  {"state": "ME", "predicted_crash_pct": -11.00}
]
```
