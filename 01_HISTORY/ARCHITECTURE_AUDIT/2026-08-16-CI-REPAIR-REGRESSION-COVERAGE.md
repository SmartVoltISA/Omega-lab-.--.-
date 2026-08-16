# CI Repair Regression Coverage — 2026-08-16

## Purpose
Record the repair verification added after the TrustLedger and ResourceManager API reconciliation.

## Repairs under test
- TrustLedger explicit initial trust must remain append-only and visible in history.
- ResourceManager compact and explicit allocation contracts must operate on the same resource/claim state.

## Regression coverage added
- `space/core/test_space_relationship.py`
  - verifies initial trust score;
  - verifies initial trust creates an auditable history event.
- `space/habitat/test_habitat_boundaries.py`
  - verifies compact resource request;
  - verifies explicit resource request;
  - verifies shared capacity accounting;
  - verifies partial release against the resource.

## Verification rule
The changes are not considered complete until the `space-organism` CI workflow runs on the `space/**` commits and passes in full.

## Structural scope
This checkpoint remains part of the larger integrity chain:

`nodes → edges → graph → cycles → memory → Guardian → feedback → organism → CI`

No green CI means no VERIFIED status.
