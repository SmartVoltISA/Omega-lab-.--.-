# RH-57 — Shimizu v8 audit checkpoint

Date: 2026-08-26

## Status
CLAIMED / NOT INDEPENDENTLY VERIFIED

## Primary observation
The v8 abstract explicitly claims the chain:
finite-window comparison -> self-adjoint Hilbert-Schmidt operator K -> determinant F_K -> local equality of logarithmic derivatives with xi -> identity theorem -> RH.

## Exact critical assertions in v8
1. The finite-part realized functional is identified with the determinant trace through finite-window scalar coefficients, cyclic tensor contractions, finite-rank compression, and a Hilbert-Schmidt limit.
2. The classical explicit-formula ledger is independently identified with the completed zeta logarithmic derivative at the target-identification stage.
3. The two transform identities are asserted to agree near w=0.
4. Identity theorem is then used to obtain F_K(s) = xi(s).

## Audit rule
Self-adjointness of K and the identity theorem are not themselves the difficult steps. The critical burden is the independent validity of the two limit/identification constructions and their exact equality, without circular use of xi's zero data or RH.

## External status
The source is a preprint and is not peer-reviewed. Therefore this checkpoint does not promote the claim to PROVEN.

## Consequence
RH remains NOT SOLVED in our audit. The next attack is G3: independent target identification F_K = xi, with G1/G2 convergence assumptions audited separately.

## Related anchors
RH-55 GLOBAL LIMIT AUDIT
RH-56 GLOBAL LIMIT REASSESSMENT
