# REL-PULSE-03 — Spatial Relational Pulsation and Propagating Modes

Date: 2026-09-08
Status: analytical + numerical audit

## Question
If the relational oscillator is extended from a finite cycle to a spatial local graph, does the same conservation/feedback structure produce a propagating oscillatory spectrum rather than only a local oscillator?

## Minimal spatial relation
Take a periodic one-dimensional graph with N sites and nearest-neighbor antisymmetric feedback:

    dx_j/dt = x_{j+1} - x_{j-1}

with periodic indices.

This is a local relational rule: site j receives the difference between its two neighboring states.

## Conservation
For

    E = 1/2 sum_j x_j^2

we obtain

    dE/dt = sum_j x_j(x_{j+1}-x_{j-1}) = 0

by index cancellation on the periodic graph.

Thus the local spatial relation redistributes the state without changing the quadratic measure.

## Plane-wave spectrum
Use

    x_j(t) = exp(i(k j - omega t)).

Then

    -i omega = exp(ik) - exp(-ik) = 2 i sin(k),

so

    omega(k) = -2 sin(k)

(up to Fourier/sign convention).

Therefore the relational network has a nontrivial dispersive oscillatory branch.

Group velocity:

    v_g = d omega/dk = -2 cos(k).

A localized disturbance is therefore transported through the graph, with a finite lattice speed bound |v_g| <= 2 in the chosen dimensionless units.

## Numerical checks
The expected tests are:

1. Construct the periodic nearest-neighbor skew matrix A_N.
2. Verify A_N + A_N^T = 0.
3. Verify conservation of E under numerical evolution.
4. Compare numerical eigenvalues with 2 i sin(2 pi m/N).
5. Initialize a localized packet and measure its center-of-mass motion.
6. Compare measured packet velocity against the group velocity predicted by omega(k).

## Countermodel
Replace the skew local feedback by the symmetric nearest-neighbor Laplacian

    dx_j/dt = x_{j+1} - 2x_j + x_{j-1}.

Its eigenvalues are

    lambda(k) = -4 sin^2(k/2),

which are real and non-positive. The modes relax/diffuse rather than oscillate.

This establishes that locality + nearest-neighbor relation alone does not select pulsation. The conservation/metric-skew condition is doing the selection in this restricted first-order class.

## Stronger chain

    local distinction
    → local relation
    → antisymmetric feedback under positive conservation
    → imaginary spectrum
    → omega(k)
    → finite-speed group transport
    → propagating relational pulsation.

## Boundary
This is still not an electromagnetic derivation. The model inputs include:

    one-dimensional periodic geometry;
    nearest-neighbor coupling;
    first-order time evolution;
    positive quadratic measure;
    a particular local difference rule.

It does not derive Maxwell's equations, transverse polarization, Lorentz invariance, c, or electromagnetic interpretation.

## Next target
Generalize the local graph to multiple coupled components per site and ask whether requiring:

    locality + positive conservation + propagating finite-speed modes + transverse constraint structure

selects a curl-like principal operator. This directly connects to REL-41/42 and the later LIGHT causal-cone work.
