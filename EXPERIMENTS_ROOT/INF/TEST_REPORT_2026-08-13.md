# Ω-INF-1 — Test report

**Date:** 2026-08-13

## Regression tests

The first draft of the regression test used a full reversal as its permutation control. That test exposed an important issue: reversal can preserve the set of observed bigrams for some sequences, so it is not a reliable generic intervention for this metric.

The test was corrected to use a deterministic pseudorandom permutation with seed `314159`.

### Final result

**4/4 tests passed.**

Validated controls:

1. permutation preserves character multiplicities;
2. permutation preserves sequence length;
3. symbol entropy is invariant under permutation;
4. at least one organization-sensitive metric (unique bigrams) changes under the deterministic intervention;
5. the main Ω-INF-1 run is deterministic for seed `20260813` and produces exactly 100 shuffled controls.

## Why the failed first test is retained

The initial test failure is not deleted from the research history. It revealed that the chosen control transformation was weaker than assumed for the selected metric.

This is exactly the Ω methodological rule: a failed test or methodological defect is part of the evidence chain and must be corrected explicitly rather than silently removed.
