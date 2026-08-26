# Ω-RH-01 — RESEARCH LOG

Public append-oriented working record for the Riemann Hypothesis investigation.

## 2026-08-26 — INIT

### Trigger

The Riemann Hypothesis was introduced as a possible mathematical problem to investigate through the Ω-Lab research process.

### Initial decision

Do not assume that the Ω-Lab Foundation solves RH. First reconstruct RH independently, then test whether a non-superficial mathematical correspondence exists.

### Initial target

`ζ(ρ)=0, 0<Re(ρ)<1  ⇒  Re(ρ)=1/2`

### Initial research architecture

```text
KNOWN MATHEMATICS
       ↓
EXACT RH FORMULATION
       ↓
KNOWN EQUIVALENCES / BARRIERS
       ↓
Ω-FOUNDATION COMPARISON
       ↓
MINIMAL MATHEMATICAL CONSTRUCTION
       ↓
COMPUTATIONAL / SYMBOLIC TESTS
       ↓
FALSIFICATION
       ↓
THEOREM CANDIDATE
       ↓
PROOF ATTEMPT
       ↓
INDEPENDENT AUDIT
```

### Important separation

The Ω-Foundation contains structural ideas such as distinction, relation, state, cycle, memory, prohibition, possibility and choice. Similar language alone is not mathematical evidence. A connection is accepted only when it can be expressed as a precise mathematical statement and checked.

### First external check

Independent public RH research repositories demonstrate that many apparently promising approaches have already encountered precise barriers. One useful model is the explicit preservation of failed approaches and no-go results. This supports using a permanent failure ledger in Ω-RH rather than repeatedly rediscovering dead ends.

### Status

`OPEN — BASELINE / NO CLAIM OF SOLUTION`

## 2026-08-26 — RH-31

### Siche / Krein–Rutman compactness attack

The continuum prime operator in the audited construction is a finite positive sum of truncated translations after the logarithmic change of variables. A finite sum of translations on an interval is not automatically compact merely because the interval is compact.

A stronger analytic obstruction was recorded: choose a sufficiently small interior support whose finitely many translated copies are disjoint, and use normalized oscillatory functions on that support. The sequence is bounded and weakly null, while the translated output retains a uniform positive L² norm. This contradicts the defining compactness property.

### Status

`KREIN–RUTMAN COMPACTNESS GATE: REJECTED FOR THE STATED SHIFT OPERATOR`

This is not an RH counterexample and does not disprove the spectral claim. It only removes the supplied compact-operator justification for simplicity.

### Next action

Find whether the correct spectral object is instead a compact resolvent, compact quadratic-form embedding, or another smoothing transform, and independently attack simplicity without assuming compactness of T.

## 2026-08-26 — RH-32

### Compact-resolvent replacement

The Siche construction explicitly decomposes the finite-cutoff Weil operator as

    QW_λ = A + Π − P.

The prime shift operator P is noncompact, so the Krein–Rutman compactness premise is rejected. The next candidate is different: the archimedean part A is an unbounded Fourier multiplier whose symbol is proportional to θ'(t), and θ'(t) grows logarithmically as |t|→∞. This suggests that A, rather than P, supplies the confining compact-resolvent mechanism.

For fixed λ, P contains only finitely many truncated shifts and is bounded; Π is finite rank in the displayed Fourier construction, subject to proving continuity of the polar evaluation functionals in the correct form topology. If A is self-adjoint with compact resolvent and Π−P is bounded self-adjoint on the same domain, then QW_λ is a bounded perturbation of A and inherits compact resolvent.

### Status

`COMPACT RESOLVENT OF QW_λ: PLAUSIBLE / KEY LEMMAS NOT YET PROVED`

This would restore a legitimate discrete-spectrum framework without claiming that P itself is compact.

### Required proofs

1. Exact Hilbert space and domain.
2. Exact archimedean multiplier and its lower bound/asymptotic.
3. Compactness of `(A+cI)^(-1)`.
4. Boundedness/form-boundedness of P_λ.
5. Continuity of Π_λ in the correct topology.
6. Self-adjointness and boundary consistency.
7. Only after these: simplicity of the ground state and λ→∞ convergence.

### Integrity

`NONCOMPACT P != NO SPECTRUM`

`COMPACT RESOLVENT CANDIDATE != PROOF`

`DISCRETE SPECTRUM != SIMPLE GROUND STATE`

`SIMPLE GROUND STATE != RH`

## 2026-08-26 — RH-33

### Compact-resolvent lemma established for the stated Fourier-cutoff model

The exact basis used in the audited Siche construction is the Fourier basis on the finite logarithmic interval, with

    L = 2 log λ,
    V_n(x) = exp(2π i n x/L),
    n ∈ Z.

The archimedean part is diagonal:

    A V_n = a_n V_n,
    a_n = θ'(nπ/log λ)/π.

Using the standard Riemann–Siegel asymptotic,

    θ'(t) = 1/2 log(|t|/(2π)) + O(t^-2),

we obtain a_n→+∞ as |n|→∞. Therefore the natural diagonal self-adjoint operator A has compact resolvent: the diagonal entries of `(A+cI)^(-1)` tend to zero.

The prime part is a finite sum of truncated translations for fixed λ. Each translation has norm ≤1, giving the finite bound

    ||P_λ|| ≤ 2 Σ_{p^k≤λ²} log(p)p^(-k/2) < ∞.

The polar vectors used by the construction have coefficients O(1/|n|), hence belong to ℓ²(Z). The polar term is consequently finite rank and bounded in this Fourier model.

Thus K_λ=Π_λ−P_λ is bounded self-adjoint, and

    QW_λ=A+K_λ

is self-adjoint on D(A), bounded below, and has compact resolvent by the bounded-perturbation theorem.

### Status

`COMPACT RESOLVENT OF QW_λ: ESTABLISHED FOR THE STATED FOURIER-CUTOFF MODEL`

This gives a legitimate discrete spectral framework at each fixed λ. It does not establish simplicity, λ→∞ convergence, or RH.

### Next attack

Attack S1 directly: determine whether the lowest eigenvalue is simple. The compact object available for Perron-type arguments is now the shifted resolvent of QW_λ, not P_λ itself. Candidate routes are positivity/irreducibility of a suitable resolvent, strict positivity of the ground state, or a direct variational nondegeneracy argument.

### Integrity

`P_λ noncompact ≠ QW_λ noncompact`

`COMPACT RESOLVENT ≠ SIMPLE GROUND STATE`

`FINITE-λ RESULT ≠ λ→∞ RESULT`

`NUMERICAL GAP ≠ PROOF`

`NO RH CLAIM`
