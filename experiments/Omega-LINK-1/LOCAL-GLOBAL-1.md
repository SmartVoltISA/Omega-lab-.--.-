# Ω-LINK-1 — LOCAL-GLOBAL-1

**Status:** FROZEN / control experiment

## Question
Can a relation disappear locally while preserving the global reachable-state space?

## Measurements

- `local_loss`: decrease in immediate outgoing choices at the source node after removal of one edge.
- `global_loss`: number of reachable source→target pairs lost after the same removal.

## Controlled topologies

1. `NO_ALTERNATIVE` — direct paths without bypass.
2. `PARTIAL_ALTERNATIVE` — an alternative path preserves some downstream reachability.
3. `SINGLE_ALTERNATIVE` — one direct edge has one alternate route.
4. `MULTIPLE_ALTERNATIVES` — more than one route can preserve reachability.

## Controls

- Node set fixed at A, B, C, D.
- Deterministic directed transitions.
- One edge removed per intervention.
- No memory, randomness, or adaptive behavior.
- The local metric is intentionally distinct from the global metric.

## Interpretation boundary

The experiment tests whether local disappearance and global structural loss are distinct measurable effects. It does not assume that either metric is the fundamental definition of a relation.

## Falsification target

If local and global losses always coincide across the controlled topologies, the proposed distinction has no explanatory value under this model.
