# RH-42 — Pólya Kernel Route Audit

Date: 2026-08-26
Status: ACTIVE / NOT PROVEN

## Objective
Audit the strongest currently found external proof candidate: global log-concavity of the Riemann Xi/Pólya kernel.

## Candidate chain
1. Establish the exact Fourier representation of Xi by a positive even kernel K.
2. Prove K is integrable, strictly positive, sufficiently rapidly decaying, and globally log-concave.
3. Apply the exact Pólya theorem whose hypotheses match this kernel.
4. Conclude the Fourier transform Xi has only real zeros.
5. Transfer real zeros of Xi to Re(rho)=1/2 for nontrivial zeta zeros.

## Independent checks performed
The central reduced inequality reported by Pavesi is

    x (S4 S0 - S2^2) <= S2 S0,

where S_k(x)=sum_{n>=1} n^k exp(-n^2 x), x>0.

High-precision spot checks at x = 0.001, 0.01, 0.1, 0.5, 1, 2, 5, 10, 20 all gave a strictly positive margin

    S2*S0 - x*(S4*S0-S2^2) > 0.

This is a sanity check only; it is NOT a proof for all x.

## Critical proof gate
The decisive issue is no longer numerical plausibility. We require a reproducible, rigorous certificate for the compact interval used in the proof, plus independently verified analytic bounds on both tails. A finite floating-point computation does not qualify.

A second gate is theorem matching: the exact Pólya theorem and all its hypotheses must be identified and checked against the precise Xi kernel and variable transformation used by the manuscript. A current independent audit source reports that the needed bridge has historically been a source-critical point, so this must be checked against a primary theorem statement rather than accepted from the preprint.

## Decision rule
PASS only if every hypothesis is established rigorously and the chain reaches the actual Riemann Xi function without an unproved transfer.
FAIL if any interval certificate, tail estimate, kernel identity, or theorem hypothesis remains conditional.

## Current conclusion
The route is a serious candidate and the reduced inequality has strong numerical support, but RH is NOT declared solved. The next action is to reconstruct the compact-core certificate and tail bounds independently, then verify the exact Pólya theorem statement.
