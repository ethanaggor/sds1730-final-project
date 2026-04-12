## Analysis and Predictions

### Pattern identification from training data

Before predicting, I examined the training data for structural patterns. Key observations:

1. **Appreciation is a weak predictor in isolation.** FL (74.37% appreciation, only -4.45% crash) and HI (80.67%, -6.55%) show that bubble-sized appreciation does not guarantee a severe crash. Conversely, MO (-55.69% crash on only 18.82% appreciation) and MI (-25.98% on 8.86%) show severe crashes without large bubbles.

2. **Unemployment rate has a loose positive association with severity.** States with UR above 5-6% cluster toward worse outcomes (MI -25.98 at 6.87%, SC -22.13 at 6.35%, MS -21.81 at 6.38%). States with very low UR sometimes avoided severe crashes even with high appreciation (HI: 2.57% UR, -6.55%; FL: 3.28% UR, -4.45%).

3. **Income does not insulate.** NY (pcpi $43,760, crash -41.04%) and DC ($55,384, -27.60%) show that high income is not protective.

4. **The dataset is noisy.** The median crash is roughly -13%, the mean roughly -16.4%, with enormous variance. State-specific factors not captured by these four features dominate.

Given this noise, I anchor predictions to the 3-4 closest training comparables and adjust with domain knowledge about each state's economic structure.

---

### State-by-state reasoning

**NC** (appr 16.94, ur 4.73, pcpi 34189, pop 5.87)
Closest match is GA (appr 15.17, ur 4.66, pcpi 34574, pop 6.18, crash -20.44). Nearly identical on all four features. Both are Southeast states with rapid suburban expansion and financial sector exposure (Charlotte for NC, Atlanta for GA). TN is also close (appr 17.18, crash -6.70) but with lower pop growth. Weighting toward GA but pulling slightly milder.
**Prediction: -15.0**

**PA** (appr 34.06, ur 4.73, pcpi 37803, pop 1.10)
Northeast state with moderate bubble in Philly suburbs and stable/declining western PA markets. Most relevant comparables are New England: NH (appr 31.83, crash -11.93), VT (appr 41.92, crash -8.67), MA (appr 28.21, crash -9.90). PA's UR (4.73) is higher than all three, but low pop growth (1.10) limits overbuilding. The Northeast cluster sits in the -9 to -12 range.
**Prediction: -12.0**

**WI** (appr 22.65, ur 4.69, pcpi 36047, pop 1.80)
Upper Midwest manufacturing state. Geographic neighbor MN (appr 24.94, ur 4.06, crash -21.83) is the top comparable. ND (appr 22.30, ur 3.12, crash -7.70) has similar appreciation but much lower UR. WI's UR (4.69) is higher than both, placing it between them. Manufacturing vulnerability pulls it toward MN; low pop growth and moderate appreciation pull toward ND.
**Prediction: -14.0**

**ME** (appr 34.89, ur 4.71, pcpi 34168, pop 1.31)
New England state. NH (appr 31.83, crash -11.93) is the closest regional comparable with similar appreciation. RI (appr 48.54, crash -10.97) and MA (appr 28.21, crash -9.90) frame the New England cluster at -10 to -12. ME's higher UR (4.71 vs NH's 3.52) and lower income ($34k vs $43k) suggest slightly worse than NH. WY has identical appreciation (34.89) but very different economy (crash -21.93); I discount it as non-comparable.
**Prediction: -13.0**

**IA** (appr 13.29, ur 3.69, pcpi 34197, pop 1.38)
Agricultural Midwest. NE (appr 11.88, ur 3.04, crash 0.00) is the closest comparable; OK (appr 14.28, ur 3.91, crash -3.57) is also similar. KS (appr 12.49, crash -24.38) appears anomalous for this cluster and I discount it. Iowa's strong agricultural economy, low appreciation (minimal bubble), and low UR all point toward a mild decline. UR is slightly higher than NE, pushing modestly negative.
**Prediction: -5.0**

**VA** (appr 53.63, ur 3.08, pcpi 42164, pop 4.16)
Northern Virginia is a DC suburb market; DC (appr 70.23, ur 5.83, crash -27.60) is the anchor comparable. But VA's appreciation is 17 points lower, its UR is far lower (3.08 vs 5.83), and the state includes large rural/military areas that dampen the statewide figure. DE (appr 45.63, ur 3.58, crash -13.02) is the nearest Mid-Atlantic comp. Splitting between DC and DE, weighting the DC connection but recognizing VA's much stronger labor market.
**Prediction: -16.0**

**MD** (appr 65.16, ur 3.85, pcpi 45293, pop 2.39)
Maryland is the other DC suburb market, and smaller/more DC-dominated than VA. DC crashed -27.60 with slightly higher appreciation (70.23). MD's UR (3.85) is much lower than DC's (5.83), and its appreciation is 5 points lower. CA (appr 73.96, crash -29.40) shows that 65-75% appreciation can produce ~-28 to -30% crashes. The government employment base and high income provide partial insulation, but the bubble size is real.
**Prediction: -21.0**

**WA** (appr 42.91, ur 4.99, pcpi 39744, pop 4.37)
Pacific Northwest, direct neighbor of OR (appr 44.87, ur 5.39, crash 0.00). OR's 0.00 crash is an outlier (Oregon did experience real declines), so I adjust upward. VT (appr 41.92, crash -8.67), ID (appr 39.45, crash -7.26), and AK (appr 36.14, crash -10.06) provide a -7 to -10 bracket. WA's tech economy (Seattle/Microsoft) provided strong fundamentals, but the bubble was real. Moderate negative.
**Prediction: -8.0**

**CO** (appr 11.88, ur 4.25, pcpi 39869, pop 4.23)
Identical appreciation to NE (11.88, crash 0.00). Colorado was still recovering from the 2001 tech bust, so the 2003-2006 bubble was muted. UR (4.25) is higher than NE (3.04) and pop growth (4.23) is higher (1.96). OK (appr 14.28, crash -3.57) is also comparable. CO's high income ($39.9k) and diversified economy (tech, energy, defense) provide resilience. Low appreciation means minimal bubble to unwind.
**Prediction: -6.0**

**CT** (appr 36.58, ur 4.42, pcpi 53224, pop 0.95)
Wealthy Northeast state with financial sector exposure (Stamford hedge funds, Hartford insurance). Income ($53.2k) is second only to DC in the training set. Northeast comparables: MA (crash -9.90), NJ (-4.21), NH (-11.93), RI (-10.97). CT's moderate appreciation and low pop growth (0.95) limit overbuilding. Financial sector job losses hurt, but high income and proximity to NYC provide a floor. Cluster average sits around -9 to -11.
**Prediction: -10.0**

**TX** (appr 11.68, ur 4.98, pcpi 35422, pop 6.03)
Texas is the canonical case of crisis resistance: strict lending laws (no cash-out refinancing until 1997 amendment, still heavily regulated), abundant land supply, and a diversified energy/tech economy. Appreciation (11.68) is nearly identical to NE (11.88, crash 0.00) and CO (11.88). High pop growth (6.03) matches GA (6.18, crash -20.44), but GA's growth was speculative; Texas's was employment-driven. IN (appr 8.68, ur 5.02, crash -7.30) and OH (appr 9.43, crash -4.97) are similar low-appreciation, moderate-UR states with mild declines.
**Prediction: -5.0**

---

### Final predictions

```json
[
  {"state": "NC", "predicted_crash_pct": -15.0},
  {"state": "PA", "predicted_crash_pct": -12.0},
  {"state": "WI", "predicted_crash_pct": -14.0},
  {"state": "ME", "predicted_crash_pct": -13.0},
  {"state": "IA", "predicted_crash_pct": -5.0},
  {"state": "VA", "predicted_crash_pct": -16.0},
  {"state": "MD", "predicted_crash_pct": -21.0},
  {"state": "WA", "predicted_crash_pct": -8.0},
  {"state": "CO", "predicted_crash_pct": -6.0},
  {"state": "CT", "predicted_crash_pct": -10.0},
  {"state": "TX", "predicted_crash_pct": -5.0}
]
```
