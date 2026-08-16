# Ω-Lab — Guardian Bidirectional Defense v1.0

## Purpose

Guardian is the system-wide defensive boundary of SPACE. It protects the organism in both directions:

```text
EXTERNAL WORLD
      ↓
   GUARDIAN
      ↓
    SPACE
      ↓
   GUARDIAN
      ↓
EXTERNAL WORLD
```

Guardian does not mean isolation. It means **controlled interaction**.

## 1. Two-way protection

### Outside → SPACE

Guardian must inspect and control incoming:

- network traffic;
- Wi-Fi;
- Bluetooth;
- USB/device events;
- external APIs;
- files and imported data;
- messages from other SPACE instances;
- sensors and peripherals;
- remote commands.

The fact that data is incoming does not make it trusted.

### SPACE → outside

Guardian must also inspect and control outgoing:

- network requests;
- Bluetooth operations;
- USB/device operations;
- API calls;
- file writes outside the protected boundary;
- messages to other SPACE instances;
- actuator commands;
- external tool execution.

The fact that the request originates inside SPACE does not make it automatically trusted.

## 2. Interaction is allowed, escape is not

SPACE must be able to interact with its environment.

The rule is:

```text
UNCONTROLLED ACCESS = NO
AUTHORIZED INTERACTION = YES
```

Therefore Guardian separates **communication** from **authority**.

A request may pass through a communication channel while still being denied execution, data access, privilege escalation or boundary crossing.

## 3. Guardian is a control plane, not the organism's brain

Guardian does not decide the organism's goals or perform its reasoning.

```text
BRAIN → proposes/requests
GUARDIAN → verifies and authorizes
HABITAT → executes
RESULT → returns through Guardian
```

Guardian is therefore a protective control plane between the active organism and its environment.

## 4. Continuous verification

Every security-sensitive interaction must be evaluated against current evidence rather than relying solely on a previous approval.

Relevant evidence includes, where applicable:

- identity;
- device identity;
- capability;
- attestation;
- integrity;
- freshness;
- revocation state;
- recovery state;
- direction;
- target;
- requested operation;
- resource scope;
- provenance;
- anomaly state.

The existing Guardian policy already blocks revoked/invalid identity, restricts failed attestation/integrity, blocks stale requests and restricts recovery mode. fileciteturn136file0

## 5. Defense in depth

Guardian should not depend on a single check.

Conceptual pipeline:

```text
REQUEST
  ↓
IDENTITY
  ↓
CAPABILITY
  ↓
INTEGRITY / ATTESTATION
  ↓
FRESHNESS / REPLAY CHECK
  ↓
TARGET / SCOPE
  ↓
ANOMALY / RATE CHECK
  ↓
POLICY
  ↓
ALLOW / RESTRICT / BLOCK
  ↓
AUDIT
```

For high-risk operations, independent checks should be performed again at the execution boundary.

## 6. No implicit trust inside SPACE

Brain, Skill, Tool, Memory, LLM, another organ, another SPACE, or an administrator does not receive unrestricted authority merely because it is internal.

Internal components receive capabilities with explicit scope.

```text
COMPONENT → CAPABILITY → GUARDIAN → TARGET
```

## 7. No implicit trust outside SPACE

External data is treated as untrusted until validated.

This includes seemingly harmless input. Data may be accepted as information without granting it authority.

```text
DATA ≠ COMMAND
MESSAGE ≠ AUTHORITY
TOOL RESULT ≠ TRUST
REMOTE SPACE ≠ TRUST
```

## 8. Separation of data and control

Guardian must preserve the distinction between:

- data plane — information being transported;
- control plane — permission to cause an operation.

An incoming document can be stored or analyzed without being allowed to execute an instruction contained inside it.

## 9. Fail-closed behavior

When evidence is missing, contradictory, stale or invalid, the safe default is:

```text
BLOCK or RESTRICT
```

not implicit ALLOW.

## 10. Guardian and Memory

Guardian decisions become part of system provenance:

```text
REQUEST → DECISION → EXECUTION → RESULT → MEMORY
```

Repeated suspicious patterns should be available to the immune/anomaly layer and to future policy decisions.

## 11. Guardian and Recovery

When the organism enters recovery mode, Guardian remains active.

Recovery does not disable the boundary. Instead it reduces permitted operations to the minimum required for safe recovery.

## 12. Guardian and SPACE-to-SPACE

Communication between organisms follows:

```text
SPACE-A
  ↓
GUARDIAN-A
  ↓
TRANSPORT
  ↓
GUARDIAN-B
  ↓
SPACE-B
```

Both sides independently authorize the interaction.

## 13. Core rule

> **Guardian protects in both directions. It does not prevent life; it prevents uncontrolled action.**

SPACE remains able to see, hear, communicate, calculate, use tools and interact with its habitat — but every security-sensitive boundary crossing is subject to explicit policy and verification.
