"""Ω-INF-3 — preserve exact bigram multiset, randomize longer-range order.

The text is represented as a directed multigraph whose edges are its
character bigrams. A randomized Eulerian traversal reconstructs a sequence
using every original bigram exactly once.

Therefore the intervention preserves:
- length;
- character multiset;
- exact multiset of adjacent character pairs;
- first-order conditional entropy;

while allowing longer-range organization to change.
"""

import json
import math
import random
import statistics
import zlib
from collections import Counter, defaultdict
from pathlib import Path

SEED = 20260813
N_RUNS = 100
TEXT = """Ω-Lab исследует системы через отношения. Элементы могут сохранять тот же набор свойств, но изменение связей меняет возникающую структуру.
Если порядок разрушить, сами элементы останутся на месте носителя, однако информация об их организации изменится. Мы поэтому различаем состав элементов и конфигурацию связей.
В эксперименте важно не объявлять такую потерю доказанной заранее. Нужно сохранить исходный набор, изменить только порядок и затем измерить, какие свойства последовательности действительно изменились.
Если две системы имеют одинаковые элементы, это ещё не означает, что они имеют одинаковую структуру. Различие может находиться не в элементах, а в отношениях между ними.
Ω-Lab проверяет эту возможность шаг за шагом: наблюдение отделяется от интерпретации, гипотеза от результата, а отрицательный результат сохраняется вместе с положительным."""


def entropy(seq):
    counts = Counter(seq)
    n = len(seq)
    return -sum((v / n) * math.log2(v / n) for v in counts.values())


def conditional_entropy(seq):
    pairs = Counter(zip(seq, seq[1:]))
    first = Counter(seq[:-1])
    n = len(seq) - 1
    return -sum((cnt / n) * math.log2(cnt / first[a]) for (a, _), cnt in pairs.items())


def metrics(text):
    seq = list(text)
    return {
        "n_chars": len(seq),
        "symbol_entropy_bits": entropy(seq),
        "conditional_entropy_bits": conditional_entropy(seq),
        "unique_bigrams": len(set(zip(seq, seq[1:]))),
        "zlib_bytes": len(zlib.compress(text.encode("utf-8"), 9)),
    }


def reconstruct_preserving_bigrams(text, seed):
    rng = random.Random(seed)
    adjacency = defaultdict(list)
    for a, b in zip(text, text[1:]):
        adjacency[a].append(b)
    for values in adjacency.values():
        rng.shuffle(values)

    stack = [text[0]]
    path = []
    while stack:
        vertex = stack[-1]
        if adjacency[vertex]:
            stack.append(adjacency[vertex].pop())
        else:
            path.append(stack.pop())

    result = "".join(reversed(path))
    if len(result) != len(text):
        raise RuntimeError("Eulerian reconstruction changed sequence length")
    if Counter(result) != Counter(text):
        raise RuntimeError("Eulerian reconstruction changed character composition")
    if Counter(zip(result, result[1:])) != Counter(zip(text, text[1:])):
        raise RuntimeError("Eulerian reconstruction did not preserve bigram multiset")
    return result


def run():
    original = metrics(TEXT)
    runs = []
    for i in range(N_RUNS):
        sequence = reconstruct_preserving_bigrams(TEXT, SEED + i)
        runs.append(metrics(sequence))

    summary = {}
    for key in original:
        if key == "n_chars":
            summary[key] = {"original": original[key], "reconstructed_mean": statistics.mean(x[key] for x in runs)}
            continue
        values = [x[key] for x in runs]
        summary[key] = {
            "original": original[key],
            "reconstructed_mean": statistics.mean(values),
            "reconstructed_sd": statistics.stdev(values),
            "reconstructed_min": min(values),
            "reconstructed_max": max(values),
            "difference_mean_minus_original": statistics.mean(values) - original[key],
        }

    return {
        "experiment": "Ω-INF-3",
        "seed_start": SEED,
        "n_runs": N_RUNS,
        "text_length_chars": len(TEXT),
        "intervention": "randomized Eulerian reconstruction preserving exact bigram multiset",
        "preserved": ["character multiset", "bigram multiset", "sequence length", "first-order conditional entropy"],
        "original_metrics": original,
        "reconstruction_summary": summary,
    }


if __name__ == "__main__":
    out = Path(__file__).with_name("RESULTS.json")
    out.write_text(json.dumps(run(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(run(), ensure_ascii=False, indent=2))
