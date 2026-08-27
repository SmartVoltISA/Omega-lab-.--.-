# EXP-C1-016 — Magic-Square Invariant / 3301↔1033

**Status:** STRONG PLAUSIBLE structural clue; no cryptographic key inferred.
**Date:** 2026-08-28

## Observation

The 5x5 matrix reproduced in Liber Primus / the 2014 puzzle is:

272 138 341 131 151
366 199 130 320 18
226 245 91 245 226
18 320 130 199 366
151 131 341 138 272

Every row, column and the two main diagonals sum to 1033. The same matrix was independently recovered from out-of-band data and from the Liber Primus image. The matrix is also centrosymmetric: M[i,j] = M[4-i,4-j].

## Critical new observation

Historical 2014 material contains three submitted/hidden magic squares. Their magic constants are:

- order 5: 3301
- order 7: 1033
- order 5: 1033

The Liber Primus matrix is the third of these and has constant 1033. Thus 1033 is not merely a row-sum accident; it recurs as a magic-square invariant in the 2014 puzzle ecosystem. 1033 is the decimal digit reversal of 3301.

## What this proves

- The 1033 constant is structurally tied to the known 2014 material.
- The matrix is not random numeric noise.
- The same object appears in distinct representation channels (OOB data and LP image), giving a genuine cross-channel invariant.

## What it does NOT prove

- 1033 is not yet proven to be a cryptographic key.
- 3301 -> 1033 is not proven to be an author-intended transformation merely because it is digit reversal.
- No endpoint/address is derived from this observation yet.

## Graph interpretation

Treat the repeated matrix as a bridge node:

OOB representation -> MAGIC-SQUARE MATRIX <- LP representation
                                  |
                                  +-> invariant = 1033
                                  |
                                  +-> historical 3301-linked square family

This is stronger evidence for a repeated representation invariant than for a particular cipher.

## Next falsifiable tests

1. Compare all three historical magic squares under symmetry, row/column sums, center values, and digit-reversal relations.
2. Test whether 3301 and 1033 act as labels, checksums, constants, or transformations elsewhere in the same 2014 chain.
3. Search for the matrix as an exact byte/number sequence in the archived OOB artifacts and verify provenance.
4. Do not promote 3301↔1033 to an operational key unless it predicts an independent downstream value.
