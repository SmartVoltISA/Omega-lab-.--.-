# EXP-C1-017 — Matrix type and invariant audit

Date: 2026-08-28
Status: confirmed structural result / M3 mechanism candidate unverified

## Question
Do the Liber Primus numerical matrices share one invariant, or does the operator change with matrix type?

## Corpus
Four matrices are relevant:
- M1: 5×5 matrix from the "Some Wisdom" page.
- M2: 5×5 matrix from the "An Instruction" page.
- M7: 7×7 matrix included in the historical magic-square payload.
- M3: 4×4 Page 15 matrix.

The historical payload independently contains M1, M2 and M7. M3 is separately recorded as the Page 15 matrix.

## Strict results
### M1
- shape: 5×5
- every row sum = 1033
- every column sum = 1033
- both main diagonals = 1033
- 180° rotational symmetry = TRUE
- trace = 1033

### M2
- shape: 5×5
- every row sum = 3301
- every column sum = 3301
- both main diagonals = 3301
- 180° rotational symmetry = TRUE
- trace = 3301

### M7
- shape: 7×7
- every row sum = 1033
- every column sum = 1033
- both main diagonals = 1033
- 180° rotational symmetry = TRUE
- trace = 1033

Therefore M1 and M7 share the same magic constant 1033 while M2 has magic constant 3301. This is stronger than a generic observation that the matrices are merely symmetric.

### M3
- shape: 4×4
- row sums = 12670, 12713, 12350, 8250
- column sums = 14340, 11021, 10454, 10168
- main diagonals = 11673 and 14146
- 180° rotational symmetry = FALSE
- trace = 11673

M3 is therefore NOT a magic square and should not be forced into the M1/M2/M7 invariant class.

## Structural interpretation
The data support a type distinction:

MAGIC-SQUARE TYPE → global constant + rotational symmetry
PAGE-15 4×4 TYPE → different construction rule

This does not prove that the author intentionally defined a state machine, but it is a stronger model than treating every matrix as the same object.

## Page-15 candidate rule
External solver material records the candidate relationship that the M3 spiral may be generated from `abs(3301 - primes[fib[i]])`, and corresponding code implements Page15FiboPrimes / Page15FuncPrime transformations. This remains a candidate reconstruction, not an independently verified author rule.

## Important correction
Earlier notes incorrectly recorded M3 trace as 10673 and factored it as 13×821. The actual M3 trace from the source matrix is 11673. The 10673/821 statement is therefore RETRACTED.

## Decision
1. MAGIC-INVARIANT = CONFIRMED for M1, M2 and M7.
2. M1 and M7 share constant 1033; M2 uses 3301.
3. M3 belongs to a different structural class.
4. Do not use the M3 candidate formula as a decryption key until independently reproduced on the complete spiral/order.

## Next test
Construct a position-aware transition audit:
1. generate the exact clockwise spiral order of M3;
2. compare each element with prime indices and Fibonacci-indexed primes;
3. test `abs(3301-p)` and `abs(3301-p_fib)` against every position;
4. require exact reproduction of all 16 cells with no free parameters;
5. compare against shuffled/null matrices preserving the same value multiset.

## Research principle
Do not collapse distinct structural types into one hypothesis. Preserve corrections and promote only reproducible invariants.