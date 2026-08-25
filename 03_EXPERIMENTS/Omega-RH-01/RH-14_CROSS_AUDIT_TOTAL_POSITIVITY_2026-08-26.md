# Ω-RH-14 — Cross-audit of total-positivity closure

Date: 2026-08-26
Status: AUDITED / NO PROOF

## Objective

Cross-check the strongest apparent closure routes against the exact logical requirements of RH.

## Result

No complete proof was obtained.

A major reusable warning was confirmed: first-order or second-order Turán/log-concavity information is not equivalent to membership of the Laguerre–Pólya class. Full LP membership requires the corresponding global real-zero/hyperbolicity condition; finite-order positivity does not automatically supply all higher-order minors/Jensen conditions.

Likewise, a positive finite Gram matrix, a finite-window Weil form, or a self-adjoint approximating operator does not by itself identify the limiting object with ξ(s). The exact global identity and the relevant domain/limit theorem remain load-bearing requirements.

## Cross-check of a public claimed proof

A public repository claiming a complete φ-separation proof contains the standard RH↔LP reformulation, but its stated bridge from Turán inequalities to LP membership is too strong as written: ordinary Turán inequalities are necessary in relevant settings but are not, by themselves, a general iff characterization of LP. The manuscript also asserts that a PF∞ kernel constructed from the golden ratio supplies the required total-positivity bridge, but that construction does not establish that the Riemann Xi function itself is LP without an additional exact transformation theorem.

Therefore this claim is classified as CANDIDATE / NOT VERIFIED, not PROVEN.

## Strongest surviving routes

1. Global Weil positivity with a rigorous density/closure theorem.
2. A self-adjoint Hilbert–Pólya operator with an unconditional exact determinant identity F(s)=ξ(s).
3. A complete all-orders Jensen/hyperbolicity mechanism for Xi.

## Rejection rules

- finite positivity != global positivity;
- low-order Turán != LP;
- asymptotic Jensen hyperbolicity != all Jensen polynomials hyperbolic;
- self-adjoint approximation != exact ξ identification;
- numerical zeros != proof;
- unreviewed proof claim != established theorem.

## Current conclusion

RH remains unresolved by this investigation. The cross-audit removes another tempting but invalid shortcut and leaves the global closure/exact-identification problem as the principal target.

PROPOSED != TESTED
TESTED != PROVEN
NUMERICAL != GLOBAL
UNKNOWN != FALSE
