# Ω-MEM-4 — ORIGINAL SUBMITTED IMPLEMENTATION
# Archived verbatim from the 2026-08-10 experiment messages.
# IMPORTANT: this file is an archival record, not a validated implementation.
# Known protocol/code mismatches are documented in AUDIT_MEM4_2026-08-10.md.

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from collections import defaultdict, Counter
import json
import math

PROTOCOL = {
    "name": "Ω-MEM-4",
    "question": "Является ли failure P3 следствием недостаточной выразительности, неправильного структурного соответствия или обоих?",
    "hypothesis_tested": "H-MEM-2.2",
    "processes": {
        "P1": {"name": "Periodic-4", "type": "positive_control", "pattern": "XXYY"},
        "P2": {"name": "Markov-2-true", "type": "stochastic", "order": 2},
        "P3": {"name": "Thue-Morse", "type": "deterministic_nonperiodic"},
        "P4": {"name": "HMM-true", "type": "hidden_state", "hidden": 2},
        "P5": {"name": "Random-iid", "type": "negative_control"}
    },
    "architectures": ["Baseline", "Context-1", "Context-2", "Context-3", "Counter", "Random", "Matched"],
    "S_values": [1, 2, 4, 8, 16, 32, 64],
    "parameters": {
        "sequence_length": 2000,
        "burn_in": 100,
        "train_steps": 1000,
        "test_steps": 1000,
        "num_seeds": 30,
        "intervention_step": 500,
        "permutation_trials": 100
    }
}


def generate_periodic(seed, length=2000, burn_in=100):
    np.random.seed(seed)
    pattern = ['X', 'X', 'Y', 'Y']
    offset = np.random.randint(0, 4)
    seq = [pattern[(i + offset) % 4] for i in range(length + burn_in)]
    return seq[burn_in:]


def generate_markov2_true(seed, length=2000, burn_in=100):
    np.random.seed(seed)
    trans = {0: 0.1, 1: 0.5, 2: 0.5, 3: 0.9}
    seq = [np.random.choice(['X','Y']), np.random.choice(['X','Y'])]
    code = {'X': 1, 'Y': 0}
    for _ in range(length + burn_in - 2):
        ctx = code[seq[-2]] * 2 + code[seq[-1]]
        p_x = trans[ctx]
        seq.append('X' if np.random.random() < p_x else 'Y')
    return seq[burn_in:]


def generate_thue_morse(seed, length=2000, burn_in=100):
    np.random.seed(seed)
    offset = np.random.randint(0, 10000)
    seq = []
    for n in range(offset, offset + length + burn_in):
        bits = bin(n).count('1')
        seq.append('X' if bits % 2 == 0 else 'Y')
    return seq[burn_in:]


def generate_hmm(seed, length=2000, burn_in=100):
    np.random.seed(seed)
    hidden = 0
    seq = []
    for _ in range(length + burn_in):
        if np.random.random() < 0.1:
            hidden = 1 - hidden
        if hidden == 0:
            seq.append('X' if np.random.random() < 0.9 else 'Y')
        else:
            seq.append('Y' if np.random.random() < 0.9 else 'X')
    return seq[burn_in:]


def generate_random_iid(seed, length=2000, burn_in=100):
    np.random.seed(seed)
    return list(np.random.choice(['X','Y'], size=length + burn_in)[burn_in:])


class Machine:
    def __init__(self, arch_type, process, S, seed=None):
        self.arch_type = arch_type
        self.process = process
        self.S = S
        self.seed = seed
        self.next_state = {}
        self._build()

    def _build(self):
        code = {'X': 1, 'Y': 0}
        if self.arch_type == 'Baseline':
            self.S = 1
            self.next_state = {(0,'X'): 0, (0,'Y'): 0}
        elif self.arch_type == 'Context-1':
            self.S = 2
            for s in range(2):
                for inp in ['X','Y']:
                    self.next_state[(s,inp)] = code[inp]
        elif self.arch_type == 'Context-2':
            self.S = 4
            for s in range(4):
                for inp in ['X','Y']:
                    self.next_state[(s,inp)] = ((s % 2) * 2 + code[inp]) % 4
        elif self.arch_type == 'Context-3':
            self.S = 8
            for s in range(8):
                for inp in ['X','Y']:
                    self.next_state[(s,inp)] = ((s % 4) * 2 + code[inp]) % 8
        elif self.arch_type == 'Counter':
            for s in range(self.S):
                for inp in ['X','Y']:
                    self.next_state[(s,inp)] = (s + 1) % self.S
        elif self.arch_type == 'Random':
            np.random.seed(self.seed if self.seed else 42)
            for s in range(self.S):
                for inp in ['X','Y']:
                    self.next_state[(s,inp)] = np.random.randint(0, self.S)
        elif self.arch_type == 'Matched':
            if self.process == 'P1':
                self.S = max(4, self.S)
                for s in range(self.S):
                    for inp in ['X','Y']:
                        self.next_state[(s,inp)] = (s + 1) % self.S
            elif self.process == 'P2':
                self.S = 4
                for s in range(4):
                    for inp in ['X','Y']:
                        self.next_state[(s,inp)] = ((s % 2) * 2 + code[inp]) % 4
            elif self.process == 'P3':
                self.S = 2
                for s in range(2):
                    for inp in ['X','Y']:
                        self.next_state[(s,inp)] = (s + code[inp]) % 2
            elif self.process == 'P4':
                self.S = max(2, self.S)
                for i in range(self.S):
                    b = (i + 0.5) / self.S
                    for inp in ['X','Y']:
                        pred0 = 0.9 * b + 0.1 * (1 - b)
                        pred1 = 0.1 * b + 0.9 * (1 - b)
                        if inp == 'X':
                            lik0, lik1 = 0.9, 0.1
                        else:
                            lik0, lik1 = 0.1, 0.9
                        post0 = lik0 * pred0
                        post1 = lik1 * pred1
                        b_new = post0 / (post0 + post1 + 1e-10)
                        j = min(int(b_new * self.S), self.S - 1)
                        self.next_state[(i,inp)] = j
            elif self.process == 'P5':
                self.S = 1
                self.next_state = {(0,'X'): 0, (0,'Y'): 0}

    def step(self, state, inp):
        return self.next_state.get((state,inp), 0)

    def run(self, sequence):
        state = 0
        states = [state]
        for inp in sequence:
            state = self.step(state, inp)
            states.append(state)
        return states


def train_predictor(states, sequence):
    counts = defaultdict(Counter)
    for i in range(len(sequence) - 1):
        counts[states[i]][sequence[i+1]] += 1
    return {s: c.most_common(1)[0][0] for s, c in counts.items()}


def test_predictor(states, sequence, pred_map):
    correct = total = 0
    for i in range(len(sequence) - 1):
        s = states[i]
        if s in pred_map:
            correct += (pred_map[s] == sequence[i+1])
            total += 1
    return correct / total if total else 0.5


def conditional_entropy(states, sequence):
    counts = defaultdict(Counter)
    state_counts = Counter()
    for i in range(len(sequence) - 1):
        s = states[i]
        counts[s][sequence[i+1]] += 1
        state_counts[s] += 1
    H = 0.0
    for s, total in state_counts.items():
        p_s = total / (len(sequence) - 1)
        for sym, cnt in counts[s].items():
            p = cnt / total
            H -= p_s * p * math.log2(p + 1e-10)
    return H


def permutation_test(machine, train_seq, test_seq, pred_map, n_trials=50):
    states_test = machine.run(test_seq)
    base_acc = test_predictor(states_test, test_seq, pred_map)
    perm_accs = []
    states_list = list(pred_map.keys())
    preds = list(pred_map.values())
    for _ in range(n_trials):
        np.random.shuffle(preds)
        perm_map = dict(zip(states_list, preds))
        perm_accs.append(test_predictor(states_test, test_seq, perm_map))
    return base_acc, np.mean(perm_accs), np.std(perm_accs)


def intervention_strict(machine, sequence, pred_map, reset_step, reset_state):
    s_ctrl = 0
    for inp in sequence[:reset_step]:
        s_ctrl = machine.step(s_ctrl, inp)
    s_int = reset_state
    correct_ctrl = correct_int = total = 0
    for i in range(reset_step, len(sequence) - 1):
        inp = sequence[i]
        s_ctrl = machine.step(s_ctrl, inp)
        s_int = machine.step(s_int, inp)
        true_next = sequence[i+1]
        if s_ctrl in pred_map:
            correct_ctrl += (pred_map[s_ctrl] == true_next)
        if s_int in pred_map:
            correct_int += (pred_map[s_int] == true_next)
        total += 1
    return correct_ctrl / total if total else 0.5, correct_int / total if total else 0.5

# Main execution and visualization were supplied in the conversation immediately
# following this code. They are preserved conceptually in the audit and report;
# the repository record deliberately identifies this file as the submitted source.
