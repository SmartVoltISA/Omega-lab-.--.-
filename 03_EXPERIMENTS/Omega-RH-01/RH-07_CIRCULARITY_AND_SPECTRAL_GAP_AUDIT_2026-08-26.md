# Ω-RH-01 — RH-07: Load-bearing audit of the Gershon v1 proof

Date: 2026-08-26
Status: CRITICAL GAP IDENTIFIED / NO CLAIM OF SOLUTION

## Finding

A load-bearing implication in the v1 preprint is not established independently by the text inspected.

The paper states that Proposition 11.12 proves the unitarity condition for all n, and Theorem 11.3 Region C1 (r >= 51, n >= 100) then uses Proposition 11.12 to obtain μ_r(n) > 0 and hence D_r(n) > 0. This is the step used to close the infinite (r,n) half-plane.

However, Proposition 11.12 itself contains conditional reasoning in its analytical alternative: positivity D_r(n) > 0 for all r implies L_r > 1, then μ_r is decreasing with a positive asymptotic limit, which implies unitarity. The paper explicitly states this implication is conditional. Therefore this alternative cannot by itself supply the missing positivity required by Region C1.

## More serious issue: spectral-gap estimate

Lemma 11.6 asserts

|C_s(n) - C_s^(∞)| <= K_s δ^n,

with Σ K_s < 2, based on a Hadamard expansion and residue ratios. The proof sketch establishes the dominant-term form asymptotically, but the global bound on the constants K_s and the uniform summability ΣK_s < 2 are not derived in the displayed argument. The text cites a numerical comparison of C_s(30) and C_s(50) as verification.

A numerical comparison of two finite n values does not by itself certify a uniform bound on all s and all n >= 100, especially when the K_s are said to depend on Hadamard residues at level s.

## Tail-envelope issue

The proof of S <= 19.41 uses an observed ratio q = 0.951 for the first 11 computed ratios and then treats q as an analytically justified geometric envelope. The text notes that the asymptotic ratio is <= 0.204, but asymptotic convergence to a smaller ratio does not establish that every finite ratio from s=13 onward is <= 0.951. A separate uniform bound is required.

## RH-dependence warning

The paper itself notes that statements about the ordered zeros z_k = -t_k^2 on the critical line require care: the critical-line representation of all zeros cannot be assumed while proving RH. Only the individually certified initial zeros may be used unconditionally. Any global Binet–Cauchy/dominant-pole argument must explicitly control possible off-line zeros and their residues.

## Consequence

The current evidence is insufficient to accept Theorem 11.3 as a proof of D_r(n) > 0 for every r,n. Consequently the chain

D_r(n) > 0 for all r,n
→ PF∞
→ Xi in Laguerre–Polya
→ Lambda = 0
→ RH

remains unclosed.

This is not a disproof of the preprint's claim. It is a proof-audit result: the load-bearing estimates must be supplied with a rigorous, non-circular, globally uniform derivation.

## Next test

1. Derive an explicit uniform bound for K_s from the full Hadamard/partial-fraction data without assuming RH.
2. Prove or disprove a uniform finite-s tail ratio q <= 0.951.
3. Separate certified on-line zeros from hypothetical off-line zeros in every spectral expansion.
4. Rebuild the Region C1 implication from only unconditional premises.

## Verdict

`GERSHON_V1: NOT VALIDATED`

`RH: UNRESOLVED`

`COUNTEREXAMPLE: NONE`

`NEXT TARGET: UNCONDITIONAL UNIFORM SPECTRAL-GAP BOUND`
