import numpy as np

N = 101
T = 500
CENTER = N // 2


def step(x, rule):
    y = np.empty_like(x)
    for i in range(N):
        code = (int(x[(i-1) % N]) << 2) | (int(x[i]) << 1) | int(x[(i+1) % N])
        y[i] = (rule >> code) & 1
    return y


def run(rule, seed_pos=CENTER, steps=T):
    x = np.zeros(N, dtype=np.uint8)
    x[seed_pos] = 1
    sizes = []
    states = []
    for _ in range(steps):
        states.append(x.copy())
        sizes.append(int(x.sum()))
        x = step(x, rule)
    return states, sizes


def com_local(x, reference=CENTER):
    xs = np.where(x)[0]
    if len(xs) == 0:
        return None
    vals = np.array([((int(i)-reference+N//2) % N)-N//2+reference for i in xs])
    return float(vals.mean())


# Exhaustive scan: all 256 binary radius-1 local interaction rules.
localized = []
for rule in range(256):
    states, sizes = run(rule)
    tail = sizes[-100:]
    if all(s > 0 for s in tail) and max(tail) <= 25:
        localized.append((rule, min(tail), max(tail), len(set(tail))))

# Stronger screen: persistent nontrivial localized structures with displacement.
traveling = []
for rule in range(256):
    states, sizes = run(rule, steps=300)
    tail = sizes[-100:]
    if min(tail) >= 2 and max(tail) <= 10 and max(tail)-min(tail) <= 2:
        cms = [com_local(x) for x in states[-50:]]
        if all(c is not None for c in cms):
            velocity = (cms[-1] - cms[0]) / 49.0
            if abs(velocity) > 0.05:
                traveling.append((rule, velocity, min(tail), max(tail)))

print('persistent localized rules:', len(localized))
print('traveling localized rules:', len(traveling))
print('traveling:', traveling)

# Direct trace for Rule 14.
states, _ = run(14, steps=12)
for t, x in enumerate(states):
    print(t, np.where(x)[0].tolist())
