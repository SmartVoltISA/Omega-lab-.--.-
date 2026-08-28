# MINIMAL BASIS SEARCH EXECUTOR AUDIT v0.1

Status: AUDIT / NOT EVIDENCE
Date: 2026-08-28

## Finding

The first bounded executor must NOT be treated as an independent minimal-basis proof. Its witness inventory is manually enumerated, so the search can only select among supplied witness patterns. It does not synthesize arbitrary programs from primitive semantics.

## Consequence

Any minima produced by that executor are provisional and cannot establish necessity or sufficiency.

## Required correction

The next executor must contain:

1. a tiny formal operational language;
2. semantics for each primitive operation;
3. a grammar capable of generating programs up to depth N;
4. an evaluator for target capabilities defined from observable traces;
5. exhaustive enumeration of programs modulo alpha-renaming;
6. dependency extraction from syntax and execution;
7. leakage detection for banned semantic aliases;
8. independent property-based controls;
9. held-out capability instances where applicable.

## Important distinction

A manually supplied witness can demonstrate POSSIBILITY of a construction, but cannot establish MINIMALITY.

A failed witness search at bounded depth can establish only:

"not found within this language/depth budget."

It cannot establish impossibility.

## Rule

Do not promote any result from the current executor to VERIFIED or CANONICAL.
