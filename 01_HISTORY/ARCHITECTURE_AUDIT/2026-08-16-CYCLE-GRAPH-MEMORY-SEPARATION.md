# Ω-Lab — Cycle / Graph / Memory Separation

**Date:** 2026-08-16  
**Status:** IMPLEMENTED — CI verification pending

## Rule

SPACE may independently operate:

1. the bidirectional cycle `different → whole → different`;
2. relations and operational graph construction;
3. memory and provenance inside their permitted domains.

These domains must never be combined into one self-continuing graph-cycle-memory structure.

## Boundary

The cycle domain now keeps its own cycle-local states and relations. It cannot:

- materialize its state as `GraphCore`;
- expose a graph snapshot;
- enter graph inspection;
- merge/attach/connect itself to an operational graph.

The operational graph remains independently usable. The protected foundation remains outside that graph as a separate stronger boundary.

## Intended structure

```text
CYCLE DOMAIN
разное → целое → разное
      ↺

GRAPH DOMAIN
узлы → связи → рёбра → граф
             ↺

MEMORY DOMAIN
состояния → история → provenance
             ↺

NO CROSS-DOMAIN CLOSURE
CYCLE ✕ GRAPH ✕ MEMORY → forbidden as one autonomous closed structure
```

Memory may preserve permitted local history, but memory does not create a hidden bridge that joins the cycle domain to the operational graph.

## Tests

Added tests for:

- normal cycle operation;
- cycle-local memory/relations;
- explicit cycle-to-graph rejection;
- independent graph operation;
- absence of cross-domain merge/attach/connect/materialize methods.

The rule is structural: **do not merely detect a forbidden combined graph after construction; do not provide the operation that constructs it.**
