# EXP-C1-004 — Permutation-first attack on LP2

**Date:** 2026-08-28
**Status:** ACTIVE / hypothesis-testing

## New evidence checked

The current community master tracker reports:
- P21–P30 remain scrambled despite high IoC artifacts;
- P31–P54 have a Caesar layer but remain scrambled;
- hill-climbing keys that produced high IoC were explicitly identified as artifacts, not plaintext;
- exhaustive LFSR(2/3) tests did not solve the unsolved pages.

Therefore the next experiment must not repeat keyword, hill-climbing, or small-LFSR attacks.

## Hypothesis family

P19 explicitly yields the clue:

`REARRANGING THE PRIMES NUMBERS WILL SHOW A PATH TO THE DEOR`

Test whether "rearranging" refers primarily to a permutation/transposition of positions rather than a direct running-key cipher.

### Candidate permutation families

1. prime ordinal order;
2. reverse prime ordinal order;
3. Fibonacci-indexed prime order;
4. Lucas-indexed prime order;
5. Euler-totient order;
6. prime-gap order;
7. missing-prime ordinal block (21..200);
8. reverse missing-prime block;
9. compositions of the above with reversal/rotation only.

## Acceptance test

A candidate permutation is NOT accepted because it produces English on one page.

It must:

1. reproduce an already verified structural/plaintext constraint;
2. work without page-specific arbitrary tuning;
3. improve multiple pages or independent fragments;
4. outperform randomized/shuffled controls;
5. remain reversible and explicitly documented.

## Important negative control

The reported missing-prime interval is 73..1223, i.e. consecutive primes from the 21st through the 200th prime. Its length alone is not evidence of a 180-degree/Fibonacci mechanism. The numerical coincidence is recorded only as a hypothesis generator.

## Current status

- P19 prime-rearrangement clue: PROVED as plaintext.
- P20 partial prime-stream result: PROVED as a reported reproducible result, but full mechanism UNKNOWN.
- Missing-prime block: PROVED as an observed archive artifact; causal role UNKNOWN.
- Missing-prime block = P20 permutation: UNKNOWN.
- Fibonacci = P20 permutation: UNKNOWN.

## Next experiment

Build a permutation-only evaluator against the known P20 partial plaintext constraints and P21–P30 structural constraints. Reject any family that cannot explain known data before applying it to unknown pages.