"""Ω-INF-8 — deliberate attempt to break Ω-INF-7.

Purpose: test whether the Ω-INF-7 observation survives changes in observable,
reconstruction policy, and control construction.

This protocol does NOT assume a preferred direction. It records the sign of
changes under several independent observables and includes a null control.
Completed Ω-INF-7 is not modified.
"""
import math
import random
import statistics
import zlib
from collections import Counter, defaultdict

SEEDS = [8101, 8102, 8103, 8104, 8105, 8106, 8107, 8108]
N_PER_TEXT = 80

CORPUS = {
    "technical_ru": "Система распределяет нагрузку по отдельным линиям. Каждый участок имеет свой автомат и проверяется независимо. Кабель прокладывается параллельно, соединения выполняются в доступных коробках, а параметры защиты выбираются по току нагрузки и условиям отключения. Перед вводом в эксплуатацию проверяются непрерывность защитного проводника, сопротивление изоляции и работа устройств защиты.",
    "literary_ru": "Вечером город медленно затихал. Свет в окнах становился редким, дорога уходила за поворот и исчезала в темноте. Человек остановился у старого дома, прислушался и заметил, как ветер перебирает сухие ветви. Ничего особенного не происходило, но именно в этой тишине каждая маленькая перемена становилась заметной.",
    "structured_en": "Alpha connects to beta. Beta connects to gamma. Gamma connects to delta. Delta returns to alpha. A second loop begins at beta and reaches epsilon before returning to gamma. The two loops share a small number of transitions, so the same local pieces can participate in different larger paths. This sequence is deliberately regular enough to test whether local statistics determine the whole arrangement.",
    "randomish_en": "q7mZp2LxA9vK4rTn8cW3fHs6Jd1Qe5Uy0BgaP7sNx2VtR9kLm4Cw8Yj3Fh6Dq1Za5Xn0Gp7Ts2Vk9Rb4Mc8Wy3Lq6Hf1Jd5Pe0Xu7Ka2Zn9Bt4Rw8Vm3Cs6Yh1Qf5Ld0Ng7Xp2Tr9Vk4Ba8Wm3Jc6Hs1Qy5Df0Zp7Ln2Kx9Vt4Rg8Cb3Wm6Yh1Fs5Qd0Ja7Pn2Lx9Kc4Vr8Tb3Mg6Wy1Hs5Fq0Zd7Jn2Xp9La4Vk8Rc3Tm6Bw1Yh5Qf0Gd7Ks2Pn9Xc4Lj8Vr3Tb6Ma1Wy5Hq0Zf7D"}


def trigram_counts(text):
    return Counter(zip(text, text[1:], text[2:]))


def reconstruct(text, seed, policy="shuffle"):
    rng = random.Random(seed)
    adj = defaultdict(list)
    for a, b, c in zip(text, text[1:], text[2:]):
        adj[(a, b)].append(c)
    for values in adj.values():
        if policy == "shuffle":
            rng.shuffle(values)
        elif policy == "reverse":
            values.reverse()
        elif policy == "sorted":
            values.sort()
        elif policy == "random_pop":
            rng.shuffle(values)
        else:
            raise ValueError(policy)
    stack = [(text[0], text[1])]
    path = []
    while stack:
        v = stack[-1]
        if adj[v]:
            if policy == "random_pop":
                idx = rng.randrange(len(adj[v]))
                nxt = adj[v].pop(idx)
            else:
                nxt = adj[v].pop()
            stack.append((v[1], nxt))
        else:
            path.append(stack.pop())
    vertices = list(reversed(path))
    out = vertices[0][0] + vertices[0][1] + "".join(v[1] for v in vertices[1:])
    assert len(out) == len(text)
    assert Counter(out) == Counter(text)
    assert trigram_counts(out) == trigram_counts(text)
    return out


def entropy(text):
    c = Counter(text)
    n = len(text)
    return -sum((v/n) * math.log2(v/n) for v in c.values())


def bigram_entropy(text):
    pairs = list(zip(text, text[1:]))
    c = Counter(pairs)
    n = len(pairs)
    return -sum((v/n) * math.log2(v/n) for v in c.values())


def observable(text):
    return {
        "zlib": len(zlib.compress(text.encode("utf-8"), 9)),
        "char_entropy": entropy(text),
        "bigram_entropy": bigram_entropy(text),
        "unique_bigrams": len(set(zip(text, text[1:]))),
    }


def run():
    result = {}
    policies = ["shuffle", "random_pop", "reverse", "sorted"]
    for name, text in CORPUS.items():
        base = observable(text)
        rows = {p: [] for p in policies}
        for i in range(N_PER_TEXT):
            seed = SEEDS[i % len(SEEDS)] * 100000 + i
            for p in policies:
                out = reconstruct(text, seed, p)
                obs = observable(out)
                rows[p].append({k: obs[k] - base[k] for k in base})
        result[name] = {
            p: {
                metric: {
                    "mean": statistics.mean(r[metric] for r in vals),
                    "median": statistics.median(r[metric] for r in vals),
                    "positive_fraction": sum(r[metric] > 0 for r in vals) / len(vals),
                    "negative_fraction": sum(r[metric] < 0 for r in vals) / len(vals),
                }
                for metric in base
            }
            for p, vals in rows.items()
        }

    # Null control: random permutations preserve the character multiset but
    # intentionally destroy trigram constraints. This is not a substitute for
    # a matched null; it only checks that the observables can respond at all.
    nulls = {}
    for name, text in CORPUS.items():
        rng = random.Random(99001)
        base = observable(text)
        deltas = []
        chars = list(text)
        for _ in range(N_PER_TEXT):
            rng.shuffle(chars)
            obs = observable("".join(chars))
            deltas.append({k: obs[k] - base[k] for k in base})
        nulls[name] = {k: statistics.mean(r[k] for r in deltas) for k in base}

    return {
        "experiment": "Ω-INF-8",
        "date": "2026-08-13",
        "question": "Can the Ω-INF-7 observation be broken by changing observable and reconstruction policy while preserving exact trigram counts?",
        "n_per_text_per_policy": N_PER_TEXT,
        "policies": policies,
        "corpus": list(CORPUS),
        "results": result,
        "null_control": nulls,
        "interpretation_limit": "A surviving sign pattern is not a universal law. A broken pattern is evidence against the stronger hypothesis."
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), ensure_ascii=False, indent=2))
