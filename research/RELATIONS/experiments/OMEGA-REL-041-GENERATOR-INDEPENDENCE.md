# Ω-REL-041 — Generator Independence

Date: 2026-08-13
Status: RESULT REGISTERED

## Question
Test whether three operation types are independently necessary to generate the full deterministic transformation monoid on finite state spaces.

## Generators

Use:

- C — cyclic permutation of all states;
- P — transposition of two states;
- E — rank-(N-1) singular map merging one state into another while fixing the rest.

## Full closure

For N=3:

| Generators | Reachable transformations |
|---|---:|
| C,P,E | 27 = 3^3 |
| P,E | 4 |
| C,E | 24 |
| C,P | 6 |

For N=4:

| Generators | Reachable transformations |
|---|---:|
| C,P,E | 256 = 4^4 |
| P,E | 4 |
| C,E | 128 |
| C,P | 24 |

## Result

For N=3 and N=4, the chosen three generator types each contribute behavior that cannot be recovered from the other two in this representation.

- Without E, only permutations are generated; for N=4 this is exactly 4! = 24.
- Without C, the reachable set collapses to 4 transformations for both tested N.
- Without P, C+E generates a large but incomplete subset: 24/27 for N=3 and 128/256 for N=4.

Therefore the tested generating set is irredundant for the full transformation monoid at N=3 and N=4.

## Interpretation boundary

This does NOT establish three fundamental Ω relations. C, P and E are operation classes in a chosen finite-state mathematical model.

The result establishes only operational independence of these three generator roles within the tested model.

## Next question

Ω-REL-042 should classify these generator roles by invariant properties rather than by their names, especially:

1. reversibility;
2. preservation or reduction of the number of distinguishable states;
3. permutation versus non-permutation behavior.

## Reproducibility

The closure was computed by exhaustive composition until no new transformations appeared.
