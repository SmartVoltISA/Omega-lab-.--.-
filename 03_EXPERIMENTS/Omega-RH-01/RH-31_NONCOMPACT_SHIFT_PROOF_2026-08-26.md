# Ω-RH-31 — NONCOMPACTNESS OF THE PRIME SHIFT OPERATOR
Date: 2026-08-26
Status: ANALYTIC OBSTRUCTION ESTABLISHED / NO RH CLAIM

## Objective
Resolve the first item of RH-30: determine whether the continuum prime-sum operator used in the Siche/Krein–Rutman route can actually be compact on the stated L² interval.

## Operator
Write x = log u and B = log(lambda). The interval becomes I = [-B,B]. For finite lambda, only finitely many prime powers q=p^m satisfy log(q)<2B. Up to the precise boundary convention, the prime operator has the form

    (Tf)(x) = sum_{q in S_B} a_q [ f(x + log q) + f(x - log q) ],

where a_q = log(p) q^(-1/2) > 0 and terms are retained only when the shifted point remains in I.

Thus T is a finite positive linear combination of truncated translation operators.

## Main finding
A nonzero truncated translation operator on L²([-B,B]) is not compact. More importantly, for the finite positive family above one can construct a bounded weakly-null sequence of functions whose images have a uniform nonzero norm.

Choose an open interval J compactly contained in (-B,B) such that the finitely many translated copies

    J ± log(q),   q in S_B,

that occur in the operator are pairwise disjoint and remain inside I. Such a J exists after choosing it sufficiently small, unless two shifts coincide; coincident shifts can simply be combined into one positive coefficient. Pick normalized oscillatory functions

    f_n(x) = |J|^(-1/2) 1_J(x) exp(i n x).

Then ||f_n||_2 = 1 and f_n -> 0 weakly in L²(I).

Because the translated supports are disjoint, the output pieces of Tf_n do not cancel in L² norm. In the ideal interior configuration,

    ||Tf_n||² = sum_s c_s²,

where c_s are the combined positive coefficients associated with the distinct shifts. Hence there is a constant c>0 independent of n such that

    ||Tf_n|| >= c.

A compact operator must map every bounded weakly-null sequence to a norm-null sequence. Therefore T cannot be compact.

## Important qualification
The construction must be applied to the actual set of shifts present for the chosen lambda and to an interior interval avoiding all boundary truncations. It is not enough merely to say that the kernel contains delta functions. The weakly-null sequence gives the required functional-analytic obstruction directly.

## Consequence for Krein–Rutman
The supplied Siche argument cannot invoke the classical compact-operator Krein–Rutman theorem for this T merely from positivity and finite truncation. The compactness gate fails for the stated shift operator unless the route changes the operator itself or works with a different compact object, such as a compact resolvent, compact quadratic-form embedding, or a genuinely smoothing transform.

This does NOT disprove the underlying spectral claim, and it does NOT disprove RH. It only removes one proposed justification for spectral simplicity.

## Next attack
1. Verify the exact boundary/truncation convention in the Siche construction.
2. Implement the weakly-null bump/oscillation test numerically as a sanity check.
3. Determine whether Q_W or a transformed resolvent has a compact object to which a spectral theorem can legitimately apply.
4. Search for a direct simplicity mechanism for the lowest eigenvalue that does not require compactness of T.

## Integrity rule
ANALYTIC OBSTRUCTION != RH COUNTEREXAMPLE
NONCOMPACT T != NO SPECTRAL GAP
NUMERICAL CHECK != PROOF
