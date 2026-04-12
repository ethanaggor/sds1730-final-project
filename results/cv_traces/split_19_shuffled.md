## Analysis of Training Data Patterns

Before predicting, I need to extract the signal from the noise in these 40 training states. Key observations:

**Income effect**: Low-pcpi states crash harder on average. States with pcpi < 33k average roughly -22%, while states above 40k average roughly -13% (excluding CT, a clear outlier at -46).

**Unemployment effect**: Lower pre-crash unemployment is mildly protective. States with ur < 3.5 average about -12%, while ur > 5.0 averages about -18%.

**Population growth**: High pop growth (>5%) is protective in this data: AZ (0.00), NC (0.00), FL (-4.15), UT (-4.97), TX (-10.14). Exception: SC (-55.69).

**Appreciation**: Counterintuitively, higher appreciation does NOT predict worse crashes here. The very high-appreciation states (>60%) average about -10%, while medium appreciation (20-50%) averages about -19%. The relationship is non-linear and noisy.

**Severe crash outliers** (SC, CT, CO, MO) don't share a single common profile, suggesting substantial state-specific noise.

---

## Predictions

### Idaho (ID)
**Features**: appreciation 39.45, ur 3.39, pcpi 31244, pop 7.72

Idaho's strongest protective signal is its very high population growth (7.72), 4th highest in the full dataset. Training states with pop > 6%: AZ (0.00), FL (-4.15), UT (-4.97), NC (0.00), TX (-10.14). Its low unemployment (3.39) reinforces this. The best overall comp is **UT** (ur 2.87, pcpi 31107, pop 7.01, crash -4.97), which matches on income, ur, and pop growth. However, ID's higher appreciation (39.45 vs 23.39) pulls it slightly worse, toward **OR** (-11.81, appreciation 44.87) territory.

**Predicted: -10.50**

---

### Massachusetts (MA)
**Features**: appreciation 28.21, ur 4.69, pcpi 47311, pop -0.19

MA maps almost exactly to **NJ** (ur 4.69, pcpi 47366, pop 0.70, crash -13.06): identical unemployment, nearly identical income, moderate pop growth. **WI** (ur 4.69, crash -12.93) reinforces the ur cluster. MA's slightly negative pop growth is a mild concern (RI at pop -0.77 crashed -24.38), but MA's far higher income provides a buffer that RI lacked. Among New England comps, NH (-6.70) is more optimistic and ME (-21.83) more pessimistic; MA's higher income puts it closer to NH but its lower pop growth and moderate appreciation split the difference toward NJ territory.

**Predicted: -13.50**

---

### Vermont (VT)
**Features**: appreciation 41.92, ur 3.68, pcpi 36609, pop 0.81

VT sits between its New England neighbors NH (-6.70, ur 3.52, pcpi 42866) and ME (-21.83, ur 4.71, pcpi 34168). VT's low ur (3.68) resembles NH, but its lower income (36609) and lower pop growth (0.81) push it worse. The appreciation (41.92) is comparable to **OR** (44.87, crash -11.81) and **WA** (42.91, crash -19.98). **PA** (appreciation 34.06, ur 4.73, pcpi 37803, pop 1.10, crash -11.93) is the closest multi-feature comp. Averaging across OR, PA, and WA gives about -14.6.

**Predicted: -14.50**

---

### Virginia (VA)
**Features**: appreciation 53.63, ur 3.08, pcpi 42164, pop 4.16

VA's natural comparisons are its DC-corridor neighbors: **MD** (appreciation 65.16, ur 3.85, pcpi 45293, crash -4.45) and **DC** (appreciation 70.23, ur 5.83, pcpi 55384, crash -3.57). VA has lower appreciation and income than both but compensates with the lowest ur in the held-out set (3.08) and strong pop growth (4.16). **NH** (ur 3.52, pcpi 42866, crash -6.70) also matches well on income and ur. The one concerning comp is **WY** (ur 3.07, pcpi 43805, crash -27.60), but WY is a tiny, undiversified resource economy. VA's large, diversified, government-anchored economy is far more comparable to MD. Weighted average of MD and NH: about -5.6.

**Predicted: -6.00**

---

### New Mexico (NM)
**Features**: appreciation 32.57, ur 4.23, pcpi 30433, pop 4.50

NM's low income (30433) places it in the vulnerable-income tier: **AL** (pcpi 31264, crash -25.98), **KY** (pcpi 30476, crash -29.40), **AR** (pcpi 29376, crash -25.19), **SC** (pcpi 30789, crash -55.69). However, NM's unemployment (4.23) is materially lower than KY (5.73), AR (5.23), and SC (6.35), which provides a buffer. NM's pop growth (4.50) is moderate. **OK** (ur 3.91, pcpi 34650, crash -10.97) is a regional comp with similar ur but higher income. Averaging AL and OK as bracket endpoints gives -18.5; NM's intermediate profile lands it in the middle.

**Predicted: -18.00**

---

### Illinois (IL)
**Features**: appreciation 25.87, ur 4.62, pcpi 40021, pop 0.70

IL maps to an extremely tight cluster: **MN** (appreciation 24.94, ur 4.06, pcpi 39362, crash -13.02), **WI** (appreciation 22.65, ur 4.69, pcpi 36047, crash -12.93), and **NJ** (ur 4.69, pcpi 47366, pop 0.70, crash -13.06). All three have nearly identical crash outcomes around -13. IL's features sit squarely among them. This is the highest-confidence prediction.

**Predicted: -13.00**

---

### West Virginia (WV)
**Features**: appreciation 25.64, ur 4.77, pcpi 28528, pop 0.86

WV has the lowest income of any held-out state, matching the poorest tier in training: **MS** (pcpi 27827, crash -18.76), **AR** (pcpi 29376, crash -25.19), **KY** (pcpi 30476, crash -29.40), **AL** (pcpi 31264, crash -25.98). Average of this cluster: about -24.8. WV's ur (4.77) is lower than KY (5.73), MS (6.38), and AR (5.23), which partially buffers it. But WV's very low pop growth (0.86) offers no demand-side support. The low income and Appalachian economic fragility are the dominant signals.

**Predicted: -22.00**

---

### North Dakota (ND)
**Features**: appreciation 22.30, ur 3.12, pcpi 33120, pop 1.66

ND's closest comp is **SD** (appreciation 17.95, ur 3.01, pcpi 34983, pop 2.53, crash -7.70): same region, similar ur, similar income and pop growth. **NE** (ur 3.04, pcpi 35718, crash 0.00) is the other Plains neighbor. **IA** (ur 3.69, pcpi 34197, pop 1.38, crash -8.67) also fits. Average of SD, NE, IA: -5.46. ND's higher appreciation (22.30 vs 11-18 range for these comps) could push it slightly worse. Energy economy provides diversification but also commodity-price sensitivity.

**Predicted: -6.00**

---

### New York (NY)
**Features**: appreciation 40.29, ur 4.50, pcpi 43760, pop -0.37

NY's closest income/ur comp is **NJ** (ur 4.69, pcpi 47366, crash -13.06). **PA** (ur 4.73, pcpi 37803, crash -11.93) brackets the lower-income side. **WA** (appreciation 42.91, ur 4.99, crash -19.98) matches on appreciation. NY's negative pop growth (-0.37) is a concern; among negative-growth states, **RI** (-0.77) crashed -24.38, though RI had lower income. The average of NJ, PA, and WA is -15.0. NY's high income and high appreciation provide some buffer, but the population decline signals weakening demand.

**Predicted: -15.00**

---

### Delaware (DE)
**Features**: appreciation 45.63, ur 3.58, pcpi 40736, pop 5.04

DE's geographic neighbor **MD** (ur 3.85, pcpi 45293, pop 2.39, crash -4.45) is the anchor comp. **NH** (ur 3.52, pcpi 42866, crash -6.70) matches on ur and income. DE's high pop growth (5.04) is a strong protective signal, similar to NC (5.87, crash 0.00) and SC (5.00, crash -55.69). However, DE's appreciation (45.63) is lower than MD's (65.16) and its income is lower, pulling it slightly worse. **OR** (appreciation 44.87, pcpi 34488, crash -11.81) matches on appreciation but has worse ur and income. Averaging MD, NH, and OR: -7.65. DE's strong pop growth and low ur weight it toward the MD end.

**Predicted: -9.50**

---

### Montana (MT)
**Features**: appreciation 36.61, ur 3.37, pcpi 31870, pop 3.60

MT's natural Mountain West comp is **WY** (appreciation 34.89, ur 3.07, pcpi 43805, pop 3.82, crash -27.60), but WY has far higher income. **OR** (appreciation 44.87, pcpi 34488, crash -11.81) matches on appreciation and income. **ME** (appreciation 34.89, pcpi 34168, crash -21.83) matches on appreciation and income. Average of WY, OR, ME: -20.4. MT's low ur (3.37) is a positive signal (similar to WY), but its low income (31870) places it in the vulnerable tier. The tug between protective low unemployment and vulnerable low income lands it between OR and ME.

**Predicted: -18.50**

---

## Final Predictions

```json
[
  {"state": "ID", "predicted_crash_pct": -10.50},
  {"state": "MA", "predicted_crash_pct": -13.50},
  {"state": "VT", "predicted_crash_pct": -14.50},
  {"state": "VA", "predicted_crash_pct": -6.00},
  {"state": "NM", "predicted_crash_pct": -18.00},
  {"state": "IL", "predicted_crash_pct": -13.00},
  {"state": "WV", "predicted_crash_pct": -22.00},
  {"state": "ND", "predicted_crash_pct": -6.00},
  {"state": "NY", "predicted_crash_pct": -15.00},
  {"state": "DE", "predicted_crash_pct": -9.50},
  {"state": "MT", "predicted_crash_pct": -18.50}
]
```
