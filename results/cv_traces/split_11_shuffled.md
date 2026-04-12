## Analysis and Predictions

### Identifying Key Patterns in Training Data

Before predicting, I'll extract the main regularities from the 40 training states.

**Appreciation alone is a weak predictor.** Nevada (79.74% appreciation) crashed only -11.81%, while Mississippi (16.40% appreciation) crashed -26.95%. The relationship is noisy.

**The appreciation-to-crash "ratio" is more stable.** For states with >40% appreciation (excluding the NJ outlier at -55.69%), the crash/appreciation ratio ranges from -0.13 to -0.44, with a central tendency around -0.20. This gives a useful baseline for bubble states.

**Economic weakness amplifies crashes independently of bubbles.** States like MS (-26.95%), MO (-25.98%), KS (-20.44%), and OK (-21.83%) had low appreciation but severe crashes, driven by high unemployment, low income, or weak fundamental demand.

**Population growth moderates severity.** Comparing NV (12.18% pop growth, -11.81% crash) vs DC (0.38% pop growth, -27.60% crash) at similar appreciation levels: high in-migration provides a real demand floor. States with negative or near-zero pop growth and high appreciation (DC, MA, NJ) tend toward more severe outcomes.

**Three states at 0% crash** (AL, ME, SD): all had moderate appreciation, reasonable fundamentals, and no outsized speculative exposure.

---

### State-by-State Predictions

#### FL (Florida) — Predicted: **-20%**

**Profile:** 74.37% appreciation, 3.28% UR, $38K PCPI, 6.84% pop growth.

Florida was the epicenter of the US housing bubble. Massive speculative building (condo flipping in Miami, exurban sprawl in Tampa/Orlando), heavy subprime lending concentration, and investor-driven purchases. The 74.37% appreciation is among the very highest.

**Comparables:**
- NV (79.74% appr, 12.18% pop → -11.81%): similar sand state, but NV's much higher pop growth (12.18 vs 6.84) provides more fundamental demand cushion
- DC (70.23% appr, 0.38% pop → -27.60%): similar appreciation, but much lower pop growth and higher UR
- HI (80.67% appr, 4.68% pop → -13.11%): high appreciation but less speculative excess

FL's pop growth (6.84%) is between NV's (12.18%) and DC's (0.38%), and FL's speculative exposure was extreme. The crash/appreciation ratio for a state at this appreciation level with moderate pop growth points to about -0.27, yielding ~-20%. This places FL worse than NV/HI (less fundamental demand to cushion) but better than DC (more growth, lower UR).

---

#### AZ (Arizona) — Predicted: **-15%**

**Profile:** 73.44% appreciation, 4.27% UR, $34.5K PCPI, 9.41% pop growth.

Arizona (Phoenix metro) was another classic sand state with massive speculative exurban building and subprime concentration. However, AZ's very high population growth (9.41%) is second only to NV in the dataset, reflecting genuine migration-driven demand that partially supports prices.

**Comparables:**
- NV (79.74% appr, 12.18% pop → -11.81%): closest match; similar sand state dynamics, similarly high pop growth
- ID (39.45% appr, 7.72% pop → -17.39%): high growth Sun Belt state

AZ has lower income ($34.5K vs NV's $39.4K) and lower pop growth (9.41% vs 12.18%), suggesting slightly less demand support. The lower PCPI means borrowers are more stretched. Estimated ratio of ~-0.20 on 73.44% appreciation ≈ -15%.

---

#### MD (Maryland) — Predicted: **-15%**

**Profile:** 65.16% appreciation, 3.85% UR, $45.3K PCPI, 2.39% pop growth.

Maryland's bubble centered on the DC suburbs (Montgomery/Prince George's counties) and parts of Baltimore. Government/defense employment provides economic stability, but the exurban areas saw significant speculative activity.

**Comparables:**
- VA (53.63% appr, 4.16% pop → -10.14%): adjacent state, similar DC-suburb dynamics
- DC (70.23% appr, 0.38% pop → -27.60%): shares the DC metro, but far more extreme on every dimension

MD sits between VA and DC on appreciation (65% vs 54% and 70%), pop growth (2.39% vs 4.16% and 0.38%), and UR (3.85% vs 3.08% and 5.83%). Weighted average of VA and DC, skewed toward the midpoint: the crash/appreciation ratio of ~-0.23 on 65.16% yields -15%.

---

#### AK (Alaska) — Predicted: **-9%**

**Profile:** 36.14% appreciation, 6.62% UR, $41K PCPI, 4.15% pop growth.

Alaska's economy is oil-dependent and isolated from the lower-48 housing dynamics. The 6.62% UR is the second-highest in the dataset, but high Alaskan unemployment is structural (seasonal industries, remote geography) rather than signaling weakness in the same way. High PCPI ($41K) reflects oil sector wages.

**Comparables:**
- MT (36.61% appr, 3.37% UR, $31.9K PCPI → -10.97%): nearly identical appreciation
- PA (34.06% appr, 4.73% UR → -2.88%): similar appreciation, mild crash
- VT (41.92% appr, 3.68% UR → -18.48%): higher appreciation, severe crash

AK's high UR is a risk factor (states with UR >5.5% have crashes averaging ~-18%), but the oil economy and geographic isolation insulate AK from the worst housing dynamics. Splitting MT's -10.97% with a small buffer for AK's unique economy: -9%.

---

#### WY (Wyoming) — Predicted: **-5%**

**Profile:** 34.89% appreciation, 3.07% UR, $43.8K PCPI, 3.82% pop growth.

Wyoming is a small, energy-dependent economy (oil, gas, coal). Very low unemployment and very high income signal economic strength during 2006-2012. The housing market is small and not subject to speculative dynamics.

**Comparables:**
- ME (34.89% appr, 4.71% UR, $34.2K PCPI → 0.00%): identical appreciation, mild crash
- PA (34.06% appr, 4.73% UR, $37.8K PCPI → -2.88%): similar appreciation, mild crash
- CT (36.58% appr, 4.42% UR, $53.2K PCPI → -4.97%): similar appreciation, mild crash

WY has better fundamentals than all three comparables: lower UR, higher PCPI (vs ME/PA), and reasonable pop growth. Energy prices remained elevated through much of the 2006-2012 window (the oil crash came in 2014). Estimate -5%, slightly worse than ME/PA due to Wyoming's small market volatility.

---

#### WA (Washington) — Predicted: **-8%**

**Profile:** 42.91% appreciation, 4.99% UR, $39.7K PCPI, 4.37% pop growth.

Washington's housing market was led by the Seattle metro, supported by Microsoft, Amazon, and Boeing. The tech economy provided significant resilience during the crash, though prices did decline.

**Comparables:**
- OR (44.87% appr, 5.39% UR, $34.5K PCPI, 3.48% pop → -8.92%): Pacific NW neighbor, closest match
- NY (40.29% appr, 4.50% UR, $43.8K PCPI → -10.06%): similar PCPI and appreciation

WA is strictly better than OR on every feature dimension: lower appreciation, lower UR, higher income, higher pop growth. The tech economy provides additional resilience that isn't captured in these features. WA should crash slightly less than OR's -8.92%. Estimate -8%.

---

#### CA (California) — Predicted: **-22%**

**Profile:** 73.96% appreciation, 4.89% UR, $41.5K PCPI, 2.18% pop growth.

California's bubble was extreme in the Inland Empire, Central Valley, and parts of Southern California, with massive subprime lending and speculative activity. However, coastal metros (San Francisco, parts of LA) were more resilient, and the state's economy is highly diversified.

**Comparables:**
- FL (74.37% appr, 6.84% pop): similar appreciation, but FL has 3x CA's pop growth
- DC (70.23% appr, 0.38% pop → -27.60%): similar ratio of high appreciation to low pop growth
- NV (79.74% appr, 12.18% pop → -11.81%): higher appreciation but 5.6x CA's pop growth

The critical factor for CA is the low population growth (2.18%) relative to its extreme appreciation. This ratio resembles DC's pattern more than NV's. States with >60% appreciation and <2.5% pop growth (DC) crashed severely. CA's diversified economy provides some buffer that DC (government-dependent) lacks. Crash/appreciation ratio of ~-0.30 on 73.96% ≈ -22%.

---

#### IN (Indiana) — Predicted: **-8%**

**Profile:** 8.68% appreciation, 5.02% UR, $32.9K PCPI, 2.20% pop growth.

Indiana barely participated in the housing bubble. At 8.68%, appreciation was roughly at inflation. The crash impact comes through economic channels (manufacturing decline) rather than bubble deflation.

**Comparables:**
- KY (14.25% appr, 5.73% UR, $30.5K PCPI → -4.21%): similar low-appreciation Midwest profile
- TX (11.68% appr, 4.98% UR, $35.4K PCPI → -4.45%): similar low appreciation and UR
- IA (13.29% appr, 3.69% UR, $34.2K PCPI → -9.38%): Midwest, moderate crash

IN has the lowest appreciation in the held-out set. Its moderate UR and moderate-low income create some vulnerability, but there's no bubble height to fall from. Slightly worse than KY/TX (more manufacturing exposure) but less severe than Rust Belt worst cases. Estimate -8%.

---

#### MI (Michigan) — Predicted: **-20%**

**Profile:** 8.86% appreciation, 6.87% UR, $33.6K PCPI, -0.05% pop growth.

Michigan presents the worst pre-crash economic fundamentals in the entire dataset: the highest unemployment rate (6.87%), negative population growth (people leaving for jobs), and an economy teetering on auto industry collapse. The housing decline here is almost entirely economic, not bubble-driven.

**Comparables:**
- MS (16.40% appr, 6.38% UR, $27.8K PCPI, 1.28% pop → -26.95%): closest in economic weakness
- LA (22.89% appr, 4.14% UR, $33.6K PCPI, -4.83% pop → -24.38%): negative pop growth precedent
- MA (28.21% appr, 4.69% UR, $47.3K PCPI, -0.19% pop → -22.13%): negative pop growth

MI has higher UR than MS (6.87% vs 6.38%) and negative pop growth (unlike MS). But MI's very low appreciation (8.86% vs MS's 16.40%) limits the distance prices can fall from the peak. The auto industry collapse is a massive unmeasured factor pushing toward severity, but the low starting bubble constrains the percentage decline. Balancing the worst fundamentals against the minimal bubble: -20%.

---

#### NH (New Hampshire) — Predicted: **-10%**

**Profile:** 31.83% appreciation, 3.52% UR, $42.9K PCPI, 2.23% pop growth.

New Hampshire had moderate appreciation as part of the New England bubble, but strong fundamentals: the lowest UR among New England states, high income, no income tax, and proximity to Boston's job market.

**Comparables:**
- CT (36.58% appr, 4.42% UR, $53.2K PCPI → -4.97%): higher appreciation, mild crash
- VT (41.92% appr, 3.68% UR, $36.6K PCPI → -18.48%): higher appreciation, severe crash
- MA (28.21% appr, 4.69% UR, $47.3K PCPI → -22.13%): lower appreciation, severe crash
- ME (34.89% appr, 4.71% UR, $34.2K PCPI → 0.00%): similar appreciation, no crash

New England outcomes are highly variable (-22% to 0%). NH's low UR and positive pop growth favor resilience (more like CT/ME), but the region's interconnected housing market creates contagion risk (closer to VT/MA). NH's moderate appreciation ratio (~-0.31) yields about -10%, splitting the New England range.

---

#### OH (Ohio) — Predicted: **-12%**

**Profile:** 9.43% appreciation, 5.43% UR, $34K PCPI, 0.41% pop growth.

Ohio is a Rust Belt state with minimal bubble exposure but significant economic vulnerability. Cleveland and parts of the state experienced persistent declines, while Columbus was more resilient. The very low pop growth (0.41%) signals stagnation.

**Comparables:**
- IL (25.87% appr, 4.62% UR, $40K PCPI, 0.70% pop → -6.70%): similar low pop growth, Midwest
- IA (13.29% appr, 3.69% UR, $34.2K PCPI, 1.38% pop → -9.38%): similar income level
- WV (25.64% appr, 4.77% UR, $28.5K PCPI, 0.86% pop → -17.56%): economic weakness parallel

OH sits between IN (which I estimate at -8%) and MI (-20%) on economic fundamentals. Higher UR than IN (5.43% vs 5.02%) and much lower pop growth (0.41% vs 2.20%) push OH worse. But OH is far less economically devastated than MI. Estimate -12%.

---

### Summary

| State | Key Driver | Comparable Anchors | Prediction |
|---|---|---|---|
| FL | Extreme bubble, sand state epicenter | NV (-12), DC (-28) | -20% |
| AZ | Sand state, high pop growth cushion | NV (-12), ID (-17) | -15% |
| MD | DC-suburb bubble, gov't stability | VA (-10), DC (-28) | -15% |
| AK | Oil economy, isolated market | MT (-11), PA (-3) | -9% |
| WY | Energy economy, strong fundamentals | ME (0), PA (-3) | -5% |
| WA | Tech economy, PNW resilience | OR (-9), NY (-10) | -8% |
| CA | Extreme bubble, low pop growth | DC (-28), NV (-12) | -22% |
| IN | No bubble, moderate econ weakness | KY (-4), TX (-4), IA (-9) | -8% |
| MI | Economic devastation, auto collapse | MS (-27), LA (-24) | -20% |
| NH | Moderate bubble, strong fundamentals | CT (-5), VT (-18), ME (0) | -10% |
| OH | No bubble, Rust Belt stagnation | IL (-7), IA (-9), WV (-18) | -12% |

```json
[
  {"state": "FL", "predicted_crash_pct": -20.00},
  {"state": "AZ", "predicted_crash_pct": -15.00},
  {"state": "MD", "predicted_crash_pct": -15.00},
  {"state": "AK", "predicted_crash_pct": -9.00},
  {"state": "WY", "predicted_crash_pct": -5.00},
  {"state": "WA", "predicted_crash_pct": -8.00},
  {"state": "CA", "predicted_crash_pct": -22.00},
  {"state": "IN", "predicted_crash_pct": -8.00},
  {"state": "MI", "predicted_crash_pct": -20.00},
  {"state": "NH", "predicted_crash_pct": -10.00},
  {"state": "OH", "predicted_crash_pct": -12.00}
]
```
