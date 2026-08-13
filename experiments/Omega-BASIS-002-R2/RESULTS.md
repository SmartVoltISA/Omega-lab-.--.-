# Ω-BASIS-002-R2 — RESULTS

Date: 2026-08-13
Status: **EXECUTED / REPRODUCED / INDEPENDENTLY RECOMPUTED**

## Provenance

Protocol commit: `6d2936a986224a8c4fcafa08fbf4f26f664520ec`
Code commit: `8f76b69dc892318a334f72e9d008fdf4f46f1b7b`
Code blob SHA: `cceea7ec016ef41eb34aea16fec997c14897c6ef`

Exact code from the GitHub blob was executed with Python/NumPy. N=5000, 100 preregistered seeds generated from NumPy seed `20260813`.

Exact-output SHA-256, run 1:
`d55a9ab382bf26c7efd0dffabace1fc447acf84afa8ffa31b1b0aca74facf934`

Exact-output SHA-256, run 2:
`d55a9ab382bf26c7efd0dffabace1fc447acf84afa8ffa31b1b0aca74facf934`

Byte-for-byte repeat: **PASS**.

## Primary metric

`BminusA_nll = NLL(state + regime) - NLL(state only)`.

Negative means B is better.

### M1 — deterministic flip

NLL difference:
- mean 0.0000000000
- SD 0.0000000000
- min 0.0000000000
- max 0.0000000000

Brier difference:
- mean 0.0000000000
- SD 0.0000000000

Shuffle NLL difference:
- mean 0.0000000000

### M2 — stationary Markov, p(stay)=0.8

NLL difference:
- mean **+0.0003959536**
- SD **0.0006289013**
- min **-0.0007311417**
- max **+0.0024796942**

Brier difference:
- mean **+0.0001268936**
- SD **0.0002041656**

Bootstrap 95% CI for NLL difference: **[+0.00027729, +0.00052337]**.

Shuffle-control NLL difference:
- mean **+0.0004994219**
- SD **0.0007540729**

Bootstrap 95% CI: **[+0.00035979, +0.00065049]**.

Interpretation: adding a regime variable to a stationary process did not improve prediction; it produced a small degradation on average, consistent with finite-sample overparameterization rather than useful time information.

### M3 — piecewise-stationary, p=0.9 then p=0.6

NLL difference:
- mean **-0.0627223918**
- SD **0.0063420223**
- min **-0.0803252127**
- max **-0.0462577211**

Brier difference:
- mean **-0.0223113692**
- SD **0.0022397374**

Bootstrap 95% CI for NLL difference: **[-0.06394978, -0.06149811]**.

Bootstrap 95% CI for Brier difference: **[-0.02274734, -0.02187332]**.

Shuffle-control NLL difference:
- mean **+0.0003602096**
- SD **0.0067752953**
- min **-0.0127489768**
- max **+0.0169881347**

Bootstrap 95% CI: **[-0.00097025, +0.00166184]**.

## Independent recomputation

The primary aggregates were independently recomputed from the per-seed result rows using NumPy, including mean, sample SD, and a 10,000-resample bootstrap confidence interval. The independent calculation reproduced the archived aggregate values.

The exact executable was run a second time from the same source logic and input seeds. The complete JSON output was byte-identical between runs.

## Decision against preregistered criteria

1. M1 stationary/deterministic: no regime benefit. **PASS**.
2. M2 stationary Markov: no predictive benefit from regime; mean difference is positive. **PASS**.
3. M3 nonstationary: regime produces a large and consistent predictive improvement. **PASS**.
4. Shuffle control: M3 advantage disappears after regime-label permutation; CI crosses zero. **PASS**.
5. Repeatability: exact output reproduced. **PASS**.
6. Independent recomputation: **PASS**.

## Result

For this model class, the current experiment supports the narrower predictive statement:

> When the observable state is sufficient for a stationary transition law, an explicit regime/time variable adds no useful predictive information. When the transition law changes with a known regime, the regime variable carries predictive information not contained in the current binary state alone.

This is **not** evidence that time is an ontological entity, nor evidence that time can never be represented as state/history. It only establishes a predictive distinction in the tested models.

## Important caution

The M3 test uses the known midpoint regime as the time-related variable. Therefore the result establishes that **regime information** is predictive. It does not yet prove that a continuous scalar clock is fundamentally required. A further experiment must test unknown change points/history and compare explicit clock, finite memory, and state augmentation.

## Scientific status

**VALIDATED WITHIN THE DECLARED MODEL CLASS, NOT A UNIVERSAL Ω RESULT.**
