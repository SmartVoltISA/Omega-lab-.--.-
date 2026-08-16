# Repair Record — TrustLedger / ResourceManager

**Date:** 2026-08-16
**Status:** FIX APPLIED / PENDING CI

## Findings
The full SPACE organism CI exposed two API-contract mismatches:

1. `TrustLedger` tests and relationship layer required an explicit initial trust operation, while the implementation only exposed `update()`.
2. `ResourceManager` implementation used the explicit `Resource`/claim contract while habitat boundary tests also exercised a compact resource registration/request/release form.

## Repairs

### TrustLedger
Added `set_initial(subject, score, reason, evidence=None)`.

The operation does not bypass memory or audit: it creates the same append-only `TrustEvent` used by normal updates and refuses to overwrite an already initialized subject.

Commit: `294525d4ffb2ba16f968f2ec47df099e5c4a829f`

### ResourceManager
Reconciled both contracts without removing the explicit resource model:

- `register(Resource(...))` remains supported.
- `register(resource_id, kind, capacity, unit)` is supported.
- Explicit claim requests remain supported.
- Compact `request(resource_id, amount)` is supported.
- Explicit claim release remains supported.
- Compact partial release is supported.

Commit: `bb9c2cffd50390cbbd9f88171e43b203be0c145c`

## Integrity constraint
Compatibility was added at the boundary rather than weakening Guardian/resource semantics or deleting the richer contract.

## Verification status
These repairs are **not yet VERIFIED**. The next required step is the full CI run, followed by graph, cycle/ring, memory-integrity, Guardian and feedback checks.

A green full CI is the only condition that closes this repair record.