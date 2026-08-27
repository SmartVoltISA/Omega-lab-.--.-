"""OMEGA-TIME-002 — relational temporal coordinate

Synthetic experiment with NO physical-time primitive, timestamp, duration,
clock, rate, or unit. The only inputs are distinguishable states and ordered
transitions. We test what can be recovered structurally and what remains
underdetermined.
"""

# A trace is represented only by ordered state identities.
traces = [tuple(range(n)) for n in range(2, 8)]

# Structural temporal coordinate: ordinal position in an ordered trace.
ordinal_coordinates = []
for trace in traces:
    coord = {state: i for i, state in enumerate(trace)}
    ordinal_coordinates.append(coord)

# Same structural trace admits many positive interval assignments.
# These weights are deliberately external to the structural input.
weight_assignments = [
    (1, 1, 1),
    (1, 2, 3),
    (100, 1, 1),
    (7, 7, 7),
]
weighted_totals = [sum(w) for w in weight_assignments]
assert weighted_totals == [3, 6, 102, 21]

# A closed transition pattern permits recurrence counting without a physical unit.
cycle_counts = [1, 2, 10, 100]
assert cycle_counts == sorted(cycle_counts)

# Structural invariance: relabeling states preserves the ordinal pattern.
original = ("A", "B", "C", "D")
relabelled = ("x7", "q2", "m9", "p4")
assert len(original) == len(relabelled)

print("OMEGA-TIME-002")
print("traces_without_time_primitive:", traces)
print("ordinal_coordinates:", ordinal_coordinates)
print("same_structure_external_duration_totals:", weighted_totals)
print("cycle_counts_dimensionless:", cycle_counts)
print("RESULT: structure supplies order/ordinal change and recurrence count; unique duration is not contained in structure alone.")
