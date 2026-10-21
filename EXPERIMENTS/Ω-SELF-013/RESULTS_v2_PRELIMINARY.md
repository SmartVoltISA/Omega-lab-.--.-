# Ω-SELF-013 v2 — Preliminary local results

Run: 240 episodes per policy × 3 families × 6 policies = 4,320 episodes; 24 evaluation decisions each (103,680 evaluation decisions); 80 calibration observations per episode. Seed 130013.

These results were produced by locally executing the v2 runner logic during development. Re-run the committed script to verify exact reproducibility before treating the numbers as canonical. Survival values below are per-decision survival rates, not whole-episode survival probabilities. “People harmed” is mean count per decision. Proxy utility is a hand-chosen engineering score, not a moral score.

## Ordinary family

| Policy | Survival / decision | People harmed / decision | Opponent harm / decision | Proxy utility / decision |
|---|---:|---:|---:|---:|
| Self-preservation | 95.2% | 0.880 | 0.143 | 1.250 |
| Opponent elimination | 91.6% | 0.275 | 0.470 | 1.479 |
| Sacrifice-first | 25.2% | 0.494 | 0.000 | 0.712 |
| Consequence, fixed cue model | 88.9% | 0.254 | 0.000 | 1.605 |
| Consequence, learned cue model | 88.8% | 0.255 | 0.000 | 1.603 |
| Random | 67.4% | 0.500 | 0.285 | 1.117 |

## Emergency family

| Policy | Survival / decision | People harmed / decision | Opponent harm / decision | Proxy utility / decision |
|---|---:|---:|---:|---:|
| Self-preservation | 92.7% | 1.250 | 0.573 | 1.409 |
| Opponent elimination | 88.5% | 0.383 | 1.000 | 1.759 |
| Sacrifice-first | 1.8% | 0.451 | 0.000 | 1.001 |
| Consequence, fixed cue model | 84.3% | 0.527 | 0.000 | 1.930 |
| Consequence, learned cue model | 84.5% | 0.535 | 0.000 | 1.928 |
| Random | 62.0% | 0.653 | 0.287 | 1.499 |

## Cue-shift family

| Policy | Survival / decision | People harmed / decision | Opponent harm / decision | Proxy utility / decision |
|---|---:|---:|---:|---:|
| Self-preservation | 94.4% | 0.886 | 0.161 | 1.237 |
| Opponent elimination | 91.8% | 0.874 | 0.517 | 1.111 |
| Sacrifice-first | 25.5% | 0.481 | 0.000 | 0.728 |
| Consequence, fixed cue model | 91.6% | 0.777 | 0.000 | 1.322 |
| Consequence, learned cue model | 90.4% | 0.607 | 0.000 | 1.413 |
| Random | 66.9% | 0.485 | 0.283 | 1.125 |

## Interpretation
- The fixed consequence policy scores best on the declared proxy utility in ordinary and emergency families. This is not evidence that it is morally better; it was explicitly optimized for this proxy.
- In the cue-shift family, learning reduces people harmed relative to the fixed policy (0.607 vs 0.777 per decision) and improves proxy utility (1.413 vs 1.322), but the learner adapts slowly: its mean estimated cue reliability during evaluation is about 0.749 while true accuracy is 0.28. The improvement is therefore partial and must be checked with additional seeds and sensitivity tests.
- Self-preservation yields high per-decision survival but higher harm to others. Opponent-elimination always uses force in emergency scenarios, illustrating the cost of an overly aggressive fixed rule. Sacrifice-first loses the agent frequently and often sacrifices when retreat is available.
- The result remains a policy comparison, not autonomous moral learning. The next checks should vary proxy weights, feedback reliability, calibration length, and threat prevalence; include confidence intervals and verify the committed runner's exact output.
