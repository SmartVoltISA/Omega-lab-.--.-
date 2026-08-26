# RH-64 — Shimizu v8 full-text audit checkpoint

Date: 2026-08-26

## Finding

The full v8 PDF is now available for direct audit. The earlier RH-63 status is refined: the G3 target-identification step is not merely an assertion in the abstract. v8 contains explicit intermediate lemmas and a theorem chain.

Key chain:

1. Lemma 6.112: Hilbert–Schmidt continuity of the central determinant transform; S2 convergence implies local uniform convergence of the logarithmic derivative and finite derivatives.
2. Lemma 6.113: finite-rank determinant/boundary central compatibility.
3. Lemma 6.135: cyclic coefficient tests converge and their pairings give Tr(K_M^ell).
4. Lemma 6.140: finite-window realized functional converges to the central functional.
5. Lemma 6.141: K_M -> K in S2.
6. Lemma 6.146: K-side central transform equals the logarithmic derivative of F_K minus its central value.
7. Lemma 6.147: classical explicit-formula ledger equals the logarithmic derivative of xi minus its central value, via the Hadamard product.
8. Lemma 6.148: restates the K-side identity.
9. Theorem 6.149: records the two separate transform identifications.
10. The comparison theorem then combines the separately constructed sides and identity theorem yields F_K = xi.

## Important correction

Therefore the correct status is NOT “G3 is absent”. The paper contains a formal closure chain for G3.

However, this does NOT independently verify the proof. The remaining audit target is now narrower: verify the hypotheses and proofs of the upstream comparison lemmas, especially the finite-window comparison-quotient equality and the S4/S2 convergence used in Lemma 6.141, rather than treating G3 as an unproved black box.

## Status

Shimizu v8: CLAIMED PROOF / FORMAL CHAIN PRESENT / INDEPENDENTLY UNVERIFIED.

No contradiction has been established in this checkpoint. No RH solution is claimed from this audit.

## Primary source

Yoshinori Shimizu, “Proof of the Riemann Hypothesis”, v8, posted 3 July 2026, DOI 10.20944/preprints202505.2110.v8. The source explicitly states that v8 is not peer-reviewed.
