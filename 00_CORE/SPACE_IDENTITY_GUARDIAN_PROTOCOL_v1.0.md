# Ω-Space — Identity & Guardian Protocol v1.0

**Status:** CORE / SECURITY ARCHITECTURE
**Date:** 2026-08-16
**Epistemic status:** design based on current Android security capabilities; implementation pending

## Purpose

Bind a Space installation to a verified user account and a specific device without treating IMEI or phone number as the sole root of trust.

## Trust hierarchy

```text
USER ACCOUNT
    ↓
SPACE IDENTITY
    ↓
DEVICE-BOUND CRYPTOGRAPHIC KEY
    ↓
HARDWARE / KEY ATTESTATION
    ↓
DEVICE INTEGRITY
    ↓
GUARDIAN
    ↓
ACCESS / ACTION
```

## Identity layers

### 1. User identity

Possible mechanisms:
- passkey / Credential Manager;
- account authentication;
- verified phone number as recovery/contact channel.

Phone number is not sufficient proof of device ownership and must not be the sole trust anchor.

### 2. Space identity

Each Space installation receives a unique logical identity and a cryptographic key pair.

The private key must remain protected by the platform keystore where supported.

### 3. Device binding

The Space public key is registered server-side as the device binding identity.

Prefer a hardware-backed Android Keystore key and verify key attestation where the device supports it.

The system must distinguish:

`same user + same device`

from:

`same user + new device`.

### 4. Device integrity

Use Play Integrity when available to obtain server-verifiable signals about application and device integrity.

The system should distinguish at least:
- trusted/genuine certified environment;
- basic but weaker integrity;
- compromised or unevaluated environment.

Do not equate an integrity verdict with absolute security.

## IMEI / hardware identifiers

IMEI and other persistent hardware identifiers are **secondary signals only**.

Reasons:
- Android restricts access to persistent device identifiers for ordinary applications;
- availability differs by Android version/device/manufacturer;
- such identifiers are privacy-sensitive;
- they are not a substitute for cryptographic device binding.

If an allowed hardware identifier is available, it may be used as supplementary evidence or diagnostics, never as the sole credential.

## Security record

Conceptual record:

```text
SPACE_ID
USER_ACCOUNT_REF
DEVICE_KEY_ID
DEVICE_PUBLIC_KEY
ATTESTATION_STATE
INTEGRITY_STATE
APP_VERSION
OS_VERSION
LAST_VERIFIED
RECOVERY_STATE
RISK_STATE
```

Avoid storing raw phone numbers, IMEI, serial numbers or other unnecessary persistent identifiers in the public graph/archive.

## Guardian decisions

Guardian evaluates the combination of identity, device binding and integrity.

Examples:

### Normal
`known user + known device key + acceptable integrity → allow`

### New phone
`known user + unknown device key + valid recovery → controlled re-bind`

### Copied Space memory
`known memory + unknown device key → do not trust memory as proof of identity`

### Compromised device
`valid account + failed integrity → restrict sensitive actions`

### Lost device
`device key revoked → deny device access even if old Space data is restored`

## Recovery

Recovery must not silently copy trust from an old device to a new device.

A new device receives a new device key. The user authenticates through an approved recovery mechanism, and Guardian establishes a new binding.

Android Credential Manager Restore Credentials may assist account restoration, but restoration must remain separate from device trust. The new device must establish its own device-bound key and integrity state.

## Revocation

Server-side records must support:
- revoke device;
- revoke Space session;
- rotate credentials;
- invalidate compromised keys;
- mark device as suspicious;
- require re-authentication.

## Privacy rule

Identity data and knowledge graph data are separate domains.

The graph should contain references such as:

`PERSON → OWNS → SPACE → BOUND_TO → DEVICE_KEY`

rather than raw personal identifiers wherever possible.

## Minimum implementation phases

### Phase 1
Local Space identity + Android Keystore key.

### Phase 2
Server registration of public key and challenge-response authentication.

### Phase 3
Key attestation where supported.

### Phase 4
Play Integrity verification at sensitive actions.

### Phase 5
Recovery / new-device binding / revocation.

### Phase 6
Guardian policy engine and audit trail.

## Required security experiments

`SEC-EXP-001` — same device, same Space identity.

`SEC-EXP-002` — copied database on another device must not authenticate the device.

`SEC-EXP-003` — revoked device key must fail authentication.

`SEC-EXP-004` — new device recovery creates a new binding.

`SEC-EXP-005` — integrity failure restricts sensitive actions.

`SEC-EXP-006` — loss of network does not corrupt or silently replace identity state.

`SEC-EXP-007` — no raw phone/IMEI leakage into the knowledge graph.

## Acceptance principle

> **Identity belongs to the user account; device trust belongs to a device-bound cryptographic identity; hardware and integrity signals strengthen the decision; Guardian decides what the Space is allowed to do.**

This protocol deliberately avoids making IMEI, phone number, IP address or any single hardware attribute the root of trust.
