## Analysis Framework

I'll anchor predictions primarily on **appreciation_03_06** (bubble proxy), then adjust for **pop_growth** (speculative overbuilding), **ur_2006** (economic fragility), **pcpi_2006** (buyer resilience), and structural factors from domain knowledge.

Key patterns from training data:
- Appreciation is the dominant predictor (NV 80% → -55.69; TX 12% → -4.15)
- Pop growth amplifies crashes at high appreciation (NV 12% pop, AZ 9% pop)
- Supply-constrained / government-driven markets resist (HI 81% appr → -18.48; DC 70% → -11.93)
- Structural shocks can override low appreciation (MI 9% appr → -29.40 from auto collapse)
- Outliers: GA crashed -24.38 on only 15% appreciation due to Atlanta exurb overbuilding

---

## Predictions

### RI (Rhode Island) — Predicted: **-23.00**

Closest comparable: **NJ** (48.76% appr → -22.13). RI's appreciation (48.54%) is nearly identical. RI has weaker fundamentals: lower income ($38,719 vs $47,366) and higher UR (5.26% vs 4.69%), meaning more stretched, vulnerable buyers. Counterbalancing this, RI's negative pop growth (-0.77%) implies less speculative overbuilding than NJ (0.70%). RI was a small state with concentrated subprime exposure in the Providence metro. Net: slightly worse than NJ.

### CT (Connecticut) — Predicted: **-17.50**

Appreciation (36.58%) places CT near ME (34.89% → -13.11) and VT (41.92% → -6.55). Low pop growth (0.95%) and very high income ($53,224, highest in the dataset after DC) are strong stabilizers. However, CT had significant financial sector concentration (Fairfield County hedge funds, insurance HQs) that was directly hit by the crisis, analogous to MI's auto exposure but less dominant. MA (28.21% appr → -17.56) is a useful anchor: CT has higher appreciation but also higher income. Net: close to MA, with financial sector drag pulling slightly worse.

### NM (New Mexico) — Predicted: **-16.00**

Moderate appreciation (32.57%) with moderate pop growth (4.50%) and low income ($30,433). Not a Sun Belt extreme like AZ/NV, but participated in the regional boom. Comparables: ME (34.89% → -13.11, low pop growth), NC (16.94%, 5.87% pop → -13.06). NM's higher appreciation than NC and lower income suggest a worse outcome. Diversified economy (national labs, military, government) provides some floor.

### PA (Pennsylvania) — Predicted: **-13.00**

Nearly identical profile to ME: appreciation (34.06% vs 34.89%), UR (4.73% vs 4.71%), low pop growth (1.10% vs 1.31%). ME crashed -13.11. PA is a large, diverse state: Philadelphia suburbs appreciated significantly, but Pittsburgh was stable and rural areas had minimal bubble. The statewide average would be moderate. Income ($37,803) slightly higher than ME ($34,168) provides marginal buffer.

### CO (Colorado) — Predicted: **-5.50**

Low appreciation (11.88%), matching NE exactly (11.88% → -2.88) and TX (11.68% → -4.15). CO already corrected 2001-2003 during the tech bust, so 2003-2006 appreciation partly reflects recovery, not fresh bubble. Higher income ($39,869) than comparable states. Moderate pop growth (4.23%) adds some risk beyond NE/TX. Denver metro had foreclosure pockets but no systemic overvaluation.

### WI (Wisconsin) — Predicted: **-13.50**

Appreciation (22.65%) puts WI between MO (18.82% → -10.97) and MN (24.94% → -21.83). MN's severe crash was driven by Twin Cities exurban overbuilding and subprime concentration; Milwaukee had smaller-scale versions of these dynamics. Low pop growth (1.80%) and moderate income ($36,047) suggest WI falls closer to MO than MN. WI doesn't have the large metro subprime concentration of IL/MN.

### NH (New Hampshire) — Predicted: **-15.50**

Moderate appreciation (31.83%) with strong fundamentals: low UR (3.52%), high income ($42,866). Comparable to MA (28.21% → -17.56) but with slightly higher appreciation offset by stronger labor market and higher income relative to regional cost. Southern NH (Nashua/Manchester, Boston commuter belt) had significant bubble activity, while northern NH was stable. ME (34.89% → -13.11) with lower income and higher UR crashed less, which constrains NH's downside. Net: between ME and MA.

### OH (Ohio) — Predicted: **-11.00**

Very low appreciation (9.43%), similar to IN (8.68% → -7.30) and MI (8.86% → -29.40). OH's UR (5.43%) sits between IN (5.02%) and MI (6.87%). The critical question is auto sector concentration: MI's -29.40 was driven by devastating auto industry collapse. OH had auto exposure but was more diversified (Columbus financial services, Cincinnati manufacturing diversity). Cleveland and Dayton had severe subprime issues that add 3-4 percentage points of crash beyond what appreciation alone predicts. Near-zero pop growth (0.41%) means no overbuilding.

### UT (Utah) — Predicted: **-17.50**

Moderate appreciation (23.39%) but high pop growth (7.01%) signals construction activity. Very low UR (2.87%, lowest in dataset) indicates genuine economic strength. Key comparable: GA (15.17% appr, 6.18% pop → -24.38) crashed hard from Atlanta overbuilding. UT has higher appreciation AND higher pop growth than GA, but much stronger labor market. St. George was among the hardest-hit markets nationally, but Salt Lake City was more resilient. UT's pop growth is partly organic (high birth rate), not purely speculative migration. Net: worse than MO (-10.97), better than GA (-24.38).

### LA (Louisiana) — Predicted: **-8.00**

Unique case: the -4.83% population decline was driven by Hurricane Katrina (2005), not economic weakness. Katrina destroyed housing supply in the New Orleans metro, which actually supported prices in surviving areas. The 22.89% appreciation includes post-Katrina supply-shock price gains, not pure speculation. When the 2008 crisis hit, LA's housing market had already undergone a structural reset. Reconstruction spending and federal aid provided economic stimulus. Comparables by appreciation (MO -10.97, AL -9.90) suggest moderate crash, reduced further by Katrina's unique supply dynamics.

### WA (Washington) — Predicted: **-22.50**

High appreciation (42.91%), most comparable to OR (44.87% → -25.98). WA has higher income ($39,744 vs $34,488), lower UR (4.99% vs 5.39%), but higher pop growth (4.37% vs 3.48%). Seattle's tech economy (Microsoft, Amazon, Boeing) provided a stronger employment floor than Portland's. OR's less diversified economy and lower income made it more vulnerable. Net: WA crashes somewhat less than OR due to tech economy resilience, but high appreciation means a significant downturn.

---

## Final Predictions

```json
[
  {"state": "RI", "predicted_crash_pct": -23.00},
  {"state": "CT", "predicted_crash_pct": -17.50},
  {"state": "NM", "predicted_crash_pct": -16.00},
  {"state": "PA", "predicted_crash_pct": -13.00},
  {"state": "CO", "predicted_crash_pct": -5.50},
  {"state": "WI", "predicted_crash_pct": -13.50},
  {"state": "NH", "predicted_crash_pct": -15.50},
  {"state": "OH", "predicted_crash_pct": -11.00},
  {"state": "UT", "predicted_crash_pct": -17.50},
  {"state": "LA", "predicted_crash_pct": -8.00},
  {"state": "WA", "predicted_crash_pct": -22.50}
]
```
