# Ω-Lab — MEMORY INTEGRITY PROTOCOL v1.0

**Status:** CORE / ACTIVE

## Purpose

Memory integrity is a non-negotiable property of the organism. Extending SPACE, replacing organs, changing tools, or integrating hardware must never silently erase, rewrite, detach, or lose historical state.

## Fundamental rule

> **New state may supersede the current state, but it must never silently destroy the history that produced it.**

The system must preserve both:

- current usable state;
- historical path and differences that led to it.

## Memory layers

```text
ARCHIVE
  ↓ immutable historical record
CURRENT GRAPH
  ↓ best current structural state
WORKING MEMORY
  ↓ active context
```

These layers may be optimized independently, but they must remain traceably connected.

## Append, don't overwrite

State transitions are recorded as events/deltas wherever practical.

```text
S0 → Δ1 → S1 → Δ2 → S2
```

Updating the current state must not delete Δ1 or Δ2.

If compaction is required, the compacted state must retain provenance to the source history.

## Provenance

Every structurally meaningful memory item should retain, where applicable:

- stable identifier;
- source;
- timestamp/cycle;
- parent or predecessor state;
- related node/relation/edge;
- operation that produced the change;
- evidence/status;
- confidence/validation state;
- links to derived state.

## Contradictions

Conflicting information is preserved rather than silently reconciled.

```text
A says X
B says Y
      ↓
CONFLICT
      ↓
retain A + B + provenance
      ↓
resolve only with evidence
```

The resolution becomes a new state; the conflict remains historical evidence.

## Guardian interaction

Guardian must protect memory integrity as well as external I/O.

An inbound or outbound operation that would:

- erase history;
- rewrite provenance;
- bypass versioning;
- corrupt current state;
- detach a relation from its origin;
- destroy recovery information

must be blocked or restricted.

## Internal safety

SPACE itself is not automatically trusted to rewrite its own history.

Brain, Skills, Tools, Habitat and external actors may request memory changes, but the memory layer must enforce integrity and provenance rules.

This does not prevent normal operation. It prevents uncontrolled historical destruction.

## Recovery

After failure, recovery must prefer:

```text
known-good state + preserved history
```

over:

```text
clean state with lost history
```

Recovery events themselves become part of memory.

## Migration

When an organ or schema changes:

1. preserve the old representation;
2. create the new representation;
3. record migration metadata;
4. maintain links between old and new identifiers;
5. verify recoverability;
6. only then mark the new representation current.

## Verification rule

Memory-related changes require two checks:

**CHECK:** does the new state work?

**RECHECK:** can the previous history still be reconstructed and traced?

A successful functional change with lost history is a failed memory-integrity change.

## Core cycle

```text
EVENT
 ↓
MEMORY APPEND
 ↓
CURRENT STATE UPDATE
 ↓
GRAPH UPDATE
 ↓
FEEDBACK
 ↓
NEW EVENT
```

History therefore remains connected to the active organism rather than becoming a detached archive.

## Final rule

> **The organism may grow, reorganize, learn, recover and replace organs. It must not forget how it became what it is.**
