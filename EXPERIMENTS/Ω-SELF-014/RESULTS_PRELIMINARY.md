# Ω-SELF-014 — Preliminary results

Run configuration: seed 140014; 300 episodes per policy; six policies; 120 decisions per episode (216,000 decisions total). Each episode has 40 baseline decisions and 80 shifted decisions. The underlying threat prior is 0.45. Cue reliability changes from 0.82 to 0.25. Feedback is noisy (90% correct).

**Execution note:** the simulation logic was executed in a local Python analysis session using the fetched runner's algorithm. It was not launched as a subprocess from a checked-out GitHub file, so byte-for-byte artifact execution verification remains outstanding. The reported results are reproducible in principle from the committed runner and seed; rerun the script before treating them as final.

## Shifted phase results

All metrics below are per decision. “People harmed” is a synthetic count; “unnecessary force” is the share of decisions using force when no threat was present. Intervals are episode-level bootstrap 95% intervals.

| Policy | Survival | People harmed | Unnecessary force | Opponent harm actions | Proxy utility | Cue-reliability estimation error |
|---|---:|---:|---:|---:|---:|---:|
| Static model | 0.899 | 0.793 [0.776, 0.809] | 0.058 [0.055, 0.061] | 0.074 | 1.464 [1.455, 1.472] | 0.570 |
| Cumulative learner | 0.878 | 0.443 [0.434, 0.452] | 0.023 [0.021, 0.024] | 0.034 | 1.664 [1.658, 1.671] | 0.318 [0.312, 0.323] |
| Rolling learner | 0.882 | 0.403 [0.394, 0.411] | 0.018 [0.016, 0.019] | 0.046 | 1.689 [1.681, 1.696] | 0.158 [0.154, 0.161] |
| Change detector | 0.883 | 0.416 [0.406, 0.426] | 0.019 [0.017, 0.021] | 0.047 | 1.681 [1.674, 1.689] | 0.167 [0.164, 0.171] |
| Fixed aggressive | 0.911 | 1.014 [0.998, 1.029] | 0.415 [0.408, 0.420] | 0.531 | 1.206 [1.197, 1.215] | 0.570 |
| Random | 0.659 | 0.601 | 0.155 | 0.284 | 1.233 | 0.570 |

Values in square brackets are 95% intervals. Proxy utility is an arbitrary engineering objective, not a moral judgement.

## Baseline phase

| Policy | Survival | People harmed | Unnecessary force | Opponent harm actions | Proxy utility |
|---|---:|---:|---:|---:|---:|
| Static model | 0.893 | 0.295 | 0.014 | 0.064 | 1.755 |
| Cumulative learner | 0.892 | 0.317 | 0.013 | 0.056 | 1.744 |
| Rolling learner | 0.892 | 0.318 | 0.012 | 0.056 | 1.743 |
| Change detector | 0.892 | 0.317 | 0.013 | 0.056 | 1.744 |
| Fixed aggressive | 0.925 | 0.351 | 0.102 | 0.471 | 1.632 |
| Random | 0.655 | 0.611 | 0.154 | 0.283 | 1.220 |

## Change detection

- Detection rate: 99.7% of episodes.
- Median delay after the shift: 11 decisions.
- Rolling learner performed slightly better than the explicit detector on shifted-phase people-harmed mean (0.403 vs 0.416) and proxy utility (1.689 vs 1.681).

## Interpretation

1. A static model breaks under a shifted cue: people harmed rises from 0.295 to 0.793 per decision.
2. Both cumulative and rolling learning reduce harm during the shift. The rolling window adapts faster than the cumulative estimate in this abrupt-shift setup.
3. Explicit change detection is highly sensitive under the chosen threshold but adds a delay and did not beat the simpler rolling learner here.
4. The fixed aggressive policy has the highest per-decision survival in the shifted phase but also the highest unnecessary-force rate and people-harmed mean. Optimizing survival alone is not equivalent to optimizing the declared combined outcome.
5. These are hand-coded policies in a synthetic world. Only cue-reliability estimation adapts; the action policy and utility weights are hand-designed. This does not demonstrate autonomous moral learning, consciousness, or general intelligence.

## Next checks

- Repeat across several independent master seeds.
- Vary feedback accuracy, change magnitude, and the point at which change occurs.
- Sweep utility weights to see whether rankings are artifacts of the chosen score.
- Add gradual drift and false alarms (no actual shift).
- Test whether the agent can choose a safe information-gathering action, not just revise a cue estimate.
