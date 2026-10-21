# Ω-SELF-002 — Calibration, self-model, and bounded self-modification

**Status:** PILOT RESULT / REQUIRES REPLICATION  
**Date:** 2026-10-21  
**Branch:** `experiment/omega-self-002-calibration`

## Research question
Under partial observability and repeated regime changes, when does a functional model of the agent's own state help? Does bounded policy self-modification help? How damaging is a systematically miscalibrated model?

This toy control experiment does not test or establish subjective consciousness, sentience, or general intelligence.

## Conditions
Five conditions were compared over 1,000 paired environment seeds each (5,000 agent-runs total), with a 600-step horizon.

- **A — reactive/noisy:** acts on a noisy observation of current energy; no persistent self-state model.
- **B — calibrated self-model:** maintains a predicted energy state and corrects it using observations.
- **C — miscalibrated self-model:** uses a systematically optimistic forage-yield model and underweights observations.
- **D — self-modifying:** uses the same basic state estimator as B and changes two policy thresholds using prewritten bounded update rules.
- **E — oracle state:** receives true energy. This is an upper-bound diagnostic, not a realistic agent.

All conditions within a seed share pre-generated exogenous noise, observation noise, cues, and environment schedule. Regime changes occur at steps 120, 240, 360, and 480. Initial energy is 42. Observations have standard deviation 10 energy units.

## Preregistered primary metric
Fraction of runs surviving the full 600-step horizon. Secondary metrics: mean survival steps, mean energy, final energy, state-prediction error, and policy changes.

## Results

| Condition | Full-horizon survival | Mean survival steps | Mean energy | Mean final energy | Mean prediction error |
|---|---:|---:|---:|---:|---:|
| A — reactive/noisy | 48.2% | 434.8 | 40.59 | 26.33 | — |
| B — calibrated self-model | 36.1% | 394.0 | 40.21 | 19.32 | 7.05 |
| C — miscalibrated self-model | 0.0% | 144.4 | 45.03* | 0.00 | 7.32 |
| D — self-modifying | 94.5% | 576.4 | 41.21 | 48.43 | 6.87 |
| E — oracle state | 99.6% | 598.3 | 37.54* | 52.19 | — |

`*` Mean energy is averaged only over steps an agent survives and can mislead when runs terminate early. Survival and survival duration are primary.

## Paired-seed comparison
Bootstrap 95% percentile intervals for the difference in full-horizon survival (10,000 resamples over 1,000 paired seeds):

- **D minus A:** +46.3 percentage points; 95% CI [+42.9, +49.6].
- **B minus A:** −12.1 points; 95% CI [−15.7, −8.5].
- **C minus A:** −48.2 points; 95% CI [−51.3, −45.1].
- **E minus A:** +51.4 points; 95% CI [+48.3, +54.5].

Intervals describe variation over selected seeds in this simulation. They do not correct for hand-designed rules, model selection, or limited environment diversity.

## Interpretation
1. A state model alone did not help in this implementation: B underperformed the reactive baseline. An internal estimate is not automatically beneficial; stale or inaccurate estimates can harm decisions.
2. Miscalibration was damaging: C failed to survive the horizon in any run. The optimistic transition model and low observation-correction gain created a poor control loop. This is a failure result, not evidence that all self-models are harmful.
3. Bounded self-modification performed best among non-oracle conditions. D survived the full horizon in 94.5% of runs. Its manually specified threshold updates appear useful in this environment.
4. This does **not** demonstrate spontaneous self-improvement. D's adaptation rules were designed by the experimenter. The result shows that bounded policy adaptation can help in this toy setting, not that an agent invented its own architecture or developed consciousness.
5. The oracle is a diagnostic upper bound. Its near-ceiling survival suggests state information can be useful, but does not isolate the value of a self-model from direct access to true state.

## Limitations
- One synthetic environment family and fixed regime-change schedule.
- Hand-designed action rules, model assumptions, and policy updates.
- Information-processing paths are not perfectly matched.
- One deliberately bad model cannot represent all model errors.
- Fixed schedule may be exploitable.
- The experiment measures control performance, not subjective awareness or intelligence.
- Bootstrap intervals are descriptive and do not establish a universal causal law.

## Decision
**Record as a useful pilot, not as confirmation of the broad hypothesis.** The narrower result: a persistent self-state estimate is not sufficient; calibration and effective policy adaptation matter. Next: vary environment families and update rules, compare against a tuned reactive baseline, include a sham-modification control, and match compute/information budgets.

## Ω-Lab cycle
`HYPOTHESIS → MODEL → PREREGISTER → RUN → CONTROL → RESULT → AUDIT → NEXT TEST`

## Reproduction
```bash
python run_experiment.py --seeds 1000 --horizon 600 --out results.csv
```
Requires Python, NumPy, and pandas. The runner emits per-run data and an aggregate summary.
