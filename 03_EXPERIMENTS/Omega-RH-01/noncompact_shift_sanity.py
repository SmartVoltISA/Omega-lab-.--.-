"""RH-31 sanity check: finite-grid translation does not become compact in the continuum limit.

This is deliberately a numerical control, not the proof. We apply a symmetric finite
sum of interior translations to oscillatory functions supported on a small interval.
The input vectors become increasingly oscillatory while remaining norm 1. For a genuine
compact continuum operator their image norms along a weakly-null sequence would have to
go to zero. The script checks that the shift operator preserves a nonzero image norm.
"""

import math
import numpy as np


def shifted_output(x, f, shifts, coeffs):
    """Piecewise-linear interpolation of a finite sum of interior translations."""
    out = np.zeros_like(f, dtype=complex)
    for s, c in zip(shifts, coeffs):
        out += c * np.interp(x + s, x, f, left=0.0, right=0.0)
        out += c * np.interp(x - s, x, f, left=0.0, right=0.0)
    return out


def run(B=4.0, N=8000):
    x = np.linspace(-B, B, N)
    dx = x[1] - x[0]

    # Deliberately small interior support so translated copies do not overlap.
    width = 0.20
    center = -2.7
    mask = np.abs(x - center) < width / 2
    J = x[mask]

    # Distinct shifts corresponding to a few prime powers.
    raw = [(math.log(2), math.log(2) / math.sqrt(2)),
           (math.log(3), math.log(3) / math.sqrt(3)),
           (math.log(5), math.log(5) / math.sqrt(5))]

    # Keep only shifts whose translated support remains inside [-B,B].
    shifts, coeffs = [], []
    for s, c in raw:
        if center - width/2 - s > -B and center + width/2 + s < B:
            shifts.append(s)
            coeffs.append(c)

    print("RH-31 numerical sanity check")
    print(f"B={B}, grid={N}, support width={width}")
    print("shifts:", [round(s, 6) for s in shifts])
    print("coeffs:", [round(c, 6) for c in coeffs])
    print()

    for n in [10, 30, 100, 300, 1000, 3000]:
        f = np.zeros(N, dtype=complex)
        f[mask] = np.exp(1j * n * J)
        norm = math.sqrt(np.sum(np.abs(f) ** 2) * dx)
        f /= norm

        Tf = shifted_output(x, f, shifts, coeffs)
        out_norm = math.sqrt(np.sum(np.abs(Tf) ** 2) * dx)
        print(f"n={n:4d}  ||f_n||={math.sqrt(np.sum(np.abs(f)**2)*dx):.8f}  ||Tf_n||={out_norm:.8f}")

    print("\nInterpretation: persistent nonzero ||Tf_n|| is the expected numerical signature")
    print("of noncompact translation behavior. The analytic weakly-null argument is RH-31's proof;")
    print("this script is only a reproducibility control.")


if __name__ == "__main__":
    run()
