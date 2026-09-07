# REL-PULSE-01 — Autonomous Relational Oscillation

Date: 2026-09-08
Status: exploratory numerical test

## Question
Can periodic motion emerge from mutual relational feedback without imposing a sinusoidal external drive?

## Minimal model
Three states x=(x1,x2,x3) are coupled cyclically by an antisymmetric relational operator:

A = [[0, 1, -1],
     [-1, 0, 1],
     [1, -1, 0]]

Evolution:

    dx/dt = A x

No sinusoidal source, no externally prescribed frequency, and no time-periodic coefficient are supplied.

## Structural property
A is antisymmetric, so for the quadratic state measure

    E = 1/2 xᵀx

we have

    dE/dt = xᵀ A x = 0.

Thus the relational dynamics redistribute the state while conserving this quadratic measure.

The eigenvalues are

    0, +i√3, -i√3.

Therefore the nontrivial relational subspace has an intrinsic angular frequency √3.

## Interpretation
A closed antisymmetric relation cycle can generate an oscillatory mode from its own relational structure. The frequency is an eigenmode of the relation operator; it is not injected by an external sinusoidal driver.

The zero eigenvalue corresponds to the uniform mode x1=x2=x3, which does not participate in the cyclic oscillation.

## Important boundary
This is not yet a derivation of physical oscillation, electromagnetic waves, or light. The antisymmetric operator, continuous time, quadratic conserved measure, and three-state topology are model inputs.

The result is stronger than an externally driven RLC analogy in one specific sense: periodicity is an internal mode of the relational operator rather than a prescribed forcing waveform.

## Next test
Remove the explicitly chosen antisymmetric matrix and search whether a more minimal Ω rule — distinction + relation + local feedback + conservation/constraint — selects an operator with a nonzero imaginary eigenpair. Test symmetric, directed, dissipative, and nonlinear countermodels.
