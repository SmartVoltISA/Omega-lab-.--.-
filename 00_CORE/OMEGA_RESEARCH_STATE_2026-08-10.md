# Ω-Lab — Consolidated Research State

**Snapshot:** 2026-08-10

This document is a compact archival bridge between the long-running Ω research discussion and the GitHub repository. It preserves major research directions, experiments, results and unresolved questions so that future work does not depend on conversational memory alone.

## 1. Project architecture

Historical working structure:

```text
Omega/
├── 00_Axioms.md
├── 01_Hypotheses.md
├── 02_Experiments.md
├── 03_Confirmed.md
├── 04_Rejected.md
├── 05_Open_Questions.md
├── data/
├── simulations/
└── reports/
```

Current repository structure is more experimental and includes `00_CORE`, `EXPERIMENTS`, `HYPOTHESES`, `experiments`, methodology and research-status documents. The repository should gradually converge toward a clear separation of axioms, hypotheses, experiments, confirmed/rejected evidence, open questions, data, simulations and reports without deleting the historical layout.

## 2. Core Ω principle

The project began by asking whether systems can be described starting from relations rather than pre-declared entities.

Working direction:

`direction → relation → node → relation → node → graph`

Graphs are not assumed to be isolated. They can intersect and form higher-level structures.

The relation-first framing is a research method, not an established statement about physical reality.

## 3. Ω-1 / comparison

A major conceptual pivot was from treating "difference vs equality" as primitive toward treating **comparison** as the primitive operation.

Working idea:

`comparison(reading) → {equality, difference}`

A minimal pair was proposed:

- Comparison / reading.
- Modification / changing.

Together these were called the **Ω Breath** in exploratory discussion.

This remains a conceptual hypothesis requiring minimal formal tests.

## 4. Ω-0 — order, trace and memory

Three minimal models were tested:

- M0: no memory, homogeneous output.
- M1: static read-only trace.
- M2: trace is updated after each act.

M2 produced an internally distinguishable alternating pattern while no explicit physical-time variable was used.

Correct interpretation:

> The model reconstructs internally distinguishable order from act + retained trace + update. It does not prove emergence of physical time from nothing.

Known methodological limitation: the program itself is sequential, so external computational order is already present.

## 5. Ω-MEM-1 — minimum functional memory

Minimal deterministic finite-state machines were studied with inputs X/Y, finite state S and outputs A/B.

Initial S sweep:

`S = 1, 2, 4, 8, 16`

Structured memory showed functional memory for S≥2 in the tested architecture. Random null models often retained state diversity but failed the same functional-memory criterion.

The first strict intervention test was flawed because the reset made both compared systems identical after intervention. It is preserved as a failed method.

Later Ω-MEM-1a–1d used 100 seeds and a proper intervention design.

Key result:

- S=1: no causal memory in the tested architecture.
- S=2: causal effect possible.
- S=4/8/16: causal effect also possible.
- A larger state space does not automatically mean a larger causal effect.

Important correction: capped lifetime values such as 50 mean `≥50`, not exactly 50.

## 6. Ω-MEM-2 — prediction/memory direction

The research moved from merely demonstrating stateful behavior toward asking whether internal memory carries predictive information about future observations and whether the form of memory update matters.

The key distinction is now:

- memory exists;
- memory contains predictive information;
- predictive information is causally usable under intervention.

These must not be conflated.

## 7. H-MEM-2 / H-MEM-2.1

Working hypothesis:

> Prediction advantage depends on correspondence between the structure of memory updating and the structure of the process pattern.

Ω-MEM-3 generalized the test across multiple process classes and produced a reproducible counterexample.

Current status: **REFINED**, not universally confirmed.

## 8. Ω-MEM-3 results

P1 Periodic-4:

`Matched 1.0000, Mismatched 0.7501, Random 0.7238, Context 0.9994, Baseline 0.5005`

P2 Markov-like:

`Matched 0.6787, Mismatched 0.4908, Random 0.5497, Context 0.6787, Baseline 0.4835`

P3 Thue-Morse:

`Matched 0.5555, Mismatched 0.5555, Random 0.5763, Context 0.6676, Baseline 0.5001`

P4 HMM-like:

`Matched 0.7045, Mismatched 0.4990, Random 0.5789, Context 0.7041, Baseline 0.4935`

P5 Random-iid:

`Matched 0.4929, Mismatched 0.4929, Random 0.4980, Context 0.4939, Baseline 0.4965`

Permutation control showed strong non-permuted advantage for P1, P2 and P4, negligible matched advantage for P3, and no advantage for P5.

### Critical corrections

- The previous P2 generator was actually first-order Markov, not second-order.
- The previous P4 matched estimator was not a Bayesian filter; it was effectively last-observation context.
- The P3 failure does not prove O(log n) memory requirement.
- Hand-designed matched architectures confound structural correspondence and implementation/expression quality.

## 9. H-MEM-2.2

Refined hypothesis:

> Prediction value depends on structural match between memory update and process pattern, provided memory expressive capacity is sufficient to represent the relevant structure.

Current status: **OPEN**.

The central next variable is expressive capacity.

## 10. Ω-B — competing dynamics / battle

Ω-B introduced the idea of competing edge potentials:

- `w+` strengthening potential.
- `w-` inhibitory/weakening potential.
- observed relation `w = w+ - w-`.
- activity/intensity concept `B = |dw+/dt| + |dw-/dt|`.

A network simulation used random walks, adaptive edges and decay/learning parameters.

Representative observations:

- decay parameter β dominated the regime more than learning α;
- long runs showed plateauing rather than simple monotonic collapse;
- for β≈0.02, early-to-late metric derivatives dropped substantially;
- giant component fraction and cluster count approached plateaus.

Interpretation was explicitly kept separate from mechanism. Connections to coarsening dynamics, Allen–Cahn/Fisher–KPP and edge-of-chaos behavior were considered as comparison hypotheses, not as proof.

## 11. Ω-C — critical connectivity

A working hypothesis was proposed:

Stable systems may occupy a range of connectivity organization bounded by critical thresholds.

Candidate quantities:

- algebraic connectivity λ₂;
- spectral gap;
- percolation threshold;
- resilience.

The expected qualitative regimes were:

- below C_min: fragmentation/collapse;
- intermediate: stable organization;
- above C_max: instability/reorganization.

This remains an OPEN research direction requiring preregistered tests and negative-control graphs.

## 12. Evolutionary / cellular experiments

Earlier Ω-Sim work included elementary cellular automata and evolutionary update rules.

A 256-rule sweep was performed for a three-state elementary-rule space.

A 100-node experiment with random initial state p=0.3 and 1000 runs showed collapse in all runs. Adding hysteresis and separated update timescales did not prevent collapse in the tested setup.

An edge-only model behaved differently:

- attractor: 15 / 200 = 7.5%;
- collapse: 0 / 200;
- cycle: 185 / 200 = 92.5%;
- average attractor time ≈632 ± 298 steps.

This motivated an evolutionary framework with populations of update functions, fitness for stable structures, nonzero entropy and diversity.

## 13. Ω-B methodology and negative controls

The project repeatedly encountered Goodhart-like risks: optimizing a chosen metric can manufacture apparent structure.

Therefore the methodological rules include:

- preregister metrics;
- use negative-control graphs;
- avoid post-hoc parameter tuning;
- require a zero-step minimality argument where appropriate;
- distinguish structural effects from implementation artifacts.

## 14. Current open questions

1. What is the minimum expressive capacity required to represent a given predictive structure?
2. Can structural match be defined quantitatively rather than by hand-design?
3. Can memory size and memory structure be separated experimentally?
4. Can a system infer the expressive capacity it needs?
5. What happens for processes of order >2?
6. Can predictive memory be distinguished from merely correlated state?
7. What is the minimum operation set needed for comparison and modification?
8. Under what conditions do stable relation intersections produce nodes?
9. Can Ω relation-first structures reproduce known graph-theoretic results while adding useful information?
10. Which Ω-B effects survive stronger null models and spatial shuffling?

## 15. Research philosophy

Ω-Lab is not allowed to protect its preferred interpretation.

The desired outcome is the smallest set of conditions that survives attempts to break it.

A useful result can therefore be:

- confirmed;
- partially confirmed;
- refined;
- rejected;
- needs retest;
- still open.

Failure is archived as data.

## 16. Immediate next step

Run the preregistered **Ω-MEM-4: EXPRESSIVENESS × STRUCTURAL MATCH**.

Do not move to a higher-level physical interpretation until the memory/prediction layer has passed these controls.
