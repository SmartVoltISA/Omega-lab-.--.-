# Ω-MEM-7 — Branching, Distinguishability, and Next Transition

**Status:** OPEN / protocol definition only
**Date:** 2026-08-14
**Relation:** continuation of Ω-MEM-5 → Ω-MEM-6.

## Question

Does increasing the number of distinguishable future alternatives change next-transition uncertainty independently of memory capacity?

Current working chain:

`history → memory → distinguishability → uncertainty → transition`

Ω-MEM-7 isolates the middle of that chain by varying the number of controlled future alternatives while keeping memory capacity fixed.

## Core design

For a current state `S`, construct conditions with controlled future branching:

- `B=1`: one possible next transition;
- `B=2`: two possible transitions;
- `B=4`: four possible transitions;
- `B=8`: eight possible transitions.

Use the same nominal memory capacity in all conditions.

For each condition compare:

1. current-state-only predictor;
2. history-relevant memory;
3. capacity-matched irrelevant/random memory.

## Measurements

Record:

- conditional entropy `H(next | current)`;
- conditional entropy `H(next | current, memory)`;
- mutual information `I(next; memory | current)`;
- empirical number of distinguishable next transitions;
- empirical transition distribution;
- intervention effect after memory reset while holding the current observable state fixed.

## Critical controls

- Equal memory capacity across conditions.
- Equal sequence length and seed count.
- No comparison of different capacities as the primary test.
- Random/irrelevant memory must be permuted independently of the target sequence.
- Current observable state must be held fixed during memory intervention.
- The generator must expose the actual branching factor used, not infer it from observed counts.

## Falsification

The working hypothesis is weakened if:

- changing controlled branching does not alter the predicted uncertainty as expected;
- relevant memory and irrelevant memory perform equivalently under equal capacity;
- intervention on memory leaves the next-transition distribution unchanged;
- observed effects disappear after controlling for finite-sample occupancy.

## Non-claims

This experiment does not test agency, consciousness, free will, or whether choice is fundamental. It tests only measurable relations among branching, memory, distinguishability, and next-transition uncertainty.

## Freeze rule

This protocol is frozen before execution. Any implementation correction must be recorded as a protocol amendment and must not silently alter the primary test.
