# Architecture Audit — Bidirectional Change Ledger

**Date:** 2026-08-16
**Status:** IMPLEMENTED / PENDING FULL CI VERIFICATION

## Decision

The organism must preserve history for consequential changes in both directions:

`external → quarantine → Guardian → internal`

and

`internal → Guardian → external`.

Guardian is the control boundary. The ledger is the immutable historical record and does not itself authorize a transition.

## Implementation

Added:

- `space/security/change_ledger.py` — append-only JSONL ledger with SHA-256 hash chaining.
- `space/security/test_change_ledger.py` — persistence, bidirectional recording and tamper-detection tests.
- `ARCHIVE/SPACE/ORGANISM/SPACE_BIDIRECTIONAL_CHANGE_LEDGER_PROTOCOL_v1.0.md` — architecture and invariants.

## Required properties

- change ID;
- direction;
- actor/source;
- target;
- action;
- before/after state hashes where available;
- Guardian decision;
- disposition;
- reason;
- previous record hash;
- current record hash.

Rejected and failed changes remain historical evidence. No mutation is considered complete if its consequential history is silently lost.

## Verification state

The runtime ledger primitive and unit tests are now present. Full integration with every mutation point and Guardian decision path is still required before the architecture is declared fully enforced.

## Next step

Run the complete CI, then connect the ledger to the Guardian bidirectional paths and quarantine acceptance boundary, followed by stress/tamper/recovery testing.
