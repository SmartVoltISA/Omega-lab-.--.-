# CICADA-GRAPH-001 — Constraint and Transition Graph

**Status:** hypothesis / structural experiment
**Branch:** `research/cicada-3301`
**Date:** 2026-08-28

## Question

Does the unresolved Liber Primus system behave better as a graph of objects and typed relations than as a linear ciphertext → key → plaintext problem?

This is a structural hypothesis, not a claim about authorship or intent.

## Core model

Represent every externally or internally identifiable object as a node:

- image / page
- rune / word / sentence
- number / prime / totient value
- key / seed
- hash
- URL / domain / onion endpoint
- QR code
- book / external text
- physical coordinate / poster
- PGP key / signature
- transformation / algorithm

Represent relationships as typed directed edges:

`CONTAINS`, `DERIVES`, `ENCODES`, `TRANSFORMS`, `INDEXES`, `POINTS_TO`, `AUTHENTICATES`, `HASHES_TO`, `REORDERS`, `VALIDATES`, `LOCATES`, `GENERATES`.

## Why this is worth testing

The documented puzzle chain repeatedly crosses representation boundaries rather than remaining a single cipher operation: image → hidden payload → URL → book/number system → phone/domain → physical coordinates → QR → Tor endpoint. The 2013 material likewise connects an operating system image, steganographic files, Gematria Primus, primes, Tor and participant-generated services.

The solved Liber Primus material also contains multiple transformation families and number-theoretic structures. The current ciphertext-only program has already eliminated many memoryless/running-key/fractionation/transposition families, while the surviving program-level conclusion is that an externally held key or seed may be required.

Therefore the next experiment should examine the **edges and dependencies between known objects**, not simply search another flat keyspace.

## Hard research rules

1. No edge is accepted because it makes an attractive story.
2. Every edge must have a source, reproducible derivation, or explicit UNKNOWN status.
3. Distinguish `OBSERVED`, `DERIVED`, `HYPOTHESIZED`, `REJECTED`.
4. A graph that explains only unsolved material but cannot reproduce solved anchors is not accepted.
5. Negative results remain part of the graph ledger.
6. Do not infer human authorship, intelligence, organization size, or biological knowledge from graph structure alone.

## First test: solved-anchor graph

Construct a graph only from confirmed/independently reproduced transitions in the 2012–2013 puzzle chain and solved Liber Primus pages.

For each transition record:

`source_node → edge_type → target_node → evidence → confidence`

Then measure:

- node degree distribution
- in/out-degree
- connected components
- bridge edges
- articulation nodes
- repeated edge motifs
- path length between representations
- whether the same transformation node/edge types recur across independent puzzle stages

## Falsification criteria

The graph hypothesis is weakened or rejected if:

- the graph adds no explanatory structure beyond an ordinary chronological list;
- typed edges are mostly arbitrary labels with no predictive value;
- solved anchors cannot be represented without ad hoc edges;
- randomized/order-preserving controls produce equivalent graph structure;
- apparent hubs disappear when source provenance is controlled.

## Positive signal

A meaningful positive result would be a reproducible structural motif that:

1. appears in multiple independently sourced solved stages;
2. is not explained by chronology alone;
3. survives a null/randomized control;
4. predicts at least one previously unclassified relationship in the unresolved material;
5. can then be tested against primary artifacts.

## Important distinction

A graph is not automatically a biological-organism model. The useful connection is narrower: complex systems can be described by components plus relations, and failure/survival may depend more on the topology of relations than on isolated components. That analogy is a hypothesis generator, not evidence.

## Current status

**UNKNOWN.** No graph-based mechanism has yet been demonstrated. This file defines the experiment so that the next result can be accepted or killed cleanly.
