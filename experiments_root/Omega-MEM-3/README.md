# Ω-MEM-3 — Generalization of H-MEM-2.1

**Date:** 2026-08-10  
**Status:** COMPLETED  
**Hypothesis:** H-MEM-2.1  
**Updated hypothesis:** H-MEM-2.2

## Question

Is the prediction advantage of memory caused by structural correspondence between memory update and process pattern, or was the earlier result an artifact of the selected processes?

## Protocol

- 5 process classes: Periodic-4, Markov-like process, Thue-Morse, Hidden-State HMM, Random-iid.
- 5 memory architectures: Matched, Mismatched cyclic, Random finite-state, Context, Baseline.
- sequence length 2000
- burn-in 100
- train/test 1000/1000
- 30 seeds
- permutation trials 100

## Main results

| Process | Matched | Mismatched | Random | Context | Baseline | Status |
|---|---:|---:|---:|---:|---:|---|
| P1 Periodic-4 | 1.0000 | 0.7501 | 0.7238 | 0.9994 | 0.5005 | CONFIRMED for tested architecture |
| P2 Markov-like | 0.6787 | 0.4908 | 0.5497 | 0.6787 | 0.4835 | CONFIRMED for tested architecture |
| P3 Thue-Morse | 0.5555 | 0.5555 | 0.5763 | 0.6676 | 0.5001 | COUNTEREXAMPLE |
| P4 HMM-like | 0.7045 | 0.4990 | 0.5789 | 0.7041 | 0.4935 | CONFIRMED for tested architecture |
| P5 Random-iid | 0.4929 | 0.4929 | 0.4980 | 0.4939 | 0.4965 | Negative control OK |

Permutation means for Matched:

- P1: 1.000 vs 0.502
- P2: 0.679 vs 0.500
- P3: 0.556 vs 0.504
- P4: 0.705 vs 0.501
- P5: 0.493 vs 0.497

## Observation

The matched architecture is not universally superior. Thue-Morse is a reproducible failure case for the particular parity-tracker architecture used.

## Interpretation

The most conservative interpretation is that architectural expressiveness matters in addition to structural correspondence.

## Important corrections

1. P2 was labelled Markov-2, but its generator depended only on the immediately previous symbol. It should be treated as Markov-1 until corrected.
2. The P4 "matched HMM estimator" was a two-state last-observation rule, not a genuine Bayesian belief filter.
3. The P3 result does not establish that Thue-Morse requires O(log n) memory. Its minimum required expressive capacity remains unknown.
4. The hand-designed "Matched" architectures confound structural match with implementation quality.

## Status change

H-MEM-2.1: PROVISIONALLY CONFIRMED → REFINED.

H-MEM-2.2: OPEN.

## Next experiment

Ω-MEM-4 will separate structural match from expressive capacity using controlled state-size sweeps, a true Markov-2 generator, a genuine HMM belief state, Thue-Morse capacity sweeps, entropy metrics and strict intervention.
