# Ω-SPACE — SECURITY BINDING TEST MATRIX v1.0

**Status:** CORE / TEST PLAN
**Date:** 2026-08-16

## Objective

Validate that Space identity is bound to a person/account and a specific device without relying on a single permanent hardware identifier.

## Trust chain

`PERSON/ACCOUNT → SPACE_ID → DEVICE_KEY → HARDWARE_ATTESTATION → APP/DEVICE_INTEGRITY → GUARDIAN`

The phone number is an account/recovery signal, not the root of device trust. IMEI/serial are optional auxiliary signals and must not be treated as the primary secret or authentication factor.

## Device key

Create an asymmetric key in Android Keystore. Where supported, require hardware-backed protection (Trusted Environment or StrongBox) and verify attestation server-side. Android documentation states that hardware-backed key attestation can provide evidence that a key is stored in secure hardware; verification should occur on a trusted server and include certificate-chain and revocation checks. citeturn0search0

## Integrity

Use Play Integrity for protected server actions. The backend should verify the returned verdict and bind it to the request. Current Android documentation describes device integrity, app integrity and optional stronger signals; on Android 13+ `MEETS_DEVICE_INTEGRITY` can include hardware-backed proof of locked bootloader and certified OS, while `MEETS_STRONG_INTEGRITY` adds recent security-update requirements. citeturn0search2turn0search3

## Test cases

### SEC-001 — Normal registration
Expected: account + new Space ID + device key registered; Guardian permits low-risk operation.

### SEC-002 — Memory clone
Copy Space memory to another device without the original private key.
Expected: memory alone does not establish device trust; sensitive operation denied or re-enrollment required.

### SEC-003 — New phone, same person
Authenticate the account and register a new device key.
Expected: new device receives a new binding; old device remains separately identifiable until revoked.

### SEC-004 — Lost phone
Revoke old device binding.
Expected: old key is rejected by backend/Guardian even if the local Space database remains.

### SEC-005 — Number change
Change recovery phone number without replacing the device key.
Expected: phone-number change does not silently transfer device trust.

### SEC-006 — Compromised / weak integrity
Present a failed or insufficient integrity verdict.
Expected: Guardian reduces permissions or blocks protected actions according to policy. Play Integrity is designed for server-side decisions based on verified verdicts. citeturn0search7

### SEC-007 — Key cloning attempt
Attempt to export/reuse the private device key.
Expected: private key remains non-exportable; a copied database cannot reproduce device cryptographic proof.

### SEC-008 — Replay
Replay an old protected request/token.
Expected: request binding and server verification reject replay or stale context. Standard Play Integrity requests include replay protection. citeturn0search7

### SEC-009 — App tampering
Modify/repackage the Space application.
Expected: app-integrity verdict is not accepted as equivalent to the trusted production app; Guardian applies restricted policy. Play Integrity exposes app-integrity verdicts for this purpose. citeturn0search5

### SEC-010 — Identifier leakage
Inspect logs, graph, telemetry and archive.
Expected: no raw phone number, IMEI, serial or private key appears in normal graph/archive records. Use opaque identifiers and protected identity storage.

## Data separation

### Graph may contain
- opaque Person ID;
- opaque Space ID;
- opaque Device ID;
- public-key fingerprint / key identifier;
- trust state;
- provenance;
- revocation state.

### Protected identity store
- phone number and recovery data;
- provider/account identifiers;
- sensitive attestation material;
- operational secrets.

### Never store in archive
- private device keys;
- authentication secrets;
- raw recovery credentials;
- unnecessary permanent hardware identifiers.

## Guardian policy levels

`TRUSTED → RESTRICTED → REAUTH_REQUIRED → DEVICE_REVOKED`

The policy should be action-specific. A weak signal should not necessarily destroy the entire Space; it may only block high-risk operations.

## Acceptance criteria

The security binding is considered validated only when all applicable tests have executable implementations, expected outcomes, evidence, and independent verification.

Until then the protocol remains `DESIGNED / NOT VALIDATED`.
