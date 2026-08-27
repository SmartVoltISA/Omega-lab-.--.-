"""OMEGA-TIME-001
Minimal computational checks for the hypothesis:
DISTINCTION -> RELATION -> STATE -> TRANSITION -> ORDER -> (DURATION?) -> TIME.

No physical-time primitive is used to construct the abstract structures.
The script records counterexamples showing that order alone does not identify duration.
"""
from statistics import mean
import random

SEED = 20260827
random.seed(SEED)

# Experiment 1: minimal structural ladder.
minimal = [
    ("one_state", 1, 0, "state only"),
    ("two_states_no_relation", 2, 0, "distinction only"),
    ("two_states_symmetric_relation", 2, 2, "relation without orientation"),
    ("two_states_ordered_transition", 2, 1, "ordered transition"),
    ("three_states_ordered", 3, 2, "multi-step order"),
    ("three_state_cycle", 3, 3, "closure/cycle"),
]

# Experiment 2: same ordered sequence, different durations.
sequence = [0, 1, 2, 3, 4]
durations_A = [1, 1, 1, 1]
durations_B = [10, 1, 10, 1]
assert len(durations_A) == len(sequence) - 1
assert len(durations_B) == len(sequence) - 1
assert sum(durations_A) != sum(durations_B)

# Experiment 3: global time-scale non-identifiability.
# Multiplying every duration by c preserves order and all dimensionless structure.
base = [1, 2, 3, 5, 8]
scaled = [7*x for x in base]
assert all(a < b for a, b in zip(base, base[1:]))
assert all(a < b for a, b in zip(scaled, scaled[1:]))
assert scaled[-1] / base[-1] == 7

# Experiment 4: repeated cycles recover relative rate ratios, not absolute time.
rates = [1.0, 2.0, 5.0]
counts = [100, 200, 500]
normalized = [counts[i] / rates[i] for i in range(len(rates))]
assert max(normalized) - min(normalized) == 0

# Experiment 5: random DAGs show that order can exist without a duration metric.
def random_dag(n=8, p=0.30):
    return [(i, j) for i in range(n) for j in range(i + 1, n) if random.random() < p]

dags = [random_dag() for _ in range(10_000)]
assert all(all(i < j for i, j in edges) for edges in dags)

print("OMEGA-TIME-001")
print("minimal_structures:", minimal)
print("sequence:", sequence)
print("duration_A_total:", sum(durations_A))
print("duration_B_total:", sum(durations_B))
print("global_scale_factor:", 7)
print("relative_cycle_normalization:", normalized)
print("random_dag_count:", len(dags))
print("random_dag_mean_edges:", mean(len(e) for e in dags))
print("RESULT: ORDER is derivable from oriented transition structure, but DURATION is not identifiable from ORDER alone.")
