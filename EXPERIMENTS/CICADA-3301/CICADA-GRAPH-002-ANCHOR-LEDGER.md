# CICADA-GRAPH-002 — Provenance-Controlled Anchor Ledger

**Branch:** `research/cicada-3301`
**Date:** 2026-08-28
**Status:** OBSERVED/DERIVED anchor graph; predictive graph mechanism not yet demonstrated

## Objective

Build the first graph using only externally documented or independently reproducible transitions. Do not use unresolved pages to manufacture the model.

## Nodes

- `N01` 2012 opening image
- `N02` OutGuess hidden payload
- `N03` PGP authentication
- `N04` book-cipher stage
- `N05` phone/prime instruction
- `N06` numeric domain `845145127.com`
- `N07` GPS coordinate set
- `N08` physical posters
- `N09` QR/book-cipher payload
- `N10` Tor/.onion endpoint
- `N11` 2013 Cicada OS
- `N12` `@1231507051321` / 2013 key material
- `N13` Gematria Primus
- `N14` prime sequence
- `N15` 2014 Liber Primus
- `N16` solved-page transformation families
- `N17` Page 56 prime/totient stream
- `N18` SHA-512 endpoint commitment
- `N19` unknown deep-web target
- `N20` PGP public key / authenticity anchor

## Confirmed / strongly sourced edges

| Source | Relation | Target | Status | Evidence |
|---|---|---|---|---|
| N01 | CONTAINS | N02 | OBSERVED | 2012 archive: OutGuess payload |
| N02 | AUTHENTICATES | N03 | OBSERVED | PGP-signed extracted message |
| N03 | POINTS_TO | N04 | DERIVED | documented 2012 chain |
| N04 | DERIVES | N05 | DERIVED | book cipher leads to phone instruction |
| N05 | GENERATES | N06 | DERIVED | 509 × 503 × 3301 = 845145127 |
| N06 | POINTS_TO | N07 | DERIVED | countdown revealed global coordinates |
| N07 | LOCATES | N08 | OBSERVED | physical poster locations |
| N08 | CONTAINS | N09 | OBSERVED | QR codes |
| N09 | POINTS_TO | N10 | DERIVED | QR/book cipher to Tor endpoint |
| N11 | CONTAINS | N12 | OBSERVED | 2013 OS/key material |
| N12 | INTRODUCES | N13 | DERIVED | 2013 Gematria introduction |
| N13 | MAPS_TO | N14 | OBSERVED | 29 runes mapped to first 29 primes |
| N13 | ENCODES | N15 | DERIVED | Gematria is used throughout Liber Primus |
| N15 | CONTAINS | N16 | OBSERVED | multiple solved transformation families |
| N17 | DERIVES | N18 | DERIVED | solved prime/totient stream produces terminal hash instruction |
| N18 | POINTS_TO | N19 | OBSERVED | digest identifies an unknown deep-web page |
| N03 | AUTHENTICATES | N20 | DERIVED | authentic Cicada messages use the preserved PGP key |

## Recurrent motifs

### Motif A — representation crossing

`artifact → hidden/encoded payload → transformation → external object`

Appears in the 2012 chain and again in LP material.

### Motif B — number system as edge generator

`image/data → primes/numerical relation → next address/object`

2012 provides a direct example: image dimensions + 3301 generate the numeric domain. Gematria later makes primes a persistent representation layer.

### Motif C — authenticity is a separate edge

`message/object → PGP authentication`

This means discovery and authentication are distinct graph operations. A candidate endpoint is not accepted merely because its text looks correct.

### Motif D — terminal commitment

`solved transformation → SHA-512 commitment → unknown external object`

Page 56 is the strongest surviving example. The hash is a commitment/check, not itself an address.

## Critical result

The anchor graph is **not merely chronological**. It contains repeated typed transitions between different representation classes: image, hidden data, numbers, text, URL, physical location, QR, Tor endpoint, rune system, cryptographic transformation, and hash commitment.

This is evidence for a **graph-like representation of the puzzle**, but it is NOT yet evidence that the original authors consciously designed it as graph theory or as a biological-organism model.

## What is still missing

The current graph has a major unresolved cut:

`N18 SHA-512 commitment → N19 unknown target`

and a second major cut:

`N15 Liber Primus → ? → N18`

The research priority is therefore to identify the missing transformation/edge rather than search arbitrary plaintext.

## Falsification / control

A graph mechanism will only be promoted beyond PLAUSIBLE if it:

1. reproduces all listed anchor edges;
2. yields a repeated structural motif across independent puzzle years;
3. predicts a previously unknown edge;
4. survives a relation-preserving/randomized control;
5. does not require post-hoc edge labels.

## Current classification

- Anchor graph: **OBSERVED/DERIVED**
- Recurrent cross-representation motifs: **PLAUSIBLE**
- Graph as authorial design: **UNKNOWN**
- Biological-organism knowledge by authors: **UNKNOWN**
- Missing endpoint edge: **UNKNOWN**
- Full Liber Primus transition algorithm: **UNKNOWN**
