import numpy as np
import matplotlib.pyplot as plt

SEED = 20260813
RUNS = 100
STEPS = 500
OPTIONS = 8
COMPETITION = 1.0
MEMORY_RATE = 0.12

def softmax(x):
    z = x - np.max(x)
    e = np.exp(z)
    return e / e.sum()

def run(memory_enabled, seed):
    rng = np.random.default_rng(seed)
    strength = rng.normal(0, 0.15, OPTIONS)
    memory = np.zeros(OPTIONS)
    winners = []
    winner_persistence = []

    for t in range(STEPS):
        drive = rng.normal(0, 0.20, OPTIONS)
        score = strength + drive + memory
        p = softmax(COMPETITION * score)
        winner = int(rng.choice(OPTIONS, p=p))
        winners.append(winner)

        strength *= 0.995
        strength[winner] += 0.08

        if memory_enabled:
            memory *= (1.0 - MEMORY_RATE)
            memory[winner] += MEMORY_RATE

        if t > 0:
            winner_persistence.append(winners[-1] == winners[-2])

    changes = sum(winners[i] != winners[i-1] for i in range(1, len(winners)))
    counts = np.bincount(winners, minlength=OPTIONS)
    probs = counts / counts.sum()
    entropy = -(probs[probs > 0] * np.log(probs[probs > 0])).sum()

    return {
        'persistence': np.mean(winner_persistence),
        'changes': changes,
        'entropy': entropy,
        'distinct': np.count_nonzero(counts),
        'final_memory_max': memory.max(),
    }

results = {0: [], 1: []}
for model in [0, 1]:
    for i in range(RUNS):
        results[model].append(run(model == 1, SEED + model * 10000 + i))

def avg(key, model):
    x = np.array([r[key] for r in results[model]], dtype=float)
    return x.mean(), x.std(ddof=1)

print('STATUS: execution completed.')
print('Omega REL-009 — Conflict -> Selection -> Memory')
print(f'Runs per model: {RUNS}')
print(f'Steps per run: {STEPS}')
for model, name in [(0, 'M0 — no memory'), (1, 'M1 — memory')]:
    print(name)
    for key in ['persistence', 'changes', 'entropy', 'distinct']:
        print(f'  {key}: {avg(key, model)[0]:.4f} +/- {avg(key, model)[1]:.4f}')

labels = ['без памяти', 'с памятью']
means = [avg('persistence', m)[0] for m in [0, 1]]
errs = [avg('persistence', m)[1] for m in [0, 1]]
plt.figure(figsize=(7, 5))
plt.errorbar(labels, means, yerr=errs, marker='o')
plt.ylabel('доля повторения победителя')
plt.title('Omega REL-009 — сохраняется ли результат борьбы?')
plt.tight_layout()
plt.savefig('omega_rel_009_persistence.png', dpi=160)
plt.show()
