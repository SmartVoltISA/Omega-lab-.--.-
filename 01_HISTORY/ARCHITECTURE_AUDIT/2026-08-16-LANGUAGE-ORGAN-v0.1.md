# Ω-Space — Ω-Language Organ v0.1

**Date:** 2026-08-16
**Status:** implementation complete; CI acceptance pending

## Purpose

Create a separate language organ rather than embedding a full LLM into the organism.

The organ is responsible for a narrow boundary:

**human language → semantic relations → local memory → semantic relations → human-readable output**

## Implemented

- `LanguageOrgan` contract;
- auditable relation parser for a small v0.1 language subset;
- explicit `SemanticRelation(subject, relation, object)` representation;
- three local memory tiers: fast, working, long-term;
- explicit promotion between memory tiers;
- local-memory answering;
- deterministic rendering back to language;
- rejection of unsupported language patterns;
- no direct graph, global-memory, network, or capability authority.

## Architectural invariant

The language organ translates meaning; it does not become the organism's graph or global memory.

## Acceptance

Unit tests were added. Final acceptance requires a green SPACE CI run for the commit containing this organ.

## Next work

1. connect the language organ to Guardian-mediated requests;
2. add semantic normalization and synonym handling;
3. connect to graph memory only through an explicit capability boundary;
4. benchmark memory retrieval against a token-context baseline;
5. only then evaluate whether a neural component is useful.
