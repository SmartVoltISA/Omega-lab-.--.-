# REL-PULSE-02 — Conservation + Local Feedback: What Is Actually Selected?

Date: 2026-09-08
Status: numerical/algebraic audit

## Question
Can the Ω package `distinction + relation + local feedback + positive conserved quadratic measure` force an oscillatory mode without explicitly postulating an antisymmetric operator?

## Linear first-order case
Consider

    dx/dt = A x

and a positive quadratic conserved measure

    E = 1/2 x^T K x,   K = K^T > 0.

Exact conservation for every state requires

    dE/dt = x^T K A x = 0,

which is equivalent to

    K A + A^T K = 0.

Thus A is skew-adjoint with respect to the positive metric K.

After the change of variables y = K^(1/2)x, the transformed generator

    B = K^(1/2) A K^(-1/2)

satisfies

    B + B^T = 0.

Therefore every eigenvalue of B (and A) is purely imaginary or zero.

## Consequence
The imaginary spectrum is NOT an extra assumption once all of the following are simultaneously imposed:

    linear first-order continuous evolution
    + positive-definite quadratic conservation
    + exact conservation for every state.

The nonzero modes are oscillatory in the linear system.

## Numerical audit
Random real matrices were generated, projected to the K=I conservation class by

    A = M - M^T.

For dimensions 2 through 6, 1000 random matrices per dimension were tested. The largest absolute real part of any eigenvalue was at machine precision:

    n=2: < 1e-15
    n=3: < 1e-15
    n=4: < 1e-15
    n=5: < 1e-15
    n=6: < 1e-15

The three-state cyclic operator used in REL-PULSE-01 has spectrum

    0, +i*sqrt(3), -i*sqrt(3).

## But this does NOT yet derive pulsation from Ω alone
The crucial hidden inputs are still:

    first-order evolution
    linearization / linear operator description
    continuous time
    positive-definite quadratic conserved measure.

Without these, conservation does not guarantee periodic motion.

## Countermodel 1 — conserved equilibrium

    dx/dt = 0

conserves every state measure but produces no motion and no pulsation.

## Countermodel 2 — higher-dimensional quasiperiodic motion

Two independent rotations with incommensurate frequencies conserve

    E = 1/2(x1^2+x2^2+x3^2+x4^2)

but the complete trajectory is generally quasiperiodic rather than periodic. Therefore conservation selects recurrence/oscillatory structure in the linear skew class, but not a single universal period.

## Countermodel 3 — dissipative feedback

A stable feedback matrix with negative real eigenvalues produces relaxation rather than oscillation. It can satisfy locality and feedback but violates exact conservation.

## Strongest result
The derivation chain is now:

    positive conserved quadratic measure
    → metric-skew generator
    → purely imaginary/zero spectrum
    → oscillatory linear modes.

This is stronger than REL-PULSE-01 because antisymmetry is no longer chosen as the starting matrix; it follows algebraically from the conservation requirement within the stated linear class.

## Remaining boundary
Ω has not yet derived:

    why evolution is first-order;
    why the conserved measure is positive and quadratic;
    why the dynamics are linear near the relevant state;
    why the state space is finite-dimensional;
    why a particular mode is selected;
    why the oscillation propagates spatially;
    why its speed is c;
    why the carrier is electromagnetic.

## Next target
Move from a finite relational cycle to a spatial local graph. Test whether

    local relation + local feedback + positive conservation

selects a nearest-neighbor skew generator whose spectrum contains a propagating branch,

    omega(k),

rather than only a spatially uniform oscillator.

That is the decisive bridge:

    RELATIONAL PULSATION → PROPAGATING PULSATION → WAVE.
