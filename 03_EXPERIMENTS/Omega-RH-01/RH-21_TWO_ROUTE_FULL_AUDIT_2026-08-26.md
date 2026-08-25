# RH-21 — Full audit of the two candidate routes

Date: 2026-08-26

## Verdict

No proof of the Riemann Hypothesis is established by either route audited here.

## Route A — Farrell local curvature / jet projection

Candidate claim: a hypothetical off-line quartet produces a local second-order jet with coefficient -δ², while prime, archimedean, endpoint, reference and far-zero sectors have zero projection.

The candidate paper (Version 2, 2026-07-03) explicitly states this chain and concludes RH, but is marked by Cambridge Open Engage as a Working Paper and not peer-reviewed.

The prime-side computation itself is coherent at the level of the probe response: the prime distribution gives a purely atomic Fourier spectrum supported on ±log n, while a point-supported second derivative produces an absolutely-continuous Fourier component. However, the proof requires that the defined local second-jet projection is a legitimate linear functional on the full explicit-formula distribution and that the lifted explicit-formula identity is represented in exactly the same distributional space. The public text does not provide an independently validated theorem establishing this complete compatibility. The quartet expansion also uses a Taylor/jet coefficient of a finite displacement δ; extracting that coefficient must be justified as an exact projection on the identity, not merely as a formal local expansion.

Status: promising candidate mechanism, NOT accepted as proof.

## Route B — Weil positivity / finite Galerkin and spectral factorisation

Groskin 2026 proves an exact finite Guinand–Weil dictionary and a rigorous archimedean-tail certification rule. A finite-cutoff positive matrix can therefore certify positivity of the corresponding cutoff-free finite-dimensional form. This removes the old objection about an uncontrolled archimedean numerical tail.

It does NOT prove positivity of the Weil form on the full admissible test-function space. The missing statement remains universal positivity for every admissible test function (or an equivalent theorem that the finite family is complete/dense with the required closed-form convergence).

The Velez 2026 preprint explicitly claims a positive spectral factorisation of the completed arithmetic Weil kernel and hence RH, but the accessible record is a preprint and the indexed source does not provide enough independently checkable mathematical detail to certify every factorisation and domain step. Therefore it is retained as an unverified candidate, not a solved route.

Status: finite part rigorously advanced; global positivity still unverified.

## Combined result

Both routes converge on the same structural requirement:

finite/local certificate -> global distributional statement.

Neither audited route currently supplies that final bridge in a form that can be independently certified without accepting an unverified premise.

Therefore:

RH = OPEN.

No numerical evidence or preprint claim is promoted to theorem status.

## Next admissible attack

1. For Route A: formalize the local-jet projection as a continuous quotient functional on the exact Weil test/distribution spaces and prove the lifted identity is preserved under it.
2. For Route B: prove universal positivity by a complete positive factorisation valid on the full test space, or prove a density/closure theorem sufficient to pass from all finite certificates to the full form.
3. If either route fails, identify an explicit invalid implication or counterexample rather than generating another intermediate certificate.
