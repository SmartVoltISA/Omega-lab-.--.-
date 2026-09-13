# Ω-BASIS-002 — STATE vs TIME

Date: 2026-08-13
Status: **PLANNED / PREREGISTERED**

## Question

Can the dimensionality required to describe a state be separated from the dimensionality/complexity required to describe transitions between states?

This experiment is deliberately abstract. It must not assume that time is itself a state component.

## Models

### M0 — Static state
A state is a vector `S=(x1,...,xd)` sampled independently. There is no transition rule.

### M1 — Deterministic transition
`S(t+1)=F(S(t))`, with F fixed and known.

### M2 — Stochastic transition
`S(t+1) ~ P(. | S(t))`.

### M3 — Hidden-memory transition
`S(t+1)` depends on a finite history, not only on the current S(t).

## Primary distinction

1. **State dimension:** minimum linear dimension needed to reconstruct individual states under the declared observation map.
2. **Transition description:** minimum description needed to predict the next state from the permitted history.
3. **Trajectory complexity:** description length/entropy/complexity of the complete sequence.

These are different quantities and must not be added as if they were coordinate dimensions.

## Falsification targets

The hypothesis "time is only a transition parameter, not a state component" is weakened if a model requires an explicit time coordinate to reconstruct its state distribution after all declared state variables are included.

The hypothesis is also weakened if a transition rule cannot be represented without embedding an equivalent time variable when the process is otherwise stationary.

Conversely, if stationary systems can be represented with fixed state variables plus a transition operator, while explicit time adds no predictive information, that supports separation of state and time in this model class.

## Required analyses

For every model:
- rank/PCA reconstruction of state vectors;
- one-step prediction error;
- multi-step prediction error;
- conditional entropy `H(S[t+1]|S[t])` where applicable;
- compare with `H(S[t+1]|S[t],t)`;
- description-length proxy for transition rule;
- permutation/time-shuffle control;
- repeated seeds;
- independent implementation of primary calculations.

No post-hoc choice of dimensionality threshold is allowed.

## Critical controls

A time-shuffle control must destroy temporal ordering while preserving the marginal state distribution. If a purported state-dimension result changes under mere reordering, it is not a pure state-dimension result.

A stationary transition model must be tested against an explicit clock variable. If adding the clock does not improve out-of-sample prediction, the clock is unnecessary for that model.

## Status rule

This file contains a protocol only. No result is claimed until code is executed, repeated, independently checked, and archived.
