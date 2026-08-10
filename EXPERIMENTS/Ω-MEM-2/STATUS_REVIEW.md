# Ω-MEM-2 — Status Review

Date: 2026-08-10

## Rule
The original experiment, code, outputs and interpretations are preserved. This document records a later audit and does not delete historical conclusions.

## H-MEM-2
**Formulation:** Memory can provide a system with an advantage in predicting the future.

**Current status: PARTIALLY CONFIRMED.**

Evidence:
- Cyclic structured memory does not improve prediction for the tested Markov-2 process.
- Random memory shows positive prediction advantage for the tested Markov-2 generator, including cross-seed testing.
- Cyclic structured memory improves prediction for the tested XXYY periodic process.
- Context memory (last input) improves prediction for Markov-2.

This establishes that memory *can* be predictive in the tested models. It does not establish a universal law.

## H-MEM-2.1
**Original formulation:** Prediction advantage occurs if and only if the memory-update structure matches the structure of the predicted pattern.

**Current status: PROVISIONAL / NEEDS GENERALIZATION.**

Reason: the experiments show compatibility between memory structure and pattern can produce advantage, but the universal "if and only if" claim has not been established. Random memory also produced an advantage in the tested Markov-2 setup.

## ERR-MEM-2b-1
The periodic test contains `for offset in range(4)`, but `offset` is never applied to the generated pattern. Therefore the reported four repetitions are not four phase-offset conditions; they are repetitions of the same XXYY sequence.

## ERR-MEM-2c-1
An earlier report stated that intervention on the periodic pattern reduced accuracy from approximately 0.75 to 0.50. The directly supplied Ω-MEM-2c code/output instead reports approximately 0.752 before reset and 0.747 after reset. The causal intervention therefore does **not** reproduce the earlier claimed 0.25 drop.

Status of the causal claim: **NOT CONFIRMED / NEEDS RETEST**.

The earlier result remains in the historical record and is not deleted.

## ERR-MEM-2d-1
The supplied Ω-MEM-2d code prints `acc0` after the seed loop, meaning the reported M0 baseline is the value from the final seed, not the mean baseline over all 50 seeds. The reported context-memory advantage therefore requires a corrected paired baseline calculation.

## Required next checks
1. Re-run periodic intervention with a strict causal protocol and multiple phase/reset positions.
2. Correct Ω-MEM-2d so context-memory accuracy is compared against the paired M0 baseline for every seed.
3. Test multiple periodic patterns and multiple Markov orders.
4. Add permutation/null controls.
5. Only then consider strengthening H-MEM-2.1.
