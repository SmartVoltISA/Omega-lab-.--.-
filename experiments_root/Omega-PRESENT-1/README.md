# Ω-PRESENT-1 — CURRENT STATE

**Status:** ACTIVE / first implementation
**Date:** 2026-08-18
**Purpose:** formalize PRESENT as a distinct, verifiable organ between MEMORY and future orientation.

## Principle

```text
MEMORY = what was
PRESENT = what is now
```

PRESENT is not a history log and not a plan. It is the minimal operational state required to describe what the organism currently knows, is doing, lacks, and is constrained by.

## Minimal state

A `CurrentState` contains:

- stable `state_id`;
- `cycle_id`;
- `timestamp`;
- current work status;
- active work items;
- active organs;
- available data;
- missing data;
- known facts;
- unknowns;
- constraints;
- last result;
- active memory references;
- graph reference.

The model deliberately does **not** contain future plans. Desired state, candidate actions and expected results belong to the next organ.

## Transition rule

A state change is represented as an append-only transition:

```text
S0 --Δ--> S1
```

The transition keeps the predecessor reference and a machine-readable delta. The previous state is never overwritten by the transition mechanism.

## Verification target

The first proof is deliberately small:

```text
STATE0
  ↓
change
  ↓
STATE1
  ↓
verify
  ↓
STATE0 remains reconstructable
```

If this passes, MEMORY ↔ PRESENT can be built on top of a real state object rather than prose.
