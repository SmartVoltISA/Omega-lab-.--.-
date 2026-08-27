# EXP-C1-016 — Magic-Square Invariant / 3301↔1033

**Status:** CORRECTED — strong structural clue; no cryptographic key inferred.
**Date:** 2026-08-28

## Observation

The 5x5 matrix reproduced in Liber Primus / the 2014 puzzle is:

272 138 341 131 151
366 199 130 320 18
226 245 91 245 226
18 320 130 199 366
151 131 341 138 272

Every row, column and the two main diagonals sum to 1033. The same matrix is independently present in archived OOB material and in Liber Primus. The matrix is centrosymmetric: M[i,j] = M[4-i,4-j].

## Correction to previous lab note

The previous note incorrectly stated that the third historical square had magic constant 1033. Direct arithmetic verification shows:

- historical 5x5 square #1: constant **3301**
- historical 7x7 square #2: constant **1033**
- Liber Primus / historical 5x5 square #3: constant **1033**

The published 2014 `magicsquares.txt` reproduces all three matrices, and independent calculation gives the constants above. Therefore the claim "three squares: 3301, 1033, 1033" is the correct one.

## What this proves

- The LP 5x5 matrix has invariant 1033.
- The same matrix appears in distinct representation channels (OOB data and LP), giving a genuine cross-channel invariant.
- 1033 is present as the magic constant of both the 7x7 historical square and the LP 5x5 square.

## What it does NOT prove

- 1033 is not proven to be a cryptographic key.
- 3301 -> 1033 is not proven to be an author-intended transformation merely because 1033 is a digit reversal of 3301.
- There is no demonstrated endpoint/address derived from this observation.

## Graph interpretation

Treat the repeated LP matrix as a bridge node:

OOB representation -> MAGIC-SQUARE MATRIX <- LP representation
                                  |
                                  +-> invariant = 1033
                                  |
                                  +-> 2014 magic-square family

The bridge is stronger evidence for a repeated representation invariant than for a particular cipher.

## Next falsifiable tests

1. Compare all three historical squares under symmetry, row/column sums, center values, and digit-reversal relations.
2. Test whether 3301 and 1033 act as labels, checksums, constants, or transformations elsewhere in the same 2014 chain.
3. Verify exact provenance of the LP matrix in the archived OOB artifacts.
4. Do not promote 3301↔1033 to an operational key unless it predicts an independent downstream value.
