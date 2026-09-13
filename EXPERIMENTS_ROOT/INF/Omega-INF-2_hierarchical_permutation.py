"""Ω-INF-2 — hierarchical permutation control.

Goal:
Measure which structural levels are visible to the current character-level metrics.

Controls preserve exactly the same Unicode character multiset and length.
Levels:
1. character permutation — destroys character order;
2. word permutation — preserves whitespace positions and word+punctuation chunks;
3. sentence permutation within each paragraph — preserves paragraphs;
4. paragraph permutation — preserves each paragraph internally.

All conditions use 100 deterministic permutations.
Seed: 20260814
"""

import json
import math
import random
import re
import statistics
import zlib
from collections import Counter
from pathlib import Path

TEXT = """Ω-Lab исследует системы через отношения. Элементы могут сохранять тот же набор свойств, но изменение связей меняет возникающую структуру.
Если порядок разрушить, сами элементы останутся на месте носителя, однако информация об их организации изменится. Мы поэтому различаем состав элементов и конфигурацию связей.
В эксперименте важно не объявлять такую потерю доказанной заранее. Нужно сохранить исходный набор, изменить только порядок и затем измерить, какие свойства последовательности действительно изменились.
Если две системы имеют одинаковые элементы, это ещё не означает, что они имеют одинаковую структуру. Различие может находиться не в элементах, а в отношениях между ними.
Ω-Lab проверяет эту возможность шаг за шагом: наблюдение отделяется от интерпретации, гипотеза от результата, а отрицательный результат сохраняется вместе с положительным."""

SEED = 20260814
N = 100


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


def shuffle_characters(text, rng):
    chars = list(text)
    rng.shuffle(chars)
    return "".join(chars)


def shuffle_words_preserve_whitespace(text, rng):
    parts = re.split(r"(\s+)", text)
    indices = [i for i, part in enumerate(parts) if part and not part.isspace()]
    words = [parts[i] for i in indices]
    rng.shuffle(words)
    for i, word in zip(indices, words):
        parts[i] = word
    return "".join(parts)


def shuffle_sentences_within_paragraphs(text, rng):
    paragraphs = []
    for paragraph in text.split("\n"):
        parts = re.split(r"(?<=[.!?])(\s+)", paragraph)
        indices = list(range(0, len(parts), 2))
        sentences = [parts[i] for i in indices]
        rng.shuffle(sentences)
        for i, sentence in zip(indices, sentences):
            parts[i] = sentence
        paragraphs.append("".join(parts))
    return "\n".join(paragraphs)


def shuffle_paragraphs(text, rng):
    paragraphs = text.split("\n")
    rng.shuffle(paragraphs)
    return "\n".join(paragraphs)


def summarize(samples, original):
    result = {}
    for key in original:
        values = [m[key] for m in samples]
        result[key] = {
            "original": original[key],
            "mean": statistics.mean(values),
            "sd": statistics.stdev(values),
            "min": min(values),
            "max": max(values),
            "mean_minus_original": statistics.mean(values) - original[key],
        }
    return result


def run():
    original = metrics(TEXT)
    rng = random.Random(SEED)
    generators = {
        "character_shuffle": shuffle_characters,
        "word_shuffle": shuffle_words_preserve_whitespace,
        "sentence_shuffle_within_paragraphs": shuffle_sentences_within_paragraphs,
        "paragraph_shuffle": shuffle_paragraphs,
    }
    conditions = {}
    for name, generator in generators.items():
        samples = []
        for _ in range(N):
            transformed = generator(TEXT, rng)
            assert len(transformed) == len(TEXT)
            assert Counter(transformed) == Counter(TEXT)
            samples.append(metrics(transformed))
        conditions[name] = summarize(samples, original)

    return {
        "experiment": "Ω-INF-2",
        "date": "2026-08-13",
        "seed": SEED,
        "n_permutations_per_condition": N,
        "text_length_chars": len(TEXT),
        "original_metrics": original,
        "conditions": conditions,
        "scope_note": "Metrics are character-sequential; weak effects at higher permutation levels do not establish preservation of semantic or discourse structure.",
    }


if __name__ == "__main__":
    output = Path(__file__).with_name("RESULTS-INF-2.json")
    output.write_text(json.dumps(run(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(run(), ensure_ascii=False, indent=2))
