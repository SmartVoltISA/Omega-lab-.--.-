# Ω-Space Language v1.0 — Semantic Communication Foundation

**Status:** CORE / ARCHITECTURE / DRAFT-STABLE

## Purpose

SPACE requires a common machine-readable semantic layer for communication between SPACE organisms, organs, tools, skills and humans through translators.

This is not intended to replace human languages. It is a canonical semantic representation that reduces ambiguity and preserves provenance, authority and uncertainty.

## Fundamental principle

> **Meaning is primary; surface language is transport.**

A human sentence, UI action, API call or another SPACE message may be translated into the same semantic representation.

## Core message structure

Every consequential SPACE message should be representable as:

```text
IDENTITY
SOURCE
TARGET
INTENT
OBJECT
OPERATION
PURPOSE
CONTEXT
CAPABILITY
AUDIENCE
EVIDENCE
TRUST
AUTHORITY
UNCERTAINTY
CONSTRAINTS
GUARDIAN
RESULT
FEEDBACK
PROVENANCE
CORRELATION
FRESHNESS
```

Not every field is mandatory for every message. Security- and decision-relevant fields must not be silently omitted.

## Distinctions that must remain separate

```text
IDENTITY     != PROVENANCE
PROVENANCE   != TRUST
TRUST        != AUTHORITY
CAPABILITY   != AUTHORITY
CONTACT      != DISCLOSURE
DISCLOSURE   != INFLUENCE
RECOMMENDATION != DECISION
DECISION     != EXECUTION
FACT         != INFERENCE
INFERENCE    != PREDICTION
PREDICTION   != CERTAINTY
```

These distinctions are architectural invariants.

## Example

```text
SOURCE: SPACE-A
TARGET: FAMILY-GROUP
INTENT: INFORM
OBJECT: EVENT-123
PURPOSE: FAMILY_UPDATE
AUDIENCE: FAMILY
CAPABILITY: MESSAGE_SEND
TRUST: 0.82
UNCERTAINTY: 0.05
GUARDIAN: REQUIRED
```

The representation describes what is intended. Guardian still decides whether the operation is authorized.

## Communication levels

```text
REACH
  ↓
SEND
  ↓
DISCLOSE
  ↓
REQUEST
  ↓
ACT
  ↓
BROADCAST / INFLUENCE
```

Each level has independent policy. Possessing a lower-level capability does not imply a higher-level capability.

## SPACE-to-SPACE

Different SPACE models may have different internal representations, but communication crosses the common semantic boundary:

```text
SPACE-A internal state
       ↓
semantic encoding
       ↓
Guardian A
       ↓
transport
       ↓
Guardian B
       ↓
semantic decoding
       ↓
SPACE-B internal state
```

The receiver must not treat the sender's claims as facts without evidence or local validation.

## Memory and provenance

Messages that materially change state, trust, graph structure, permissions or decisions must be traceable to their origin and preserved in memory.

A semantic message may therefore carry references to:

- memory events;
- graph nodes/edges;
- evidence;
- skills/tools used;
- model/version;
- Guardian decision;
- resulting state;
- feedback.

## Uncertainty

The language must represent uncertainty explicitly. Unknown, estimated, inferred and verified are distinct semantic states.

```text
UNKNOWN
ESTIMATED
INFERRED
OBSERVED
VERIFIED
```

A translator must never turn `ESTIMATED` into `VERIFIED` merely to produce fluent human language.

## Human interface

Human language remains the interface of choice for humans. SPACE Language sits underneath it:

```text
Human language
      ↕
Translator / LLM
      ↕
SPACE semantic representation
      ↕
Guardian / organs / transport
```

The LLM or translator is not the authority. It is a semantic transformation layer subject to validation and Guardian policy.

## Group communication

Messages may target individuals, families, groups or public audiences. Audience scope is explicit and must survive translation.

`FAMILY` must never silently become `PUBLIC`.

## Evolution

The language is versioned. New fields may be introduced without changing the meaning of existing fields. Deprecated forms remain interpretable for historical replay where practical.

Language changes themselves are memory events and must preserve compatibility/provenance information.

## Security

Malformed, ambiguous, stale, replayed or unauthorized semantic messages are rejected or quarantined according to Guardian policy.

The language does not bypass Guardian. It makes intent and semantics more explicit so Guardian can evaluate them.

## Core law

> **SPACE may understand many languages, but its internal semantic foundation must preserve meaning, provenance, uncertainty, individuality and authority boundaries.**
