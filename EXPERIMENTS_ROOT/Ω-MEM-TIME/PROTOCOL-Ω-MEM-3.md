# Ω-MEM-3 — Memory and Emergent Order / Time

Status: PROTOCOL DRAFT — NOT YET RUN
Date: 2026-08-10

## Research direction

The next Ω-Lab stage investigates memory and time together rather than treating them as independent objects.

Working idea:

> Memory preserves distinctions between prior states; temporal order may be reconstructed from changes in that preserved state.

This is a hypothesis, not an established physical claim.

## Starting point

Ω-0 showed in a minimal machine that an updating trace can create distinguishable internal phases without an externally supplied clock.

Ω-MEM-1 showed that a state with at least two possible values can have a causal effect on later outputs, while a single-state memory cannot.

Ω-MEM-2 showed that memory can be predictive, but its usefulness depends on the relationship between memory structure and process structure.

## Main question

Can temporal order be reconstructed from memory transitions alone, without supplying an external time variable (`t`, `dt`, clock ticks, timestamps or ordered history as an independent input)?

## Secondary questions

1. What is the minimum memory structure required to distinguish two internal states?
2. What is the minimum transition structure required to distinguish "before" from "after"?
3. Can a system reconstruct temporal order from state transitions alone?
4. Does removing memory destroy the internally reconstructed order?
5. Can two systems have the same instantaneous state but different memory histories and therefore different future behaviour?
6. Is temporal direction equivalent to an asymmetry in memory transitions, or does an additional primitive remain necessary?

## Controls

### M0 — no memory
No persistent state. No internal ordering variable.

### M1 — static memory
Persistent state exists but cannot be updated.

### M2 — binary updating memory
Two states with a deterministic transition rule.

### M3 — reversible updating memory
Transitions can be traversed in both directions under controlled interventions.

### M4 — asymmetric updating memory
Forward and reverse transitions are deliberately made structurally different.

### Null — shuffled transitions
Preserve state counts and transition counts while destroying directional ordering.

## Critical intervention

Construct two systems with identical current observable input/state but different internal memory histories.

Then apply the same future input sequence.

Measure whether their future trajectories diverge.

If they diverge, memory carries information about the past that has causal consequences for the future.

## Time reconstruction test

The system must be asked to infer an ordering relation using only its internal state-transition structure.

No variable named time may be provided to the model.

Success requires that the reconstructed order be better than the appropriate null model.

## Important methodological constraint

Do not encode "before", "after", "+1", "-1", or a clock into the model merely under different names. If directional information is required, identify exactly where it enters.

## Expected outcomes

### Outcome A
Memory alone is sufficient to reconstruct order.

### Outcome B
Memory preserves distinctions but cannot generate direction without an additional asymmetry.

### Outcome C
The apparent temporal order is an artifact of externally imposed sequence/iteration.

### Outcome D
A smaller primitive than the current memory model is sufficient.

All outcomes are valid research results.

## Status rule

This protocol does not claim that physical time is emergent. It tests only whether a formal system can reconstruct an internal order without taking an external time variable as a primitive.

## Reproducibility

Before execution, record:
- complete source code;
- parameters;
- seeds;
- transition tables;
- success/failure criteria;
- null-model construction;
- intervention procedure.

After execution, preserve raw output, analysis code, figures and report.

Nothing from earlier experiments may be deleted when this experiment produces a contradiction.
