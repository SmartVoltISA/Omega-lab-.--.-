"""OMEGA-TIME-010 executable experiment.
Common causal update coordinate lambda; local temporal accumulation from internal state changes.
"""
import numpy as np

rng = np.random.default_rng(42)
N = 1000
K = 1000
p = {"gas_like": 0.95, "liquid_like": 0.45, "crystal_like": 0.05}

out = {}
for name, prob in p.items():
    state = np.zeros(N, dtype=np.int8)
    activity = []
    for _ in range(K):
        changed = rng.random(N) < prob
        state ^= changed.astype(np.int8)
        activity.append(changed.mean())
    activity = np.asarray(activity)
    tau = activity.sum()
    out[name] = (activity.mean(), activity.std(), tau)

print("OMEGA-TIME-010")
for name, (mean, std, tau) in out.items():
    print(name, "mean_activity=", mean, "std=", std, "tau_1000=", tau)
ratio = out["gas_like"][2] / out["crystal_like"][2]
print("gas_to_crystal_tau_ratio=", ratio)
print("RESULT: same causal-update count yields strongly different accumulated internal change rates across dynamical states.")
print("PHYSICAL_CLAIM_ESTABLISHED=", False)
