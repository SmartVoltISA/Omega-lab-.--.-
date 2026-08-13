import numpy as np
import matplotlib.pyplot as plt

# Ω-REL-002 — add a weight to each relation and observe the dynamics.
# Exploratory relation-level model; NOT a reproduction of the historical
# Ω edge-only experiment.

SEED = 42
N = 12
STEPS = 250
DECAY = 0.985
COUPLING = 0.08
NOISE = 0.015

rng = np.random.default_rng(SEED)
W = rng.uniform(0.2, 1.0, size=(N, N))
np.fill_diagonal(W, 0.0)

history_mean = []
history_std = []
history_concentration = []

for _ in range(STEPS):
    mean_w = W.sum() / (N * (N - 1))
    W += COUPLING * (mean_w - W)
    W *= DECAY
    W += rng.normal(0, NOISE, size=W.shape)
    W = np.clip(W, 0.0, 1.0)
    np.fill_diagonal(W, 0.0)

    vals = W[~np.eye(N, dtype=bool)]
    history_mean.append(vals.mean())
    history_std.append(vals.std())

    k = max(1, int(0.10 * len(vals)))
    ordered = np.sort(vals)[::-1]
    concentration = ordered[:k].sum() / ordered.sum() if ordered.sum() else 0.0
    history_concentration.append(concentration)

plt.figure(figsize=(8, 6))
plt.imshow(W, interpolation="nearest", vmin=0, vmax=1)
plt.title("Ω REL-002 — Relation weights after evolution")
plt.xlabel("Target relation index")
plt.ylabel("Source relation index")
plt.colorbar(label="relation weight")
plt.tight_layout()
plt.savefig("omega_rel_002_final_weights.png", dpi=160)
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(history_mean, label="mean weight")
plt.plot(history_std, label="spread of weights")
plt.plot(history_concentration, label="top-10% concentration")
plt.title("Ω REL-002 — Evolution of relation weights")
plt.xlabel("step")
plt.ylabel("value")
plt.legend()
plt.tight_layout()
plt.savefig("omega_rel_002_weight_evolution.png", dpi=160)
plt.show()

print("STATUS: exploratory execution.")
print(f"Seed: {SEED}")
print(f"Nodes: {N}")
print(f"Directed relations: {N*(N-1)}")
print(f"Steps: {STEPS}")
print(f"Final mean relation weight: {history_mean[-1]:.6f}")
print(f"Final spread (std): {history_std[-1]:.6f}")
print(f"Final top-10% concentration: {history_concentration[-1]:.6f}")
