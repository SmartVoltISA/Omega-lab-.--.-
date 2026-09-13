# Ω-LINK-1 — RESULT-005

**Status:** OBSERVED RESULT / not a universal law
**Run:** 31779728476
**Commit:** b4b683b071898c8c104306c8292961f7d6eae6ef

## Observation

Reversing the direction of the same edge changes the reachable-state structure even when the number of nodes and edges is unchanged.

For a single directed edge, `A→B` gives the reachable pair `A→B`, while `B→A` gives `B→A`.

For chains and branching structures, reversing directions changes both the number and identity of reachable source→target pairs. In the tested branching case, reversing the directions changed the reachable-pair count from 2 to 3.

## Interpretation

Direction is part of the structural behavior of a relation. A relation cannot, in general, be represented only as an undirected connection between two nodes if transition direction affects the reachable-state space.

## Interpretation boundary

This result concerns directed transition graphs and the chosen reachability metric. It does not establish that every real-world relation is inherently directed.

## Next question

Test time-dependent direction changes: whether two systems with the same current relational state can produce different next states when their prior direction history differs.
