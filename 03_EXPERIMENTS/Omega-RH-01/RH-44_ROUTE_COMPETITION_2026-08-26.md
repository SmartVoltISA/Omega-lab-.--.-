# RH-44 — Route Competition / Theorem Gate

Date: 2026-08-26
Status: ACTIVE / NOT PROVEN

## Purpose
Compare independent proof architectures rather than advancing one route in isolation.

## Current leaders
1. Pólya-kernel route (Pavesi): claims global log-concavity of the Xi kernel and a Pólya 1927 real-zero theorem. Reduced inequality: x(S4 S0 - S2^2) <= S2 S0.
2. Weil positive-factorization route (Velez): claims direct nonnegativity of the completed arithmetic Weil quadratic form.
3. Certified log-concavity audit (Pierson/Gershon line): independently reports rigorous log-concavity, but explicitly flags the theorem bridge as the decisive dependency; therefore log-concavity alone is not accepted without exact theorem hypotheses.
4. Finite Weil route: certified positivity on finite-dimensional support families; not sufficient for RH without universal closure.

## Critical comparison
The competition changes the attack strategy: do not try to prove every route from scratch if one route contains a theorem-level shortcut. First verify whether the exact Pólya theorem has hypotheses matching the actual Xi kernel: positivity, integrability, global concavity of log K, and the required decay.

## Acceptance gate
A route is SOLVED only if the complete chain is established with no conditional theorem, finite-N substitution, numerical-only step, or hidden assumption:
K identity -> exact global property -> theorem with matching hypotheses -> Xi real zeros -> zeta critical-line conclusion.

## Current result
Fresh literature contains explicit preprints claiming the Pólya chain, but the claims are not independently validated here. Clay still lists RH among unsolved Millennium problems. Therefore status remains NOT PROVEN.

## Next action
Make the Pólya theorem the primary competition target. Independently reconstruct its statement and verify every hypothesis against the exact Xi kernel. In parallel audit Velez's factorization as a completely separate route. The first route to pass all gates wins; the others become cross-checks.
