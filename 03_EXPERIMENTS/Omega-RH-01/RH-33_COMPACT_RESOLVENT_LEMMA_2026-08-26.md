# Ω-RH-33 — COMPACT RESOLVENT LEMMA FOR THE TRUNCATED WEIL OPERATOR
Date: 2026-08-26
Status: ANALYTIC LEMMA ESTABLISHED FOR THE STATED FOURIER-CUTOFF MODEL / NO RH CLAIM

## Purpose
Close the main operator-theoretic gap identified in RH-32 for the actual finite-logarithmic-interval model used by the Siche numerical construction.

## 1. Exact model
For fixed λ>1 put

    L = 2 log λ,
    I = [0,L],
    H = ℓ²(Z)

with Fourier basis V_n(x)=exp(2π i n x/L), n∈Z. The archimedean matrix used in the audited construction is diagonal:

    A V_n = a_n V_n,
    a_n = θ'(nπ/log λ)/π,

where θ is the Riemann–Siegel theta function. The numerical script writes the same coefficient as 2θ'/(2π).

The natural operator domain is

    D(A) = {c∈ℓ²(Z): Σ_n |a_n c_n|² < ∞}.

## 2. Compact resolvent of A
The Riemann–Siegel asymptotic gives

    θ'(t) = 1/2 log(|t|/(2π)) + O(t^-2),   |t|→∞,

hence

    a_n → +∞  as |n|→∞.

Therefore A is a real diagonal self-adjoint operator on D(A), bounded below, with purely discrete spectrum. For any c>−inf a_n,

    (A+cI)^(-1) V_n = (a_n+c)^(-1) V_n,

and (a_n+c)^(-1)→0. A diagonal operator on ℓ²(Z) whose diagonal entries tend to zero is compact. Thus

    (A+cI)^(-1) ∈ K(H).

This is an exact proof for the Fourier-cutoff model; no numerical convergence argument is needed.

## 3. Prime operator is bounded for fixed λ
For each prime power q=p^k≤λ² define the truncated translation on L²(I)

    (S_q f)(x) = 1_{I∩(I−log q)}(x) f(x+log q).

With Lebesgue measure dx, S_q is a partial isometry, hence

    ||S_q|| ≤ 1.

The prime contribution is a finite sum

    P_λ = Σ_{p^k≤λ²} w_{p,k}(S_{p^k}+S_{p^k}^*),

with

    w_{p,k}=log(p) p^{-k/2}.

Consequently

    ||P_λ|| ≤ 2 Σ_{p^k≤λ²} log(p) p^{-k/2} < ∞.

The earlier RH-31 obstruction remains valid: bounded does not mean compact. P_λ is not compact in the continuum L² model, but compactness is no longer required here.

## 4. Polar term is bounded in the Fourier model
For the basis used in the audited construction,

    v_n^+ = λ^{-1/2} (e^{(1/2+2πin/L)L}−1)/(1/2+2πin/L)

and

    v_n^- = λ^{-1/2} (e^{(-1/2+2πin/L)L}−1)/(-1/2+2πin/L).

Since e^{2πin}=1, these satisfy

    |v_n^±| = O(1/|n|).

Hence v^+,v^-∈ℓ²(Z). The polar quadratic form

    2 Re(<c,v^-?> ...)

is therefore represented by a finite-rank operator (rank at most two) built from these ℓ² vectors. In particular Π_λ is bounded and self-adjoint.

The exact conjugation convention must follow the chosen Fourier inner-product convention, but boundedness only uses v^±∈ℓ².

## 5. Full operator
Set

    K_λ = Π_λ − P_λ.

Then K_λ is bounded self-adjoint for fixed λ. Define

    QW_λ = A + K_λ,
    D(QW_λ)=D(A).

By the bounded perturbation theorem, QW_λ is self-adjoint on D(A), bounded below, and has compact resolvent. Equivalently, for sufficiently large c,

    (QW_λ+cI)^(-1) ∈ K(H).

The resolvent identity is

    (QW_λ+cI)^(-1)
      = (A+cI)^(-1)[I+K_λ(A+cI)^(-1)]^(-1),

whenever c is in the resolvent set. The first factor is compact and the second bounded, so the product is compact.

## 6. Consequences
For every fixed λ in this model:

1. QW_λ has discrete real spectrum;
2. every eigenvalue has finite multiplicity;
3. eigenvalues can accumulate only at +∞;
4. QW_λ has a lowest eigenvalue because it is self-adjoint, bounded below, and has compact resolvent;
5. the spectral gap is well-defined, but may be zero if the lowest eigenvalue is degenerate.

## 7. What is NOT proved
This lemma does not prove:

- simplicity of the ground state;
- positivity/irreducibility of QW_λ;
- convergence as λ→∞;
- convergence to the Riemann Xi spectrum;
- the Riemann Hypothesis.

## 8. Critical distinction
RH-31:

    P_λ noncompact.

RH-33:

    A has compact resolvent,
    Π_λ−P_λ is bounded,
    therefore QW_λ has compact resolvent.

There is no contradiction. The compact object has moved from the arithmetic shift operator itself to the resolvent of the full operator.

## 9. Remaining attack
The next mathematical bottleneck is now S1:

    Is the lowest eigenvalue of QW_λ simple?

This must be attacked independently. Candidate routes:

A. positivity/irreducibility after an appropriate shift of QW_λ;
B. a Perron-type theorem for the compact resolvent, not for P_λ;
C. strict positivity of the ground-state eigenfunction;
D. a direct variational nondegeneracy argument.

## Integrity rule
COMPACT RESOLVENT ≠ RH
DISCRETE SPECTRUM ≠ SIMPLE GROUND STATE
FINITE-λ THEOREM ≠ λ→∞ THEOREM
NUMERICAL GAP ≠ PROOF
