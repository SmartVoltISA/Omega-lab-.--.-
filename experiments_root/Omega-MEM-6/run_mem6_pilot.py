"""Ω-MEM-6 pilot: predictive distinguishability -> next-transition uncertainty.

This is intentionally small and auditable. It compares conditional next-symbol
entropy with relevant versus random/irrelevant memory at matched nominal capacity.
"""
from collections import Counter, defaultdict
from math import log2
import random

N = 20_000
SEED = 7


def entropy(xs):
    c = Counter(xs)
    n = len(xs)
    return -sum((v/n) * log2(v/n) for v in c.values()) if n else 0.0


def conditional_entropy(xs, ys):
    groups = defaultdict(list)
    for x, y in zip(xs, ys):
        groups[x].append(y)
    n = len(ys)
    return sum(len(g)/n * entropy(g) for g in groups.values())


def periodic_4():
    seq = ([0, 1, 0, 2] * (N // 4 + 1))[:N]
    cur, nxt = seq[:-1], seq[1:]
    phase = list(range(4)) * (N // 4 + 1)
    phase = phase[:N-1]
    rng = random.Random(SEED)
    random_memory = [rng.randrange(4) for _ in nxt]
    return (
        conditional_entropy(cur, nxt),
        conditional_entropy(list(zip(cur, phase)), nxt),
        conditional_entropy(list(zip(cur, random_memory)), nxt),
    )


def markov_2():
    seq = [0, 1]
    for _ in range(N - 2):
        seq.append(seq[-1] ^ seq[-2])
    cur = seq[1:-1]
    nxt = seq[2:]
    relevant = list(zip(seq[:-2], cur))
    rng = random.Random(SEED)
    random_memory = [rng.randrange(4) for _ in nxt]
    return (
        conditional_entropy(cur, nxt),
        conditional_entropy(relevant, nxt),
        conditional_entropy(list(zip(cur, random_memory)), nxt),
    )


def thue_morse():
    seq = [bin(i).count("1") % 2 for i in range(N)]
    cur = seq[1:-1]
    nxt = seq[2:]
    relevant = list(zip(seq[:-2], cur))
    rng = random.Random(SEED)
    random_memory = [rng.randrange(4) for _ in nxt]
    return (
        conditional_entropy(cur, nxt),
        conditional_entropy(relevant, nxt),
        conditional_entropy(list(zip(cur, random_memory)), nxt),
    )


def iid():
    rng = random.Random(SEED)
    seq = [rng.randrange(2) for _ in range(N)]
    cur, nxt = seq[:-1], seq[1:]
    random_memory = [rng.randrange(4) for _ in nxt]
    return (
        conditional_entropy(cur, nxt),
        conditional_entropy(list(zip(cur, random_memory)), nxt),
    )


def main():
    results = {
        "Periodic-4": periodic_4(),
        "Markov-2": markov_2(),
        "Thue-Morse": thue_morse(),
        "IID": iid(),
    }
    for name, values in results.items():
        print(name, values)


if __name__ == "__main__":
    main()
