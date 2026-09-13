# Ω-B4 — Fair comparison of three mechanisms

## Question

After matching the principal parameters, do the three update mechanisms still produce different dynamics?

## Reported parameters

- `N = 200`
- `T = 1500`
- `δ = 0.025`
- `α = 0.06`
- `β = 0.28`
- forcing variance = `0.0299`

Exact source code and seed set are not yet archived, so these are preliminary reported results.

## Reported results

| Metric | Classical | Pure relation | Internal-dynamics (“will”) |
|---|---:|---:|---:|
| Domains | 12.5 | 14.2 | 25.0 |
| Mean lifetime | 123 | 113 | 611 |
| Mean domain size | 16.0 | 14.1 | 8.0 |
| Births near `u = 0` | 100% | 100% | 100% |

## Interpretation

The internal-dynamics condition shows substantially longer-lived structures in the reported comparison. However, the mechanism still cannot be called “will” on this evidence.

The universal 100% transition result across all three mechanisms also shows why that metric cannot distinguish the mechanisms.

## Mathematical model identification

The reported update equation was:

```text
u' = (1−δ)u + α·(u_left + u_right)/2 − β·u³ + η
```

For a homogeneous stationary state, the reported analysis obtains:

```text
0 = (α−δ)u − βu³
```

with corresponding double-well potential:

```text
V(u) = −(α−δ)u²/2 + βu⁴/4
```

Under the stated equation this is a discrete noisy φ⁴ / Ginzburg–Landau-type model. The identification should be checked directly against the archived implementation before being treated as final.

## Classification

**C — internal dynamics remain interesting as a statistical mechanism, but no evidence for “will” or new physics.**

## Required next controls

1. Spatially shuffle `v` while preserving its time sequence and marginal distribution.
2. Replicate each condition across many independent seeds.
3. Use effect sizes and confidence intervals, not single-run values.
4. Replace the B3 null model with a matched event-count null.
