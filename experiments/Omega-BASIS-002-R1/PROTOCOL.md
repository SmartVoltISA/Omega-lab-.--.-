# Ω-BASIS-002-R1 — STATE vs TIME, Corrected

Status: **PLANNED / PREREGISTERED**

## Objective

Test a narrower statement:

> For a process whose observable state variables are already sufficient to specify a stationary transition law, adding an explicit clock should not improve out-of-sample prediction. For a deliberately nonstationary process, a clock or equivalent regime variable may improve prediction.

This does not test whether time is ontologically fundamental. It tests only whether an explicit time coordinate is predictive beyond state under specified models.

## Models

- M1: deterministic flip `x[t+1]=1-x[t]`.
- M2: stationary Markov chain with fixed stay probability `p=0.8`.
- M3: piecewise-stationary Markov chain with `p=0.9` before midpoint and `p=0.6` after midpoint.

## Predictors

For each model compare:

A. state-only predictor: empirical `P(x[t+1]|x[t])` trained on the training half;
B. state+time-regime predictor: empirical `P(x[t+1]|x[t], regime[t])`, where regime is determined by the known midpoint;
C. state+continuous-time predictor: logistic regression with state and normalized time as covariates, treated as a secondary control only.

The primary comparison is A vs B, because B exactly represents the declared M3 construction and does not force a linear time trend.

## Evaluation

- Generate a fixed-length sequence with a fixed preregistered seed.
- Split chronologically: first 50% training, second 50% test.
- Score negative log-likelihood and Brier score on the held-out half.
- Repeat over 100 preregistered seeds.
- Report mean difference, standard deviation, and bootstrap 95% CI.
- Independently recompute the primary score from archived predictions.

## Time-shuffle control

Shuffle the time labels/regime labels while preserving the state sequence. The regime predictor should lose its advantage when the correspondence between regime and transition probabilities is destroyed.

## Falsification

The separation claim is weakened if A and B differ systematically for stationary M1/M2, or if B fails to improve M3 despite the declared regime change.

The claim that explicit time is necessary is weakened if A is sufficient for stationary M1/M2 and B provides no systematic gain there.

## Important boundary

Even a successful result establishes only a predictive distinction between state and an explicit clock/regime variable for this model class. It does not establish a metaphysical conclusion about the nature of time.

No result is claimed until execution, repeatability, independent recomputation, and adversarial control are complete.
