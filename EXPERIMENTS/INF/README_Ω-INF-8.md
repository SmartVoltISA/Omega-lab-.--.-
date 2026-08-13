# Ω-INF-8 — Deliberate Falsification / Break Test

Date: 2026-08-13

## Purpose

Ω-INF-8 is explicitly adversarial. Its job is not to confirm Ω-INF-7, but to find a plausible way to make its apparent effect disappear.

## What is held fixed

For the reconstruction arm, the exact trigram multiset and character multiset must remain unchanged.

## What is changed

1. Reconstruction policy: stochastic shuffle, random-pop traversal, deterministic reverse, deterministic sorted.
2. Observable: zlib size, character entropy, bigram entropy, unique-bigram count.
3. Replication: 4 corpora, 8 seed families, 80 samples per policy/corpus.
4. Null control: random character permutations, which preserve character composition but intentionally destroy trigram constraints.

## Falsification logic

The stronger Ω-INF-7 interpretation is weakened if the observed corpus-dependent effect disappears under reasonable alternative reconstruction policies or if the apparent effect is shown to be mainly a property of one observable.

A surviving effect does not prove a universal law. It only makes the narrow artifact hypothesis harder to sustain.

## Non-negotiable rule

Ω-INF-7 is historical data and must not be edited after Ω-INF-8. If Ω-INF-8 contradicts it, both results remain visible.
