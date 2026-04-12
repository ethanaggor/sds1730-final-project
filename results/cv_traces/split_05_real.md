## Approach

I'll identify the key patterns in the training data, then apply them to each held-out state. The primary drivers of crash severity in 2008 were:

1. **Bubble magnitude** (appreciation_03_06) -- the single strongest predictor
2. **Speculative overbuilding** (pop_growth as proxy for construction exceeding fundamental demand)
3. **Economic vulnerability** (ur_2006, pcpi_2006 -- weak economies amplify crashes)
4. **Structural constraints** (supply-limited geographies or recession-proof employment dampen crashes)

The interaction between appreciation and pop_growth is critical: high appreciation + high pop growth = worst outcomes (NV, AZ, FL), while high appreciation + supply constraints = dampened outcomes (HI, DC).

---

## State-by-State Predictions

### Tennessee (TN)
**Features**: 17.18 appreciation, 5.22 UR, $32,878 income, 4.12 pop growth

**Comparables**: AL (18.37 appreciation, 4.01 UR, $31,264, 2.79 pop → -9.90), AR (20.02, 5.23, $29,376, 3.56 → -6.70), SC (19.42, 6.35, $30,789, 5.00 → -13.02)

TN sits squarely in the low-appreciation Southern band. Nashville had solid fundamentals and no extreme speculation. Memphis had more subprime exposure. The profile is nearly identical to Alabama: similar appreciation, similar income, slightly higher UR and pop growth. A blend of AL and SC dynamics.

**Prediction: -10.0**

---

### Pennsylvania (PA)
**Features**: 34.06 appreciation, 4.73 UR, $37,803 income, 1.10 pop growth

**Comparables**: ME (34.89, 4.71, $34,168, 1.31 → -13.11), CT (36.58, 4.42, $53,224, 0.95 → -18.76), WY (34.89, 3.07, $43,805, 3.82 → -7.70)

PA's profile is strikingly close to Maine: nearly identical appreciation, UR, and pop growth, with slightly higher income. PA is a blend of Philadelphia suburbs (significant decline, subprime exposure) and Pittsburgh (stable, no bubble, diversified post-industrial economy). Low pop growth (1.10) limits overbuilding. CT crashed harder (-18.76) with similar appreciation, but CT is a wealthier, smaller commuter state with different leverage dynamics. ME is the best single-state match.

**Prediction: -13.0**

---

### New Mexico (NM)
**Features**: 32.57 appreciation, 4.23 UR, $30,433 income, 4.50 pop growth

**Comparables**: MT (36.61, 3.37, $31,870, 3.60 → -10.06), CO (11.88, 4.25, $39,869, 4.23 → -10.14), ID (39.45, 3.39, $31,244, 7.72 → -26.95)

NM is a Southwest state adjacent to Arizona, with some spillover of speculative activity into Albuquerque and Las Cruces. MT has similar income and slightly higher appreciation but crashed only -10.06 due to its isolated market. NM's proximity to the Sand State epicenter, its higher pop growth (4.50 vs MT's 3.60), and its low income ($30,433, the lowest in the held-out set) add vulnerability. It should land between MT and the harder-hit Western states. CO has almost identical UR and pop growth but much lower appreciation and higher income, yielding -10.14. NM's higher appreciation and lower income push it beyond CO.

**Prediction: -15.0**

---

### North Dakota (ND)
**Features**: 22.30 appreciation, 3.12 UR, $33,120 income, 1.66 pop growth

**Comparables**: SD (17.95, 3.01, $34,983, 2.53 → 0.00), IA (13.29, 3.69, $34,197, 1.38 → 0.00), AK (36.14, 6.62, $41,013, 4.15 → 0.00)

ND shares SD's agricultural/energy economy, low unemployment, and conservative lending culture. The Bakken shale oil boom was actively supporting the economy through the crisis years, similar to how Alaska's oil economy shielded it. SD and IA saw zero decline with lower appreciation. ND's appreciation (22.30) is higher, suggesting some price to give back. But the oil boom provided a powerful demand cushion. The combination of low UR, low pop growth, resource-sector strength, and no speculative excess limits downside severely.

**Prediction: -2.0**

---

### Utah (UT)
**Features**: 23.39 appreciation, 2.87 UR, $31,107 income, 7.01 pop growth

**Comparables**: ID (39.45, 3.39, $31,244, 7.72 → -26.95), SC (19.42, 6.35, $30,789, 5.00 → -13.02), TX (11.68, 4.98, $35,422, 6.03 → -4.15)

UT presents a tension: the lowest unemployment in either dataset (2.87) versus the second-highest pop growth (7.01). The very high pop growth, particularly in St. George and SLC exurbs, drove significant overbuilding. Idaho's profile is the most informative high-pop-growth comparable, but ID had much higher appreciation (39.45 vs 23.39), so UT's bubble deflation component is smaller. TX avoided major decline despite 6.03 pop growth due to conservative lending and very low appreciation. UT's appreciation is double TX's, and its Mountain West market lacked TX's lending regulations. The very low UR limits foreclosure cascades, pulling the prediction below ID. Between SC and ID, closer to SC but pushed higher by the pop growth overhang.

**Prediction: -17.0**

---

### Rhode Island (RI)
**Features**: 48.54 appreciation, 5.26 UR, $38,719 income, -0.77 pop growth

**Comparables**: NJ (48.76, 4.69, $47,366, 0.70 → -22.13), DE (45.63, 3.58, $40,736, 5.04 → -20.44), MA (28.21, 4.69, $47,311, -0.19 → -17.56)

RI's appreciation (48.54) is almost identical to NJ (48.76 → -22.13). But RI has higher unemployment (5.26 vs 4.69), lower income ($38,719 vs $47,366), and a weaker economy overall. Providence had significant subprime exposure, and the state's manufacturing base was declining. Negative pop growth (-0.77) limits overbuilding but also signals outmigration, weakening demand. The combination of large bubble, high UR, low income, and declining population all point to a crash at least as severe as NJ's. RI's weaker economic fundamentals push it slightly beyond NJ.

**Prediction: -23.0**

---

### North Carolina (NC)
**Features**: 16.94 appreciation, 4.73 UR, $34,189 income, 5.87 pop growth

**Comparables**: GA (15.17, 4.66, $34,574, 6.18 → -24.38), SC (19.42, 6.35, $30,789, 5.00 → -13.02), TX (11.68, 4.98, $35,422, 6.03 → -4.15)

NC is a southeastern growth state with features remarkably close to Georgia: almost identical appreciation, UR, and income, with slightly lower pop growth. GA crashed severely (-24.38) due to Atlanta's extreme subprime exposure and exurban sprawl. Charlotte had similar but less extreme dynamics (banking center with Wachovia, significant subprime lending in surrounding counties). Research Triangle (Raleigh-Durham) was more resilient, with tech/university-driven fundamentals. NC should land between SC (-13.02) and GA (-24.38), closer to the SC end since NC's subprime crisis was less concentrated than Atlanta's.

**Prediction: -15.0**

---

### Michigan (MI)
**Features**: 8.86 appreciation, 6.87 UR, $33,563 income, -0.05 pop growth

**Comparables**: OH (9.43, 5.43, $33,976, 0.41 → -12.93), IN (8.68, 5.02, $32,905, 2.20 → -7.30)

MI is the clearest example of an economic-fundamental crash rather than a bubble crash. With only 8.86% appreciation, there was almost no bubble to deflate. Instead, the crash was driven by the auto industry collapse: MI has the highest pre-crash unemployment (6.87) in either dataset, negative pop growth (outmigration), and deep concentration in a single industry entering crisis. Detroit's housing market was catastrophic. OH is the closest comparable as a fellow Rust Belt state, but OH's UR was 1.4 points lower and its economy was more diversified. MI's auto-sector concentration amplified every negative feedback loop: job losses, foreclosures, demand collapse. Significantly worse than OH (-12.93).

**Prediction: -19.0**

---

### Illinois (IL)
**Features**: 25.87 appreciation, 4.62 UR, $40,021 income, 0.70 pop growth

**Comparables**: MN (24.94, 4.06, $39,362, 2.18 → -21.83), WI (22.65, 4.69, $36,047, 1.80 → -11.81), MA (28.21, 4.69, $47,311, -0.19 → -17.56)

IL is dominated by the Chicago metro, which had significant subprime exposure particularly on the south side and in south suburbs. MN is the closest comparable: nearly identical appreciation (24.94 vs 25.87) and income (~$39-40K), both anchored by a major metro with subprime issues (Minneapolis vs Chicago). MN crashed -21.83. IL has lower pop growth (0.70 vs 2.18), which limits overbuilding, pulling the prediction milder than MN. But IL has slightly higher UR (4.62 vs 4.06). WI (-11.81) brackets the low end with lower appreciation. MA (-17.56) sits in between with slightly higher appreciation and negative pop growth. IL should land between WI and MN, closer to MN given Chicago's subprime dynamics.

**Prediction: -18.0**

---

### New York (NY)
**Features**: 40.29 appreciation, 4.50 UR, $43,760 income, -0.37 pop growth

**Comparables**: DC (70.23, 5.83, $55,384, 0.38 → -11.93), VT (41.92, 3.68, $36,609, 0.81 → -6.55), NJ (48.76, 4.69, $47,366, 0.70 → -22.13), CT (36.58, 4.42, $53,224, 0.95 → -18.76)

NY's 40.29% appreciation would normally predict a substantial crash (the 40-65 band averages roughly -20). But NY has critical dampening factors: Manhattan's extreme supply constraints mirror DC's dynamics (DC had 70% appreciation but crashed only -11.93), high income ($43,760), and negative pop growth (no overbuilding). NYC's rental market provides a demand floor. However, NY state is not just Manhattan: Long Island, Westchester suburbs, and upstate markets were more vulnerable. The state average blends resilient NYC with weaker surrounding areas. NJ (-22.13) had higher appreciation and represents the more vulnerable commuter-suburb dynamics. NY should land well below NJ but above DC, reflecting the supply-constrained core with a more vulnerable periphery.

**Prediction: -13.0**

---

### Missouri (MO)
**Features**: 18.82 appreciation, 4.89 UR, $33,860 income, 2.33 pop growth

**Comparables**: AL (18.37, 4.01, $31,264, 2.79 → -9.90), WI (22.65, 4.69, $36,047, 1.80 → -11.81), SC (19.42, 6.35, $30,789, 5.00 → -13.02)

MO has moderate everything: moderate appreciation, moderate UR, moderate income, moderate pop growth. St. Louis and Kansas City both had some subprime exposure, but neither was an epicenter. Rural Missouri was relatively stable. AL (18.37 appreciation → -9.90) is the closest appreciation match, with MO having slightly higher UR (4.89 vs 4.01) suggesting marginally worse outcome. WI (-11.81) provides an upper bound with slightly higher appreciation. MO's profile is solidly in the moderate-decline Midwestern/Southern band.

**Prediction: -11.0**

---

## Final Predictions

```json
[
  {"state": "TN", "predicted_crash_pct": -10.0},
  {"state": "PA", "predicted_crash_pct": -13.0},
  {"state": "NM", "predicted_crash_pct": -15.0},
  {"state": "ND", "predicted_crash_pct": -2.0},
  {"state": "UT", "predicted_crash_pct": -17.0},
  {"state": "RI", "predicted_crash_pct": -23.0},
  {"state": "NC", "predicted_crash_pct": -15.0},
  {"state": "MI", "predicted_crash_pct": -19.0},
  {"state": "IL", "predicted_crash_pct": -18.0},
  {"state": "NY", "predicted_crash_pct": -13.0},
  {"state": "MO", "predicted_crash_pct": -11.0}
]
```
