# Ω-SELF-008 — Adaptation after regime change and transfer to an unseen family

**Status:** Local reference run completed; committed runner updated to match the protocol. Exploratory pilot.  
**Date:** 2026-10-21

## Question
Does outcome feedback help a controller adapt after conditions change, and does that benefit transfer to a held-out environment family?

## Protocol
- Conditions: A fixed controller; B reward-only feedback; C punishment-only feedback; D combined reward + punishment; E sham feedback.
- Training/tuning families: `rapid`, `slow`, and `surprise`; held-out test also includes `unseen_drift`.
- 80 seeds per family, 300 steps per episode, 320 episodes per condition.
- Feedback updates every 25 steps.
- Primary outcomes: useful task progress before and after the change, adaptation lag, survival, and resource state.
- For the gradual-drift family, which has no abrupt change point, pre/post rates are split at the episode midpoint.
- Paired bootstrap intervals use 3,000 resamples.

## Results

| Condition | Survival | Mean progress | Post-change progress rate | Adaptation lag | Mean energy |
|---|---:|---:|---:|---:|---:|
| A — fixed | 100% | 190.838 | 0.435 | 8.78 | 24.85 |
| B — reward only | 100% | **191.578** | **0.441** | **6.61** | 23.37 |
| C — punishment only | 100% | 190.895 | 0.435 | 8.38 | 24.02 |
| D — combined | 100% | 191.330 | 0.438 | 9.33 | 23.89 |
| E — sham | 100% | 190.731 | 0.436 | 9.52 | 25.28 |

The reward-only controller had the highest mean progress and the highest post-change progress rate, and its average adaptation lag was shorter than the combined controller's. The combined controller exceeded the fixed and punishment-only controllers slightly on post-change progress, but did not beat reward-only feedback.

### Paired bootstrap: post-change progress rate

| Comparison | Difference | 95% interval |
|---|---:|---:|
| Combined − fixed | +0.0028 | [0.0018, 0.0037] |
| Combined − reward only | −0.0043 | [−0.0054, −0.0034] |
| Combined − punishment only | +0.0027 | [0.0020, 0.0034] |
| Combined − sham | +0.0015 | [0.0004, 0.0026] |
| Combined − fixed, unseen drift family | +0.0037 | [0.0015, 0.0058] |

All conditions survived all episodes and recorded zero steps beyond the defined violation thresholds. Survival and violation metrics therefore cannot discriminate between them in this setup.

## Interpretation
This pilot **does not support the claim that combining reward and punishment is best**. The reward-only controller performed slightly better on average, and the combined controller did not adapt faster by the chosen lag metric. The combined controller's small post-change advantage over fixed behavior is not sufficient to justify additional complexity.

This result is limited to hand-coded feedback rules in a synthetic simulator. The unseen-drift result is only one designed stress test, not broad generalization. It is not evidence of consciousness or general intelligence.

## Decision
For Ω-SELF-009, retain separate metrics rather than collapsing them into one score. Make useful task completion the primary objective, use safety/resource thresholds as constraints, and test learned or tunable feedback parameters against a compute-matched baseline. Increase difficulty using training families only, then freeze the test set.
