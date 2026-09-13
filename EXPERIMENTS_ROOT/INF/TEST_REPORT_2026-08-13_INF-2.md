# Ω-INF-2 — Test Report

**Date:** 2026-08-13

## Automated checks

The regression suite checks:

1. all interventions preserve character count;
2. all interventions preserve the exact character multiset;
3. symbol entropy is invariant under permutation;
4. T1 increases the selected low-level relational metrics relative to T0;
5. the experiment is deterministic for the fixed seed.

## Result

**5/5 checks passed in local execution.**

## Methodological note

The test suite verifies implementation properties. It does not verify the philosophical interpretation of the experiment.

In particular, passing the tests does not establish that a semantic quantity called "information" has been measured. It establishes that the programmed interventions and selected metrics behave as specified.

## Negative/control finding

T2, T3 and T4 produced only small changes in the selected low-level metrics. This is retained as evidence against the stronger interpretation that any meaningful destruction of textual organization must cause a large change in these metrics.
