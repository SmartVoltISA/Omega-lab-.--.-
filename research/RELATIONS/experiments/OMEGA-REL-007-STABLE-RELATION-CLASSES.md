# Ω-REL-007 — Stable Relation Classes

Date: 2026-08-13
Status: EXECUTED AS CLASSIFICATION ANALYSIS — PARTIAL RESULT

## Historical numbering

Ω-REL-005 and the existing Ω-REL-006 history are preserved unchanged.

The present investigation is therefore registered as Ω-REL-007.

## Question

After Ω-REL-006 showed that stable relational invariants can emerge without an explicitly stored relation variable, how many distinct stable relational states are available in the tested 8-state pair model?

## Model inherited from Ω-REL-006

`A, B ∈ {0,1,2,3,4,5,6,7}`

Observed relational invariant:

`D = (B - A) mod 8`

Therefore the complete mathematical state space of the observable relative relation contains exactly eight possible values:

`D* ∈ {0,1,2,3,4,5,6,7}`

## Important distinction

Eight possible values does NOT yet mean eight fundamental relation types.

The values may be equivalent under symmetries, may form larger classes, or may differ only by representation.

Therefore this experiment separates:

1. number of possible observable invariant values;
2. number of dynamically realized values;
3. number of symmetry-equivalent classes;
4. number of genuinely distinct relation classes.

## Result that follows directly from the model

The observable invariant `D` has exactly 8 possible values.

This is a complete enumeration of the chosen state space, not a claim about nature or about the fundamental Ω ontology.

## Symmetry analysis

The transformation

`A → (A+k) mod 8`

`B → (B+k) mod 8`

leaves `D` unchanged.

A reversal of the ordered pair changes:

`D → (-D) mod 8`.

Therefore, if A/B reversal is treated as an equivalence, the eight values reduce to the classes:

- `{0}`
- `{4}`
- `{1,7}`
- `{2,6}`
- `{3,5}`

which gives 5 symmetry classes under reversal.

This is a mathematical classification of the representation, not yet a dynamical result.

## Stronger unresolved question

The registered Ω-REL-006 result reports 2024 successful rules out of 6561. The available record does not contain the executable rule-generation source needed to independently reconstruct the exact empirical distribution of the 2024 successes by `D*`.

Therefore this document deliberately does NOT claim that all eight values were dynamically realized, nor does it assign the 2024 successes to classes without rerunning the exact Ω-REL-006 generator.

## Required next execution

Recover or recreate the exact Ω-REL-006 rule generator from its executable source, then for every successful rule:

1. record the final stable `D*`;
2. count unique `D*` values;
3. count frequencies;
4. group values under pair reversal;
5. test whether different `D*` values have distinguishable dynamical properties;
6. determine whether any classes can be merged without loss of predictive behavior.

## Current conclusion

The current model admits exactly 8 observable relative-state values and 5 classes if A/B reversal is declared an equivalence.

The number of dynamically realized and genuinely independent relation classes remains unresolved.

`No unsupported empirical distribution is claimed.`
