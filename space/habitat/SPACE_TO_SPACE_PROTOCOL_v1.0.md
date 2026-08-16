# Ω-Space — SPACE-to-SPACE Protocol v1.0

## Purpose

Define how independent SPACE organisms exchange information without bypassing identity, capability control, memory, feedback or Guardian.

## Communication layers

```text
Application / Skill
        ↓
Message
        ↓
Nervous System
        ↓
Guardian
        ↓
Transport Adapter
        ↓
Guardian
        ↓
Nervous System
        ↓
Receiving SPACE
```

## Message envelope

```text
message_id
correlation_id
sender_id
receiver_id
sender_epoch
created_at
expires_at
message_type
capability
requested_action
payload
provenance
reply_to
```

The payload is not trusted merely because it arrived from another SPACE.

## Message classes

- OBSERVATION — sensor/telemetry information
- KNOWLEDGE — derived information
- REQUEST — ask another SPACE to perform work
- COMMAND — authorized action request
- RESULT — execution result
- FEEDBACK — outcome evaluation
- RESOURCE — resource availability/claim information
- HEALTH — system health
- RECOVERY — recovery coordination
- HEARTBEAT — liveness only; never an authorization

## Request lifecycle

```text
CREATE
 ↓
IDENTIFY
 ↓
CAPABILITY CHECK
 ↓
GUARDIAN AUTHORIZATION
 ↓
TRANSMIT
 ↓
RECEIVE
 ↓
VERIFY
 ↓
EXECUTE OR REJECT
 ↓
RESULT
 ↓
FEEDBACK
 ↓
MEMORY / GRAPH
```

## Separation of concerns

Transport carries bytes/messages.

Nervous System routes signals.

Guardian decides whether a protected action or communication is permitted.

Brain/Planner decides what should be attempted.

Memory records what happened.

Graph records structural relationships and provenance.

Skill records reusable capability acquired from verified experience.

## SPACE federation

A group of SPACE organisms may form a higher-order graph:

```text
SPACE A ←→ SPACE B ←→ SPACE C
     \          |          /
       ---- shared graph ----
```

Federation does not merge identities. Each SPACE retains its own state, memory and security boundary.

## Failure behavior

No response:
- timeout;
- retry only when policy allows;
- preserve correlation ID;
- record failure;
- do not assume success.

Invalid identity/evidence:
- reject;
- record security event;
- do not execute payload.

Stale message:
- reject or quarantine according to policy.

Repeated failed interaction:
- loop guard / recovery path.

## Principle

SPACE may cooperate with SPACE, but no SPACE becomes trusted merely by being another SPACE.
