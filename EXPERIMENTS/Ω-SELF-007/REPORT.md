# Ω-SELF-007 — Two signals: reward, punishment, and outcome feedback

**Status:** PILOT EXECUTED LOCALLY — diagnostic result  
**Date:** 2026-10-21

## Hypothesis
A controller using both a positive signal for useful task progress (“carrot”) and a negative signal for risk/resource violations (“whip”), with updates driven by observed outcomes, will outperform reward-only, punishment-only, fixed, and sham-feedback controllers.

## Protocol
- Four test families: rapid shift, slow shift, surprise shift, and an unseen gradual-drift family.
- 60 seeds per family; 240 episodes per condition; 250 steps per episode.
- Conditions: A fixed thresholds; B reward-only feedback; C punishment-only feedback; D combined reward + punishment; E sham feedback unrelated to actual outcomes.
- All conditions begin with the same energy and stress thresholds.
- Feedback updates every 25 steps.
- Positive signal: incremental useful task progress.
- Negative signal: low-energy and high-stress penalties.
- Paired bootstrap: 3,000 resamples for differences in useful progress.

Note: despite the hypothesis wording, this pilot compares hand-coded feedback rules; it does not train an open-ended learner or optimize learned weights. The listed “unseen” family is one designed stress test, not broad out-of-distribution validation.

## Results

| Condition | Full survival | Mean task progress | Mean energy | Descriptive score |
|---|---:|---:|---:|---:|
| A — fixed | 100% | 188.30 | 25.80 | 0.75303 |
| B — reward only | 100% | 189.16 | 24.44 | 0.75408 |
| C — punishment only | 100% | 188.41 | 25.33 | 0.75287 |
| D — reward + punishment | 100% | 189.22 | 24.21 | 0.75403 |
| E — sham feedback | 100% | 188.04 | 26.20 | 0.75270 |

The descriptive score is a compact summary only; do not treat it as the primary result. All conditions achieved 100% survival, so survival is saturated in this setup.

### Paired bootstrap for task progress

| Comparison | Mean difference | 95% interval |
|---|---:|---:|
| D − A | +0.925 | [+0.729, +1.121] |
| D − B | +0.067 | [−0.069, +0.215] |
| D − C | +0.815 | [+0.631, +0.996] |

Combined feedback exceeded fixed and punishment-only controllers by a small amount in this toy environment. Its difference from reward-only feedback was small and uncertain: the interval includes zero. Thus this run does **not** establish that “whip + carrot” is better than reward-only feedback.

## Interpretation
The user’s proposed architecture is a useful next design:
- **Carrot:** reinforce verified useful progress.
- **Whip:** impose a cost for constraint violations, danger, or wasted resources.
- **Feedback:** use measured outcomes to revise behavior, not merely the reward signal itself.

The two signals should not be collapsed too early into one scalar. Keep task progress, safety violations, resource state, and task completion visible as separate metrics. Otherwise the controller can game the combined score.

## Decision
Keep the hypothesis alive but unconfirmed. Ω-SELF-008 should:
1. Make task completion the primary objective and safety/resource limits hard constraints.
2. Compare reward-only, punishment-only, combined feedback, and sham feedback with more seeds and multiple unseen families.
3. Test whether the feedback update rules actually change behavior in a useful way across shifts.
4. Add explicit task-failure penalties and measure completion quality, not only accumulated progress.
5. Publish all metrics and paired uncertainty intervals.

This is a toy-control result, not evidence of consciousness or general intelligence.
