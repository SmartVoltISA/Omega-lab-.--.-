# Ω-Lab — Foundation / Operational Graph Isolation

**Date:** 2026-08-16  
**Status:** IMPLEMENTED

## Requirement

The protected Ω foundation must remain separate from the operational SPACE graph.
SPACE must not be able to discover protected foundation relations through graph traversal and must never connect the protected foundation into its operational graph.

## Enforcement

`space/core/graph.py` now treats the `foundation:` namespace as protected:

- protected foundation nodes cannot be inserted into `GraphCore`;
- edges cannot start or end at protected foundation nodes;
- protected foundation relations cannot be created;
- neighbor discovery for protected foundation identifiers returns no operational graph nodes;
- ordinary graph nodes and relations remain functional.

Guardian remains the authority for foundation integrity. The operational graph is deliberately unable to represent a foundation edge, so this boundary cannot be bypassed by ordinary graph construction.

## Tests

Added `space/core/test_graph_foundation_boundary.py` covering:

1. foundation node insertion rejection;
2. operational → foundation edge rejection;
3. foundation → operational edge rejection;
4. foundation relation rejection;
5. normal graph operation;
6. protected foundation neighbor non-discoverability.

## Principle

**Фундамент хранится отдельно. Guardian его защищает. SPACE может работать с графом, но не может включить фундамент в свой граф.**
