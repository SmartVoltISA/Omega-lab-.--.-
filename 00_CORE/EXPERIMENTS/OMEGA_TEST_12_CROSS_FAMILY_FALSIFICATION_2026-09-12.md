# Ω-Test-12 — Cross-family falsification: graph boundary + coupled oscillators

**Experiment ID:** Ω-TEST-12-CROSS-FAMILY-FALSIFICATION-2026-09-12  
**Status:** COMPLETED / EXPLORATORY NUMERICAL TEST

## Question
Does the counterfactual signature from Ω-Test-11 survive when the generating mechanism changes?

## Design
Two independent families were tested:

1. graph/network dynamics;
2. coupled oscillators.

For the graph model, the designated relation between two boundary nodes was active, cut for a middle interval, then restored. Controls removed the direct edge or used shared external drive without a direct edge.

For oscillators, coupling was similarly active → cut → restored. The observable was phase-locking rather than predictive regression.

## Graph result
60 seeds × 3 conditions.

Threshold from negative controls (99th percentile): `0.004006`.

- sensitivity: `0.933`
- specificity: `0.983`
- TP: `56`
- FN: `4`
- FP: `2`
- TN: `118`
- direct mean suppression: `0.014190`
- direct mean recovery: `0.014214`
- control mean suppression: `-0.000109`

## Oscillator result
- direct mean suppression: `0.900914`
- direct mean recovery: `0.899444`
- no-edge mean suppression: `0.001020`
- shared-drive mean suppression: `0.001020`

## Interpretation
The intervention signature survives a change of model family and observable:

`relation active → signal high → relation cut → signal low → relation restored → signal high`

This is stronger evidence than a single-model correlation test. It still does not establish a universal physical law.

## Classification
**CONDITIONAL PASS — cross-family replication.**

Not foundational. The remaining decisive challenge is to define the boundary independently of the detector and test systems where the boundary geometry is specified before the outcome is measured.

## Safeguards
- predictive dependence is not automatically causality;
- direct interaction is distinguished from shared forcing;
- boundary is not identified merely with trajectory;
- statistical replication is not proof of physical universality.

**Canonical rule:** RESULT ≠ TRUTH. Failed and negative results remain part of the research history.
