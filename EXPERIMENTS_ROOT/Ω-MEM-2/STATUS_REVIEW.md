# Ω-MEM-2 — Status Review

Date: 2026-08-10

## Rule
The original experiment, code, outputs and interpretations are preserved. This document records later audits and does not delete historical conclusions.

## H-MEM-2
**Formulation:** Memory can provide a system with an advantage in predicting the future.

**Current status: PARTIALLY CONFIRMED.**

Evidence:
- Cyclic structured memory does not improve prediction for the earlier tested Markov-like process.
- Random memory showed positive prediction advantage in one earlier tested setup, demonstrating the need for matched-size and structure controls.
- Cyclic structured memory improves prediction for the tested XXYY periodic process.
- Context memory improves prediction for Markov-like processes.
- Ω-MEM-3 reproduced predictive advantages on Periodic-4 and an HMM-like process and retained the Random-iid negative control.

This establishes that memory *can* be predictive in tested models. It does not establish a universal law.

## H-MEM-2.1
**Original formulation:** Prediction advantage occurs if and only if the memory-update structure matches the structure of the predicted pattern.

**Current status: REFINED.**

Ω-MEM-3 showed support on P1/P2/P4 but a reproducible counterexample on P3 Thue-Morse for the tested parity-tracker "matched" architecture. Therefore the universal claim is not supported.

The current refinement is H-MEM-2.2: structural correspondence may matter **conditional on sufficient expressive capacity**.

## ERR-MEM-2b-1
The periodic test contains `for offset in range(4)`, but `offset` is never applied to the generated pattern. Therefore the reported four repetitions are not four phase-offset conditions; they are repetitions of the same XXYY sequence.

## ERR-MEM-2c-1
An earlier report stated that intervention on the periodic pattern reduced accuracy from approximately 0.75 to 0.50. The directly supplied Ω-MEM-2c code/output instead reports approximately 0.752 before reset and 0.747 after reset. The causal intervention therefore does **not** reproduce the earlier claimed 0.25 drop.

Status of the causal claim: **NOT CONFIRMED / NEEDS RETEST**.

The earlier result remains in the historical record and is not deleted.

## ERR-MEM-2d-1
The supplied Ω-MEM-2d code prints `acc0` after the seed loop, meaning the reported M0 baseline is the value from the final seed, not the mean baseline over all 50 seeds. The reported context-memory advantage therefore requires a corrected paired baseline calculation.

## Ω-MEM-3 corrections

1. The previous P2 generator labelled Markov-2 actually depends only on the previous symbol; it is first-order Markov.
2. The previous P4 "matched HMM estimator" is not a Bayesian belief filter and is effectively last-observation context.
3. P3 Thue-Morse demonstrates insufficiency of the tested parity tracker but does not establish an O(log n) lower bound.
4. Hand-designed matched architectures confound structural match with expressive capacity.

## Required next checks

1. Re-run periodic intervention with a strict causal protocol and multiple phase/reset positions.
2. Correct Ω-MEM-2d so context-memory accuracy is compared against the paired M0 baseline for every seed.
3. Test multiple periodic patterns and multiple Markov orders.
4. Add permutation/null controls.
5. Use true Markov-2 and genuine HMM belief-state architectures.
6. Sweep expressive capacity and state size.
7. Only then consider strengthening H-MEM-2.2.
