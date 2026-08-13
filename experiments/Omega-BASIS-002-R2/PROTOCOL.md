# Ω-BASIS-002-R2 — STATE vs TIME, Stratified Replication

Date: 2026-08-13
Status: PLANNED / PREREGISTERED

## Objective
Test only whether a regime/time variable contains predictive information beyond the observable state for stationary and deliberately nonstationary processes.

## Models
M1 deterministic flip: x[t+1]=1-x[t].
M2 stationary Markov: stay probability 0.8 at all times.
M3 piecewise-stationary Markov: stay probability 0.9 in regime 0 and 0.6 in regime 1; regime boundary is at the midpoint.

## Critical correction from R1
Both regimes must occur in both training and test sets. We therefore use a stratified evaluation: within each regime, alternate samples by deterministic index parity into train/test. Temporal order is retained for generation; only the evaluation split is stratified. The model never receives future outcomes.

## Primary models
A: empirical P(x[t+1]|x[t]) trained from training samples.
B: empirical P(x[t+1]|x[t], regime[t]) trained from training samples.

## Metrics
Held-out negative log-likelihood and Brier score. Report B-A improvement per seed and aggregate mean, SD, bootstrap 95% CI over 100 preregistered seeds.

## Controls
1. M1/M2 should show no systematic benefit from regime because their transition law is stationary (M1 is deterministic).
2. M3 should show a benefit if the regime is predictive beyond state.
3. Shuffle-control: independently permute regime labels across observations while preserving x and y. This destroys correspondence between regime and transition law; B should lose its M3 advantage.
4. Repeat exact implementation with the same seeds and independently recompute aggregate statistics from archived per-seed rows.

## Falsification
The state/time-separation claim is weakened if regime materially improves prediction for stationary M1/M2, or if it fails to improve prediction for M3 despite the known regime-dependent transition law.

## Boundary
This tests predictive sufficiency of an explicit regime variable. It does not establish that time is ontologically fundamental, nor that time can never be encoded as part of state/history.

No result is claimed until execution, repeatability, and independent recomputation pass.
