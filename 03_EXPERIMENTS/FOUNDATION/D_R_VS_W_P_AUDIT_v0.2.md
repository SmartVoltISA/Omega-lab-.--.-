# D+R vs W+P — AUDIT v0.2

Date: 2026-08-28
Status: CORRECTION / EXPERIMENTAL

## Audit finding

The v0.1 evaluator is executable Python, but its classification table hard-codes dependency assumptions and therefore is NOT an independent proof of reduction. In particular, it declares several D+R capabilities DERIVED without executing a formal derivation, and declares W+P dependencies from a pre-specified dependency map.

Therefore the previous conclusion that D+R is the stronger reduction candidate is RECLASSIFIED as **UNPROVEN**.

## What remains valid

1. The primitive-budget idea is useful.
2. Hidden dependency leakage must be counted.
3. A capability must be constructible from the declared inventory, not merely described in prose.
4. Renaming a primitive must not change dependency classification.
5. Canonical status must not be updated from this experiment.

## Required correction

The next evaluator must use an explicit term language and constructor rules. A capability receives credit only when a term can be generated from the primitive grammar and all referenced symbols are present in the declared inventory or are themselves derived by an already accepted constructor.

No capability may be labelled DERIVED merely because a human-written rule says it is derived.

## Minimal formal target

Represent terms as:

- Atom(x)
- Pair(x,y)
- Rel(x,y)
- Select(x,S)
- Restrict(x,C)
- Next(s,a)
- Trace(s,h)
- Cycle(s,g)

Each constructor declares its required primitive symbols. The evaluator computes transitive dependency closure. Any banned primitive appearing in the closure is IMPORTED.

## Critical issue to resolve

The comparison cannot be made fairly until the semantics of "selection" and "prohibition" are fixed. Otherwise W/P can hide distinction or relation in the meanings of W and P, while D/R can hide selection in an unspecified rule.

Therefore v0.2 must test at least two semantics:

A. extensional / purely formal semantics;
B. operational semantics with explicit input, output and transition objects.

If the outcome changes between A and B, the result is semantic-model dependent and cannot support a fundamental claim.

## Current conclusion

**D+R stronger than W+P: UNKNOWN.**

The experiment has successfully identified the methodological requirement: reduction claims need executable derivation plus dependency closure, not a hard-coded classification table.

Next: implement the term-language evaluator and run both semantics with the same capability suite T1–T7.
