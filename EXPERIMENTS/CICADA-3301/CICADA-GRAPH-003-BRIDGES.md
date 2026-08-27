# CICADA-GRAPH-003 — Bridge Nodes and Transition Invariants

**Status:** experimental / not yet solved
**Date:** 2026-08-28

## Question

Do the same *types of transitions* recur across independent Cicada rounds strongly enough to identify bridge mechanisms between representation spaces?

## Confirmed anchor motifs

### 2012
image → hidden payload → signed message → book/number system → primes → numeric endpoint → coordinates → physical artifact → QR → Tor endpoint.

### 2013
Cicada OS / hidden data → cryptographic transformation → signed message → Gematria / prime system → network endpoint.

### Liber Primus
runes → Gematria index/value → number-theoretic transformation → plaintext or instruction → SHA-512 commitment → external/deep-web object.

These are sourced from archived primary/community reconstructions, but individual community reconstructions are not automatically treated as proof of author intent.

## Candidate invariant

The repeated object-level pattern is:

`encoded state → deterministic transform → verifier/addressable object`

The repeated *bridge types* are more interesting than the particular ciphers:

1. representation conversion;
2. number-theoretic indexing;
3. cryptographic authentication/verification;
4. endpoint generation or commitment;
5. transition to another representation space.

## Critical hypothesis

A Cicada key may be better modeled as a **transition function** or ordered path through states than as a static string.

Formal placeholder:

`K = F(S_t, E_t, C_t) → S_(t+1)`

where `S` is system state, `E` is the typed edge/operation, and `C` is the constraint set.

This is only a hypothesis. It must reproduce known transitions before being applied to unresolved LP2.

## Candidate bridge tests

A. 2012 numeric endpoint: verify that the prime-derived number is an address-generating transition, not merely a puzzle answer.

B. 2013 prime/gematria stage: determine whether prime tests and Gematria are separate nodes or one combined transformation node.

C. P56: treat the SHA-512 value as a commitment node and explicitly separate `GENERATES` from `HASHES_TO`.

D. PGP: model signature verification as an authentication edge, not as content.

E. LP2: test whether an unknown page can be represented by the same transition schema without choosing an arbitrary missing edge.

## Falsification

Reject the invariant if:

- it is merely a restatement of chronology;
- the same motif disappears when provenance is controlled;
- it cannot reproduce at least two independent known transitions;
- a shuffled graph preserves the same predictive structure;
- the proposed transition function requires page-specific hand tuning.

## Current result

**PLAUSIBLE STRUCTURAL INVARIANT; NOT PROVED.**

The important result is not that Cicada "used graph theory". We have no evidence sufficient for that authorship claim. The testable claim is narrower: the puzzle corpus repeatedly uses typed transitions between different representation spaces, and those transitions may constrain the unknown LP2 mechanism.

## Next experiment

Build a minimal state-transition table for 2012, 2013, and P56/P57 using only provenance-controlled anchors. Then search for the smallest transition rule that explains all anchors without page-specific parameters. Only after that rule survives null controls should it be used to generate candidate missing edges for LP2.