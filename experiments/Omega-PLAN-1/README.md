# Ω-PLAN-1 — FUTURE → PLAN

**Status:** ACTIVE / first implementation
**Date:** 2026-08-18

## Boundary

FUTURE ORIENTATION proposes a direction. PLAN converts that direction into explicit, auditable steps. PLAN does not execute anything.

```text
FUTURE
  ↓
DESIRED STATE
  ↓
NEXT RESULT
  ↓
DATA NEEDED
  ↓
CANDIDATE ACTIONS
  ↓
PLAN
  ↓
GUARDIAN / EXECUTION
```

## Minimal plan contract

Each plan contains:

- `plan_id`
- source future-orientation id
- source current-state id
- goal / desired state
- ordered steps
- expected result per step
- required data per step
- constraints
- status

Every step must have an expected result. A plan is invalid if it contains an action without an expected result.

## Execution boundary

This organ produces a plan only. It cannot execute an action, modify PRESENT, or write MEMORY as a side effect.

Execution and verification are separate organs.
