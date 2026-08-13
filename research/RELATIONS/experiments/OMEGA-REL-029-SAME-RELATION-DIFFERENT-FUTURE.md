# Ω-REL-029 — Same Relation, Different Future

Date: 2026-08-13
Status: RESULT REGISTERED

## Question

Does the instantaneous relation R=(ΔA,ΔB) alone determine the next relation, or is the absolute state of the endpoints additionally required?

## Model

A,B ∈ {0,1}.

All 256 deterministic transition rules over the four joint states are exhaustively enumerated.

For each transition:

R_t = (A'−A, B'−B)

Then the next relation R_{t+1} is computed from the next transition of the reached state.

## Test

Find cases where two different source states produce the same current relation R, but their reached states produce different next relations under the same deterministic rule.

## Result

Exactly 56 deterministic rules contain at least one such ambiguity.

Therefore the instantaneous relation R=(ΔA,ΔB) is NOT sufficient to determine the next relation in the full binary model.

A concrete example is:

(0,0) → (1,0)

and

(0,1) → (1,1)

Both have:

R=(+1,0).

However, because their reached absolute states differ, the following transition can produce different R_{t+1}.

## Interpretation

The result does NOT establish that the relation has memory.

It establishes a narrower fact:

> The change vector R loses information about the absolute endpoint state whenever a component does not change.

Thus two identical instantaneous relations can have different futures because they originate from different absolute endpoint states.

## Important distinction

Do not collapse this lost information into a new relational property prematurely.

The current result separates two descriptions:

1. relation/change: R=(ΔA,ΔB)
2. endpoint state: (A,B)

The deterministic transition law acts on the complete endpoint state, while R is a derived observation of one transition.

## Conclusion

Within this model:

`R_t` alone is insufficient as a complete state variable.

`(A_t,B_t,R_t)` contains redundant information because R_t is derived from the transition, while `(A_t,B_t)` is sufficient for the deterministic rule.

Therefore the next investigation must determine whether a genuinely relational state variable can be defined that is independent of the absolute endpoint coordinates, rather than simply reintroducing endpoint state under another name.

## Status

Result confirmed by exhaustive enumeration of all 256 deterministic rules. Previous experiment files are not modified.
