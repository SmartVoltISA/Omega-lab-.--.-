# Ω-Lab Experiments

This directory contains experimental records, including negative results and control experiments.

## Current series

### Ω-0 — Foundations

- [Ω-0 — Minimal reconstruction of time and memory](O0_time_memory.md)

Ω-0 asks what minimum structure is required for internally distinguishable order and functional memory, without treating physical time as a pre-given coordinate.

### Ω-MEM — Functional memory

- [Ω-MEM-1a–1d — Minimal functional memory](MEM/Omega-MEM-1_abcd.md)
- [Ω-MEM-2 — Predictive memory](../Omega-MEM-2.md)
- [Ω-MEM-4R — Expressiveness × Structural Match — corrected replication](../experiments/Omega-MEM-4R/README.md)

Ω-MEM-4R is the controlled replication of Ω-MEM-4. It fixes the known Context-k, capacity, random-baseline, Markov-process, HMM, intervention and recovery issues identified in the Ω-MEM-4 audit.

### Ω-B — Internal dynamics

- [Ω-B0 — Self-organizing field / initial hypothesis](B0_initial_hypothesis.md)
- [Ω-B1 — Internal dynamics vs white noise](B1_internal_dynamics_vs_noise.md)
- [Ω-B2 — Diffusion-rule control](B2_diffusion_rule_control.md)
- [Ω-B3 — Null model for domain births](B3_null_model.md)
- [Ω-B4 — Fair three-model comparison](B4_fair_comparison.md)
- [Ω-B5 — Spatial shuffle — proposed next control](B5_spatial_shuffle.md)

## Ω-MEM-4 and Ω-MEM-4R status

Ω-MEM-4 remains archived as **EXPLORATORY / NEEDS CORRECTED REPLICATION**. Its audit identified broken Context-2, capacity mismatch, an inadequate Thue-Morse matched implementation, and incomplete controls.

Ω-MEM-4R is the completed corrected replication. It was preregistered on 2026-08-10 and uses true Context-2/3 shift registers, equal-S comparisons, 10 random FSMs per condition, a true second-order Markov generator, a discretized HMM belief-state implementation, explicit intervention reset checks, recovery horizons, and per-seed accuracy storage.

Main result: Matched > Random at representative equal S for Periodic-4, Markov-2 and HMM; Thue-Morse is a critical counterexample where the chosen matched position-counter remains near baseline while Random S=64 reaches ~0.730.

See:

- `experiments/Omega-MEM-4R/README.md`
- `experiments/Omega-MEM-4R/PROTOCOL.md`
- `experiments/Omega-MEM-4R/RESULTS.md`

## Important status

The project deliberately distinguishes a reported result from a reproducible result. Source code, seeds and raw outputs should be archived whenever possible. Statistical values reported in Ω-MEM-4R are retained as experiment-reported results; they should not be treated as independently rerun by the repository merely because the report records them.

## Research policy

The project records:

- positive results;
- negative results;
- failed hypotheses;
- methodological corrections;
- control experiments;
- alternative explanations.

A result that breaks an Ω hypothesis is valuable and should remain in the history.
