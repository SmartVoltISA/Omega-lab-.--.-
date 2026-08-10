import numpy as np

# ============================================================
# Ω-MEM-1a–1d: PARAMETER FIXATION BEFORE RUN
# ============================================================
PARAMS = {
    'history_length': 15,
    'intervention_step': 5,
    'num_seeds': 100,
    'seed_range': range(100),
    'sizes': [1, 2, 4, 8, 16],
    'input_alphabet': ['X', 'Y'],
    'output_alphabet': ['A', 'B'],
    'max_steps_after_intervention': 10,
}

class StructuredMemoryMachine:
    def __init__(self, S):
        self.S = S
        self.next_state = {}
        self.output = {}
        for s in range(S):
            self.next_state[(s, 'X')] = (s + 1) % S
            self.next_state[(s, 'Y')] = s
            self.output[(s, 'X')] = 'A' if s % 2 == 0 else 'B'
            self.output[(s, 'Y')] = 'A' if (s + 1) % 2 == 0 else 'B'

    def step(self, state, inp):
        return self.next_state[(state, inp)], self.output[(state, inp)]

class RandomMemoryMachine:
    def __init__(self, S, seed):
        np.random.seed(seed)
        self.S = S
        self.next_state = {}
        self.output = {}
        for s in range(S):
            for inp in ['X', 'Y']:
                self.next_state[(s, inp)] = np.random.randint(0, S)
                self.output[(s, inp)] = np.random.choice(['A', 'B'])

    def step(self, state, inp):
        return self.next_state[(state, inp)], self.output[(state, inp)]

def generate_history(length, seed):
    np.random.seed(seed)
    return list(np.random.choice(['X', 'Y'], size=length))

def strict_intervention(machine, history, reset_step):
    sA = 0
    outs_A, states_A = [], [0]
    for inp in history:
        sA, o = machine.step(sA, inp)
        states_A.append(sA); outs_A.append(o)

    sB = 0
    outs_B, states_B = [], [0]
    for i, inp in enumerate(history):
        if i == reset_step:
            sB = 0
        sB, o = machine.step(sB, inp)
        states_B.append(sB); outs_B.append(o)

    post_A = outs_A[reset_step:]
    post_B = outs_B[reset_step:]
    diff = sum(a != b for a, b in zip(post_A, post_B))

    first_diff_step = next((i for i, (a,b) in enumerate(zip(post_A,post_B)) if a != b), None)
    reconverge = False
    reconverge_step = None
    for i in range(len(post_A)):
        if all(post_A[j] == post_B[j] for j in range(i, len(post_A))):
            reconverge = True
            reconverge_step = i
            break

    return {
        'diff': diff,
        'total': len(post_A),
        'first_diff': first_diff_step,
        'reconverge': reconverge,
        'reconverge_step': reconverge_step,
        'states_A': states_A,
        'states_B': states_B,
        'outs_A': outs_A,
        'outs_B': outs_B,
        'state_at_reset_A': states_A[reset_step],
    }

# Ω-MEM-1a: repeatability
repeatability_results = {}
for S in PARAMS['sizes']:
    machine = StructuredMemoryMachine(S)
    diffs, successes, first_diffs, reconverges, reconverge_steps, state_at_reset = [], [], [], [], [], []
    for seed in PARAMS['seed_range']:
        history = generate_history(PARAMS['history_length'], seed)
        result = strict_intervention(machine, history, PARAMS['intervention_step'])
        diffs.append(result['diff'])
        successes.append(int(result['diff'] > 0))
        first_diffs.append(result['first_diff'] if result['first_diff'] is not None else -1)
        reconverges.append(int(result['reconverge']))
        reconverge_steps.append(result['reconverge_step'] if result['reconverge_step'] is not None else -1)
        state_at_reset.append(result['state_at_reset_A'])
    repeatability_results[S] = {
        'diffs': diffs,
        'successes': successes,
        'first_diffs': first_diffs,
        'reconverges': reconverges,
        'reconverge_steps': reconverge_steps,
        'state_at_reset': state_at_reset,
    }
    success_rate = np.mean(successes)
    ci_low = success_rate - 1.96*np.sqrt(success_rate*(1-success_rate)/PARAMS['num_seeds'])
    ci_high = success_rate + 1.96*np.sqrt(success_rate*(1-success_rate)/PARAMS['num_seeds'])
    print(f'M{S if S>1 else 0}: success={success_rate:.2%}, CI=[{max(0,ci_low):.3f},{min(1,ci_high):.3f}], mean Δ={np.mean(diffs):.2f}/10, std Δ={np.std(diffs):.2f}, state0={sum(s==0 for s in state_at_reset)}/100, first_diff0={sum(f==0 for f in first_diffs)}/100, reconverge={np.mean(reconverges):.2%}')
