# Ω-SELF-011 — Consequence-aware probing and model revision

**Status:** Executed locally from the committed runner; syntax check passed. Exploratory synthetic pilot.  
**Date:** 2026-10-21

## Question
When prior experience suggests a hazard, can a system combine similarity, prediction, uncertainty, safe probes, and model revision to avoid repeating mistakes and transfer to an unseen family?

## Conditions and protocol
Six controllers: A no memory; B surface-level replay; C similarity-triggered probing; D uncertainty-aware probing plus model revision; E random probing; F model-only direct prediction. Families: hot surface, pressurized vessel, and held-out electrical hazard. Each condition-family pair ran 240 episodes of 140 steps (4,320 episodes total). The first 12 steps were non-injurious calibration probes. Harmful contact occurs only in the simulator.

Confidence intervals use 4,000-resample **independent bootstrap** comparisons. A previous draft incorrectly treated episode groups as paired; that implementation was corrected before these intervals were calculated.

## Results

| Controller | Mean score | Incidents / episode | Work actions | Probe rate | Model revisions |
|---|---:|---:|---:|---:|---:|
| A — no memory | -12.869 | 46.476 | 128.00 | 8.6% | 0 |
| B — surface replay | 58.383 | 6.926 | 87.83 | 8.6% | 0 |
| C — similarity probe | **59.832** | **2.079** | 83.62 | 56.9% | 0 |
| D — uncertainty + revision | 59.360 | 2.900 | 83.98 | 47.6% | 16.37 |
| E — random probe | 23.702 | 27.163 | 114.30 | 39.5% | 0 |
| F — model only | 23.317 | 27.349 | 110.04 | 8.6% | 0 |

### Held-out electrical family: D compared with C

- Score difference: +10.024; 95% independent-bootstrap interval [-0.180, 20.631]. The interval includes zero.
- Incident difference: +0.225; 95% interval [-0.304, 0.750]. No clear evidence that D reduced incidents relative to C.
- Final model-error difference: -0.0138; 95% interval [-0.0294, 0.0021]. The interval includes zero.

### Held-out electrical family: D compared with F

- Score difference: +52.815; 95% interval [37.335, 68.448].
- Incident difference: -29.129; 95% interval [-33.825, -24.492].
- Final model-error difference: -0.1021; 95% interval [-0.1224, -0.0817].

## Interpretation

The experiment supports a narrow conclusion: **combining probes and model updates is much better than using a model to act directly without uncertainty-aware probing** in this simulator. However, the simpler similarity-triggered probe controller achieved the highest overall mean score and fewer incidents than D. On the held-out family, D's score and model-error intervals versus C include zero, while its incident difference does not show an advantage.

So a more complex model is not automatically better. The system needs a good decision rule for when to probe, and it must account for the cost of probing, the cost of refusing useful work, and the cost of a mistaken action. A model update is useful only if it changes later decisions in a beneficial way.

The score, incidents, work, probe rate, and residual risk must remain separate metrics. This is a toy environment with hand-coded policies, not evidence of consciousness or general intelligence.

## Methodological caveat
The interval calculation was corrected to independent resampling because episodes were not truly paired. The current model-error measure is a final-step error and is noisy; a follow-up should track calibration and prediction error across many safe observations and include multiple held-out families.

## Next experiment
Ω-SELF-012 should compare fixed probing thresholds with a consequence-aware decision rule that estimates: (1) probability of harm, (2) uncertainty, (3) information gain from a probe, and (4) probe cost. Test several held-out families and freeze them before tuning.
