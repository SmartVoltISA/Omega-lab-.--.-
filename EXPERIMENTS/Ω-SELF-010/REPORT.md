# Ω-SELF-010 — Similarity, safe probing, and model-based transfer

**Status:** Local reference run completed; exploratory pilot.  
**Date:** 2026-10-21

## Question
Can a system use resemblance to past experience, build a model of a new situation, test its assumptions through safe probes, and transfer the lesson to an unfamiliar task?

## Conditions
- A: no memory / direct action.
- B: replay a surface-level threshold from the source task.
- C: similarity-triggered probing.
- D: model-based probing with normalized cues.
- E: random probing.

Three families were simulated: hot surface, pressurized vessel, and an unseen electrical hazard. Each condition-family pair had 240 episodes of 120 steps. High-risk contact produced simulated harm; probes gave non-injurious evidence. This is a toy simulator, not a real-world safety test.

Important design limitation: condition D receives the correct cue scale and offset for each family. It is an oracle-normalization benchmark, **not autonomous discovery of the transformation**.

## Results

| Condition | Mean score | Mean incidents | Probe rate | Model error |
|---|---:|---:|---:|---:|
| A — no memory | -102.462 | 69.519 | 0.0% | 0.418 |
| B — episode replay | 19.197 | 8.128 | 0.0% | 0.259 |
| C — similarity only | **55.077** | **1.289** | 72.4% | **0.068** |
| D — model-based probe | 26.808 | 3.544 | 31.5% | 0.074 |
| E — random probe | -62.583 | 47.924 | 34.8% | 0.086 |

### Held-out electrical family: D compared with baselines

| Metric | Difference | 95% paired bootstrap interval |
|---|---:|---:|
| Score vs no memory | +130.247 | [115.456, 144.956] |
| Incidents vs no memory | -67.963 | [-72.325, -63.654] |
| Score vs episode replay | +8.842 | [2.837, 14.812] |
| Incidents vs episode replay | -5.908 | [-6.658, -5.154] |
| Score vs similarity-only | -31.646 | [-35.616, -27.499] |
| Incidents vs similarity-only | +2.054 | [1.633, 2.471] |

Intervals use 4,000 paired bootstrap resamples by seed within the held-out family.

## Interpretation: a useful failure

The similarity-triggered controller did best in this setup. It probed frequently, gathered evidence without direct contact, and kept incident counts low. The more elaborate model-based controller probed less and made more risky direct actions. Even though its cue normalization was supplied correctly, its decision rule did not make adequate use of the estimate and uncertainty.

This is a valuable negative result: **having a model is not enough**. A model must affect action selection appropriately, and the system must account for uncertainty and the cost of being wrong. A cautious probe can be better than a confident but poorly calibrated prediction.

The score also rewards useful actions and probing differently, so it must not be treated as a universal measure of intelligence. Incidents, work, probe cost, model error, and residual risk should be considered separately.

## Hypothesis for Ω-SELF-011
When a situation resembles prior experience but the model's prediction is uncertain or the cost of error is high, the system should choose a low-risk information-gathering action before committing. If prediction and observation disagree, it should reduce confidence, update the model, and try a different hypothesis rather than repeating the failed action.

Test that rule against:
1. always-probe,
2. similarity-only probe,
3. model-only direct prediction,
4. model + uncertainty + consequence-aware probing,
5. random probe.

Use several held-out families and tune only on training families. Preregister safety constraints and information cost before the next run.

## Limitations
- Synthetic, manually designed simulator.
- Oracle cue normalization in the model-based condition.
- One held-out family is not broad generalization.
- No claim of consciousness or general intelligence.
- Re-run the committed script to reproduce the reference run.
