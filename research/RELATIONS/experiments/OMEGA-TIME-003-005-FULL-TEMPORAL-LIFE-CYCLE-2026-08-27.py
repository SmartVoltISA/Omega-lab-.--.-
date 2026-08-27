"""OMEGA-TIME-003 -> 005
Full temporal life-cycle computational cross-check.
No physical time variable is used; iteration is only an ordinal index.
"""
import math
import random
import numpy as np

SEED = 20260827
random.seed(SEED)
rng = np.random.default_rng(SEED)

# TIME-003: continuation and recurrence
period_a, period_b = 5, 7
common = [n for n in range(1, 501) if n % period_a == 0 and n % period_b == 0]
assert common[:4] == [35, 70, 105, 140]

# TIME-004: scale ambiguity of relational continuation
q = list(range(101))
scales = [0.1, 1.0, 3.7, 100.0]
for c in scales:
    d = [c*x for x in q]
    assert all(d[i] < d[i+1] for i in range(100))

# TIME-005: arrow-like asymmetry from coarse-grained mixing
P = np.eye(16)[0]
M = np.zeros((16, 16))
for i in range(16):
    M[i, i] = 0.9
    M[i, (i-1) % 16] += 0.05
    M[i, (i+1) % 16] += 0.05
entropy = []
for _ in range(101):
    p = P[P > 0]
    entropy.append(float(-(p*np.log2(p)).sum()))
    P = P @ M
assert all(entropy[i+1] >= entropy[i] - 1e-12 for i in range(100))

print("OMEGA-TIME-003")
print("periods:", period_a, period_b)
print("first_common_recurrences:", common[:6])
print("OMEGA-TIME-004")
print("scales_tested:", scales)
print("OMEGA-TIME-005")
print("entropy_iteration_0:", entropy[0])
print("entropy_iteration_10:", entropy[10])
print("entropy_iteration_50:", entropy[50])
print("entropy_iteration_100:", entropy[100])
print("entropy_non_decreasing:", True)
print("RESULT: continuation/order exists without physical duration; duration needs a metric; an arrow requires an asymmetry in the ordered history.")
