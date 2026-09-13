"""E-ENERGY-HYSTERESIS-BALANCE-001

Dimensionless magnetic-relaxation toy model for energy-accounting tests.
This is not a material-identification model and makes no physical claim by itself.

F(H,M) = 0.5*a*M^2 - b*H*M
Mdot = -gamma*dF/dM
W_ext = - integral(b*M*dH)
D = integral(Mdot^2/gamma dt) >= 0
Therefore W_ext = Delta F + D (up to numerical integration error).

The experiment deliberately compares a full boundary (H,M) with an
incomplete visible boundary that records H only. Over a closed H cycle,
Delta of any H-only endpoint quantity is zero, while W_ext remains nonzero;
the missing accounting channel is the internal state M and its dissipation.
"""

import numpy as np

A = 2.0
B = 1.0
GAMMA = 8.0
DT = 1e-4
N = 5000
CYCLES = 20

H = np.concatenate((np.linspace(-1, 1, N), np.linspace(1, -1, N)[1:]))

M = 0.0
for _ in range(CYCLES):
    W = 0.0
    D = 0.0
    F0 = None
    prev_h = H[0]
    for h in H:
        F = 0.5 * A * M * M - B * h * M
        if F0 is None:
            F0 = F
        dh = h - prev_h
        W += -B * M * dh
        mdot = -GAMMA * (A * M - B * h)
        D += (mdot * mdot / GAMMA) * DT
        M += DT * mdot
        prev_h = h
    F1 = 0.5 * A * M * M - B * H[-1] * M

full_residual = W - (F1 - F0) - D
visible_only_residual = W  # H returns to its initial value; no internal M is recorded.

print(f"cycles={CYCLES}")
print(f"W_ext={W:.12f}")
print(f"Delta_F={F1 - F0:.12f}")
print(f"Dissipation={D:.12f}")
print(f"full_residual={full_residual:.12e}")
print(f"visible_only_residual={visible_only_residual:.12f}")
print(f"final_M={M:.12f}")

assert abs(full_residual) < 5e-4
assert visible_only_residual > 0.3
