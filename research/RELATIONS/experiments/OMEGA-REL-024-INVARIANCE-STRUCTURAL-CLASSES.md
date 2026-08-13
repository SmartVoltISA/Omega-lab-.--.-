# Ω-REL-024 — Invariance of Structural Relation Classes

Date: 2026-08-13
Status: EXECUTED — RESULT REGISTERED

## Question

Ω-REL-023 proposed four structural classes in the minimal binary model:

1. neither endpoint changes;
2. exactly one endpoint changes;
3. both endpoints change in the same sign direction;
4. both endpoints change in opposite sign directions.

Ω-REL-024 tests whether these four structural classes survive when the carrier state space is enlarged.

## Carrier model

For each N >= 2, endpoint changes are taken from:

`Δ ∈ {-(N-1), ..., -1, 0, +1, ..., +(N-1)}`

For a pair `(ΔA, ΔB)`, classification is based only on zero/nonzero status and relative sign:

- REST: ΔA=0 and ΔB=0
- SINGLE: exactly one of ΔA, ΔB is nonzero
- SAME: both nonzero and ΔA*ΔB > 0
- OPPOSITE: both nonzero and ΔA*ΔB < 0

Magnitude is deliberately ignored.

## Exhaustive counts

| N | REST | SINGLE | SAME | OPPOSITE | Total |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 4 | 2 | 2 | 9 |
| 3 | 1 | 8 | 8 | 8 | 25 |
| 4 | 1 | 12 | 18 | 18 | 49 |
| 5 | 1 | 16 | 32 | 32 | 81 |
| 6 | 1 | 20 | 50 | 50 | 121 |
| 7 | 1 | 24 | 72 | 72 | 169 |
| 8 | 1 | 28 | 98 | 98 | 225 |
| 9 | 1 | 32 | 128 | 128 | 289 |
| 10 | 1 | 36 | 162 | 162 | 361 |

The total is `(2N-1)^2`, as expected.

## Result

All four structural classes exist for every tested `N >= 2`.

Therefore the four-way structural partition is invariant under enlargement of the carrier state space **within this classification scheme**.

The result is not dependent on the binary choice N=2.

## Important limitation

This does NOT establish four fundamental Ω relation types.

The four classes were defined by a particular abstraction of endpoint changes: zero/nonzero and sign agreement. The experiment demonstrates invariance of that structural partition, not ontological fundamentality.

It also does not determine whether additional relational properties (magnitude, history, persistence, directionality, cost, etc.) are independent dimensions.

## Key observation

The raw number of possible endpoint-change pairs grows as:

`(2N-1)^2`

while the proposed structural partition remains exactly four classes.

This cleanly separates:

- carrier-state cardinality;
- magnitude of change;
- structural relation class.

## Current working map

`carrier states → changes → structural class`

with structural class in:

`{REST, SINGLE, SAME, OPPOSITE}`.

## Next question

Ω-REL-025 should test whether these four structural classes remain distinct under behavioral intervention, rather than merely by instantaneous classification.

Specifically: can one class be transformed into another without passing through an observable intermediate distinction, and do the four classes produce different future behavior under identical interventions?

## Reproducibility

The enumeration is finite and exhaustive for each tested N. No stochastic sampling was used.

Tested N: 2 through 10.

## Final status

The four structural classes are empirically invariant across N=2..10 under the declared abstraction. They remain a candidate structural basis, not a fundamental Ω ontology.
