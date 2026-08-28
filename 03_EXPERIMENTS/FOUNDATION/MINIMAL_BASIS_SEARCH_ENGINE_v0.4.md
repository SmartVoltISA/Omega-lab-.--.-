# MINIMAL BASIS SEARCH ENGINE v0.4

Status: WORKING EXPERIMENT / NOT CANONICAL
Date: 2026-08-28

## Purpose
Remove semantic capability labels from the generator/evaluator. The search produces raw finite traces from neutral rewrite systems. A separate observer classifies traces using independently specified predicates.

## Separation of concerns

Generator knows only:
- symbols;
- ordered tuples;
- rewrite rules;
- bounded execution.

Generator does NOT know:
- distinction;
- choice;
- state;
- memory;
- cycle;
- will;
- prohibition.

Observer receives only a trace and a capability predicate. Capability predicates are maintained outside the generator and are tested against independently generated null traces.

## Leakage controls

1. Primitive names are randomly alpha-renamed before generation.
2. Generator source is scanned for target capability words.
3. Observer source is separated from generator source.
4. Permutation control randomizes symbol identities while preserving trace length.
5. Null control generates traces with identical size/depth distributions but independent rewrite rules.
6. Replay control requires every reported witness to execute from the declared initial configuration.

## Minimality

Search budgets are subsets of {D,R,W,P}. For each budget, enumerate neutral rewrite systems up to bounded rule count and execution depth. A capability counts only if its independently defined observer returns true and all leakage controls pass.

A failure at depth d means only: no witness found within the tested bound.

## Evidence status

This document specifies the corrected separation architecture. Numerical claims require an execution artifact and replay before becoming VERIFIED.

## Decision policy

No canonical foundation change follows from v0.4 automatically. Results are experimental until independently replayed.
