## Analysis Framework

Looking at the training data, I notice several patterns that diverge from conventional narratives about the crisis:

1. **Appreciation is not a reliable predictor of crash severity.** High-appreciation states (CA -6.70, NV -8.67, DC -4.21) often had mild crashes, while low-appreciation states (SD -55.69, AL -46.01, IN -25.19) sometimes crashed severely. This suggests unmeasured structural or compositional factors dominate.
2. **The 20-25% appreciation band in the Midwest/Plains is toxic.** MN (-44.73), WI (-24.38), LA (-41.04), AR (-26.95) all fall here with severe outcomes.
3. **High income provides a partial buffer.** CT (53k, 0.00), DC (55k, -4.21), NJ (47k, -7.70), MA (47k, -7.30) all avoided severe crashes. But it is not absolute (MD at 45k crashed -17.56).
4. **High population growth has mixed effects.** NV (12.18%, -8.67) and TX (6.03%, -4.45) did well; ID (7.72%, -25.98) and FL (6.84%, -21.83) did not.
5. **The training mean is approximately -15.8** with enormous variance (range: -55.69 to 0.00).

Given the high variance, predictions are anchored toward the mean with adjustments based on nearest-neighbor composites and economic logic.

---

## State-by-State Predictions

### TN (appreciation 17.18, ur 5.22, pcpi 32878, pop 4.12)

Southern state with low-moderate appreciation and a moderately elevated unemployment rate. Closest comps: AR (20.02, 5.23, 29376 → -26.95), SC (19.42, 6.35, 30789 → -19.98), GA (15.17, 4.66, 34574 → -4.15), KS (12.49, 4.42, 35411 → -17.39). TN sits between the mild-crash Southern growth states (GA, TX, OK) and the severe-crash moderate-appreciation states (AR, AL). UR of 5.22 is a negative signal matching AR closely. Pop growth of 4.12 provides moderate demand support. **Prediction: -16.00**

### PA (appreciation 34.06, ur 4.73, pcpi 37803, pop 1.10)

Northeast state with moderate-high appreciation and decent income. Strongest comp is ME (34.89, 4.71, 34168, 1.31 → -9.90), which matches on appreciation, UR, and pop growth almost exactly. Also similar to VT (41.92 → -7.26) and NH (31.83 → -13.02). Income at 37.8k is above ME, providing a slight buffer. Northeast states in the 30-45% appreciation range average about -10. **Prediction: -10.00**

### NM (appreciation 32.57, ur 4.23, pcpi 30433, pop 4.50)

Mountain West state with moderate appreciation and low income. Key comps: MT (36.61, 3.37, 31870, 3.60 → -2.88), ID (39.45, 3.39, 31244, 7.72 → -25.98), WY (34.89, 3.07, 43805, 3.82 → -12.93), CO (11.88, 4.25, 39869, 4.23 → -13.11). MT is mild and ID is severe; NM falls between with lower pop growth than ID and lower income than WY/CO. Average of Mountain West comps: -13.73. **Prediction: -14.00**

### ND (appreciation 22.30, ur 3.12, pcpi 33120, pop 1.66)

Great Plains state geographically adjacent to SD (-55.69), which is the worst crash in the dataset. ND's features are similar to SD (17.95, 3.01, 34983, 2.53). Other Plains/Midwest comps: NE (11.88, 3.04, 35718 → -25.30), KS (12.49, 4.42, 35411 → -17.39), IA (13.29, 3.69, 34197 → -4.97). The 20-25% appreciation band in this dataset is associated with severe crashes (MN -44.73, WI -24.38, AR -26.95). ND's low UR (3.12) doesn't provide safety (SD had 3.01). Hedging between SD's extreme and the NE/KS norm. **Prediction: -20.00**

### UT (appreciation 23.39, ur 2.87, pcpi 31107, pop 7.01)

Mountain West state with the lowest UR in the full dataset and strong population growth. Best comp is ID (39.45, 3.39, 31244, 7.72 → -25.98), nearly identical on income and pop growth. High-pop-growth states average about -12.8 (NV -8.67, AZ -11.81, ID -25.98, FL -21.83, TX -4.45, GA -4.15). UT's very low UR and strong demographic tailwinds argue for the milder end. MT (31870, 3.37 → -2.88) is another low-UR Mountain West comp. **Prediction: -13.00**

### RI (appreciation 48.54, ur 5.26, pcpi 38719, pop -0.77)

High-appreciation Northeast state with negative population growth and above-average unemployment. Nearest appreciation comp is NJ (48.76 → -7.70), but RI has lower income (38.7k vs 47.4k) and higher UR. UR and income match OR (44.87, 5.39, 34488 → -22.13). Northeast neighbors MA (-7.30) and CT (0.00) were mild. Negative pop growth is rare in training: LA (-4.83 → -41.04) and MA (-0.19 → -7.30). Averaging NJ, OR, and MA as primary comps yields -12.4. **Prediction: -13.00**

### NC (appreciation 16.94, ur 4.73, pcpi 34189, pop 5.87)

Southern growth state with features nearly identical to GA (15.17, 4.66, 34574, 6.18 → -4.15). Appreciation, UR, income, and pop growth all closely match. Also comparable to SC (19.42, 6.35, 30789 → -19.98), but NC has lower UR and higher income, so it weights much closer to GA. A 70/30 blend of GA and SC outcomes gives -8.90. **Prediction: -9.00**

### MI (appreciation 8.86, ur 6.87, pcpi 33563, pop -0.05)

Rust Belt state with the highest UR in the entire dataset (training + held-out) and near-zero population growth, signaling deep structural weakness in the auto-dependent economy. Strongest comps: IN (8.68, 5.02, 32905, 2.20 → -25.19) and OH (9.43, 5.43, 33976, 0.41 → -18.76). MI has significantly worse UR (6.87 vs 5.02/5.43) and worse pop growth (-0.05 vs 2.20/0.41) than both. Low appreciation suggests fundamentals were already weak, not bubble-driven. This warrants a more severe outcome than either comp. **Prediction: -23.00**

### IL (appreciation 25.87, ur 4.62, pcpi 40021, pop 0.70)

Midwest state whose appreciation falls squarely in the dangerous 20-25% band where MN (24.94 → -44.73) and WI (22.65 → -24.38) both crashed severely. IL's income (40k) is modestly higher than WI (36k) and MN (39k), providing a small buffer. Low pop growth (0.70) echoes NJ (0.70 → -7.70) and CT (0.95 → 0.00), but those are high-income Northeast states. The Midwest + moderate appreciation pattern dominates. Average of WI and MN: -34.56; tempered by higher income and non-Midwest comps like NJ. **Prediction: -20.00**

### NY (appreciation 40.29, ur 4.50, pcpi 43760, pop -0.37)

High-income Northeast state with substantial appreciation and negative pop growth. Immediate comps: NJ (48.76, 4.69, 47366 → -7.70), CT (36.58, 4.42, 53224 → 0.00), VT (41.92, 3.68, 36609 → -7.26), MA (28.21, 4.69, 47311 → -7.30). These four average -5.57. NY's income at 43.8k is slightly below NJ/MA but well above the median. Negative pop growth matches MA closely (-0.19 → -7.30). Northeast high-income states in this appreciation range consistently avoided severe crashes. **Prediction: -7.00**

### MO (appreciation 18.82, ur 4.89, pcpi 33860, pop 2.33)

Central state straddling the Midwest and South, with moderate features across the board. Comps: KS (12.49, 4.42, 35411 → -17.39), AR (20.02, 5.23, 29376 → -26.95), SC (19.42, 6.35, 30789 → -19.98), OH (9.43, 5.43, 33976 → -18.76). OK (14.28, 3.91, 34650 → -3.57) and TX (11.68, 4.98, 35422 → -4.45) are also regional neighbors but with lower appreciation. Average of KS, SC, OH: -18.71. MO's moderate UR (4.89) and income (33.9k) don't provide strong buffers. **Prediction: -17.00**

---

## Final Predictions

```json
[
  {"state": "TN", "predicted_crash_pct": -16.00},
  {"state": "PA", "predicted_crash_pct": -10.00},
  {"state": "NM", "predicted_crash_pct": -14.00},
  {"state": "ND", "predicted_crash_pct": -20.00},
  {"state": "UT", "predicted_crash_pct": -13.00},
  {"state": "RI", "predicted_crash_pct": -13.00},
  {"state": "NC", "predicted_crash_pct": -9.00},
  {"state": "MI", "predicted_crash_pct": -23.00},
  {"state": "IL", "predicted_crash_pct": -20.00},
  {"state": "NY", "predicted_crash_pct": -7.00},
  {"state": "MO", "predicted_crash_pct": -17.00}
]
```
