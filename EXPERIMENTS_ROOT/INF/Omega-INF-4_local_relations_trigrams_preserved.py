"""Ω-INF-4 — preserve exact trigram multiset, randomize longer-range order.

The text is represented as a directed multigraph whose vertices are
character bigrams and whose edges are character trigrams. A randomized
Eulerian traversal uses every original trigram exactly once.

Preserved by construction:
- sequence length;
- character multiset;
- exact bigram multiset;
- exact trigram multiset;
- first-order conditional entropy;
- second-order conditional entropy.

The intervention asks whether measurable structure remains after all
character 3-gram statistics are held fixed.
"""

import json
import math
import random
import statistics
import zlib
from collections import Counter, defaultdict
from pathlib import Path

SEED = 20260815
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


def conditional_entropy(seq, order):
    contexts = Counter(tuple(seq[i - order:i]) for i in range(order, len(seq)))
    joint = Counter((tuple(seq[i - order:i]), seq[i]) for i in range(order, len(seq)))
    n = len(seq) - order
    return -sum((count / n) * math.log2(count / contexts[context])
                for (context, _), count in joint.items())


def metrics(text):
    seq = list(text)
    return {
        "n_chars": len(seq),
        "symbol_entropy_bits": entropy(seq),
        "conditional_entropy_order1_bits": conditional_entropy(seq, 1),
        "conditional_entropy_order2_bits": conditional_entropy(seq, 2),
        "unique_bigrams": len(set(zip(seq, seq[1:]))),
        "unique_trigrams": len(set(zip(seq, seq[1:], seq[2:]))),
        "zlib_bytes": len(zlib.compress(text.encode("utf-8"), 9)),
    }


def reconstruct_preserving_trigrams(text, seed):
    rng = random.Random(seed)
    adjacency = defaultdict(list)
    for a, b, c in zip(text, text[1:], text[2:]):
        adjacency[(a, b)].append(c)
    for values in adjacency.values():
        rng.shuffle(values)

    start = (text[0], text[1])
    stack = [start]
    path = []
    while stack:
        vertex = stack[-1]
        if adjacency[vertex]:
            next_char = adjacency[vertex].pop()
            stack.append((vertex[1], next_char))
        else:
            path.append(stack.pop())

    vertices = list(reversed(path))
    result = vertices[0][0] + "".join(vertex[1] for vertex in vertices)

    if len(result) != len(text):
        raise RuntimeError("Trigram reconstruction changed sequence length")
    if Counter(result) != Counter(text):
        raise RuntimeError("Trigram reconstruction changed character composition")
    if Counter(zip(result, result[1:])) != Counter(zip(text, text[1:])):
        raise RuntimeError("Trigram reconstruction changed bigram multiset")
    if Counter(zip(result, result[1:], result[2:])) != Counter(zip(text, text[1:], text[2:])):
        raise RuntimeError("Trigram reconstruction did not preserve trigram multiset")
    return result


def run():
    original = metrics(TEXT)
    runs = [metrics(reconstruct_preserving_trigrams(TEXT, SEED + i)) for i in range(N_RUNS)]
    summary = {}
    for key, original_value in original.items():
        values = [item[key] for item in runs]
        summary[key] = {
            "original": original_value,
            "reconstructed_mean": statistics.mean(values),
            "reconstructed_sd": statistics.stdev(values),
            "reconstructed_min": min(values),
            "reconstructed_max": max(values),
            "difference_mean_minus_original": statistics.mean(values) - original_value,
        }

    return {
        "experiment": "Ω-INF-4",
        "seed_start": SEED,
        "n_runs": N_RUNS,
        "text_length_chars": len(TEXT),
        "intervention": "randomized Eulerian reconstruction preserving exact trigram multiset",
        "preserved": [
            "character multiset",
            "bigram multiset",
            "trigram multiset",
            "sequence length",
            "first-order conditional entropy",
            "second-order conditional entropy",
        ],
        "original_metrics": original,
        "reconstruction_summary": summary,
        "interpretation_limit": "Compression is an operational sequence proxy, not a direct semantic-information measure.",
    }


if __name__ == "__main__":
    output = Path(__file__).with_name("RESULTS_Omega-INF-4.json")
    output.write_text(json.dumps(run(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(run(), ensure_ascii=False, indent=2))
