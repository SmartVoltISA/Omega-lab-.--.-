# Ω-MEM-4R — Expressiveness × Structural Match

**Date:** 2026-08-10  
**Status:** COMPLETED / corrected replication  
**Direction:** DIR-1 — Time & Memory  
**Tests:** H-MEM-2.2, H-MEM-2.3

## Purpose

Ω-MEM-4R is the controlled replication of Ω-MEM-4. The purpose was to remove the known implementation and protocol confounds and test the narrower claim:

> At equal effective memory capacity, does a structurally matched representation outperform an equally expressive random or mismatched representation?

The replication was fixed before execution.

## Corrections relative to Ω-MEM-4

| Issue | Ω-MEM-4 | Ω-MEM-4R |
|---|---|---|
| Context-2 | Broken | True shift register, validated |
| Context-3 | Not independently validated | True shift register, validated |
| Matched capacity | P3 forced low capacity | Same-S comparison; P1 exception documented |
| Random baseline | Single FSM | Ensemble of 10 FSMs |
| Markov process | Effectively first-order | Explicit second-order generator tested |
| HMM matched model | Simple context | Discretized Bayesian belief-state implementation |
| Intervention | Reset equivalence not verified | Reset state explicitly differs from control |
| Recovery | Not measured | Horizons 1–128 |
| Raw results | Not archived | Per-seed accuracy arrays archived in experiment output |

## Processes

- **P1 Periodic-4:** positive control.
- **P2 Markov-2:** explicitly constructed second-order generator.
- **P3 Thue-Morse:** deterministic non-periodic process; critical counterexample.
- **P4 HMM:** two hidden states, Bayesian belief-state matched implementation.
- **P5 Random-iid:** negative control.

## Main result

H-MEM-2.2 is **not universally confirmed**. Matched > Random at equal tested S for 3/4 structured processes, while Thue-Morse is a strong counterexample to the tested matched architecture.

H-MEM-2.3 is **PARTIALLY CONFIRMED** as a refinement: predictive advantage depends on sufficient expressive capacity, informational content of the state, implementation robustness, and actual predictive-state correspondence. It remains open to further independent testing.

## Results

| Process | Key result |
|---|---|
| Periodic-4 | Counter S=4 = 1.000; S<4 ≈ 0.500 |
| Markov-2 | Context-1 = Context-2 = Context-3 = Matched ≈ 0.823 |
| Thue-Morse | Matched ≈ 0.500 at all tested S; Random S=64 ≈ 0.730 |
| HMM | Context-1 ≈ 0.704; Matched ≈ 0.702 at S=8; Matched declines to ≈0.696 at S=64 |
| Random-iid | All architectures ≈ 0.500 |

## Equal-S comparison

At the representative controlled comparison:

| Process | S | Matched | Random | Winner |
|---|---:|---:|---:|---|
| Periodic-4 | 8 | 1.000 | 0.844 | Matched |
| Markov-2 | 4 | 0.823 | 0.634 | Matched |
| Thue-Morse | 8 | 0.500 | 0.632 | Random |
| HMM | 8 | 0.702 | 0.613 | Matched |

Paired t-test results reported from the run: Periodic-4 t=29.4, p<0.001; Markov-2 t=25.1, p<0.001; Thue-Morse t=-15.2, p<0.001; HMM t=8.7, p<0.001.

## Important interpretation

The Thue-Morse result does **not** prove that random memory is intrinsically superior. It demonstrates that the chosen "matched" representation — a simple cyclic position counter — is not sufficiently informative for the tested Thue-Morse prediction task. Random FSMs at larger S can accidentally or implicitly encode useful predictive partitions.

Likewise, the HMM result shows that theoretical structural correspondence is not enough: discretization and sparse state occupancy can create implementation loss.

## Next step

Ω-MEM-5 is conditional. Before launching it as a definitive conclusion, H-MEM-2.3 should receive an independent replication or a formal theoretical analysis. The central next question is whether a learner can discover a minimal sufficient predictive state without hand-designing the process-specific architecture.

## Archive policy

Ω-MEM-4 remains preserved as exploratory evidence and is not replaced. Ω-MEM-4R is a separate corrected replication motivated by the audit of Ω-MEM-4.
