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

EXECUTED — TOY RESULT RECORDED 2026-10-08.

Result: a fixed 12-state relational ring reproduced the same topology while retained trace differed strongly between equivalent positions separated by one cycle. See `EXPERIMENTS/RESULTS/GEOMETRY_FOUNDATION_RESULTS_2026-10-08.md`.

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

EXECUTED — CURRENT LEARNED-BOUNDARY METHOD NEGATIVE 2026-10-08.

A spectral/Fiedler boundary failed to reliably recover the planted dynamical boundary. A simple retention threshold succeeded because it encoded the same defining statistic. Therefore the learned-boundary mechanism is not promoted. Full result is in `EXPERIMENTS/RESULTS/GEOMETRY_FOUNDATION_RESULTS_2026-10-08.md`.

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



## Full independent rerun — 2026-10-10

A reproducible NumPy-only runner was added at `EXPERIMENTS/geometry_foundation_full_run.py`, with CI workflow `.github/workflows/geometry-foundation-full-run.yml`. Run: https://github.com/SmartVoltISA/Omega-lab-.--.-/actions/runs/37998378477

Raw per-seed output and summary:
- `EXPERIMENTS/RESULTS/GEOMETRY_FOUNDATION_FULL_RUN_2026-10-10.json`
- `EXPERIMENTS/RESULTS/GEOMETRY_FOUNDATION_FULL_RUN_2026-10-10.md`

Verified run counts: EXP-001 30; EXP-002 30; EXP-003 50; EXP-004 150 (30 × 5 conditions); EXP-005 30; EXP-006 80 (40 modular positive-control + 40 homogeneous null). CI validation and artifact upload passed; generated results were committed to the repository.

### Results of this independent operationalization

- **EXP-001:** fixed-representation FLAT accuracy 0.1143 ± 0.0499; fixed MEMORY 0.1781 ± 0.0691; simple BOUNDARY 0.1781 ± 0.0691; GROW 0.2147 ± 0.0615 (30 seeds). The boundary threshold added no measurable advantage over MEMORY. GROW did better in this benchmark, but the implementation is a new operationalization and must not be numerically conflated with earlier reported values.
- **EXP-002:** fixed 12-node ring returned to the same topology while the retained trace differed; mean trace delta 1.125 in this run. This is a toy recurrence/history distinction only.
- **EXP-003:** the spectral partition recovered the hidden 6+6 modular positive control with F1 = 1.000 ± 0.000 (50 seeds). Since the generator contained the hidden modules, this is recovery, not spontaneous boundary creation.
- **EXP-004:** hidden 6+6 boundary F1 averaged 1.000 for cross-module probabilities 0.10–0.40 and 0.994 ± 0.030 at 0.45 (30 seeds per condition). Held-out within-partition transition rate fell from 0.901 at cross=0.10 to 0.550 at cross=0.45. This is robustness under a planted positive control, not proof of a fundamental boundary.
- **EXP-005:** under homogeneous relational reinforcement with no supplied groups, candidate cut conductance was 0.5476 ± 0.0102, worse than the mean random balanced-partition cut 0.5217 ± 0.0008 (30 seeds; 100 random balanced controls per seed). This is negative evidence for the current spontaneous-boundary mechanism.
- **EXP-006:** in the planted modular positive control, inferred partition F1 = 1.000; crossing probability for an intervention row rose from 0.150 to 0.500 (delta +0.350), while a random balanced partition changed by about +0.0015 on average. In the homogeneous condition, the inferred partition's crossing delta was +0.055 ± 0.098, with substantial variability. Thus the test distinguishes the deliberately modular positive control, but does not demonstrate a robust spontaneously formed causal boundary in the homogeneous system.

### Integrity / limitations

These are new independent implementations where exact historical source code was not available; historical results remain preserved and were not overwritten. The EXP-006 statistic was revised during testing: long-run module occupancy was rejected as an unsuitable measure for a symmetric two-module Markov chain, and replaced with the direct one-step boundary-crossing probability under a controlled row intervention. The runner's successful CI status confirms execution and row-count validation, not scientific validity.

Current decision:
1. Memory and representational growth improve prediction in this particular toy benchmark; the simple threshold boundary does not add value beyond memory.
2. Recurrent topology can coexist with a different retained trace in the ring model.
3. A planted dynamical boundary is recoverable from transition structure.
4. No meaningful spontaneously emerging boundary is demonstrated under the current homogeneous relational-learning rule.
5. EXP-006 remains an exploratory positive-control intervention test, not a certified general causal-boundary detector.

No result here establishes a universal law of physical space, consciousness, or nature.


### Identifier crosswalk to the infographic

The numbering in the infographic differs from the repository ledger numbering for the first three experiments. To avoid accidental mis-citation:
- Infographic EXP-001 (ring/cycle and memory) → repository rerun EXP-002.
- Infographic EXP-002 (spectral boundary instability) → repository historical boundary-method result EXP-003 / `GEOMETRY_FOUNDATION_RESULTS_2026-10-08.md`.
- Infographic EXP-003 (memory and representational growth) → repository rerun EXP-001.
- Infographic EXP-004 (recovery of a hidden relational boundary) → repository rerun EXP-004.
- Infographic EXP-005 (spontaneous boundary without supplied groups) → repository rerun EXP-005.
- Infographic EXP-006 (functional boundary under intervention) → repository rerun EXP-006.

The runner IDs follow the repository ledger and are not silently renumbered to match the image.
