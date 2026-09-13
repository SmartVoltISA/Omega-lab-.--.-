"""Ω-INF-1 — character-order intervention.

Deterministic experiment:
- preserve exactly the same characters and multiplicities;
- shuffle only their order;
- measure organization-sensitive metrics.

Seed: 20260813
Shuffles: 100
"""

import json
import math
import random
import statistics
import zlib
from collections import Counter
from pathlib import Path

TEXT = """Ω-Lab исследует системы через отношения. Элементы могут сохранять тот же набор свойств, но изменение связей меняет возникающую структуру.
Если порядок разрушить, сами элементы останутся на месте носителя, однако информация об их организации изменится. Мы поэтому различаем состав элементов и конфигурацию связей.
В эксперименте важно не объявлять такую потерю доказанной заранее. Нужно сохранить исходный набор, изменить только порядок и затем измерить, какие свойства последовательности действительно изменились.
Если две системы имеют одинаковые элементы, это ещё не означает, что они имеют одинаковую структуру. Различие может находиться не в элементах, а в отношениях между ними.
Ω-Lab проверяет эту возможность шаг за шагом: наблюдение отделяется от интерпретации, гипотеза от результата, а отрицательный результат сохраняется вместе с положительным."""
SEED = 20260813
N_SHUFFLES = 100


def entropy(seq):
    counts = Counter(seq)
    n = len(seq)
    return -sum((v / n) * math.log2(v / n) for v in counts.values())


def conditional_entropy(seq):
    pairs = Counter(zip(seq, seq[1:]))
    first = Counter(seq[:-1])
    n = len(seq) - 1
    return -sum((cnt / n) * math.log2(cnt / first[a]) for (a, _), cnt in pairs.items())


def unique_bigrams(seq):
    return len(set(zip(seq, seq[1:])))


def lz_complexity(seq):
    """Simple deterministic phrase-dictionary complexity proxy."""
    s = "".join(seq)
    n = len(s)
    i = 0
    length = 1
    complexity = 1
    seen = set()
    while i + length <= n:
        phrase = s[i : i + length]
        if phrase in seen:
            length += 1
        else:
            seen.add(phrase)
            complexity += 1
            i += length
            length = 1
    return complexity


def metrics(seq):
    return {
        "n_chars": len(seq),
        "symbol_entropy_bits": entropy(seq),
        "conditional_entropy_bits": conditional_entropy(seq),
        "unique_bigrams": unique_bigrams(seq),
        "zlib_bytes": len(zlib.compress("".join(seq).encode("utf-8"), 9)),
        "lz_complexity": lz_complexity(seq),
    }


def run():
    original = metrics(TEXT)
    rng = random.Random(SEED)
    shuffled = []
    for _ in range(N_SHUFFLES):
        chars = list(TEXT)
        rng.shuffle(chars)
        shuffled.append(metrics(chars))

    summary = {}
    for key in original:
        if key == "n_chars":
            summary[key] = {"original": original[key], "shuffle_mean": statistics.mean(x[key] for x in shuffled)}
            continue
        values = [x[key] for x in shuffled]
        summary[key] = {
            "original": original[key],
            "shuffle_mean": statistics.mean(values),
            "shuffle_sd": statistics.stdev(values),
            "shuffle_min": min(values),
            "shuffle_max": max(values),
            "difference_mean_minus_original": statistics.mean(values) - original[key],
        }

    return {
        "experiment": "Ω-INF-1",
        "seed": SEED,
        "n_shuffles": N_SHUFFLES,
        "text_length_chars": len(TEXT),
        "intervention": "random permutation of characters; composition and length preserved",
        "original_metrics": original,
        "shuffle_summary": summary,
    }


if __name__ == "__main__":
    out = Path(__file__).with_name("RESULTS.json")
    out.write_text(json.dumps(run(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(run(), ensure_ascii=False, indent=2))
