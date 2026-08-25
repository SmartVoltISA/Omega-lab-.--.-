# Ω-RH-01 — SECOND ATTACK: KERNEL / ZERO-PRESERVING STRUCTURE

**Date:** 2026-08-26
**Status:** OPEN / NO PROOF

## 1. Exact reduction

Define

`ξ(s) = 1/2 s(s-1) π^(-s/2) Γ(s/2) ζ(s)`

and

`Ξ(t) = ξ(1/2 + i t)`.

Then RH is equivalent to: every zero of the entire even function `Ξ(z)` is real.

The classical Fourier representation is

`Ξ(z) = ∫_{-∞}^{∞} Φ(u) exp(i z u) du`

with

`Φ(u) = Σ_{n≥1} (2π² n⁴ exp(9u/2) - 3π n² exp(5u/2)) exp(-π n² exp(2u))`,

up to the equivalent normalization convention used for the two-sided/cosine integral. The kernel is even and rapidly decaying. Classical sources and modern summaries confirm this representation. See the linked research sources in the investigation log.

## 2. Candidate mechanism

A positive/even rapidly decaying Fourier kernel is NOT by itself sufficient to imply that its Fourier transform has only real zeros.

Therefore the required property must be stronger. Candidate sufficient mechanisms include:

- membership of `Ξ` in the Laguerre–Pólya class;
- total positivity / Pólya-frequency structure of the relevant kernel;
- a valid self-adjoint spectral realization whose eigenvalues are exactly the zero ordinates;
- an equivalent de Bruijn–Newman argument proving the critical parameter is exactly zero.

## 3. Important mathematical checkpoint

There is a known conceptual chain:

`RH ⇔ Ξ has only real zeros`

and, for an appropriate entire-function formulation,

`all real zeros ⇔ Laguerre–Pólya type`.

But proving that `Ξ` belongs to the Laguerre–Pólya class is essentially another formulation of the original problem; merely observing positivity, smoothness, evenness or rapid decay of `Φ` does not close the implication.

Recent literature also studies shifted Laguerre–Pólya classes and Jensen/Turán inequalities for `Ξ`. These results are useful diagnostics but do not by themselves constitute RH.

## 4. Ω attack

The useful Ω question is therefore narrower:

> Can the relation structure of the theta kernel produce a zero-preserving theorem that is stronger than ordinary positivity and strong enough to force `Ξ ∈ LP`?

We must derive an explicit mathematical operator or inequality. Vocabulary such as relation, cycle or distinction is irrelevant unless it yields a theorem.

## 5. Current barrier

At this stage no such theorem has been derived.

The first attractive route — positive kernel ⇒ real zeros — is rejected as insufficient.

A recent 2026 preprint claims a route through kernel/total-positivity machinery and `Λ=0`, but this is a claim in a preprint, not an independently accepted resolution. It must not be copied into Ω as a solved result. Its exact inequalities may nevertheless be audited as a source of candidate lemmas.

## 6. Next experiment

Construct finite truncations of the exact theta kernel and test, with exact or interval arithmetic where possible:

1. kernel positivity;
2. log-concavity;
3. Toeplitz minors / total positivity of increasing order;
4. Jensen polynomial hyperbolicity;
5. stability as truncation order increases;
6. whether any observed property admits a uniform analytic bound.

A numerical pass can generate conjectures only. The target is a uniform theorem valid for the infinite kernel.

## 7. Status

**No proof. No disproof.**

The research target has been narrowed from “solve RH” to a precise structural bottleneck: derive a genuinely zero-preserving property of the Riemann theta kernel strong enough to force all zeros of `Ξ` to be real.
