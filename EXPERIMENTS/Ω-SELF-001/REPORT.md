# Ω-SELF-001 — Self-model, self-modification, and adaptation

**Status:** PILOT / INCONCLUSIVE  
**Date:** 2026-10-21  
**Repository:** `SmartVoltISA/Omega-lab-.--.-`  
**Branch:** `experiment/omega-self-001-self-model`

## Research question

Does giving an agent a functional model of its own internal state improve adaptation in a changing environment? Does allowing bounded policy self-modification add benefit?

This experiment tests functional self-monitoring only. It does **not** test or establish subjective consciousness, sentience, or general intelligence.

## Preregistered hypotheses

- **H1 (primary):** Self-modeling increases the fraction of runs that survive the full 500-step horizon after an environmental regime change.
- **H2 (secondary):** Self-modeling increases mean energy over the run.
- **H3 (secondary):** Bounded self-modification improves full-horizon survival compared with a self-model without policy modification.

## Conditions

- **A — A_reactive:** fixed reactive policy; no explicit internal self-model.
- **B — B_self_model:** noisy estimate of own energy/fatigue informs decisions; policy thresholds fixed.
- **C — C_self_modifying:** same basic self-model plus bounded threshold updates based on observed outcomes.

All conditions use a 500-step horizon, a regime shift at step 250, 200 runs per condition, and deterministic seeds. Energy is clipped to [0, 100]. Forage yield drops after the regime shift. Each condition receives a separate deterministic random stream; the runs are reproducible but are not perfectly paired at the per-step noise level.

## Results

| Metric | A: Reactive | B: Self-model | C: Self-modifying |
|---|---:|---:|---:|
| Runs | 200 | 200 | 200 |
| Full-horizon survival | 100.0% | 91.5% | 96.5% |
| Mean survival steps | 500.00 | 493.77 | 497.71 |
| Mean energy over run | 63.55 | 75.53 | 73.61 |
| Mean final energy | 20.02 | 42.73 | 39.57 |
| Mean absolute self-estimation error | N/A | 13.29 | 13.22 |
| Mean policy changes | 0 | 0 | 76.57 |

## Interpretation

- **H1 was not supported in this pilot.** The reactive baseline survived the full horizon in every run; self-model conditions had lower full-horizon survival.
- **H2 was supported descriptively in this toy model.** Both self-model conditions had higher mean energy and higher mean final energy than the reactive baseline.
- **H3 was partially supported descriptively.** Self-modification raised full-horizon survival from 91.5% to 96.5% compared with B, but did not reach the 100% baseline rate and had lower mean energy than B.
- The self-estimation error is large enough to be a likely failure mechanism. A model of oneself is only useful when it is sufficiently calibrated and improves decisions.

These are descriptive results from a simplified synthetic environment, not evidence of statistical significance or real-world intelligence. The model's action rules and thresholds are hand-designed; they may favor or disadvantage particular conditions.

## Limitations and failure modes

1. Only one environment design and one regime shift were tested.
2. The baseline is a strong hand-coded heuristic and survives all runs, creating a ceiling effect for survival.
3. Self-model estimates are noisy and can drift; the model does not yet include explicit calibration or uncertainty-aware decisions.
4. The self-modification rule is hand-designed, not an open-ended architecture search.
5. No population, reproduction, inheritance, or multi-agent selection was tested in this run.
6. No claim about consciousness or subjective experience follows from these results.
7. The run-level seed streams are deterministic but use different streams by condition, so paired causal comparisons require a follow-up with common random numbers.

## Next experiment

Run **Ω-SELF-002** with:
- common random numbers and multiple environment regimes;
- a calibrated self-model and an explicit no-self-model control with matched computational budget;
- an oracle-state upper bound and a deliberately miscalibrated self-model control;
- predefined primary metrics: survival, cumulative energy, adaptation delay after regime change, and generalization to an unseen regime;
- at least 1,000 seeds per condition, confidence intervals, and an archived raw dataset.

Do not conclude that a self-model is necessary unless it beats well-matched controls across multiple environments. The current result suggests a more precise question: **when is a model of self useful, and what level of calibration is required?**

## Reproduction

From a Python environment with NumPy and pandas:

```bash
python run_experiment.py --seeds 200 --horizon 500 --change-at 250 --out results.csv
```

The script emits per-run CSV, summary CSV, and summary JSON. Seed, model rules, and parameters are recorded in the script.

## Ω-Lab record

Cycle: **HYPOTHESIS → MODEL → EXPERIMENT → CONTROL → RESULT → AUDIT → NEXT TEST**

Decision: **RECORD PILOT; DO NOT CLAIM CONFIRMATION.** Preserve the negative/ambiguous outcome and proceed to Ω-SELF-002 only after improving the controls.
