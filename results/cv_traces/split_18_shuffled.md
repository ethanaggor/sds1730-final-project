## Approach

I'll identify the key patterns in the training data, then use nearest-neighbor reasoning with economic logic to predict each held-out state.

### Key Patterns in the Training Data

After examining all 40 training states, three features show meaningful signal for crash severity:

1. **Appreciation (positive relationship with crash_pct):** States with higher 2003-2006 appreciation tended to have *milder* crashes. The 17 mildest-crash states averaged ~32.5% appreciation; the 14 most severe averaged ~22.6%. This is counterintuitive from a pure-bubble perspective, but may reflect that high-appreciation states had fundamentally strong demand that cushioned the downturn.

2. **Per-capita income (positive relationship):** Higher-income states had milder crashes. Mild-crash states averaged ~$36,500 pcpi; severe-crash states averaged ~$33,300. Wealthier households absorb shocks better, with lower subprime exposure and more equity cushion.

3. **Population growth (positive relationship):** States with higher in-migration had milder crashes (~3.75% avg for mild, ~2.5% for severe). Growing populations sustain housing demand through the downturn.

4. **Unemployment:** Essentially no discriminating power between severity groups (~4.55 vs ~4.59).

**Notable outliers:** WV (-55.69), NE (-46.01), and NC (-44.73) are extreme. States with very similar feature profiles can differ by 15+ points (e.g., MN -24.38 vs IL -8.92), indicating substantial unobserved factors (subprime concentration, construction overbuilding, local banking health).

---

## State-by-State Predictions

### WY (Wyoming) — Predicted: **-1.0**
**Closest comps:** MT (0.00), ID (0.00), VT (0.00), AK (-3.57), NH (-4.15)

WY's profile (appreciation 34.89, ur 3.07, pcpi 43805, pop 3.82) closely matches Montana (appreciation 36.61, ur 3.37, pcpi 31870, pop 3.60), which experienced no crash. WY actually has a much higher pcpi ($43,805 vs $31,870), which is strongly protective. All three zero-crash states share moderate-high appreciation (>36%) and low UR (<3.7%); WY fits this archetype at 34.89% and 3.07% UR. The small energy-driven economy with strong income provides resilience.

### VA (Virginia) — Predicted: **-4.5**
**Closest comps:** DE (-6.70), NJ (-7.30), NH (-4.15)

VA has high appreciation (53.63), very low UR (3.08), high pcpi ($42,164), and solid pop growth (4.16). Delaware is the best comp (mid-Atlantic, appreciation 45.63, ur 3.58, pcpi $40,736, pop 5.04) at -6.70. VA improves on DE with 8 points higher appreciation and lower UR, both strongly protective. The federal government employment base (especially Northern Virginia's defense/contracting corridor) provides unusual economic stability. Slightly better than DE.

### MD (Maryland) — Predicted: **-6.0**
**Closest comps:** DE (-6.70), NJ (-7.30), FL (-10.06)

MD has very high appreciation (65.16), low UR (3.85), high pcpi ($45,293), and moderate pop growth. This is a protective profile on all dimensions. DE (-6.70) is the nearest mid-Atlantic comp, but MD has 20 points more appreciation and $4,500 more pcpi. NJ (-7.30) has similar pcpi but much lower appreciation. MD benefits from proximity to DC's federal economy, but its appreciation approaches bubble-state territory (60%+), where the four high-bubble training states averaged about -9. I rate it slightly better than NJ/DE given the income base, but the extreme appreciation adds some risk.

### CA (California) — Predicted: **-10.5**
**Closest comps:** AZ (-8.67), FL (-10.06), NV (-7.26), HI (-10.14)

CA's appreciation (73.96) is nearly identical to AZ (73.44) and FL (74.37). In this dataset, all four bubble states (AZ, FL, NV, HI) clustered in the -7 to -10 range. However, CA has worse ancillary features: higher UR (4.89 vs AZ 4.27, FL 3.28) and much lower pop growth (2.18 vs AZ 9.41, FL 6.84). The lower pop growth means less demand absorption as prices corrected. CA's pcpi ($41,454) is the highest among bubble comps, providing some offset. Net effect: slightly worse than the bubble-state average of -9.0.

### DC (Washington DC) — Predicted: **-12.5**
**Closest comps:** Bubble states (AZ/FL/NV/HI: -7 to -10), RI (-25.98), CT (-18.48)

DC is unique: very high appreciation (70.23), highest pcpi in the dataset ($55,384), but also high UR (5.83) and low pop growth (0.38). The high appreciation and pcpi strongly pull toward mild crashes. But high UR + low pop growth are significant risk factors; RI (appreciation 48.54, ur 5.26, pop -0.77) had -25.98 with a similar high-UR/low-growth profile. DC's federal employment base provides stability (like a much richer CT), and its pcpi is $17k higher than RI's, which should significantly buffer the crash. I estimate DC between the bubble states (-9 avg) and RI (-26), weighted heavily toward the milder end by its extreme pcpi advantage.

### NY (New York) — Predicted: **-13.0**
**Closest comps:** NJ (-7.30), CT (-18.48), PA (-19.98), IL (-8.92)

NY's appreciation (40.29) sits between NJ (48.76) and CT (36.58). Its pcpi ($43,760) is between NJ ($47,366) and CT ($53,224), closer to NJ. NY's negative pop growth (-0.37) is a notable risk factor; RI is the only training state with negative pop growth and high appreciation, and it crashed badly (-25.98). Adjusting NJ's -7.30 downward for NY's ~8 points less appreciation (~4 points penalty) and negative pop growth (~2 point penalty) yields about -13. This aligns with the midpoint between NJ and CT.

### MA (Massachusetts) — Predicted: **-15.0**
**Closest comps:** NJ (-7.30), CT (-18.48), PA (-19.98), IL (-8.92)

MA has moderate appreciation (28.21), the lowest among Northeast high-income states. Its pcpi ($47,311) nearly matches NJ ($47,366), but appreciation is 20 points lower. In this dataset, each 10 points of additional appreciation corresponds to roughly 5 points milder crash. So MA at 28.21 vs NJ at 48.76 (20-point gap) implies about 10 points worse: -7.30 - 10 ≈ -17. But MA's very high pcpi offsets this somewhat. Negative pop growth (-0.19) is an additional small risk factor. I estimate -15 as a compromise between the NJ-adjusted estimate and the PA comp (-20).

### SC (South Carolina) — Predicted: **-17.0**
**Closest comps:** MS (-26.95), TN (-10.97), AL (-25.19), KY (-9.38), GA (-4.45)

SC has high UR (6.35, close to MS at 6.38), low pcpi ($30,789), moderate appreciation (19.42), and good pop growth (5.00). Among high-UR training states (>5.5), MS (-26.95) and AK (-3.57) show the extremes. SC's low pcpi aligns with MS (crash risk), but its strong pop growth (5.00 vs MS's 1.28) provides significant demand support. TN is the best overall profile match (appreciation 17.18, ur 5.22, pcpi $32,878, pop 4.12) at -10.97; adjusting for SC's 1.13 higher UR suggests about 6 points worse crash. This yields approximately -17.

### WI (Wisconsin) — Predicted: **-17.5**
**Closest comps:** MN (-24.38), IL (-8.92), PA (-19.98), IA (-27.60)

WI's profile (appreciation 22.65, ur 4.69, pcpi $36,047, pop 1.80) is closest to neighboring MN (appreciation 24.94, ur 4.06, pcpi $39,362, pop 2.18). MN had -24.38. But IL, with very similar appreciation (25.87) and UR (4.62), had only -8.92. This 15-point gap between similar Midwest states reflects unobserved factors. WI has lower pcpi than both MN and IL, which pushes worse. PA (-19.98) with very similar UR (4.73) and moderate pcpi ($37,803) provides another anchor. I estimate roughly the midpoint of MN and IL, slightly weighted toward the more severe end given WI's lower pcpi.

### ME (Maine) — Predicted: **-21.0**
**Closest comps:** PA (-19.98), NM (-21.93), OR (-21.83), CT (-18.48)

ME (appreciation 34.89, ur 4.71, pcpi $34,168, pop 1.31) is strikingly similar to PA (appreciation 34.06, ur 4.73, pcpi $37,803, pop 1.10). Nearly identical appreciation and UR, with ME having ~$3,600 less pcpi. That income gap suggests a slightly worse outcome than PA's -19.98. New England neighbors VT (0.00) and NH (-4.15) had milder crashes, but both had lower UR (3.68, 3.52) and VT had higher appreciation. ME lacks those protective features, sitting closer to the PA/NM/OR cluster at -20 to -22.

### SD (South Dakota) — Predicted: **-24.0**
**Closest comps:** ND (-29.40), NE (-46.01), IA (-27.60), OK (-9.90), KS (-6.55)

SD is a Plains state with features closest to neighboring ND (appreciation 22.30, ur 3.12, pcpi $33,120, pop 1.66). ND crashed -29.40. NE, the other neighbor (ur 3.04, pcpi $35,718), crashed -46.01. SD has lower appreciation than ND (17.95 vs 22.30), pushing toward worse crash, but higher pcpi ($34,983 vs $33,120) and higher pop growth (2.53 vs 1.66), both protective. OK (-9.90) and KS (-6.55) have similar pcpi but higher UR, representing a much milder scenario. The Plains states (ND, NE, IA) consistently show severe crashes in this data. I estimate SD somewhat better than ND due to higher pcpi and pop growth, landing at -24.

---

## Final Predictions

```json
[
  {"state": "MA", "predicted_crash_pct": -15.0},
  {"state": "SC", "predicted_crash_pct": -17.0},
  {"state": "SD", "predicted_crash_pct": -24.0},
  {"state": "CA", "predicted_crash_pct": -10.5},
  {"state": "ME", "predicted_crash_pct": -21.0},
  {"state": "VA", "predicted_crash_pct": -4.5},
  {"state": "NY", "predicted_crash_pct": -13.0},
  {"state": "DC", "predicted_crash_pct": -12.5},
  {"state": "MD", "predicted_crash_pct": -6.0},
  {"state": "WI", "predicted_crash_pct": -17.5},
  {"state": "WY", "predicted_crash_pct": -1.0}
]
```
