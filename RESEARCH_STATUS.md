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

Results included support for structural prediction on some processes and a Thue-Morse counterexample. H-MEM-2.1 was therefore refined rather than universally confirmed.

**H-MEM-2.1:** REFINED.

## 5. Ω-MEM-4 — Exploratory expressiveness experiment

Ω-MEM-4 produced useful observations but violated parts of its intended protocol. The audit identified broken Context-2, forced capacity overrides, unequal comparisons, inadequate matched Thue-Morse representation and incomplete controls.

**Status:** EXPLORATORY / NEEDS CORRECTED REPLICATION.

Ω-MEM-4 remains archived and is not deleted or rewritten as if it never occurred.

## 6. Ω-MEM-4R — Corrected controlled replication

**Date:** 2026-08-10  
**Status:** COMPLETED  
**Hypotheses:** H-MEM-2.2, H-MEM-2.3

The protocol was fixed before execution. The corrected run used:

- validated true Context-2/3 shift registers;
- equal-S comparisons where valid;
- 10 independent random FSMs per random condition;
- an explicitly second-order Markov generator;
- a discretized HMM Bayesian belief-state implementation;
- intervention reset states checked to differ from control;
- recovery horizons 1–128;
- per-seed accuracy arrays.

### Key observations

**P1 Periodic-4:** Counter S=4 reaches 1.000; S<4 is approximately baseline. This supports an expressive-capacity threshold for this architecture/process pair.

**P2 Markov-2:** Context-1 = Context-2 = Context-3 = Matched ≈ 0.823 in the tested generator. The tested transition table is already predictable from the last-symbol partition, so additional context adds little predictive information. This is evidence for a process-specific minimal sufficient statistic, not a universal statement about all Markov-2 processes.

**P3 Thue-Morse:** the chosen matched position-counter is ≈0.500 for all tested S, while Random S=64 reaches ≈0.730 and Context-2/3 ≈0.666. This is the critical counterexample. It shows that a nominal structural label is not sufficient if the implementation does not encode the relevant predictive information.

**P4 HMM:** Context-1 ≈0.704; Matched is ≈0.702 at S=8 and falls to ≈0.696 at S=64. Conditional entropy falls with S, but predictive accuracy does not improve, consistent with discretization/sparse-state implementation loss.

**P5 Random-iid:** all architectures remain approximately 0.500. Negative control works.

### Equal-S comparison

Representative results:

| Process | S | Matched | Random | Winner |
|---|---:|---:|---:|---|
| Periodic-4 | 8 | 1.000 | 0.844 | Matched |
| Markov-2 | 4 | 0.823 | 0.634 | Matched |
| Thue-Morse | 8 | 0.500 | 0.632 | Random |
| HMM | 8 | 0.702 | 0.613 | Matched |

Reported paired t-tests were significant in all four comparisons (p<0.001): Periodic t=29.4; Markov-2 t=25.1; Thue-Morse t=-15.2; HMM t=8.7.

These statistical values are archived as **reported experiment outputs**; they are not independently rerun by this repository unless an executable reproduction is separately archived and executed.

### Hypothesis status after Ω-MEM-4R

**H-MEM-2.2: REFINED.** The equal-S prediction is supported for 3/4 tested structured processes but fails for Thue-Morse under the chosen matched implementation. The universal claim "Matched always wins at equal S" is therefore not accepted.

**H-MEM-2.3: PARTIALLY CONFIRMED.** The run supports four components: expressive threshold, process-specific minimal sufficient statistic, implementation/discretization loss, and successful iid negative control. Counterevidence remains the Thue-Morse failure and the ability of random features at high S to outperform a hand-designed matched implementation.

## 7. Required next control

Before treating H-MEM-2.3 as stable, perform an independent replication or theoretical analysis. If it survives, proceed to Ω-MEM-5:

> Can a system autonomously discover a minimal sufficient predictive state without hand-designing the process-specific architecture?

Ω-MEM-5 is therefore **conditional**, not yet a confirmed conclusion.

## 8. Ω-B — internal dynamics

The original self-organizing/self-will interpretation was not established. Controls exposed dependence on diffusion rules and an architectural artifact. Candidate effects remain under investigation with stronger null models and spatial shuffling.

## 9. Ω-C — critical connectivity

OPEN research direction: whether stable organization occupies a bounded connectivity regime measurable through quantities such as algebraic connectivity, spectral gap, percolation threshold and resilience.

## 10. Methodological rules

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
13. Treat a process-specific matched architecture as an implementation, not as a proof of universal structural correspondence.

## 11. Current research order

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
independent check / theory of H-MEM-2.3
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
