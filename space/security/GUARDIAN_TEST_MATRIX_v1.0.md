# Guardian Core Test Matrix v1.0

## Purpose

Every security rule must be runnable independently and as part of the complete suite.

## Individual tests

1. Valid identity + attested key + good integrity + fresh request → ALLOW.
2. Missing Space identity → BLOCK.
3. Missing device key identity → BLOCK.
4. Unattested key → RESTRICT.
5. Failed device/app integrity → RESTRICT.
6. Stale/replayed request → BLOCK.
7. Revoked device → BLOCK.
8. Recovery mode → RESTRICT.

## Combined scenarios

9. Revoked + compromised → BLOCK.
10. Recovery + good evidence → RESTRICT.
11. Unattested + stale → BLOCK (freshness is mandatory).
12. Missing identity + otherwise valid evidence → BLOCK.
13. All failures simultaneously → BLOCK.

## Isolation rule

Each individual rule must be testable without requiring the other rules to fail. Combined tests verify precedence and fail-closed behaviour.

## Current decision precedence

`revoked / invalid identity → BLOCK`

`stale request → BLOCK`

`unattested key or bad integrity → RESTRICT`

`recovery mode → RESTRICT`

`all required evidence valid → ALLOW`

## External integration boundary

The core receives evidence; it does not collect secrets or directly trust client claims. Android Key Attestation and Play Integrity evidence must be verified by the backend before being converted into trusted evidence for this policy core.

## Validation levels

- LEVEL 0: unit tests of policy logic;
- LEVEL 1: combined policy scenarios;
- LEVEL 2: simulated attestation/integrity evidence;
- LEVEL 3: Android integration with real device;
- LEVEL 4: adversarial/device-recovery testing.

Guardian is `VALIDATED` only for the highest level actually completed. Passing unit tests does not imply Android or adversarial validation.
