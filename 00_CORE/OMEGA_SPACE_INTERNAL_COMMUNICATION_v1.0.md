# Ω-Space — Internal Communication Protocol v1.0

**Status:** CORE / FOUNDATION / ACTIVE-DESIGN

## Priority

Internal communication is optimized in this order:

1. **Relation** — who/what is connected to whom.
2. **Meaning** — what the message means.
3. **Place** — where the sender, receiver, object or event belongs in the SPACE environment/graph.
4. **State** — what is currently true or observed.
5. **Transport cost** — use the minimum resources required.

> **First preserve connection and meaning; only then optimize transport.**

## Internal SPACE communication

Organs and processes inside one SPACE should not behave like independent network clients when a local reference is sufficient.

```text
SPACE
 ├── Brain
 ├── Memory
 ├── Graph
 ├── Skills
 ├── Tools
 ├── Guardian
 └── I/O
       ↕
   local semantic bus
```

The internal bus carries semantic events and references rather than repeatedly copying complete state.

## Minimal message

For routine local communication, the smallest useful semantic envelope is:

```text
SOURCE
TARGET
RELATION
MEANING
OBJECT/REFERENCE
PLACE
STATE/CHANGE
CORRELATION
```

Security, authority, provenance and Guardian metadata are attached when required by the operation or inherited from the local trust context.

## References before copies

Prefer:

```text
send(reference + meaning + delta)
```

over:

```text
send(full_object + full_context + full_history)
```

The receiver resolves local references through shared memory/graph access according to capability policy.

## Event-driven communication

Use events for changes rather than continuous polling wherever possible.

```text
STATE CHANGE
   ↓
EVENT
   ↓
TARGETED WAKE-UP
   ↓
PROCESS
   ↓
FEEDBACK
```

Idle organs remain dormant when no relevant event exists.

## Place / locality

`PLACE` is a semantic relation, not necessarily geographic coordinates. It may identify:

- graph location;
- organ/subsystem location;
- physical habitat location;
- logical workspace;
- conversation/group context;
- object location;
- temporal/contextual position.

The protocol should use the cheapest representation that preserves the required meaning.

## Resource economy

Internal communication should minimize:

- CPU wakeups;
- memory copies;
- serialization/deserialization;
- redundant inference;
- repeated context transfer;
- unnecessary storage writes;
- network use when a local path exists.

A local semantic reference should normally cost less than a full remote-style message.

## Communication modes

```text
LOCAL_REFERENCE  — same process/address space where safe
LOCAL_EVENT      — same SPACE event bus
LOCAL_MESSAGE    — structured internal message
SPACE_MESSAGE    — message between organisms
EXTERNAL_MESSAGE — communication outside the Habitat
```

Escalation between modes is explicit and Guardian-controlled where a boundary is crossed.

## Meaning preservation

Optimization must never silently remove meaning. If a compact representation loses information required to interpret the event, the system must retain or request the missing context.

```text
COMPRESSION OK
SEMANTIC LOSS NOT OK
```

## Feedback

Every consequential internal operation may produce a compact result event:

```text
RESULT = SUCCESS | FAILURE | PARTIAL | UNKNOWN
```

The full provenance remains in Memory; the active bus carries only the minimum context required for the next step.

## Guardian

Guardian monitors boundary crossings, unusual communication volume, capability escalation, unauthorized audience expansion and attempts to bypass the internal semantic bus.

Guardian itself must use the protected communication path and must not become a hidden unrestricted transport channel.

## Core law

> **Inside SPACE, communicate through meaning and relations, use locality and references, wake only what is needed, and spend resources only where they add information or action.**
