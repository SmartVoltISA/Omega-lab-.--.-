# EXP-C1-018 — Magic-Square Relations / 3301–1033

**Status:** TESTABLE STRUCTURAL HYPOTHESIS
**Date:** 2026-08-28

## Verified inputs

The archived 2014 `magicsquares.txt` contains three squares:

1. 5x5 square with magic constant 3301.
2. 7x7 square with magic constant 1033.
3. 5x5 square reproduced in Liber Primus with magic constant 1033.

Independent arithmetic confirms these constants. The LP square is also centrosymmetric and is reproduced in OOB material.

## Important correction

Do not infer `3301 -> 1033` merely from decimal reversal. That is an observation requiring predictive evidence, not an established transformation.

## Research question

Does a deterministic transformation or shared invariant connect the 3301 square, the 1033 7x7 square, and the LP 1033 square?

## Tests

A. Compare normalized symmetry classes.
B. Compare centers and symmetry axes.
C. Compare row/column/diagonal sums after normalization.
D. Compare element multiplicities and sorted spectra.
E. Test digit reversal only as a null candidate, not as an assumed rule.
F. Test whether constants 3301/1033 appear as labels, filenames, payload identifiers, or cryptographic parameters in the same 2014 chain.
G. Require an independently predicted downstream value before promoting any relation to an operational rule.

## Null model

For each candidate relation, compare against equally-sized random integer matrices constrained to the same row/column sum and symmetry class where feasible. A relation is interesting only if its observed preservation is substantially less likely under the null.

## Current conclusion

The repeated LP matrix is a genuine cross-channel invariant. A common generator for the three historical squares remains UNKNOWN. The graph interpretation remains a hypothesis, not a fact.
