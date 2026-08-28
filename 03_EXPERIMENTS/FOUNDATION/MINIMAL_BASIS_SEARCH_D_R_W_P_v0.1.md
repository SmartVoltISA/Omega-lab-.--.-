# MINIMAL BASIS SEARCH — D+R vs W+P v0.1

Status: WORKING EXPERIMENT / NOT CANONICAL
Date: 2026-08-28

## Objective
Find minimal primitive sets sufficient to construct target capabilities without predeclaring their dependency sets.

## Method
Enumerate candidate primitive budgets from {D,R,W,P} and constructor grammars. For each budget, enumerate finite terms up to bounded depth. Evaluate only syntactic/operational properties defined by the target capability itself. Record the smallest budget for which a witness term exists.

## Target capability witnesses

T1: at least two values that the evaluator can distinguish.
T2: a stable boundary/identity predicate over values.
T3: an executable transition accepted for one case and rejected for another.
T4: a deterministic selection from at least two available candidates.
T5: two successive configurations with a detectable difference.
T6: a retained prior configuration that can affect a later transition.
T7: a repeatable transition cycle with an explicit stopping condition.

## Anti-circularity rules

1. No target capability may name a primitive it is supposed to discover as necessary.
2. Capability predicates operate only on constructed terms and execution traces.
3. Renaming D/R/W/P must preserve results.
4. A witness must be replayable from the declared budget.
5. Semantic conveniences such as “choice”, “state”, “history”, “identity” are forbidden inside primitive definitions.

## Search order

Enumerate all subsets of {D,R,W,P}, beginning with cardinality 0, then 1, 2, 3, 4.
For each subset:
- enumerate constructor programs up to depth 6;
- execute against finite test domains;
- retain the shortest witness per capability;
- compute primitive dependency closure from the actual syntax;
- reject witnesses containing undeclared primitives or semantic aliases.

## Decision

The output is an operational minimal-basis result only. It does not establish metaphysical fundamentality.

A result is interesting when:
- one budget constructs a capability without another budget’s primitive;
- the same capability cannot be constructed by a smaller budget;
- the result survives renaming, leakage and reverse-replay controls.

## Expected output

CSV/JSON evidence containing:
- capability;
- minimal budget(s);
- witness program;
- depth;
- dependency closure;
- control results;
- status.

## Current status

Protocol written. Evaluator implementation and independent execution remain required. No fundamental claim is made yet.
