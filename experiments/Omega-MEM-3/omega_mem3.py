import numpy as np
from collections import defaultdict, Counter
import json

# ============================================================
# Ω-MEM-3: GENERALIZATION OF H-MEM-2.1
# Archived execution code from 2026-08-10.
# NOTE: This is the exact tested architecture family used for the
# reported Ω-MEM-3 results. Known methodological limitations are
# documented in README.md and AUDIT_2026-08-10.md.
# ============================================================

PROTOCOL = {
    "name": "Ω-MEM-3",
    "date": "2026-08-10",
    "hypothesis_tested": "H-MEM-2.1",
    "sequence_length": 2000,
    "burn_in": 100,
    "train_steps": 1000,
    "test_steps": 1000,
    "num_seeds": 30,
    "permutation_trials": 100,
}


def generate_periodic(seed, pattern=('X','X','Y','Y'), length=2000, burn_in=100):
    np.random.seed(seed)
    offset = np.random.randint(0, len(pattern))
    seq = [pattern[(i + offset) % len(pattern)] for i in range(length + burn_in)]
    return seq[burn_in:]


def generate_markov_like(seed, p_repeat=0.8, length=2000, burn_in=100):
    # Historical generator used in Ω-MEM-3. Despite the old label
    # "Markov-2", this depends only on the immediately previous symbol.
    np.random.seed(seed)
    seq = [np.random.choice(['X','Y']), np.random.choice(['X','Y'])]
    for _ in range(length + burn_in - 2):
        if np.random.random() < p_repeat:
            seq.append(seq[-1])
        else:
            seq.append('Y' if seq[-1] == 'X' else 'X')
    return seq[burn_in:]


def generate_thue_morse(seed, length=2000, burn_in=100):
    np.random.seed(seed)
    offset = np.random.randint(0, 1000)
    seq = []
    for n in range(offset, offset + length + burn_in):
        bits = bin(n).count('1')
        seq.append('X' if bits % 2 == 0 else 'Y')
    return seq[burn_in:]


def generate_hmm(seed, length=2000, burn_in=100):
    # Historical HMM generator used in Ω-MEM-3.
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


class MemoryMachine:
    def __init__(self, arch_type, S=None, process=None, seed=None):
        self.arch_type = arch_type
        self.S = S
        self.process = process
        self.seed = seed
        self.next_state = {}
        self._build()

    def _build(self):
        if self.arch_type == 'E':
            self.S = 1
            self.next_state = {(0,'X'): 0, (0,'Y'): 0}

        elif self.arch_type == 'D':
            self.S = 2
            self.next_state = {
                (0,'X'): 1, (0,'Y'): 0,
                (1,'X'): 1, (1,'Y'): 0
            }

        elif self.arch_type == 'B':
            S = self.S or 4
            self.S = S
            for s in range(S):
                self.next_state[(s,'X')] = (s + 1) % S
                self.next_state[(s,'Y')] = s

        elif self.arch_type == 'C':
            np.random.seed(self.seed)
            S = self.S or 4
            self.S = S
            for s in range(S):
                for inp in ['X','Y']:
                    self.next_state[(s,inp)] = np.random.randint(0, S)

        elif self.arch_type == 'A':
            if self.process == 'P1':
                self.S = 4
                for s in range(4):
                    self.next_state[(s,'X')] = (s + 1) % 4
                    self.next_state[(s,'Y')] = (s + 1) % 4

            elif self.process == 'P2':
                self.S = 4
                self.next_state = {
                    (0,'X'): 2, (0,'Y'): 0,
                    (1,'X'): 2, (1,'Y'): 0,
                    (2,'X'): 3, (2,'Y'): 1,
                    (3,'X'): 3, (3,'Y'): 1
                }

            elif self.process == 'P3':
                self.S = 2
                self.next_state = {
                    (0,'X'): 1, (0,'Y'): 0,
                    (1,'X'): 0, (1,'Y'): 1
                }

            elif self.process == 'P4':
                self.S = 2
                self.next_state = {
                    (0,'X'): 0, (0,'Y'): 1,
                    (1,'X'): 0, (1,'Y'): 1
                }

            elif self.process == 'P5':
                self.S = 4
                for s in range(4):
                    self.next_state[(s,'X')] = (s + 1) % 4
                    self.next_state[(s,'Y')] = s

    def step(self, state, inp):
        return self.next_state[(state, inp)]

    def run(self, sequence):
        state = 0
        states = [state]
        for inp in sequence:
            state = self.step(state, inp)
            states.append(state)
        return states


def train_predictor(states, sequence):
    state_next_counts = defaultdict(Counter)
    for i in range(len(sequence) - 1):
        s = states[i]
        state_next_counts[s][sequence[i + 1]] += 1

    pred_map = {}
    for s, counts in state_next_counts.items():
        pred_map[s] = counts.most_common(1)[0][0]
    return pred_map


def test_predictor(states, sequence, pred_map):
    correct = 0
    total = 0
    for i in range(len(sequence) - 1):
        s = states[i]
        if s in pred_map:
            correct += int(pred_map[s] == sequence[i + 1])
            total += 1
    return correct / total if total else 0.5


def permutation_test(machine, test_seq, pred_map, num_trials=100):
    states_test = machine.run(test_seq)
    baseline_acc = test_predictor(states_test, test_seq, pred_map)
    perm_accs = []
    for _ in range(num_trials):
        states_list = list(pred_map.keys())
        preds = list(pred_map.values())
        np.random.shuffle(preds)
        perm_map = dict(zip(states_list, preds))
        perm_accs.append(test_predictor(states_test, test_seq, perm_map))
    return baseline_acc, float(np.mean(perm_accs)), float(np.std(perm_accs))


def run_experiment():
    processes = {
        'P1': generate_periodic,
        'P2': generate_markov_like,
        'P3': generate_thue_morse,
        'P4': generate_hmm,
        'P5': generate_random_iid,
    }
    architectures = ['A', 'B', 'C', 'D', 'E']
    results = defaultdict(dict)

    for proc_id, proc_gen in processes.items():
        for arch in architectures:
            accs = []
            perm_results = []
            for seed in range(PROTOCOL['num_seeds']):
                if proc_id == 'P2':
                    seq = proc_gen(seed, p_repeat=0.8,
                                   length=PROTOCOL['sequence_length'],
                                   burn_in=PROTOCOL['burn_in'])
                else:
                    seq = proc_gen(seed,
                                   length=PROTOCOL['sequence_length'],
                                   burn_in=PROTOCOL['burn_in'])

                train_seq = seq[:PROTOCOL['train_steps']]
                test_seq = seq[PROTOCOL['train_steps']:]

                if arch == 'C':
                    machine = MemoryMachine(arch, S=4, process=proc_id, seed=seed+1000)
                elif arch == 'B':
                    machine = MemoryMachine(arch, S=4, process=proc_id)
                else:
                    machine = MemoryMachine(arch, process=proc_id)

                states_train = machine.run(train_seq)
                pred_map = train_predictor(states_train, train_seq)
                states_test = machine.run(test_seq)
                accs.append(test_predictor(states_test, test_seq, pred_map))

                if arch != 'E':
                    perm_results.append(
                        permutation_test(machine, test_seq, pred_map,
                                         PROTOCOL['permutation_trials'])
                    )

            results[proc_id][arch] = {
                'mean': float(np.mean(accs)),
                'std': float(np.std(accs)),
                'accs': accs,
                'perm': perm_results,
            }

    return results


if __name__ == '__main__':
    results = run_experiment()
    print(json.dumps(results, ensure_ascii=False, indent=2))
