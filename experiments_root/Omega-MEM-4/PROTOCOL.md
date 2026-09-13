# Ω-MEM-4 — EXPRESSIVENESS × STRUCTURAL MATCH

**Protocol status:** PRE-REGISTERED BEFORE EXECUTION  
**Date:** 2026-08-10  
**Target:** H-MEM-2.2

## Main question

Is the failure of the P3 Thue–Morse matched architecture caused by insufficient expressive capacity, incorrect structural matching, or both?

## H-MEM-2.2

Prediction value of memory depends on structural correspondence between memory update and process pattern **provided that the memory architecture is sufficiently expressive to represent the relevant structure**.

Operational form:

`Prediction Advantage = f(Structural Match, Expressive Capacity)`

No functional form is assumed in advance.

## Processes

1. Periodic-4 positive control.
2. True Markov-2 process using the pair `(X[t-1], X[t])`.
3. Thue–Morse.
4. Genuine two-state HMM with fixed transition and observation matrices.
5. Random-iid negative control.

## Memory families

- Baseline: S=1.
- Context-k, k=0..4.
- Counter/cyclic finite-state memory.
- Random finite-state machine.
- Process-specific matched architecture.
- Oracle/ideal representation where formally defined.

State-size sweep:

`S = 1, 2, 4, 8, 16, 32, 64, 128`

Use the largest range only where meaningful and computationally practical.

## Required metrics

For every process × architecture × S:

1. Accuracy.
2. Baseline accuracy.
3. Prediction advantage = accuracy - baseline.
4. Conditional entropy `H(next | state)`.
5. Unconditional entropy `H(next)`.
6. Number of reachable states.
7. Effective state entropy.
8. Intervention effect.
9. Memory lifetime / reconvergence time.
10. Permutation control.
11. Train/test generalization.
12. 95% confidence intervals.

## Controls

### Size control

Same S, different architectures.

### Structure control

Same architecture, different S.

### Positive control

Periodic-4 should reveal a known phase-memory threshold.

### Negative control

Random-iid should remain approximately at baseline regardless of memory structure or state count.

## Strict intervention

For history `P` and future `F`:

CONTROL:

`run(P)` then `F`.

INTERVENTION:

`run(P[:k])`, reset state, then the identical `F`.

Measure both state and output divergence. Where feasible, enumerate all reachable reset states.

## Markov-2 requirement

The generator must depend on the previous two observations. Explicitly define the four context states `XX, XY, YX, YY` and a fixed transition table before execution.

## HMM requirement

Use a real hidden-state process with a fixed transition matrix and observation matrix. The matched representation must be a genuine posterior/belief state or a declared discretization of it. The previous `X→0, Y→1` heuristic is not acceptable as a Bayesian estimator.

## Thue–Morse requirement

Do not assume that O(log n) memory is required. Measure expressive capacity empirically. Sweep finite contexts, counters, position representations and state sizes. Report the minimum tested representation that obtains a stable advantage, if any.

## Statistical requirements

Use paired comparisons on identical seeds for key architecture contrasts:

- Matched vs Mismatched.
- Matched vs Context.
- Matched vs Random.
- S_low vs S_high.

Report mean, standard deviation, 95% CI and paired differences. Do not choose the primary metric after seeing results.

## Failure criteria

H-MEM-2.2 is weakened or broken if:

1. increasing expressive capacity does not rescue matched architectures where representation should become sufficient;
2. random architectures systematically beat matched architectures after controlling for S;
3. iid random produces a reproducible memory advantage;
4. permutation preserves the advantage;
5. predictive states show no causal intervention effect;
6. effects disappear across seeds;
7. the apparent advantage is explained entirely by state count rather than structure.

## Interpretation rule

Do not infer a general law from one architecture. Distinguish:

**OBSERVATION → INTERPRETATION → HYPOTHESIS.**

A failure of a matched implementation first falsifies that implementation's adequacy, not necessarily the abstract structural-match principle.

## Required artifacts

- `omega_mem4.py`
- `omega_mem4_protocol.json`
- `omega_mem4_data.json`
- `omega_mem4_results.png`
- `omega_mem4_report.txt`
- updated `01_Hypotheses.md`
- updated `RESEARCH_STATUS.md`
- updated Ω-Lab graph/history
