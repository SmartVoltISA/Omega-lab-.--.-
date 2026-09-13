# Ω-FUTURE-1 — FUTURE ORIENTATION

**Status:** ACTIVE / first implementation
**Date:** 2026-08-18

This organ is the non-magical replacement for the informal word `INTUITION`.

## Contract

```text
CURRENT STATE
+ RELEVANT MEMORY
+ GOAL
+ CONSTRAINTS
+ AVAILABLE DATA
        ↓
FUTURE ORIENTATION
        ↓
DESIRED STATE
NEXT RESULT
DATA GAP
CANDIDATE ACTIONS
EXPECTED RESULTS
```

It does **not** execute actions. It does **not** claim to know the future. It produces structured candidate directions that must pass through PLAN, Guardian/execution, and verification.

## Distance

Every orientation has a horizon:

- `NEXT` — immediate, smallest verifiable state/result;
- `NEAR` — next connected objective;
- `FAR` — longer-range direction.

The implementation must prioritize `NEXT` before `NEAR` and `FAR`.

## Evidence rule

A candidate is an orientation, not a fact. Its expected result must remain separate from the later actual result.
