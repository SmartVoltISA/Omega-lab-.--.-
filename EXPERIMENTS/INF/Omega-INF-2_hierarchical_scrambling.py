"""Ω-INF-2 — hierarchical scrambling intervention.

Purpose:
Measure which statistical properties survive when organization is
progressively destroyed at different levels of a text.

Conditions:
T0 original text
T1 characters shuffled globally
T2 word order shuffled within each paragraph
T3 sentence order shuffled within each paragraph
T4 paragraph order shuffled globally

Important: these interventions are intentionally different transformations;
there is no claim that they destroy the same amount of information.
They are a controlled map of which metrics respond to which organizational level.
"""

import json
import math
import random
import statistics
import zlib
from collections import Counter
from pathlib import Path

SEED = 20260813
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


def unique_bigrams(seq):
    return len(set(zip(seq, seq[1:])))


def metrics(text):
    seq = list(text)
    return {
        "n_chars": len(seq),
        "symbol_entropy_bits": entropy(seq),
        "conditional_entropy_bits": conditional_entropy(seq),
        "unique_bigrams": unique_bigrams(seq),
        "zlib_bytes": len(zlib.compress(text.encode("utf-8"), 9)),
    }


def sentences(paragraph):
    parts = []
    current = ""
    for ch in paragraph:
        current += ch
        if ch in ".!?" and current.strip():
            parts.append(current.strip())
            current = ""
    if current.strip():
        parts.append(current.strip())
    return parts


def condition_t1(text, rng):
    chars = list(text)
    rng.shuffle(chars)
    return "".join(chars)


def condition_t2(text, rng):
    paragraphs = text.split("\n")
    out = []
    for p in paragraphs:
        words = p.split()
        rng.shuffle(words)
        out.append(" ".join(words))
    return "\n".join(out)


def condition_t3(text, rng):
    paragraphs = text.split("\n")
    out = []
    for p in paragraphs:
        s = sentences(p)
        rng.shuffle(s)
        out.append(" ".join(s))
    return "\n".join(out)


def condition_t4(text, rng):
    paragraphs = text.split("\n")
    rng.shuffle(paragraphs)
    return "\n".join(paragraphs)


def run():
    base_rng = random.Random(SEED)
    transforms = {
        "T0_original": lambda: TEXT,
        "T1_character_shuffle": lambda: condition_t1(TEXT, random.Random(base_rng.randrange(2**32))),
        "T2_word_shuffle_within_paragraph": lambda: condition_t2(TEXT, random.Random(base_rng.randrange(2**32))),
        "T3_sentence_shuffle_within_paragraph": lambda: condition_t3(TEXT, random.Random(base_rng.randrange(2**32))),
        "T4_paragraph_shuffle": lambda: condition_t4(TEXT, random.Random(base_rng.randrange(2**32))),
    }
    results = {name: metrics(fn()) for name, fn in transforms.items()}
    return {
        "experiment": "Ω-INF-2",
        "seed": SEED,
        "text_length_chars": len(TEXT),
        "conditions": list(results),
        "results": results,
        "scope": "descriptive intervention experiment; not a direct measure of semantic information",
    }


if __name__ == "__main__":
    out = Path(__file__).with_name("RESULTS.json")
    out.write_text(json.dumps(run(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(run(), ensure_ascii=False, indent=2))
