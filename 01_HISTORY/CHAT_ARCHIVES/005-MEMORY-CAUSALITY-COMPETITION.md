# Ω-LAB — ARCHIVE 005

## Direction
**MEMORY / CAUSALITY / COMPETITION / CRITICAL CONNECTIVITY**

## Source
Uploaded historical archive: `OMEGA_CHAT_FULL_ARCHIVE-3.md`.

## Archival status
This document preserves the supplied archive as a historical source. The source itself states that the full original transcript was unavailable and that some material was reconstructed from available project context. Therefore reconstructed material must not be treated as a verbatim transcript.

---

# PART I — SOURCE ARCHIVE

The supplied archive covers the following established context:

- Ω-Lab as an open experimental laboratory.
- Principle: «НЕ ВЕРИТЬ — ПРОВЕРЯТЬ».
- Ω-1: comparison as a basic operation instead of the initial difference/equality pair.
- Minimal pair: Comparison (reading) + Modification (changing), named «Omega Breath».
- Research into memory and causality.
- Ω-0: act → trace → update.
- Ω-MEM-1: minimal functional memory.
- Preliminary S=1 / S≥2 distinction concerning causal effect.
- Need for repeatability, strict causal intervention, size-vs-structure analysis, minimality and negative/null controls.
- Cellular automata and evolutionary architecture experiments.
- Metrics: entropy, autocorrelation, Lempel-Ziv complexity, modularity, Hurst exponent.
- 256 elementary rules for N=3 states.
- Models M0–M3.
- Ω-B / «battle» experiments.
- Competing edge potentials w⁺ and w⁻ with w = w⁺ − w⁻.
- B = |dw⁺/dt| + |dw⁻/dt|.
- Ω-C / critical connectivity hypothesis.
- Interest in λ₂, spectral gap, percolation threshold and resilience.
- Methodological requirements: preregistration, negative controls and avoidance of post-hoc tuning.
- «Zero step»: demonstrate that a model cannot be made simpler.
- Goodhart's law and multiple-comparisons concerns.
- Interest in phase boundaries, plasma, crystal, gas, water, structure and memory.
- Possibility that an interaction boundary can generate a new structure C rather than merely selecting A or B.

---

# PART II — KNOWLEDGE EXTRACTION

## Core ideas

### I-001 — Comparison as a fundamental operation
`comparison → {equality, difference}`

Comparison was proposed as a more basic operation than beginning with the categories difference and equality.

### I-002 — Omega Breath
Minimal pair:
- Comparison — reading/comparison;
- Modification — changing.

Named «Omega Breath».

### I-003 — Memory as a causal factor
Ω-MEM-1 asks what minimal structure is required for a past state to become a causal factor of a future state.

### I-004 — Critical connectivity
Ω-C proposes that stable systems may exist only within a range of connection organization:
- below C_min — possible collapse;
- above C_max — possible instability/reorganization.

This remains a hypothesis, not an established law.

---

# Definitions

### Ω-0
**act → trace → update**

### Ω-B
Battle / competition of opposing processes.

### Ω-C
Critical Connectivity / critical connectivity.

### Omega Breath
Comparison + Modification.

---

# Hypotheses

### H-001 — Minimal functional memory
Preliminary formulation:
- S=1: causal effect provisionally absent;
- S≥2: causal effect provisionally appears.

Status: DEVELOPMENT / OPEN.

Not a universal law without controls and further experiments.

### H-002 — Critical connectivity range
Stability may depend on connectivity remaining inside a critical range.

Status: OPEN / UNTESTED as a universal formulation.

---

# Experiments

## EXP-001 — Cellular automaton baseline
Parameters:
- N=100;
- p=0.3;
- 1000 runs.

Observation:
- collapse occurred in 100% of runs.

Status: TESTED.

## EXP-002 — Hysteresis + separated timescales
Changes:
- hysteresis T=0.3;
- 10 weight updates per state update.

Parameters:
- 200 runs.

Result:
- collapse still occurred in 100% of runs.

Status: TESTED.

## EXP-003 — Edges-only model
Model:
- weights evolve;
- node states are not used.

Parameters:
- 200 runs.

Results:
- Attractor: 15 (7.5%);
- Collapse: 0%;
- Cycle: 185 (92.5%);
- mean steps to attractor: 632.3 ± 298.2.

Status: TESTED.

---

# Ω-B experiment

Model:
- 1000 nodes;
- random initial connections;
- initial connection strength 0..1;
- strengthening on interaction;
- weakening when unused;
- creation of new links randomly or through neighbours;
- 30 parallel random walks per step to avoid collapse.

Parameter grid:
- α ∈ {0.05, 0.10, 0.20, 0.30};
- β ∈ {0.01, 0.02, 0.04, 0.08};
- 2 repeats per grid cell;
- 3000 steps;
- snapshots.

Observation:
β affected the regime more strongly than α.

Example for β=0.01:
- giant_frac ≈ 0.95;
- about 60 clusters;
- modularity ≈ 0.26.

Longer run:
- 12,000 steps;
- β ∈ {0.015 ... 0.03};
- 2 repeats;
- snapshots every 500 steps.

Plateau observation:
metric derivatives decreased by approximately 6–9× between the first and second halves.

For β=0.02:
- |d(giant_frac)/dt|: 0.000071 → 0.000011;
- |d(num_clusters)/dt|: 0.067 → 0.009.

At t=6000 → t=12000:
- giant_frac: 0.593 → 0.576;
- clusters: 398 → 408.

Interpretation in the supplied archive:
visual plateau rather than simple monotonic collapse.

Status: TESTED.

---

# Mathematics / Metrics

Metrics recorded:
- entropy;
- autocorrelation;
- Lempel-Ziv complexity;
- modularity;
- Hurst exponent;
- algebraic connectivity λ₂;
- spectral gap;
- percolation threshold;
- resilience.

Ω-B relations:

**w = w⁺ − w⁻**

**B = |dw⁺/dt| + |dw⁻/dt|**

The supplied archive explicitly warns that the complete original mathematical derivation is unavailable.

---

# Code

The source indicates Python code and an experimental pipeline existed, but the complete historical code is unavailable in this archive.

Do not reconstruct missing code as if it were original.

---

# Methodological warnings

The archive records requirements to:

- avoid presenting preliminary results as universal laws;
- perform repeatability checks;
- use causal intervention;
- separate system size from structure;
- test minimality;
- use negative/null controls;
- avoid post-hoc tuning;
- account for Goodhart's law;
- account for multiple comparisons;
- preserve negative results;
- use preregistration-like methodology;
- require a «zero step» demonstration that the model is actually minimal.

---

# Architecture

An evolutionary cycle was discussed:

population of update functions
→ fitness for stable structures
→ non-zero entropy
→ diversity
→ selection/evolution.

A reproducible experimental pipeline was also discussed.

---

# Connections

### Memory ↔ Time
Memory allows past and present states to be distinguished; time is related to the sequence of updates.

### Memory ↔ Causality
Ω-MEM-1 asks whether a past state can causally affect the future.

### Connection ↔ Structure
Connection organization affects clusters, cycles, attractors and stable structures.

### Competition ↔ Structure
Ω-B studies opposing processes and the possibility of new structure formation.

### Critical Connectivity ↔ Stability
Ω-C connects connection organization with stability and reorganization.

---

# PART III — CHRONOLOGY

1. Simple dynamic systems and cellular automata were investigated.
2. Baseline models showed collapse.
3. Hysteresis and separated timescales were introduced; collapse persisted.
4. The edges-only model removed node states; collapse disappeared and cycles dominated.
5. Evolutionary selection of update functions was proposed.
6. Ω-B investigated competition using w⁺ and w⁻.
7. Longer Ω-B runs showed plateau-like behaviour and a stronger role for β.
8. Ω-C was formulated as a critical-connectivity hypothesis.
9. Attention moved toward memory and causality.
10. Ω-0 was formulated as act → trace → update.
11. Ω-MEM-1 focused on minimal functional memory.
12. Comparison was elevated to a candidate fundamental operation.
13. Comparison + Modification was named Omega Breath.

---

# PART IV — ARCHIVAL GAPS

The supplied source explicitly identifies these limitations:

1. Full original transcript unavailable.
2. Exact message-by-message chronology unavailable.
3. Some mathematical derivations unavailable.
4. Full Python code unavailable.
5. Seeds for individual experiments unavailable.
6. Raw experimental data and outputs unavailable.
7. Full M0–M3 model definitions unavailable.
8. Not all parameters for all experiments are available.
9. The archive cannot guarantee it exhausts the entire original chat.
10. Material marked as reconstructed is not a verbatim transcript.

---

# FINAL STATE

## Finished / Recorded
- baseline collapse experiments;
- hysteresis + separated-timescale experiment;
- edges-only experiment;
- Ω-B simulation series;
- Ω-C hypothesis formulation;
- Ω-0 formulation;
- Ω-MEM-1 direction;
- comparison → {equality, difference};
- Omega Breath: Comparison + Modification;
- methodological requirements for validation.

## Started
- minimal-memory research;
- causal influence of past states;
- relationship among memory, time, connection and structure;
- criteria for stable structure.

## Unfinished
- complete validation of Ω-MEM-1;
- strict causal intervention;
- repeatability;
- minimality;
- negative/null controls;
- full validation of Ω-C;
- reconstruction of complete mathematical derivations;
- reconstruction of original code;
- complete historical chronology.

## Open questions
- What is the minimal structure of memory?
- When does the past become a causal factor of the future?
- What is the minimal connection?
- How are memory and time related?
- Can memory, time and connection be reduced to a common mechanism?
- Under what conditions does competition produce new structure?
- Does a universal critical connectivity range exist?

## Archival principle
Old versions, errors, negative results and changes of hypotheses must be preserved. History must not be rewritten retrospectively.
