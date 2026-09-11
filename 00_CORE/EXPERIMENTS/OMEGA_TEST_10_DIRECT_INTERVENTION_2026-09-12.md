# Ω-TEST-10 — DIRECT-INTERVENTION / NEGATIVE-CONTROL TEST

**Status:** COMPLETED — FAILED AS A VALIDATED EFFECT METRIC.

## Purpose

Separate direct interaction from shared-drive dependence using an explicit intervention while preserving the empirical marginal distribution of the intervened variable.

## Results

- direct mean intervention effect: `-0.000049`
- nonlinear direct mean effect: `-0.000068`
- none control mean effect: `-0.000043`
- shared-drive control mean effect: `-0.000043`
- mean absolute control effect: `0.000043`
- mean direct/nonlinear signal: `-0.000058`

The proposed global-mean response statistic does **not** separate direct interaction from controls.

## Scientific conclusion

**FAIL — candidate effect metric rejected.**

No promotion is justified.

This failure is retained because the intervention did not produce a discriminating downstream observable. Preserving one-dimensional marginals is not sufficient if the chosen outcome statistic is insensitive to the causal change.

The next test must measure a response variable directly downstream of the intervened channel and use explicit negative controls.
