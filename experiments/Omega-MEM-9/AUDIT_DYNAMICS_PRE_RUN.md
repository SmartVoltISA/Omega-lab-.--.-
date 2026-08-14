# Ω-MEM-9 — Pre-run audit of indirect dynamics

**Status:** PASS WITH LIMITATIONS / READY FOR PILOT

## Leakage checks

- Memory does not store `X` or `Y`.
- No future transition is used to update memory.
- The future transition is sampled from normalized graph-edge weights.
- History enters only through the path-trace update from the incoming edge.
- The observable current state is identical (`S`) for both history classes.

## Important limitation

The memory trace changes the relative weights of the two outgoing graph edges. Therefore the model intentionally contains a causal pathway from internal memory to future transition probabilities. This is not considered a forbidden direct lookup because memory contains a generic trace statistic rather than a future-state label or lookup table. However, the construction is still minimal and engineered; it is not evidence for a universal law.

## Required pilot checks

1. Verify both history classes have identical observable `S`.
2. Verify memory traces differ only because of the preceding path.
3. Verify memory is never updated from `nxt`.
4. Compare against capacity-matched shuffled/irrelevant trace.
5. Reset memory while holding `S` fixed and measure change in transition distribution.
6. Run all 30 seeds before interpreting effect size.

## Decision

The implementation is sufficiently clean for a PILOT execution. Results must remain labeled preliminary until controls and reset intervention pass.
