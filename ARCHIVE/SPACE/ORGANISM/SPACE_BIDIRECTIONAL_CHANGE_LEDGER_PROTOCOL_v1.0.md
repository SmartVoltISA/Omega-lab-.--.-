# SPACE Bidirectional Change Ledger — v1.0

## Purpose

Every consequential mutation of the organism must remain recoverable as history, regardless of direction.

## Two directions

```text
EXTERNAL → QUARANTINE → GUARDIAN → INTERNAL
INTERNAL → GUARDIAN → EXTERNAL
```

Guardian is the boundary controller in both directions. The ledger records the attempted transition; recording never grants permission.

## What is recorded

Every consequential change records:

- `change_id`
- UTC timestamp
- direction
- actor/source
- target node/organ/tool
- action
- before-state hash, when available
- after-state hash, when available
- Guardian decision
- disposition
- reason
- previous ledger-record hash
- current ledger-record hash

## Dispositions

`PROPOSED`, `ACCEPTED`, `REJECTED`, `ISOLATED`, `FAILED`.

## Invariants

1. No consequential change may silently mutate trusted state.
2. A rejected change remains historical evidence.
3. A failed change remains historical evidence.
4. Internal and external changes use the same audit boundary.
5. The ledger is append-only and hash chained.
6. Ledger history is independent from authorization: an entry is not permission.
7. Before/after hashes must be used where a state snapshot exists.
8. Guardian decisions must be attributable to the change record.

## Recovery

The ledger is intended to answer:

- what changed;
- who/what caused it;
- from which direction;
- what state existed before;
- what state existed after;
- whether Guardian allowed it;
- why it was accepted/rejected/isolated/failed.

This makes later inspection and controlled rollback possible without rewriting history.

## Implementation

Runtime primitive: `space/security/change_ledger.py`.

The primitive uses JSONL persistence and a SHA-256 record chain. Runtime integration with Guardian and all mutation points must be added and tested before this protocol is marked fully enforced.

## Status

Architecture + runtime ledger primitive implemented. Full Guardian integration and mutation-point coverage remain verification targets.
