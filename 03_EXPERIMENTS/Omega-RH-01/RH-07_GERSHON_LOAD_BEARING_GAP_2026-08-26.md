# Ω-RH-01 — RH-07: Load-bearing audit of Gershon v1

Date: 2026-08-26
Status: CRITICAL GAP IDENTIFIED / NO CLAIM OF SOLUTION

## Finding
The claimed proof reduces RH to positivity of all Toeplitz minors D_r(n), then uses Proposition 22 / Lemma 10 to close the infinite-r region. The load-bearing spectral-gap step requires a rigorous dominant-pole expansion of the coefficients of g(z)=Xi(sqrt(z)).

## Critical issue
Lemma 10 states an unconditional Hadamard factorisation, but then writes the coefficient asymptotics using rho_k=1/|z_k| and uses z_1=-t_1^2, z_2=-t_2^2. The fact that the first two relevant zeros are on the critical line is supported by certified computations, but the manuscript must independently prove the quantitative remainder/residue bounds needed for the claimed uniform estimate

  |C_s(n)-C_s^(infty)| <= K_s delta^n,
  sum_s K_s < 2.

Hadamard factorisation alone does not supply those positive-coefficient/dominant-pole bounds. In particular, later zeros may be complex, and replacing their signed/complex contributions by absolute-modulus reciprocal terms requires an explicit bound on residues and cancellation. The manuscript says K_s is explicit, but the proof as presented does not derive the required global bound from the stated hypotheses.

## Second issue
The manuscript itself acknowledges in Remark 19 that the interpretation |z_j| increasing -> positive growth is trivial if RH is assumed. Therefore the independent proof must not use the same ordering/sign structure in establishing the spectral-gap estimate. The distinction between "first two zeros are certified on the line" and "the complete zero expansion has a controlled positive dominant-pole remainder" must be made explicit and proved.

## Consequence
Until the bound on K_s and the passage from the full Hadamard expansion to the uniform spectral-gap inequality are independently established, Proposition 22 is not independently verified. Since Theorem 11 Region C1 depends on Proposition 22, the infinite half-plane r>=51,n>=100 remains unclosed by the audit.

## Status classification
OBSERVATION: strong numerical/symbolic structure.
PROOF: not independently established.
COUNTEREXAMPLE: none.
RH: unresolved.

## Next test
Reconstruct Lemma 10 from first principles using only certified information about the first two zeros and a rigorous bound for the complete remainder. If the bound cannot be obtained without RH or an equivalent total-positivity statement, mark the route circular.
