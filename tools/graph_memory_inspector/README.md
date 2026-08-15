# Ω Graph Memory Inspector v0.1

## Status
PROTOTYPE — read-only design.

## Purpose
Inspect graph-memory structure without modifying memory.

## Core invariant
Observation must not mutate the inspected graph.

## Input
A graph represented as nodes and relations. Each node may contain:
- identity
- state
- confidence
- provenance
- timestamps

Each relation may contain:
- source
- target
- relation type
- confidence
- provenance

## Output
For a requested node or subgraph:
1. node identity and state;
2. direct relations;
3. relation provenance;
4. confidence values;
5. conflicting relations/states;
6. disconnected or orphan elements;
7. a deterministic inspection summary.

## Required checks
- identity collisions;
- missing provenance;
- dangling relations;
- conflicting state claims;
- duplicate relations;
- unreachable nodes;
- invalid references.

## Non-goals
- no automatic correction;
- no inference presented as fact;
- no deletion;
- no mutation of source memory;
- no ranking of truth without explicit evidence.

## Provenance chain
Every reported finding should be traceable to:
`source → relation/node → observation → finding`.

## Validation plan
Test against:
1. clean graph;
2. duplicate-node graph;
3. conflicting-state graph;
4. missing-provenance graph;
5. dangling-edge graph;
6. mixed failure graph.

Expected result: deterministic detection of injected defects with zero source mutation.

## Promotion gate
PROTOTYPE → VALIDATED only after an independent test suite confirms the checks and mutation invariant.