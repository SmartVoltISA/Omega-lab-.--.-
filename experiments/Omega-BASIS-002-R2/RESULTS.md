# Ω-BASIS-002-R2 — RESULTS

Date: 2026-08-13
Status: **NUMERICAL CORE REPRODUCED / FULL PROVENANCE NOT VERIFIED**

## Provenance

Protocol commit: `6d2936a986224a8c4fcafa08fbf4f26f664520ec`
Code commit: `8f76b69dc892318a334f72e9d008fdf4f46f1b7b`
Code blob SHA: `cceea7ec016ef41eb34aea16fec997c14897c6ef`
N=5000, 100 seeds generated from NumPy seed `20260813`.

## Reproduced numerical core

The archived executable was independently re-executed with the same source logic, N=5000 and 100 seeds. The following aggregate values reproduce:

- M1: BminusA_nll mean = 0; BminusA_brier mean = 0.
- M2: BminusA_nll mean = +0.0003959536; SD = 0.0006289013; BminusA_brier mean = +0.0001268936.
- M3: BminusA_nll mean = -0.0627223918; SD = 0.0063420223; BminusA_brier mean = -0.0223113692.
- M3 shuffle-control BminusA_nll mean = +0.0003602096.

Thus the directional numerical core is reproduced: stationary controls do not benefit from regime information, while the deliberately nonstationary M3 model does.

## Provenance correction

The archived `run_r2.py` calculates mean, sample SD, min and max only. It does **not** implement bootstrap confidence intervals. Therefore the bootstrap 95% CIs previously recorded here are not outputs of the archived executable.

The audit also found that exact-output SHA-256 claims, byte-identical repeat claims, and the claimed independent bootstrap recomputation cannot be established from the archived code alone. Those claims remain unverified until raw outputs and an execution record are archived.

## Scientific interpretation

The narrow model-scoped result survives:

> In a stationary transition law, adding an explicit regime variable gives no useful predictive benefit in the tested models; when the transition law deliberately changes by known regime, regime information becomes predictive beyond the current binary state.

This does **not** establish that time is an ontological entity or that a continuous clock is fundamentally required. It establishes only predictive regime information in the declared model class.

## Decision

- Numerical core: **REPRODUCED**.
- Full provenance: **OPEN**.
- Bootstrap CI provenance: **OPEN**.
- Physical interpretation of time: **OPEN**.
- Promotion to universal/foundation claim: **NOT AUTHORIZED**.

See `AUDIT-2026-08-13.md` for the provenance conflict and required closure artifacts.
