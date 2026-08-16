# Ω-Language Organ — Work Order v0.1

**Date:** 2026-08-16
**Status:** IN PROGRESS

## Objective

Build a standalone language organ that translates human language into explicit Ω semantic relations and renders validated local structure back into human language.

The organ is not a full LLM. It is a language interface organ inside SPACE.

## Current verified base

- `space/organs/language_organ.py` exists.
- Semantic relation representation exists: subject → relation → object.
- Local memory is split into fast, working and long-term tiers.
- Promotion between tiers is explicit.
- Output can be rendered from local evidence.
- The organ has no direct global graph, network, Guardian or capability-escalation authority.
- Full SPACE Run #88 executed 61 tests with `OK`.

## Execution order

### 1. Contract lock
- Define accepted input/output contract.
- Keep unsupported language patterns fail-closed.
- Keep semantic representation deterministic and auditable.

### 2. Memory integration
- Fast memory: current utterance/context.
- Working memory: active relations for the current task.
- Long-term memory: only promoted/validated relations.
- Add provenance, confidence and timestamps before persistent use.

### 3. Ω-structure bridge
- Convert semantic relations into graph requests, not direct graph mutations.
- Guardian controls any future graph write.
- Language organ may request retrieval but cannot bypass memory/graph boundaries.

### 4. Answer generation
- Retrieve evidence first.
- Build an internal semantic response.
- Render human language last.
- If evidence is absent, explicitly report absence rather than inventing a fact.

### 5. Learning interface
- Add a replaceable model adapter later.
- The language organ remains independent from the chosen neural/model implementation.
- Compare deterministic parser, small neural model and hybrid approach experimentally.

### 6. Acceptance tests
- parse → semantic relation;
- semantic relation → text;
- three-tier memory separation;
- promotion rules;
- provenance retention;
- unknown language rejection;
- no direct graph mutation;
- Guardian-mediated graph access;
- long-context retrieval benchmark;
- regression and stress tests.

## Architectural invariant

> **Language is an interface organ, not the organism itself.**

The internal Ω representation remains stable even if the external language implementation changes.
