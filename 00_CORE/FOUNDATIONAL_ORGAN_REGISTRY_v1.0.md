# Ω-Lab — FOUNDATIONAL ORGAN REGISTRY v1.0

**Status:** CORE / ACTIVE  
**Date:** 2026-08-18

## Purpose

Identify mechanisms that are foundational to the organism and therefore must be available across projects and applicable organs.

## Registry rule

An organ enters this registry only when its mechanism has been sufficiently demonstrated as general architecture. Before that point it remains a project experiment or candidate foundation.

## Current foundational candidate

### MEMORY

**Scope:** UNIVERSAL / CROSS-PROJECT

Memory is treated as structural persistence rather than an external log.

Required properties:

- active / passive / archive states where applicable;
- append-only history;
- provenance;
- state transitions;
- recovery / reconstruction;
- verification and recheck;
- preservation of failed and rejected states;
- relation-aware retrieval rather than blind recency only;
- explicit linkage to the state that produced each memory event.

Canonical principle:

```text
PAST / HISTORY
      ↓
    MEMORY
      ↓
PRESENT / CONTEXT
      ↓
RESULT / CHANGE
      ↓
MEMORY EVENT
```

### PRESENT

**Current scope:** SPACE implementation; candidate for universal foundation.

Do not promote to universal merely because SPACE needs it. Promotion requires architectural evidence that the same current-state contract is applicable across the organism.

### FUTURE / PLAN / EXECUTION / VERIFICATION / FEEDBACK

**Current scope:** SPACE implementation under active reconstruction.

These may later become universal organs if their contracts prove project-independent. Until then, preserve their SPACE provenance.

## Propagation model

For a promoted universal organ:

```text
OMEGA canonical contract
       │
       ├── SPACE implementation
       ├── MARKET implementation
       └── other applicable implementations
```

Implementations may differ internally, but must preserve the canonical semantic contract and provenance.

## Promotion rule

```text
candidate
  ↓
implemented
  ↓
verified
  ↓
reused independently
  ↓
shown project-independent
  ↓
FOUNDATIONAL
```

No premature promotion.
