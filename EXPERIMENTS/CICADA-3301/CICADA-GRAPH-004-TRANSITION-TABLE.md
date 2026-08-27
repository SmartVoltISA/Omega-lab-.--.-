# CICADA-GRAPH-004 — Provenance-Controlled Transition Table

**Branch:** `research/cicada-3301`
**Status:** partial result / invariant not yet predictive
**Date:** 2026-08-28

## Objective
Test whether a single transition schema can describe independent known Cicada stages without page-specific hand tuning.

## Anchor table

| Era / node | Input state | Transform | Output state | Verification | Confidence |
|---|---|---|---|---|---|
| 2012 image | image dimensions + 3301 | multiply 509 × 503 × 3301 | numeric endpoint 845145127 | endpoint existed historically | PROVED historical transition |
| 2012 endpoint | numeric endpoint | countdown / timed reveal | GPS coordinates | coordinates archived | PROVED historical transition |
| 2012 physical stage | GPS coordinates | locate physical artifact | QR payload | QR artifacts archived | PROVED historical transition |
| 2013 Gematria | rune representation | Gematria mapping to 29 prime values | numeric representation | mapping independently documented | PROVED mechanism |
| P56/P57 reported solve | rune stream | prime/totient stream + offset 57 | plaintext instruction + SHA-512 commitment | plaintext method is community-reported; commitment is present in archived transcription | SPLIT: commitment PROVED as text, decryption attribution NOT independently proven |

## Common structural schema

The smallest common schema supported by these anchors is:

`representation -> deterministic transform -> addressable/identifiable state`

with an optional verifier edge:

`state -> authentication/commitment -> verified state`

This is weaker than a claim that one universal mathematical function generated all transitions.

## Important negative result

No single numeric function has yet been demonstrated to reproduce both:

1. the 2012 endpoint construction `509 × 503 × 3301 = 845145127`, and
2. the P56 reported prime/totient stream,

without introducing context-specific parameters.

Therefore **a universal transition function is currently UNKNOWN**, not proved.

## Graph interpretation

The data support typed edges such as:

- `ENCODES`
- `TRANSFORMS`
- `INDEXES`
- `GENERATES_ENDPOINT`
- `POINTS_TO`
- `HASHES_TO`
- `AUTHENTICATES`

The useful hypothesis is that the missing LP2 mechanism may be an absent edge or ordered path between already-known node types.

## Null-control requirement

A candidate bridge mechanism must beat a shuffled/null graph and must reproduce at least two independent known transitions without page-specific tuning.

## Current verdict

**PLAUSIBLE STRUCTURAL INVARIANT; NO PREDICTIVE UNIVERSAL RULE YET.**

Do not infer author knowledge of graph theory from this result. The evidence only supports a recurring transition architecture.

## Next target

Search for bridge variables that are present in multiple eras: prime ordinal, page number, dimensions, coordinate/order information, hash, and authentication key. Test whether any one of these variables can serve as a conserved state component across transitions.
