# Ω-MEM-8 — Pilot Audit

## Verified

- Current observable state is always `S` at measured decision points.
- Memory values are derived from the immediately preceding path node.
- No next-transition label is stored in the memory variable.
- Irrelevant control uses the same observed memory values after independent permutation.
- 30 independent seeds are used.
- Sequence length is equal across seeds.

## Important limitation

The pilot generator itself defines the dynamics `A→S→B` and `X→S→Y`. Therefore the path trace is intentionally predictive by construction. This is a valid architecture check, not evidence for a universal law.

## Next requirement

A stronger Ω-MEM-8 run must use a richer transition system in which path history influences a latent/internal state through a rule that does not trivially map one preceding symbol to one future symbol. It must also include a memory-reset intervention while holding the observable current state fixed.

**Status:** PILOT ACCEPTED FOR CONTINUATION; NOT FINAL.
