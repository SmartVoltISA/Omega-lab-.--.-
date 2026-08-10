# Ω-MEM — Memory as a minimal functional structure

This branch follows Ω-0. It does not assume a philosophical definition of memory. It asks for an operational one.

## Working definition

> **Memory is retained state from an earlier act that can causally alter the behavior of a later act.**

A record that cannot influence anything later is a log, not functional memory.

## Research question

What is the smallest retained state that can produce a measurable change in a later comparison or action?

## Planned ladder

### M0 — No retained state

Each act receives no state from previous acts.

Expected: no demonstrated memory effect.

### M1 — Read-only trace

A trace exists but cannot change.

Expected: information can be present, but cannot encode changing history.

### M2 — One mutable bit / two-state trace

The smallest possible discrete mutable state is tested.

Questions:

- Can it distinguish at least two histories?
- Can changing it alter a later act?
- Can it create a reproducible sequence-dependent behavior?

### M3 — Minimal overwrite memory

A state is replaced by information from the current act.

Test whether overwrite alone is sufficient for useful history dependence.

### M4 — Minimal accumulative memory

The retained state incorporates information rather than simply replacing it.

Test whether accumulation creates behavior unavailable to overwrite-only memory.

## Controls

Every memory claim must be compared against controls that preserve as much as possible while removing the proposed memory mechanism.

At minimum:

1. no memory;
2. static trace;
3. mutable one-bit state;
4. shuffled trace / randomized trace;
5. delayed replay of the same trace where applicable.

## Metrics

Do not introduce arbitrary metrics after seeing results. Candidate preregistered metrics:

- history dependence: change in output when retained state is altered;
- mutual information between prior state and later output;
- conditional predictability with vs without memory;
- minimum state size required for a measurable effect;
- persistence time of the retained state;
- overwrite rate;
- information retained after repeated updates.

## Important distinction

Memory should not be equated with a large `history[]` buffer.

The research target is **causal memory**, not storage capacity.

## Status

Protocol stage. No claim of emergence has been established yet.
