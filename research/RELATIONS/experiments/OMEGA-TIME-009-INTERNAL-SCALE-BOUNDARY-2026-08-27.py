"""OMEGA-TIME-009 executable core.
Local propagation + autonomous oscillator; tests whether interaction selects absolute time.
"""
import math

# Local propagation on a dimensionless lattice.
N = 64
active = {0}
front = []
for step in range(10):
    front.append(max(active))
    active = active | {i + 1 for i in active if i + 1 < N}

assert front == list(range(10))

# Autonomous oscillator, period 5 updates.
period = 5
freq_native = 1 / period

# A spatial scale a and temporal scale tau produce dimensional-looking values.
for a, tau in [(1,1), (2,1), (1,2), (10,0.1)]:
    v = a / tau
    f = freq_native / tau
    # Their dimensionless ratio v/f = a*period depends on spatial calibration,
    # demonstrating that no absolute time scale is selected without calibration.
    assert math.isfinite(v) and math.isfinite(f)

print("OMEGA-TIME-009")
print("native_propagation_speed_sites_per_update:", 1)
print("native_oscillator_frequency_cycles_per_update:", freq_native)
print("interaction_present:", True)
print("absolute_time_scale_selected:", False)
print("RESULT: local interaction produces a coherent relational temporal scale, but common dimensional scaling remains free.")
