# REL-PULSE-04 — Curl Selection Audit

Date: 2026-09-08
Status: analytical + numerical audit

## Question
Can the spatial relational-pulsation chain be extended to a 3D vector field so that, within a restricted real isotropic first-order local class, positive quadratic conservation plus transverse propagation selects a curl-type principal operator?

## Restricted principal ansatz
For a real 3-component field X(x,t), translation invariance and rotational covariance constrain a first-order Fourier symbol to be built from the available isotropic tensors: I, kk^T, and the cross-product matrix [k]_x.

The cross-product matrix is

    [k]_x = [[0,-k_z,k_y],
             [k_z,0,-k_x],
             [-k_y,k_x,0]].

It is real and skew-symmetric:

    [k]_x^T = -[k]_x.

For a positive quadratic conserved measure, the generator must be skew with respect to that metric. In the Euclidean normalized case this excludes symmetric longitudinal gradient pieces from the conservative principal generator. The curl sector remains skew and local at first spatial order.

## Transverse structure
The curl symbol annihilates the longitudinal direction:

    [k]_x k = 0.

Thus one longitudinal mode has zero principal frequency while the two transverse modes have eigenvalues

    0, +|k|, -|k|

for i[k]_x in the Hermitian Fourier representation. A coefficient a changes these to

    0, +a|k|, -a|k|.

Hence the propagating branch is linear in |k| and the longitudinal sector is non-propagating at principal order.

## Numerical audit
1000 random 3D wavevectors were tested.

Checks:

    [k]_x + [k]_x^T = 0
    [k]_x k = 0
    eig(i[k]_x) = {-|k|, 0, +|k|}

The numerical residuals are at floating-point roundoff level.

## Countermodels

### 1. Isotropic identity/gradient sector
An identity-type first-order symbol does not annihilate k. It therefore propagates the longitudinal component as well. Isotropy alone does not imply transverse propagation.

### 2. Preferred-axis skew sector
A fixed skew matrix generated from a preferred vector is energy-conserving and can oscillate, but it breaks rotational isotropy. Therefore conservation + pulsation alone does not select curl.

### 3. Higher-order isotropic curl sectors
Terms such as f(|k|^2)[k]_x also preserve the transverse structure. First spatial order is therefore essential if the goal is to select the principal curl operator rather than an arbitrary higher-derivative function of curl.

## Result
Within the restricted class

    real field
    + translation invariance
    + rotational isotropy
    + local first spatial order
    + positive quadratic conservation
    + exactly transverse propagating principal modes

there is a strong selection of the curl-type principal structure, up to coefficient/sign and field normalization.

This is a genuine bridge:

    local distinction
    → local relation
    → feedback
    → positive conservation
    → oscillatory spectrum
    → spatial propagation
    → transverse constraint
    → curl-like principal operator

## What is NOT derived
This does not derive:

    Maxwell's full equations;
    electric/magnetic interpretation;
    two independent fields E and B;
    epsilon_0 or mu_0;
    SI scale;
    c's numerical value;
    Lorentz invariance;
    U(1) gauge group;
    photon quantization.

Those remain separate gates already audited in REL-41 through REL-47.

## Next gate
The next decisive test is to use TWO coupled vector fields and require the same conservation, locality, isotropy and transverse structure. Then test whether the minimal first-order coupled system is forced into the Maxwell principal class

    dE/dt = alpha curl B
    dB/dt = -beta curl E

rather than merely a single-field curl oscillator.

Even if selected, alpha*beta remains a free scale until a further physical normalization/matching condition is supplied.
