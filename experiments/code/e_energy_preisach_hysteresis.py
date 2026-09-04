"""E-ENERGY-PREISACH-001
Dimensionless Preisach-style relay ensemble.
Tests history-dependent internal state and loop work.
This is a computational model, not a physical measurement.
"""
import numpy as np


def build_relays(n=20):
    relays = []
    for alpha in np.linspace(0.1, 1.0, n):
        for beta in np.linspace(-1.0, -0.1, n):
            if alpha > beta:
                relays.append((alpha, beta))
    for alpha in np.linspace(0.1, 1.0, n):
        for beta in np.linspace(-0.1, 0.1, max(3, n // 4)):
            if alpha > beta:
                relays.append((alpha, beta))
    return np.asarray(relays, dtype=float)


def simulate(H, relays):
    state = -np.ones(len(relays))
    M = []
    for h in H:
        high = h >= relays[:, 0]
        low = h <= relays[:, 1]
        state[high] = 1.0
        state[low] = -1.0
        M.append(state.mean())
    return np.asarray(M)


def loop_area(H, M):
    return float(np.trapezoid(M, H))


def main():
    relays = build_relays(20)
    up = np.linspace(-1.0, 1.0, 4001)
    down = np.linspace(1.0, -1.0, 4001)
    H = np.concatenate([up, down, up])
    M = simulate(H, relays)

    area = loop_area(H, M)
    # A history-dependent check: same H can have different M on opposite branches.
    checks = {}
    for target in (-0.5, 0.0, 0.5):
        idx = np.where(np.isclose(H, target, atol=2.5e-4))[0]
        checks[target] = (float(M[idx].min()), float(M[idx].max()))

    assert area < 0.0, area  # orientation is down/up convention; magnitude is dissipation proxy.
    assert abs(area) > 1.0, area
    for lo, hi in checks.values():
        assert hi - lo > 0.1

    print(f"relays={len(relays)}")
    print(f"M_min={M.min():.12f}")
    print(f"M_max={M.max():.12f}")
    print(f"oriented_loop_area={area:.12f}")
    print(f"loop_area_magnitude={abs(area):.12f}")
    for h, (lo, hi) in checks.items():
        print(f"H={h:+.1f}: M_range=[{lo:.12f}, {hi:.12f}]")


if __name__ == "__main__":
    main()
