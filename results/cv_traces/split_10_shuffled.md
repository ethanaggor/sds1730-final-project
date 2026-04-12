## Analysis and Predictions

### Key Patterns in Training Data

Before predicting, I identified several dynamics in the training data:

1. **Two crash pathways**: (a) Bubble-driven (CA, AZ, NV: high appreciation → overshoot → crash) and (b) Vulnerability-driven (MS, KY, IN: low income, weak labor markets, subprime exposure → default cascades even without extreme bubbles).

2. **Population growth as a moderator among bubble states**: Among states with >70% appreciation, those with high pop growth (NV: 12.18, AZ: 9.41) crashed around -18 to -22, while CA (pop growth only 2.18) crashed -46. Higher pop growth signals fundamental demand; lower signals speculative-only froth.

3. **High income is partially protective**: DC ($55k, -7.70), VA ($42k, 0.00), NJ ($47k, -11.93) all had high appreciation but muted crashes. However, MA ($47k, -25.98) breaks this pattern, suggesting income alone is insufficient.

4. **Plains/energy states were resilient**: OK (0.00), ND (-4.45), TX (-4.15), UT (-6.55) all had low appreciation, low unemployment, and stable non-housing-dependent economies.

---

### State-by-State Reasoning

**Maryland (MD)** — appreciation 65.16, ur 3.85, pcpi $45,293, pop 2.39

Very high appreciation (close to CA 73.96, DC 70.23). High income ($45k) provides some buffer, similar to NJ ($47k, -11.93). Benefits from DC-area government employment stability, but Baltimore was heavily exposed to subprime and foreclosures. Moderate pop growth (2.39) is similar to CA (2.18), suggesting much of the appreciation was speculative. Worse than DC (-7.70) and VA (0.00) due to Baltimore exposure; better than CA (-46) due to higher income and government sector anchor. Comparable: DE (45.63 appreciation, $40k, -26.95) but MD has higher income.

**Prediction: -20.00**

---

**Arkansas (AR)** — appreciation 20.02, ur 5.23, pcpi $29,376, pop 3.56

Modest appreciation, lowest income in the held-out set (close to MS $27,827). MS crashed -41.04 but was an extreme case driven by pervasive subprime in a deeply poor state. AR's economy (Walmart HQ, agriculture, diversified base) provides more stability. Most comparable to AL (18.37, $31k, -10.06) and SC (19.42, $31k, -4.21). AR's slightly higher unemployment (5.23) and lower income than AL pull it slightly negative. Limited speculative activity.

**Prediction: -9.00**

---

**Nebraska (NE)** — appreciation 11.88, ur 3.04, pcpi $35,718, pop 1.96

Identical appreciation to CO (11.88, -9.38), but NE has much lower unemployment (3.04 vs 4.25). Profile is close to the resilient plains cluster: ND (22.30, 3.12, -4.45), TX (11.68, 4.98, -4.15), OK (14.28, 3.91, 0.00). Strong agricultural economy, no speculative building, very tight labor market. No meaningful bubble.

**Prediction: -5.50**

---

**South Dakota (SD)** — appreciation 17.95, ur 3.01, pcpi $34,983, pop 2.53

Remarkably similar to OK (14.28, 3.91, $34,650, 2.54, 0.00) in income and pop growth, with even lower unemployment (3.01). Also comparable to ND (22.30, 3.12, -4.45). SD's slightly higher appreciation than OK offsets its better unemployment. Rural, agricultural, minimal speculation. Among the most crisis-resilient profiles in the dataset.

**Prediction: -3.50**

---

**Florida (FL)** — appreciation 74.37, ur 3.28, pcpi $38,009, pop 6.84

The other classic sand-state bubble alongside CA, AZ, NV. Appreciation (74.37) is nearly identical to CA (73.96) and AZ (73.44). The key differentiator in the training data is pop growth: CA (2.18, -46.01) vs AZ (9.41, -18.48) vs NV (12.18, -21.83). FL's pop growth (6.84) is intermediate, suggesting a mix of real migration demand (retirees, Sunbelt growth) and massive speculation (Miami condo flipping, Cape Coral overbuilding). FL had enormous construction overbuilding, heavy subprime exposure, and a construction-dependent economy. Worse than AZ/NV but less extreme than CA due to higher fundamental demand signaled by pop growth. Income ($38k) is moderate, close to HI ($38k, -21.81).

**Prediction: -26.00**

---

**Georgia (GA)** — appreciation 15.17, ur 4.66, pcpi $34,574, pop 6.18

Strikingly similar to NC (16.94, 4.73, $34,189, 5.87, -19.98) across all four features. Metro Atlanta was hit by suburban overbuilding and significant subprime exposure, particularly in outer-ring exurbs. High pop growth (6.18) provided some genuine demand but also attracted speculative development. Modest appreciation means the bubble pathway is limited; the crash is driven more by subprime defaults and construction job losses. Slightly worse than TX (-4.15) which had structural advantages (energy, elastic supply); comparable to NC.

**Prediction: -17.00**

---

**Missouri (MO)** — appreciation 18.82, ur 4.89, pcpi $33,860, pop 2.33

Middle-of-the-road on every dimension. Most comparable to AL (18.37, 4.01, $31k, -10.06), LA (22.89, 4.14, $34k, -13.02), and WV (25.64, 4.77, $29k, -13.06). St. Louis and Kansas City had moderate housing markets without extreme speculation. MO's slightly higher unemployment (4.89) than AL (4.01) nudges it negative. No dominant sector exposure (not energy, not finance, not manufacturing-heavy).

**Prediction: -12.00**

---

**Connecticut (CT)** — appreciation 36.58, ur 4.42, pcpi $53,224, pop 0.95

Very high income ($53k, second only to DC $55k in the training data). DC with much higher appreciation (70.23) crashed only -7.70, buffered by income and government employment. CT lacks the government anchor but shares the income shield. Financial sector vulnerability (Greenwich/Stamford hedge funds, Hartford insurance) creates downside risk that DC avoided. Appreciation (36.58) is lower than NJ (48.76, -11.93). Higher income than NJ ($47k). These factors suggest CT should crash less than NJ. But low pop growth (0.95) signals limited fundamental demand.

**Prediction: -13.00**

---

**New York (NY)** — appreciation 40.29, ur 4.50, pcpi $43,760, pop -0.37

Moderate-high appreciation, high income, negative pop growth. Statewide figure blends resilient NYC (constrained supply, global demand) with weaker upstate/Long Island suburbs. Most comparable to NJ (48.76, $47k, -11.93) and NH (31.83, $43k, -11.81). NY's appreciation is between NJ and NH, with income between them. Negative pop growth (-0.37) is a negative signal (similar to MA at -0.19, which crashed -25.98). However, NYC's supply constraints provide a floor that MA/Boston lacked. Financial sector crisis is a significant headwind.

**Prediction: -14.00**

---

**Ohio (OH)** — appreciation 9.43, ur 5.43, pcpi $33,976, pop 0.41

Classic Rust Belt profile: very low appreciation, elevated unemployment, stagnant population. Near-identical to MI (8.86, 6.87, $34k, -15.68) and IN (8.68, 5.02, $33k, -20.44). OH sits between MI and IN on unemployment (5.43 vs 6.87 and 5.02). Cleveland was one of the epicenters of predatory/subprime lending nationally. Low appreciation means the crash is vulnerability-driven (manufacturing decline, subprime defaults) rather than bubble-driven. Very low pop growth (0.41) signals economic stagnation.

**Prediction: -16.00**

---

**Maine (ME)** — appreciation 34.89, ur 4.71, pcpi $34,168, pop 1.31

Moderate-high appreciation, moderate income and unemployment, low pop growth. Nearly identical to PA (34.06, 4.73, $37,803, 1.10, -22.13) in appreciation, unemployment, and pop growth, but with lower income ($34k vs $38k). In the New England context: VT (41.92, 3.68, $37k, -3.57) and NH (31.83, 3.52, $43k, -11.81) both had better unemployment and higher income. ME's higher unemployment and lower income than its New England peers suggests a worse outcome than NH (-11.81) but not as extreme as MA (-25.98, an outlier). Portland-area bubble dynamics and seasonal/second-home market add risk. The PA comparison (-22.13) anchors the upper bound.

**Prediction: -15.00**

---

### Final Predictions

```json
[
  {"state": "MD", "predicted_crash_pct": -20.00},
  {"state": "AR", "predicted_crash_pct": -9.00},
  {"state": "NE", "predicted_crash_pct": -5.50},
  {"state": "SD", "predicted_crash_pct": -3.50},
  {"state": "FL", "predicted_crash_pct": -26.00},
  {"state": "GA", "predicted_crash_pct": -17.00},
  {"state": "MO", "predicted_crash_pct": -12.00},
  {"state": "CT", "predicted_crash_pct": -13.00},
  {"state": "NY", "predicted_crash_pct": -14.00},
  {"state": "OH", "predicted_crash_pct": -16.00},
  {"state": "ME", "predicted_crash_pct": -15.00}
]
```
