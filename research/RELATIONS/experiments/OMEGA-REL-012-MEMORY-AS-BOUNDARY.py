# Ω REL-012 — Memory as Boundary
# Reproducible exploratory experiment.
#
# M0: no memory.
# M1: memory stored but does not alter transitions.
# M2: stored transition record forbids the same transition for K steps.
#
# All paired models share the same initial state, external scores and draw stream.

import numpy as np
import matplotlib.pyplot as plt

RUNS = 200
STEPS = 600
N = 10
K = 5
BASE_SEED = 20260813


def choose(scores, allowed, u):
    p = np.zeros(N)
    p[allowed] = np.exp(scores[allowed] - np.max(scores[allowed]))
    p /= p.sum()
    c = np.cumsum(p)
    return min(int(np.searchsorted(c, u, side="right")), N - 1)


def run_model(seed, mode):
    rng = np.random.default_rng(seed)
    external = rng.normal(0, 0.7, (STEPS, N))
    draws = rng.random(STEPS)
    state = int(rng.integers(N))
    memory = {}
    allowed_counts = []

    for t in range(STEPS):
        memory = {edge: remaining - 1
                  for edge, remaining in memory.items()
                  if remaining > 1}

        allowed = np.ones(N, dtype=bool)
        allowed[state] = False

        if mode == "boundary":
            for j in range(N):
                if (state, j) in memory:
                    allowed[j] = False
            if not allowed.any():
                allowed[:] = True
                allowed[state] = False

        next_state = choose(external[t], allowed, draws[t])

        if mode == "boundary":
            memory[(state, next_state)] = K

        state = next_state
        allowed_counts.append(int(allowed.sum()))

    return np.array(allowed_counts)


def run_intervention(seed):
    rng = np.random.default_rng(seed)
    external = rng.normal(0, 0.7, (STEPS, N))
    draws = rng.random(STEPS)
    state = int(rng.integers(N))
    memory = {}
    allowed_counts = []

    for t in range(STEPS):
        memory = {edge: remaining - 1
                  for edge, remaining in memory.items()
                  if remaining > 1}

        boundary_on = not (STEPS // 3 <= t < 2 * STEPS // 3)
        allowed = np.ones(N, dtype=bool)
        allowed[state] = False

        if boundary_on:
            for j in range(N):
                if (state, j) in memory:
                    allowed[j] = False
            if not allowed.any():
                allowed[:] = True
                allowed[state] = False

        next_state = choose(external[t], allowed, draws[t])

        if boundary_on:
            memory[(state, next_state)] = K

        state = next_state
        allowed_counts.append(int(allowed.sum()))

    return np.array(allowed_counts)


if __name__ == "__main__":
    m0 = np.array([run_model(BASE_SEED + i, "none") for i in range(RUNS)])
    m1 = np.array([run_model(BASE_SEED + i, "none") for i in range(RUNS)])
    m2 = np.array([run_model(BASE_SEED + i, "boundary") for i in range(RUNS)])
    intervention = np.array([
        run_intervention(BASE_SEED + 10000 + i) for i in range(RUNS)
    ])

    print("M0 mean available transitions:", m0.mean())
    print("M1 mean available transitions:", m1.mean())
    print("M2 mean available transitions:", m2.mean())
    print("M2 intervention ON before:", intervention[:, :STEPS//3].mean())
    print("M2 intervention OFF:", intervention[:, STEPS//3:2*STEPS//3].mean())
    print("M2 intervention ON after:", intervention[:, 2*STEPS//3:].mean())

    plt.figure(figsize=(8, 5))
    plt.boxplot(
        [m0.mean(axis=1), m1.mean(axis=1), m2.mean(axis=1)],
        tick_labels=["no memory", "stored only", "memory boundary"]
    )
    plt.ylabel("mean available transitions")
    plt.title("Ω REL-012 — Memory as Boundary")
    plt.tight_layout()
    plt.show()
