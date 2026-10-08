# Ω-LAB — GEOMETRY FOUNDATION EXPERIMENT LEDGER v1.0

STATUS: ACTIVE / EXPERIMENTAL FOUNDATION
DATE: 2026-10-08

## Purpose

This ledger records experiments that test the geometry-as-relational-foundation program.

It is an experimental ledger, not a declaration of proof.

Every experiment must preserve:
- hypothesis;
- null/control;
- model and code;
- parameters;
- seeds;
- raw/derived results;
- negative results;
- interpretation;
- next decision.

## Foundation under test

`RELATION → GEOMETRY → CONFIGURATION → TRANSFORMATION → TRACE → STRUCTURE → NEW RELATIONS ↺`

Working state:

`G = (R, B, S, T, M)`

R = relations; B = boundaries; S = state/configuration; T = ordered transformations; M = retained trace.

## Experiment 001 — Dynamic memory / growing geometry

### Question

Does persistent memory and the ability to expand the represented state-space improve prediction/adaptation when the environment introduces genuinely new states?

### Model

Toy discrete dynamical environment.

- 20,000 steps
- initial state count: 8
- environment expansion probability: approximately 0.00035 per step
- expansion adds 1–3 states
- maximum state count: 24
- random perturbation: approximately 8%
- 30 independent seeds

Compared:
1. FLAT — last observed transition only
2. MEMORY — exponentially weighted transition statistics with fixed representation
3. BOUNDARY — MEMORY plus a simple threshold boundary
4. GROW — memory plus ability to represent new states

### Observed aggregate result

Mean accuracy:
- FLAT: ~0.0784
- MEMORY: ~0.8354
- BOUNDARY: ~0.8354
- GROW: ~0.8732

These values are from a toy simulation and must not be interpreted as biological or physical evidence.

### Result

- Memory produced the dominant improvement over flat history.
- The implemented simple boundary filter added essentially no measurable benefit.
- Growing representation improved performance over fixed-memory representation in this toy environment.

### Negative result

The current boundary implementation did not demonstrate an independent advantage.

Therefore **BOUNDARY remains unresolved**. It must not be promoted merely because it is part of the conceptual architecture.

### Interpretation

Supported at toy-model level:
- retained transition history can improve prediction;
- representational growth can improve adaptation when new states appear.

Not established:
- universal geometry;
- brain mechanism;
- physical law;
- self-awareness;
- Gödel mechanism.

### Next test

Replace the arbitrary threshold boundary with a dynamically measurable boundary based on relational/predictive structure, while controlling model capacity.

Required comparison:
A. no boundary
B. threshold boundary
C. learned dynamical boundary
D. learned boundary + growth

## Experiment 002 — Geometry / memory / cycle distinction

### Status

FORMALIZATION / NEXT EXPERIMENT.

### Question

Can a recurrent relational form be distinguished from a return to the previous state?

### Working prediction

A system may reproduce the same relational topology while carrying a different retained trace.

Test criterion:

`topology(G_t) ≈ topology(G_{t+n})`

while

`M_t ≠ M_{t+n}`

and/or future action distributions differ.

### Required controls

- same topology, different history;
- same history, different topology;
- closed relation without memory;
- closed relation with retained trace.

No claim of proof until executed.

## Experiment 003 — Boundary as dynamical separation

### Status

PREREGISTRATION TARGET / NOT YET EXECUTED.

### Hypothesis

A meaningful boundary should emerge from differences in internal versus external transition dynamics rather than from an arbitrary threshold.

Candidate measurements:
- predictive information;
- temporal persistence;
- graph conductance / cut structure;
- intervention-based causal influence;
- description-length/compression gain.

### Falsification

Reject the boundary mechanism if it does not:
1. emerge without manual labels;
2. remain stable under noise;
3. predict perturbation behavior better than controls;
4. improve adaptation under controlled environmental change.

## Experimental integrity rule

No result may be marked CONFIRMED unless the experiment was actually executed with preserved code, parameters, seeds, controls and output.

A failed experiment is retained.

A null result is retained.

A coding artifact is retained as an artifact and must not be promoted into a relation.

