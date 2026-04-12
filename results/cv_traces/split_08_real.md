## Analysis & Predictions

### Key Patterns from Training Data

The training data reveals several structural drivers of crash severity:

1. **Appreciation is the primary predictor**, but the relationship is noisy. States above ~40% appreciation almost always crashed worse than -14%, while states below ~15% rarely exceeded -10% (Michigan excepted).
2. **Population growth amplifies bubbles.** High appreciation + high pop growth = speculative overbuilding (NV, AZ). Low pop growth moderates the crash even at high appreciation (VT at 41.9% appreciation crashed only -6.6%).
3. **Unemployment captures structural economic vulnerability.** Michigan (6.87% UR, only 8.9% appreciation) crashed -29.4% due to the auto industry collapse, not bubble unwinding. High pre-crisis UR signals fragile labor markets that amplify foreclosure cascades.
4. **Unique economic structures create outliers.** DC (-11.9% despite 70.2% appreciation) and HI (-18.5% despite 80.7% appreciation) were buffered by government employment and island supply constraints, respectively.

---

### State-by-State Reasoning

**FL (Florida)** — The clearest prediction. Florida is a Sand State with near-identical appreciation to AZ (73.4%) and CA (74.0%). Its pop growth (6.84%) sits between CA (2.18%) and AZ (9.41%). Linear interpolation by pop growth between CA (-41.0%) and AZ (-46.0%) yields roughly -44%. Florida had massive condo speculation in Miami, overbuilding in Cape Coral/Tampa, and deep subprime penetration. The very low pre-crisis UR (3.28%) reflects a construction-dependent economy that collapsed violently.
**Prediction: -44.0%**

**OR (Oregon)** — Most comparable to WA (42.9% appreciation, -25.2% crash). Oregon has slightly higher appreciation (44.9%) and higher UR (5.39% vs 4.99%), both pushing toward a worse outcome, but lower pop growth (3.48% vs 4.37%) suggesting less overbuilding. Lower income ($34.5k vs $39.7k) increases foreclosure vulnerability. Portland's bubble tracked Seattle's closely. These factors roughly offset, placing Oregon slightly milder than Washington.
**Prediction: -23.0%**

**SC (South Carolina)** — Sits between NC (16.9% appreciation, -13.1%) and GA (15.2% appreciation, -24.4%) geographically and economically. SC has the worst UR in this group (6.35%), the lowest income ($30.8k), and high pop growth (5.0%). However, SC lacks an Atlanta-scale metro with comparable overbuilding. Myrtle Beach had severe condo speculation, but Greenville and Columbia moderated the statewide figure. Worse fundamentals than NC push it a few points deeper.
**Prediction: -15.0%**

**MT (Montana)** — Appreciation (36.6%) is nearly identical to CT (36.6% → -18.8%) and close to NM (32.6% → -15.7%). Montana's very low UR (3.37%) and moderate pop growth (3.60%) resemble NM's profile but with better labor markets. The housing market is small and driven by lifestyle migration rather than leveraged speculation. Idaho (39.5% appreciation, 7.72% pop growth → -27.0%) is a nearby Western comparison, but Idaho's much higher pop growth drove far more overbuilding. Montana lands near NM.
**Prediction: -15.0%**

**OH (Ohio)** — Rust Belt state with very low appreciation (9.43%), similar to MI (8.86% → -29.4%). But Michigan's crash was driven by a unique auto industry collapse. Ohio's UR (5.43%) is elevated but well below MI (6.87%), and Ohio's economy was more diversified (finance, healthcare, manufacturing). The low appreciation means minimal bubble component; the crash was driven by subprime concentration (Cleveland was among the worst nationally) and manufacturing job losses. Falls well below MI but above stable low-appreciation states like TX (-4.2%) and KS (-5.0%).
**Prediction: -13.0%**

**AK (Alaska)** — Isolated, oil-dependent market with 36.1% appreciation. The 6.62% UR is structural for Alaska (seasonal industries, remoteness), not indicative of economic distress as it would be in the lower 48. Comparable appreciation to PA (34.1% → -9.4%) and ME (34.9% → -13.1%). Alaska shares characteristics with "buffered" markets like DC and HI: limited supply, government/resource employment base, low speculative interest due to isolation. Moderate pop growth (4.15%). The oil economy provided partial insulation but didn't fully shield the state.
**Prediction: -11.0%**

**IN (Indiana)** — Similar to Ohio (fellow Rust Belt manufacturing state) but with slightly better fundamentals: lower UR (5.02% vs 5.43%), higher pop growth (2.20% vs 0.41%), and very low appreciation (8.68%). Indianapolis was more diversified than Cleveland and lacked comparable subprime concentration. Less severe than Ohio.
**Prediction: -11.0%**

**WY (Wyoming)** — Small, resource-dependent state (oil, coal, gas). The 34.9% appreciation was energy-boom-driven rather than speculative. Very low UR (3.07%) and high income ($43.8k) indicate a strong economic base. Most comparable to PA (34.1% appreciation, -9.4%) and VT (41.9% appreciation, -6.6%): states where moderate-high appreciation met small or illiquid markets with low pop growth, limiting crash severity.
**Prediction: -9.5%**

**WV (West Virginia)** — Appalachian economy with moderate appreciation (25.6%), lowest income in the held-out set ($28.5k), and minimal pop growth (0.86%). The 25.6% appreciation is similar to IL (25.9% → -21.8%), but Illinois had Chicago's bubble. WV's small, illiquid market with near-zero pop growth means very little overbuilding. More comparable to KY (14.3% → -4.5%) and AR (20.0% → -6.7%) as low-income states with modest appreciation. WV's higher appreciation pushes it somewhat worse, but the lack of speculative building limits the downside.
**Prediction: -7.5%**

**OK (Oklahoma)** — Energy state with conservative lending practices, nearly identical profile to TX (11.7% appreciation, -4.2%) and KS (12.5% appreciation, -5.0%). Oklahoma's 14.3% appreciation is slightly higher, and its UR (3.91%) is low. Stable energy and agricultural economy with no meaningful speculative building. Almost no bubble to unwind.
**Prediction: -5.0%**

**SD (South Dakota)** — Great Plains agricultural state, directly comparable to its neighbors ND (22.3% appreciation, 0.0% crash), IA (13.3% appreciation, 0.0% crash), and NE (11.9% appreciation, -2.9%). SD's appreciation (18.0%) falls between IA/NE and ND, with the lowest UR in the held-out set (3.01%). Stable agricultural economy, conservative lending, no speculation. Minimal crash expected.
**Prediction: -2.5%**

---

### Final Predictions

```json
[
  {"state": "OR", "predicted_crash_pct": -23.00},
  {"state": "OK", "predicted_crash_pct": -5.00},
  {"state": "SC", "predicted_crash_pct": -15.00},
  {"state": "AK", "predicted_crash_pct": -11.00},
  {"state": "MT", "predicted_crash_pct": -15.00},
  {"state": "WV", "predicted_crash_pct": -7.50},
  {"state": "OH", "predicted_crash_pct": -13.00},
  {"state": "FL", "predicted_crash_pct": -44.00},
  {"state": "WY", "predicted_crash_pct": -9.50},
  {"state": "IN", "predicted_crash_pct": -11.00},
  {"state": "SD", "predicted_crash_pct": -2.50}
]
```
