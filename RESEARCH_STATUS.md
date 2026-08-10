# Ω-Lab Research Status

**Snapshot:** 2026-08-10

## 1. Ω-0 — Internal order and trace

**Question:** what minimum structure is required for internally distinguishable order and functional memory without an explicit physical-time variable?

**Result:** the tested updating-trace construction produces internally distinguishable order.

**Correct scope:** this is a model result about internal order, not proof that physical time emerges from nothing. The computation itself is externally sequential.

**Status:** PARTIALLY CONFIRMED as a minimal model result.

## 2. Ω-MEM-1 — Functional and causal memory

The minimal finite-state experiments show that an updating retained state can affect future outputs under intervention in the tested architectures. S=1 has no alternative internal state; S=2 can support causal effects.

**Status:** PARTIALLY CONFIRMED.

Important corrections are archived in `AUDIT_2026-08-10.md`: the first strict intervention was flawed; capped lifetime/decay windows are lower bounds, not exact lifetimes; early deterministic prediction tests were partly tautological.

## 3. Ω-MEM-2 / H-MEM-2

The research moved from existence of memory toward predictive information and structural correspondence.

**H-MEM-2:** PARTIALLY CONFIRMED.

## 4. Ω-MEM-3 — Generalization attempt

Results:

- P1 Periodic-4: Matched 1.000 vs Mismatched 0.750 → supports structural match in the tested architecture.
- P2 Markov-like: Matched 0.679 vs Mismatched 0.491 → supports structure-aware prediction, but the previous generator was actually first-order in the tested prediction behaviour.
- P3 Thue-Morse: Matched 0.556 = Mismatched 0.556; Context 0.668 → counterexample to universal superiority of the tested matched implementation.
- P4 HMM-like: Matched 0.705 vs Mismatched 0.499 → supports structure-aware memory, but the matched estimator was not a genuine Bayesian filter.
- P5 Random-iid: all ≈0.50 → negative control works.

**H-MEM-2.1:** REFINED.

The result establishes a failure mode of a specific matched architecture but does not establish the minimum memory complexity of Thue–Morse.

## 5. Ω-MEM-4 — Expressiveness × Structural Match

The experiment was designed to separate structural match from expressive capacity. The submitted implementation produced useful exploratory observations, including the Periodic-4 S=4 threshold, strong Thue-Morse context prediction, increasing performance of random FSMs with S, and a working iid negative control.

However, the run did **not** satisfy its own pre-registered protocol. The full audit is in:

`experiments/Omega-MEM-4/AUDIT_MEM4_2026-08-10.md`

Critical issues:

1. Context-2 stores only one previous symbol and is effectively Context-1.
2. P3 Matched is forcibly fixed at S=2, so the expressive-capacity sweep does not actually test matched expressiveness.
3. P3 Matched is not a genuine online position/carry representation of Thue–Morse.
4. Random S=64 vs Matched S=2 is not a controlled same-S comparison.
5. The claimed Periodic-4 intervention drop is inconsistent with reset_step=500 for a period-4 counter.
6. Required 95% CIs, paired comparisons, unconditional entropy, reachable-state counts, effective state entropy, memory lifetime/reconvergence and full raw per-seed data were not archived.
7. Permutation evidence is predictive-information evidence, not a standalone proof of causality.

Therefore Ω-MEM-4 is classified as **EXPLORATORY / NEEDS CORRECTED REPLICATION**, not as a clean confirmation of H-MEM-2.2.

### Current hypothesis statuses

**H-MEM-2:** PARTIALLY CONFIRMED.

**H-MEM-2.1:** REFINED.

**H-MEM-2.2:** REFINED / NEEDS_RETEST.

**H-MEM-2.3:** OPEN.

A useful weaker candidate formulation is:

> Prediction advantage depends on whether the memory state is a sufficiently informative representation of the predictive state, subject to capacity and implementation constraints.

This formulation is intentionally weaker than the earlier universal structural-match claim.

## 6. Required corrected experiment: Ω-MEM-4R

Before moving to a definitive Ω-MEM-5 claim, run a corrected replication:

- true Context-k implementations;
- true same-S matched/mismatched/random comparisons;
- a genuine Thue-Morse position/carry representation and explicit finite approximations;
- actual matched S sweep;
- multiple random FSMs per condition;
- paired seed-level contrasts and 95% CIs;
- unconditional and conditional entropy;
- reachable-state and effective-state statistics;
- strict intervention with non-equivalent reset states;
- recovery-time / memory-lifetime measurement;
- full raw per-seed data;
- machine-readable protocol and results;
- no claim of O(log n) necessity without a dedicated complexity experiment.

Primary falsification question:

> At equal effective capacity, does a correctly matched representation outperform an equally expressive structurally mismatched representation?

Secondary question:

> Can a learner discover a predictive-state representation without being told the process-specific structure?

## 7. Ω-B — internal dynamics

The original self-organizing/self-will interpretation was not established. Controls exposed dependence on diffusion rules and an architectural artifact. Candidate effects remain under investigation with stronger null models and spatial shuffling.

## 8. Ω-C — critical connectivity

OPEN research direction: whether stable organization occupies a bounded connectivity regime measurable through quantities such as algebraic connectivity, spectral gap, percolation threshold and resilience.

## 9. Methodological rules

1. Do not treat attractive visualizations as evidence by themselves.
2. Separate data, observation, interpretation and hypothesis.
3. Fix metrics and thresholds before inspecting final results when possible.
4. Preserve negative results and detected artifacts.
5. Compare against null models and conventional models.
6. Archive code, parameters, seeds and raw outputs.
7. Never rename an unexplained effect as a mechanism.
8. Do not protect an Ω hypothesis from falsification.
9. Distinguish state count from expressive capacity.
10. Distinguish predictive correlation from causal memory via intervention.
11. Do not claim a controlled comparison when state capacity differs.
12. Preserve submitted implementations separately from corrected replications.

## 10. Current research order

```text
Ω-0
  ↓
internal order / trace
  ↓
Ω-MEM-1
  ↓
minimum causal memory
  ↓
Ω-MEM-2/3
  ↓
predictive memory and structural match
  ↓
Ω-MEM-4 exploratory result + audit
  ↓
Ω-MEM-4R corrected capacity × structure test
  ↓
Ω-MEM-5 adaptive predictive-state discovery
  ↓
Ω-0.6 / minimal comparison
  ↓
relation classes / nodes / structures
  ↓
only then: higher-level physical interpretation
```

The project must not jump from philosophical framing directly to physical claims.
