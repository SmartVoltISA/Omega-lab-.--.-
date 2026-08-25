# Ω-RH-13 — Global closure attack

Date: 2026-08-26
Status: OPEN / NO PROOF CLAIMED

## Objective

Attempt to close the remaining global step in the Weil/spectral route without assuming RH.

## Current mathematical target

RH is equivalent to a suitable global positivity statement for the Weil quadratic form. The finite-dimensional route gives certified evidence, but the unresolved step is a theorem that upgrades finite/local positivity to positivity on the full admissible test-function space.

## New observation

The strongest current candidate is not another finite matrix search. It is a direct factorization of the global form into manifestly nonnegative pieces, or a closed positive operator representation whose domain and completion are proved independently of the zero set.

Target forms:

    Q_W(f) = ||T f||^2

or

    Q_W(f) = sum_k Q_k(f),   Q_k(f) >= 0.

The factorization must reproduce the exact explicit formula, including prime, archimedean and zero-side terms, without inserting RH through a spectral assumption.

## External cross-check

Current Clay status still lists RH among the unsolved Millennium Problems and states that only the first 10^13 nontrivial zeros have been checked computationally. Numerical verification is not a proof.

A recent 2026 paper proves second-level concavity of the Riemann Xi kernel and associated double Turan inequalities, but explicitly makes no RH claim. This confirms that stronger local positivity properties do not automatically close RH.

A recent AI-assisted program reports a positivity certificate for a localized Weil quadratic form up to a finite parameter range, but explicitly does not claim RH. This is useful as a research direction, not as a proof.

## Falsification rules

1. Any factorization whose positivity depends on RH is rejected.
2. Any limiting argument without a stated domain, topology, and uniform bound is rejected.
3. Finite numerical positivity is not promoted to global positivity.
4. Self-adjointness alone is insufficient; exact correspondence with xi must be proved.
5. A claim from an unreviewed manuscript is treated as a candidate only.

## Result

NO PROOF YET.

The attack has reduced the remaining problem to finding an RH-independent global positive representation of the completed Weil form, or an equivalent theorem giving the required closed positive operator. This is the current load-bearing target.

## Status discipline

PROPOSED != TESTED
TESTED != PROVEN
NUMERICAL != GLOBAL
UNKNOWN != FALSE
