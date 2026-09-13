# Ω-BASIS-002-R2 — Provenance Closure v1.0

Date: 2026-09-08

## Closure decision

The archived numerical core is reproducible. The stronger bootstrap/repeat/hash provenance claims are not independently established by the archived executable and are therefore removed from the authoritative result status.

## Verified

- Protocol and model definitions are archived.
- `run_r2.py` source is archived at the declared commit/blob.
- N=5000 and 100 generated seeds reproduce the reported directional aggregate values.
- M1 stationary control: no regime benefit.
- M2 stationary control: no average regime benefit.
- M3 piecewise-stationary model: strong regime predictive benefit.
- M3 shuffled-regime control: advantage collapses near zero.

## Not verified from archived primary artifacts

- 10,000-resample bootstrap implementation.
- Raw-output files supporting the recorded SHA-256 values.
- Independent recomputation script as a separately archived executable.
- Byte-identical repeat as an independently auditable artifact.

## Scientific status

`NUMERICAL CORE REPRODUCED / FULL PROVENANCE NOT VERIFIED`

The result remains model-scoped. No ontological claim about time is promoted.

## Closure rule

Future provenance-grade promotion requires archiving raw outputs, an explicit bootstrap implementation, an independent analysis script, and execution metadata before restoring any stronger status.
