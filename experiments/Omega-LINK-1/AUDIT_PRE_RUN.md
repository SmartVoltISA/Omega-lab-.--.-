# Ω-LINK-1 — Pre-run audit

**Audit status:** PASS WITH SCOPE NOTE

## Verified

- Node set is fixed: A, B, C, D.
- G1 and G2 contain exactly four directed edges each.
- Node attributes are not used.
- The manipulated variable is edge placement/topology.
- Reachability is computed by deterministic BFS.
- Single-edge interventions remove exactly one edge.
- No memory, stochastic process, or hidden future label is present.

## Scope note

This is a directed-graph reachability experiment. It tests structural accessibility under the specified directed transition relation; it does not by itself establish a general physical law about all notions of connection.

## Important interpretation constraint

`next_count` is an immediate out-degree measure, while `reachable` is multi-step reachability. They must not be conflated. A topology may preserve immediate degree counts while changing multi-step accessibility.

## Decision

PASS for deterministic pilot execution. Results must be interpreted only within the frozen protocol.
