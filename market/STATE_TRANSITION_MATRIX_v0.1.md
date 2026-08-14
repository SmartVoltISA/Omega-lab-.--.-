# Ω-MARKET-1 — State Transition Matrix v0.1

**Status:** research record / hypothesis
**Date:** 2026-08-14
**Purpose:** фиксация текущей гипотезы о дискретных состояниях рынка и переходах между ними.

## 1. Principle

The state labels below are not treated as established market regimes. They are candidate labels for subsequent data-driven validation.

The key methodological rule is:

> Do not define the final states from visual interpretation alone. First derive candidate states from observable variables, then test whether the resulting states are stable, reproducible and useful for describing future behavior.

## 2. Candidate states

- **S0 — Compression:** reduced movement / contraction candidate.
- **S1 — Impact:** strong directional displacement candidate.
- **S2 — Continuation:** continuation of an existing directional configuration.
- **S3 — Absorption:** movement with evidence of opposing absorption / exhaustion candidate.
- **S4 — Recovery:** return from a stressed/displaced configuration toward another stable configuration.
- **S5 — New compression:** formation of a new compressed configuration after a displacement/recovery cycle.

These names are provisional and must not be treated as features supplied to the model.

## 3. Transition matrix — hypothesis v0.1

| From / To | S0 | S1 | S2 | S3 | S4 | S5 |
|---|---:|---:|---:|---:|---:|---:|
| **S0** | ✓ | ✓✓ | — | — | — | ✓ |
| **S1** | — | ✓ | ✓✓ | ✓ | ✓ | — |
| **S2** | — | ✓ | ✓ | ✓✓ | ✓ | — |
| **S3** | — | ✓ | — | ✓ | ✓✓ | ✓ |
| **S4** | ✓ | ✓ | ✓ | ✓✓ | ✓ | ✓✓ |
| **S5** | ✓✓ | ✓✓ | ✓ | — | — | ✓ |

`✓` = candidate transition.

`✓✓` = stronger candidate transition observed during the initial qualitative inspection.

These marks are **not probabilities** and are not statistically validated.

## 4. Important structural correction

A "transition" is not a state. Therefore the previous idea of adding a separate state such as `S6 = transition` is rejected for this version.

The model is represented as:

```text
States:     S0 S1 S2 S3 S4 S5
Transitions: Si → Sj
```

This keeps the state space and the transition operator conceptually separate.

## 5. Initial observable variables

The next experiment must avoid human regime labels as direct inputs. Candidate states should be derived from observable market variables such as:

```text
ΔP        price change / return
Range     candle range
Volume    traded volume
V/Range   volume density relative to range
ΔP(t+1)   subsequent response, used only for validation and never as a feature for current-state construction
```

Additional volatility-normalized variables may be introduced only after the baseline is fixed.

## 6. Falsification question

The central test is:

> Do stable and statistically distinguishable states emerge from the observable variables without imposing the S0–S5 labels beforehand?

If yes, compare the discovered clusters/states with the candidate S0–S5 interpretation.

If no, the S0–S5 scheme is considered unsupported and must be revised or discarded.

## 7. Anti-leakage rule

Future variables such as `ΔP(t+1)` may be used to evaluate whether a discovered state has predictive or transitional meaning, but must not be used to construct the current state.

No random train/test split may mix overlapping temporal windows. Validation must respect chronology.

## 8. Current status

This document records a **hypothesis**, not a result.

The next step is a data-driven state discovery experiment on the available BTC/USDT market series, followed by transition counting and out-of-sample validation.

Negative or null results must be preserved alongside positive findings.
