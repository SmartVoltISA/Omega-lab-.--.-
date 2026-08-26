# Ω-RH-24 — Residual Formula Full Run
Date: 2026-08-26
Status: ACTIVE — FORMULA DERIVATION CHECKPOINT

## Objective

Turn the Viceré T3 claim into an explicit identity rather than accepting the word “stabilization”. Define

    R_λ(f) := Q_W(f) - Q_λ(f)

and separate every contribution before any limit is taken.

## Canonical decomposition

At the level required for an honest audit, write

    R_λ(f) = R_prime,λ(f) + R_arch,λ(f) + R_zero,λ(f) + R_boundary,λ(f).

The four symbols are bookkeeping components, not assumed-zero terms. Their definitions must come from the same test-function space and the same normalization as Q_W and Q_λ.

## Acceptance target

A proof of exact stabilization requires an explicit finite λ₀(f) such that

    R_λ(f) = 0  for every λ ≥ λ₀(f).

A bound of the form

    |R_λ(f)| ≤ ε_λ(f),  ε_λ(f) → 0

is only convergence and is NOT exact stabilization.

## Critical logical check

Positivity of Q_λ(f) gives

    Q_λ(f) ≥ 0.

If only R_λ(f) → 0 is known, this does not by itself imply Q_W(f) ≥ 0 unless a separate closedness/limit argument preserves positivity. The sign margin may vanish. Therefore no limit is promoted to an equality without proof.

## Current external control

The Viceré preprint explicitly claims T3 form stability for compactly supported smooth test functions and uses it to bypass the spectral convergence gap. The public record remains a preprint and the claim is not treated as established mathematics.

A newer independent semilocal Weil/prolate-proxy study explicitly states that its mechanism does NOT prove RH and identifies the missing zeta-specific bridge. This is a useful negative control against treating finite spectral agreement as a theorem.

## Result of this checkpoint

No independently derived identity R_λ(f) ≡ 0 has yet been obtained from first principles in this repository. Therefore T3 is NOT promoted to PROOF.

The next decisive mathematical operation is to obtain the complete definitions of Q_λ and the semilocal truncation map used by T3, then derive each remainder term symbolically and identify whether any term survives for finite λ.

## Rule

Do not claim RH solved unless the exact remainder identity is closed and the Weil positivity criterion is reached without assuming RH.