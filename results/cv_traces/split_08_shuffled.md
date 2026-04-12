## Analysis Framework

Before predicting each state, let me identify the key patterns in the training data.

**Two distinct crash mechanisms emerge:**
1. **Bubble correction**: States with high appreciation (>50%) experienced moderate crashes (-4% to -22%), buffered by high income (CA, MD, DC) or not (AZ, NV).
2. **Economic deterioration**: States with low appreciation but weak labor markets (high UR, low income, stagnant population) suffered the worst crashes (KY -55.69, MI -46.01, KS -41.04). The recession hit these economies structurally, not just through housing deflation.

**Key observations from training data:**
- High appreciation + high income is protective (MD -4.15, CA -6.70, DC -9.90)
- Very high UR (>5.5) combined with low appreciation produces extreme outcomes, but inconsistently (MI -46.01 vs MS -2.88)
- Low appreciation states have enormous variance (0.00 to -55.69), suggesting important unobserved factors
- Population growth has an ambiguous effect: it can signal speculative overbuilding (NV) or genuine demand (NC)

Training set mean: approximately -16.8%. Median: approximately -14.9%.

---

## State-by-State Predictions

### OR (Oregon)
**Features:** appr 44.87, ur 5.39, pcpi 34488, pop 3.48

Oregon is a Pacific Northwest state most comparable to its neighbor WA (42.91 appr, 4.99 ur, 39744 pcpi → -9.38). However, OR has meaningfully higher unemployment (5.39 vs 4.99) and lower income (34488 vs 39744), both indicating weaker fundamentals. ME (34.89 appr, 4.71 ur, 34168 pcpi → -18.76) is another strong comparable with similar appreciation and income. Oregon's timber-dependent rural economy was vulnerable, and the Portland metro saw significant bubble activity. The higher UR and lower income relative to WA push OR toward the ME range rather than the WA range.

**Prediction: -17.0**

---

### OK (Oklahoma)
**Features:** appr 14.28, ur 3.91, pcpi 34650, pop 2.54

Low appreciation and low unemployment place OK squarely in the stable-economy cluster. Direct comparables: AL (18.37 appr, 4.01 ur, 31264 pcpi → -4.97), ND (22.30 appr, 3.12 ur, 33120 pcpi → -4.45), NE (11.88 appr, 3.04 ur, 35718 pcpi → 0.00). Oklahoma's energy economy (oil and natural gas) provided significant resilience during the crisis, as commodity prices were elevated. Its UR (3.91) is slightly lower than AL's (4.01), and its income (34650) is higher than both AL and ND. Minimal bubble means minimal correction, but not fully immune given states like TX (11.68 appr, 4.98 ur → -19.98), though TX had notably higher UR and population-growth-driven construction.

**Prediction: -7.0**

---

### SC (South Carolina)
**Features:** appr 19.42, ur 6.35, pcpi 30789, pop 5.00

SC's high unemployment (6.35) is the headline risk factor, comparable to MS (6.38 ur → -2.88). However, SC has higher appreciation, higher income, and much higher population growth than MS. Southeast comparables: NC (16.94 appr, 4.73 ur, 34189 pcpi → -6.55), GA (15.17 appr, 4.66 ur, 34574 pcpi → -18.48), TN (17.18 appr, 5.22 ur, 32878 pcpi → -14.02). SC's UR is much higher than all of these, but MS shows that high UR in the South doesn't necessarily produce catastrophic crashes. SC's coastal resort markets (Myrtle Beach, Hilton Head) introduced some speculative vulnerability that MS lacked, pulling the estimate toward GA/TN territory. The high pop growth (5.00) suggests genuine migration-driven demand, providing some floor.

**Prediction: -12.0**

---

### AK (Alaska)
**Features:** appr 36.14, ur 6.62, pcpi 41013, pop 4.15

Alaska is sui generis: the highest UR in the held-out set (6.62, comparable to MI's 6.87) but also very high income (41013, comparable to WA/VA). In the training data, the two states with UR above 6 produced wildly different outcomes: MI (-46.01) and MS (-2.88). Alaska's oil-driven economy and high income buffer against MI-style collapse; its remote, isolated housing market didn't experience the speculative construction booms of lower-48 bubble states. The moderate appreciation (36.14) is comparable to ME (34.89 appr → -18.76) and PA (34.06 appr → -25.19). Alaska's high income pushes it toward NH (31.83 appr, 3.52 ur, 42866 pcpi → -11.81), but the much higher UR drags it worse. Net assessment: moderate crash, buffered by oil wealth but dragged by structural unemployment.

**Prediction: -15.0**

---

### MT (Montana)
**Features:** appr 36.61, ur 3.37, pcpi 31870, pop 3.60

Montana's closest training comparable is ID (39.45 appr, 3.39 ur, 31244 pcpi → -29.40): nearly identical appreciation, UR, and income. The critical difference is population growth: MT (3.60) vs ID (7.72). Idaho's extreme population growth likely fueled speculative overbuilding that amplified its crash. NM (32.57 appr, 4.23 ur, 30433 pcpi → -8.92) offers a lower bound: similar appreciation and income, slightly higher UR, moderate pop growth. Montana's mountain resort markets (Big Sky, Whitefish) saw some speculative appreciation, but the state's modest pop growth suggests less overbuilding than Idaho. Splitting between NM's -8.92 and ID's -29.40, weighted toward ID given the closer feature match in appreciation and UR.

**Prediction: -17.0**

---

### WV (West Virginia)
**Features:** appr 25.64, ur 4.77, pcpi 28528, pop 0.86

WV is an Appalachian state with the lowest income in the held-out set, raising the specter of KY (14.25 appr, 5.73 ur, 30476 pcpi → -55.69). However, WV differs meaningfully: higher appreciation (25.64 vs 14.25, suggesting some genuine price support), lower UR (4.77 vs 5.73), and KY's crash appears to be an extreme outlier even among weak-economy states. Other low-income comparables: MS (27827 pcpi → -2.88), AR (29376 pcpi → -8.67) had mild crashes. MO (18.82 appr, 4.89 ur, 33860 pcpi → -21.83) is a closer overall match. WV's coal-dependent economy was in structural decline, and near-zero population growth (0.86) signals stagnation. These factors push beyond MO-type moderate crash territory but not toward KY extremes.

**Prediction: -18.0**

---

### OH (Ohio)
**Features:** appr 9.43, ur 5.43, pcpi 33976, pop 0.41

Ohio is a Rust Belt manufacturing state with the clearest training comparable being MI (8.86 appr, 6.87 ur, 33563 pcpi, -0.05 pop → -46.01). Nearly identical appreciation and income, but OH has significantly lower UR (5.43 vs 6.87) and slightly positive population growth (0.41 vs -0.05). Ohio's economy was more diversified than Michigan's (less concentrated in auto manufacturing), with Columbus providing a government/education anchor. The 1.44 percentage point UR advantage over MI is substantial. Other Midwest comparables: IL (25.87 appr, 4.62 ur → -20.44, but much higher appreciation), IA (13.29 appr, 3.69 ur → -13.11, much lower UR). OH sits between the MI extreme and the IL/IA moderate range, weighted toward severe given the very low appreciation and moderately high UR.

**Prediction: -25.0**

---

### FL (Florida)
**Features:** appr 74.37, ur 3.28, pcpi 38009, pop 6.84

FL is a classic bubble state. The highest appreciation in the held-out set puts it alongside training bubble states: AZ (73.44 appr, 4.27 ur → -17.56), CA (73.96 appr, 4.89 ur → -6.70), NV (79.74 appr, 4.17 ur → -22.13), HI (80.67 appr, 2.57 ur → -17.39). FL's very low UR (3.28) is second only to HI (2.57) among these, which is a protective factor. However, FL's high population growth (6.84) signals speculative, migration-driven overbuilding (condo towers in Miami, retirement community sprawl), similar to AZ (9.41 pop) and NV (12.18 pop). FL lacks CA's high income buffer (38009 vs 41454) and CA's lower pop growth. FL is most comparable to AZ: similar appreciation, moderate income, high pop growth. FL's lower UR offsets slightly, but its economy was heavily construction-dependent.

**Prediction: -18.0**

---

### WY (Wyoming)
**Features:** appr 34.89, ur 3.07, pcpi 43805, pop 3.82

Wyoming combines moderate-high appreciation with very low unemployment and the highest income in the held-out set. Closest comparables: NH (31.83 appr, 3.52 ur, 42866 pcpi → -11.81) is a near-perfect match in appreciation, UR, and income. VA (53.63 appr, 3.08 ur, 42164 pcpi → -15.68) has similar UR and income but higher appreciation. NE (11.88 appr, 3.04 ur, 35718 pcpi → 0.00) has similar UR but much lower appreciation. Wyoming's energy economy (coal, natural gas, oil) was resilient during the crisis period. Its very low UR and high income provide substantial buffers. The moderate appreciation suggests some bubble activity in resort/vacation markets (Jackson Hole) but not extreme overbuilding given modest pop growth. Very close to NH.

**Prediction: -12.0**

---

### IN (Indiana)
**Features:** appr 8.68, ur 5.02, pcpi 32905, pop 2.20

Indiana is a Midwest manufacturing state with nearly identical appreciation to MI (8.86). Key differences: substantially lower UR (5.02 vs 6.87) and positive population growth (2.20 vs -0.05). IN's economy was manufacturing-heavy but more diversified than MI (Indianapolis as a services hub, pharmaceutical industry). Comparables: TX (11.68 appr, 4.98 ur, 35422 pcpi → -19.98) and MO (18.82 appr, 4.89 ur, 33860 pcpi → -21.83) have very similar UR and income. IL (25.87 appr, 4.62 ur, 40021 pcpi → -20.44) is also comparable but with higher appreciation and income. IN's very low appreciation means there was minimal bubble to correct; the crash here is driven by economic recession impacts. The moderate UR (5.02) puts it in the -19 to -22 range of TX, MO, and IL.

**Prediction: -20.0**

---

### SD (South Dakota)
**Features:** appr 17.95, ur 3.01, pcpi 34983, pop 2.53

SD is a Great Plains state that maps almost perfectly to its neighbors: NE (11.88 appr, 3.04 ur, 35718 pcpi → 0.00) and ND (22.30 appr, 3.12 ur, 33120 pcpi → -4.45). Very low UR, moderate income, low-moderate appreciation, stable agricultural/service economy. SD's appreciation (17.95) falls between NE and ND; its UR (3.01) is slightly lower than both; its income (34983) is between them. These states were among the most insulated from the housing crisis: minimal bubble, strong labor markets, no speculative overbuilding. SD should fall squarely between NE and ND.

**Prediction: -4.0**

---

## Final Predictions

```json
[
  {"state": "OR", "predicted_crash_pct": -17.00},
  {"state": "OK", "predicted_crash_pct": -7.00},
  {"state": "SC", "predicted_crash_pct": -12.00},
  {"state": "AK", "predicted_crash_pct": -15.00},
  {"state": "MT", "predicted_crash_pct": -17.00},
  {"state": "WV", "predicted_crash_pct": -18.00},
  {"state": "OH", "predicted_crash_pct": -25.00},
  {"state": "FL", "predicted_crash_pct": -18.00},
  {"state": "WY", "predicted_crash_pct": -12.00},
  {"state": "IN", "predicted_crash_pct": -20.00},
  {"state": "SD", "predicted_crash_pct": -4.00}
]
```
