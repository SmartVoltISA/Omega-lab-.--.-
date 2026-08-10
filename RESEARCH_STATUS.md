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
- P2 Markov-like: Matched 0.679 vs Mismatched 0.491 → supports structural match, but the previous generator was actually first-order.
- P3 Thue-Morse: Matched 0.556 = Mismatched 0.556; Context 0.668 → counterexample to universal superiority of the tested matched architecture.
- P4 HMM-like: Matched 0.705 vs Mismatched 0.499 → supports structure-aware memory, but the matched estimator was not a genuine Bayesian filter.
- P5 Random-iid: all ≈0.50 → negative control works.

**H-MEM-2.1:** REFINED.

The result establishes a failure mode of a specific matched architecture but does not by itself establish the minimum memory complexity of Thue–Morse.

## 5. H-MEM-2.2 — Expressiveness condition

> Prediction value depends on structural match provided memory expressive capacity is sufficient to represent the relevant structure.

**Status:** OPEN.

## 6. Ω-MEM-4 — next experiment

Target: **EXPRESSIVENESS × STRUCTURAL MATCH**.

Required controls:

- same S, different architecture;
- same architecture, different S;
- true Markov-2;
- genuine HMM belief state;
- Thue-Morse state-size/architecture sweep;
- conditional entropy;
- paired intervention;
- permutation controls;
- positive Periodic-4 control;
- negative Random-iid control.

Protocol is archived in `experiments/Omega-MEM-4/PROTOCOL.md`.

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
Ω-MEM-4
  ↓
expressive capacity × structural match
  ↓
Ω-0.6 / minimal comparison
  ↓
relation classes / nodes / structures
  ↓
only then: higher-level physical interpretation
```

The project must not jump from philosophical framing directly to physical claims.
