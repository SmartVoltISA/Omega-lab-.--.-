# Ω-RH-17 — Friedrichs / spectral audit

Date: 2026-08-26
Status: OPEN / NO PROOF CLAIMED

## Objective
Test whether the current Friedrichs/self-adjoint operator route closes the final RH gap.

## New external candidate
Hedenmalm (arXiv:2606.17494, 2026) constructs an eigenvalue problem for second-order differential operators on the half-line and develops a notion of self-adjointness for the operator pair (LD,L), adapting the Hilbert–Pólya idea.

The construction identifies a differential equation whose spectral parameter is tied to real zeros of Xi. However, the crucial self-adjointness/Hilbert-space step required to force every zero to be real is not thereby established as a theorem proving RH.

## Independent numerical cross-check
Kim et al. (arXiv:2607.24830, 2026) numerically realize Suzuki's Weil-quadratic-form operator. The work reports real spectra and the expected response to injected off-line zeros, but explicitly states that it does not prove RH.

## Key logical test
A valid proof needs:

1. A rigorously defined Hilbert space H.
2. A densely defined closed quadratic form or operator.
3. A genuine self-adjoint/Friedrichs realization independent of RH.
4. Exact spectral correspondence with Xi, not only on the critical line.
5. A proof that every non-real zero would correspond to a forbidden non-real spectral value.
6. No boundary condition, domain choice, or norm identity may encode RH implicitly.

## Current result
The spectral route remains LIVE but NOT CLOSED.

A differential eigenvalue equation associated with Xi is not enough. Self-adjointness must hold for the exact operator/domain that carries the full zero set. If self-adjointness is assumed only as a pair property or established only on the real spectral parameter, the argument does not imply RH.

## Important nearby result
Yang (JMAA 2026) studies Friedrichs angles in Nyman–Beurling spaces and gives further equivalences with RH. This reinforces that completeness/closure of the relevant Hilbert-space structure is itself a load-bearing issue, not an automatic consequence of finite-dimensional positivity.

## Decision
NO PROOF.

The next attack is to isolate the minimal domain/boundary-condition statement needed for self-adjointness and test whether it can be derived from the theta-kernel and explicit formula without assuming RH.

Status discipline:
PROPOSED != TESTED
TESTED != PROVEN
NUMERICAL != GLOBAL
SELF-ADJOINT CANDIDATE != SELF-ADJOINT RH OPERATOR
