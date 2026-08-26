# Ω-RH-23 — Full Viceré Formula / Residual Audit
Date: 2026-08-26
Status: AUDITED TO PUBLICLY VERIFIABLE MATERIAL — NOT A PROOF

## Objective

Test the central Viceré claim: exact stabilization of the cutoff Weil quadratic form and recovery of the full Weil form.

Public source: Simon Velez, “A proof of the Riemann Hypothesis”, Zenodo 21184595, v5, published 2026-07-04. The record explicitly claims that the Weil quadratic form is non-negative on C_c^∞(R_+^×), using Connes' semilocal trace formula, with exact stabilization recovering the full Weil form. The record classifies the item as a Preprint.

## Target identity

For each admissible test function f, the decisive claim would have to establish a finite cutoff threshold λ0(f) such that

    Q_λ(f) = Q_W(f)    for all λ >= λ0(f).

The weaker statement

    Q_λ(f) = Q_W(f) + R_λ(f),   R_λ(f) -> 0

is not equivalent to exact stabilization and requires a separate positivity-preserving limit argument.

## Residual decomposition

Define formally

    R_λ(f) := Q_W(f) - Q_λ(f).

The audit requires the residual to be decomposed into all λ-dependent sectors, including prime, archimedean, zero/spectral, cutoff/boundary, and any trace-regularization terms. Each term must be controlled in the same test-function space.

Acceptance requires either an exact identity R_λ(f) = 0 beyond a finite threshold, or a theorem showing that the actual residual limit preserves non-negativity for the complete Weil domain. Numerical smallness is insufficient.

## External control

A public 2026 verification survey records Viceré's semilocal spectral descent as a non-peer-reviewed preprint and reports numerical eigenvector restructuring of roughly 7–22 modes as cutoff increases. This is a diagnostic challenge to any implicit eigenvector-stability argument, not by itself a mathematical disproof of form stability.

The same survey records that the broader Connes/CCM convergence problem remains an open analytic issue in the established literature.

## What is established by this run

1. Viceré's public record contains a genuine, explicit proof claim.
2. The proof claim is centered on exact stabilization of the cutoff Weil form.
3. The public record alone does not provide independently verified evidence sufficient to promote the claim to established RH proof status.
4. The current accessible audit material does not justify asserting a specific algebraic error in T3 without the complete proof text.
5. Therefore the correct status is: CANDIDATE / UNVERIFIED, not PROOF and not DISPROVED.

## Decisive next test

Obtain the complete paper PDF and extract the proof of exact stabilization. For every equality involving λ:

- identify whether it is exact or asymptotic;
- identify the domain of f;
- identify the dependence λ0(f);
- derive the residual explicitly;
- verify interchange of sums, traces, limits and distributions;
- verify that no use of Re(ρ)=1/2 enters the spectral positivity or stabilization step.

If all checks pass, reconstruct T1–T5 independently. If any check fails, record the first failed equation and construct a minimal counterexample where possible.

## Current verdict

RH remains OPEN.

Viceré remains a serious candidate claim, but the decisive stabilization theorem has not been independently verified in this audit.

This file is an Ω-Lab working support: it preserves the exact question and prevents future runs from silently changing the acceptance standard.