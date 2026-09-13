import numpy as np
from scipy import stats
from collections import defaultdict, Counter

# Ω-MEM-2 — archived source supplied by the experiment run
PROTOCOL = {
    "name": "Ω-MEM-2",
    "question": "Может ли память давать системе преимущество в предсказании будущего?",
    "generator": {"type": "Markov order-2", "alphabet": ["X", "Y"], "p_repeat": 0.9,
                   "length": 1000, "burn_in": 100, "num_seeds": 50},
    "models": {"M0": 1, "M2": 2, "M4": 4, "M8": 8, "R2": 2, "R4": 4, "R8": 8}
}

class PredictionMachine:
    def __init__(self, S, rule_type='structured', seed=None):
        self.S, self.rule_type, self.seed = S, rule_type, seed
        self.next_state = {}
        if rule_type == 'structured':
            for s in range(S):
                self.next_state[(s, 'X')] = (s + 1) % S
                self.next_state[(s, 'Y')] = s
        elif rule_type == 'random':
            rng = np.random.RandomState(seed)
            for s in range(S):
                for inp in ['X', 'Y']:
                    self.next_state[(s, inp)] = rng.randint(0, S)
        elif rule_type == 'no_memory':
            for s in range(S):
                for inp in ['X', 'Y']:
                    self.next_state[(s, inp)] = 0

    def step(self, state, inp):
        return self.next_state[(state, inp)]

    def run(self, sequence):
        state, states = 0, [0]
        for inp in sequence:
            state = self.step(state, inp)
            states.append(state)
        return states

def generate_markov2(seed, length=1000, burn_in=100, p_repeat=0.9):
    rng = np.random.RandomState(seed)
    seq = [rng.choice(['X', 'Y']), rng.choice(['X', 'Y'])]
    for _ in range(length + burn_in - 2):
        if rng.random_sample() < p_repeat:
            seq.append(seq[-1])
        else:
            seq.append('Y' if seq[-1] == 'X' else 'X')
    return seq[burn_in:]

def generate_random_sequence(seed, length=1000, burn_in=100):
    rng = np.random.RandomState(seed)
    return list(rng.choice(['X', 'Y'], size=length + burn_in)[burn_in:])

def generate_periodic(period_pattern, length=500):
    return [period_pattern[i % len(period_pattern)] for i in range(length)]

def train_predictor(states, sequence):
    counts = defaultdict(Counter)
    for i in range(len(sequence) - 1):
        counts[states[i]][sequence[i + 1]] += 1
    return {s: c.most_common(1)[0][0] for s, c in counts.items()}

def test_predictor(states, sequence, pred_map):
    correct = total = 0
    for i in range(len(sequence) - 1):
        if states[i] in pred_map:
            total += 1
            correct += pred_map[states[i]] == sequence[i + 1]
    return correct / total if total else 0.5

def intervention_prediction(machine, sequence, pred_map, reset_step):
    states = machine.run(sequence)
    cb = tb = 0
    for i in range(reset_step):
        if states[i] in pred_map:
            tb += 1
            cb += pred_map[states[i]] == sequence[i + 1]
    states_after = [0]
    for i in range(reset_step, len(sequence) - 1):
        states_after.append(machine.step(states_after[-1], sequence[i]))
    ca = ta = 0
    for i in range(len(states_after) - 1):
        idx = reset_step + i
        if idx < len(sequence) - 1 and states_after[i] in pred_map:
            ta += 1
            ca += pred_map[states_after[i]] == sequence[idx + 1]
    return (cb / tb if tb else 0.5, ca / ta if ta else 0.5)

# Ω-MEM-2 main experiment
results = defaultdict(list)
intervention_results = defaultdict(list)
for seed in range(50):
    seq = generate_markov2(seed)
    train_seq, test_seq = seq[:500], seq[500:]
    m0 = PredictionMachine(1, 'no_memory')
    p0 = train_predictor(m0.run(train_seq), train_seq)
    results['M0'].append(test_predictor(m0.run(test_seq), test_seq, p0))
    for S in [2, 4, 8]:
        m = PredictionMachine(S, 'structured')
        p = train_predictor(m.run(train_seq), train_seq)
        results[f'M{S}'].append(test_predictor(m.run(test_seq), test_seq, p))
        intervention_results[f'M{S}'].append(intervention_prediction(m, test_seq, p, 250))
    for S in [2, 4, 8]:
        m = PredictionMachine(S, 'random', seed=seed + S * 1000)
        p = train_predictor(m.run(train_seq), train_seq)
        results[f'R{S}'].append(test_predictor(m.run(test_seq), test_seq, p))

# Ω-MEM-2a: cross-seed test
cross_results = defaultdict(list)
for seed_train in range(25):
    for seed_test in range(25, 50):
        a, b = generate_markov2(seed_train, 500), generate_markov2(seed_test, 500)
        m0 = PredictionMachine(1, 'no_memory')
        p0 = train_predictor(m0.run(a), a)
        cross_results['M0'].append(test_predictor(m0.run(b), b, p0))
        for S in [2, 4, 8]:
            m = PredictionMachine(S, 'structured')
            p = train_predictor(m.run(a), a)
            cross_results[f'M{S}'].append(test_predictor(m.run(b), b, p))
        for S in [2, 4, 8]:
            m = PredictionMachine(S, 'random', seed=seed_train + S * 1000)
            p = train_predictor(m.run(a), a)
            cross_results[f'R{S}'].append(test_predictor(m.run(b), b, p))

# Ω-MEM-2b: periodic XXYY
periodic_results = defaultdict(list)
for _offset in range(4):
    seq = generate_periodic(['X', 'X', 'Y', 'Y'], 1000)
    train_seq, test_seq = seq[:500], seq[500:]
    m0 = PredictionMachine(1, 'no_memory')
    p0 = train_predictor(m0.run(train_seq), train_seq)
    periodic_results['M0'].append(test_predictor(m0.run(test_seq), test_seq, p0))
    for S in [2, 4, 8]:
        m = PredictionMachine(S, 'structured')
        p = train_predictor(m.run(train_seq), train_seq)
        periodic_results[f'M{S}'].append(test_predictor(m.run(test_seq), test_seq, p))

# Ω-MEM-2c: intervention on periodic pattern
pattern = ['X', 'X', 'Y', 'Y']
seq = generate_periodic(pattern, 1000)
train_seq, test_seq = seq[:500], seq[500:]
periodic_intervention = {}
for S in [2, 4, 8]:
    m = PredictionMachine(S, 'structured')
    p = train_predictor(m.run(train_seq), train_seq)
    normal = test_predictor(m.run(test_seq), test_seq, p)
    before, after = intervention_prediction(m, test_seq, p, 250)
    periodic_intervention[f'M{S}'] = (normal, before, after, before-after)

# Ω-MEM-2d: context memory
class ContextMemoryMachine:
    def __init__(self):
        self.next_state = {(0,'X'):1, (0,'Y'):0, (1,'X'):1, (1,'Y'):0}
    def step(self, state, inp): return self.next_state[(state, inp)]
    def run(self, sequence):
        state, states = 0, [0]
        for inp in sequence:
            state = self.step(state, inp); states.append(state)
        return states

context_results, context_baselines = [], []
for seed in range(50):
    seq = generate_markov2(seed)
    train_seq, test_seq = seq[:500], seq[500:]
    m = ContextMemoryMachine()
    p = train_predictor(m.run(train_seq), train_seq)
    context_results.append(test_predictor(m.run(test_seq), test_seq, p))
    m0 = PredictionMachine(1, 'no_memory')
    p0 = train_predictor(m0.run(train_seq), train_seq)
    context_baselines.append(test_predictor(m0.run(test_seq), test_seq, p0))

# Print compact reproducibility summary
print('same-seed means:', {k: round(float(np.mean(v)),4) for k,v in results.items()})
print('cross-seed means:', {k: round(float(np.mean(v)),4) for k,v in cross_results.items()})
print('periodic means:', {k: round(float(np.mean(v)),4) for k,v in periodic_results.items()})
print('periodic intervention:', periodic_intervention)
print('context:', float(np.mean(context_results)), float(np.mean(context_baselines)),
      float(np.mean(context_results)-np.mean(context_baselines)))
