"""OMEGA-TIME-007
Frequency, speed, and temporal interval decomposition.
No claim about the ontology of time is made by this script.
"""
import numpy as np

# Fixed change per transition; vary frequency.
dx = 0.25
freqs = np.array([1.0, 2.0, 5.0, 10.0])
dt = 1.0 / freqs
speed = dx / dt
assert np.allclose(speed, dx * freqs)

# Same state sequence, different replay/traversal rates.
n = 10
total_duration = n / freqs
assert np.allclose(total_duration, [10.0, 5.0, 2.0, 1.0])

# Inverse control: fixed speed, vary transition size and frequency.
target_speed = 1.0
dx_inverse = target_speed / freqs
speed_recovered = dx_inverse * freqs
assert np.allclose(speed_recovered, target_speed)

# Periodic relation example: two frequencies; common recurrence is
# determined by their ratio when frequencies are commensurate.
f_a, f_b = 5.0, 7.0
common_period = 1.0  # both have integer cycles in one second here
assert np.isclose(f_a * common_period, 5.0)
assert np.isclose(f_b * common_period, 7.0)

print("OMEGA-TIME-007")
print("fixed_dx_m:", dx)
print("frequencies_hz:", freqs.tolist())
print("intervals_s:", dt.tolist())
print("speeds_m_per_s:", speed.tolist())
print("10_transition_durations_s:", total_duration.tolist())
print("inverse_dx_m_for_1m_per_s:", dx_inverse.tolist())
print("RESULT: frequency and speed are rates defined relative to temporal interval; changing frequency changes traversal duration/speed while preserving the state sequence.")
print("ONTOLOGY: not determined; fundamental-time and relational-time interpretations remain open.")
