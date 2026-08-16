# Ω-Space — Language Organ / Multi-Organ CI Repair

**Date:** 2026-08-16

## Finding

After adding provenance/confidence tests to the language organ, the full SPACE suite ran **73 tests** but failed in four multi-organ exchange tests.

## Root cause

The new multi-organ test fixture constructed `SecurityEvidence` with fields that do not exist in the actual Guardian contract (`source`, `action`). The failure was in the test fixture, not in Guardian or the language organ.

## Repair

The fixture was aligned with the real Guardian evidence contract:

- `space_id`
- `device_key_id`
- `key_attested`
- `integrity_ok`
- `request_fresh`

No production security boundary was weakened or bypassed.

## Acceptance

A new CI run is required for commit `fa6e46a316ffb791453cf3080b5872e3d68fb746` before this repair is accepted.
