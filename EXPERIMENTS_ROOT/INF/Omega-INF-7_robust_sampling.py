"""Ω-INF-7 — expanded robustness/sampling control.

Goal: increase independent corpora, seeds and reconstruction samples before
raising n-gram order. The experiment asks whether observed effects depend
strongly on one text, one seed, or one reconstruction sample.
"""
import json, random, statistics, zlib
from collections import Counter, defaultdict
from pathlib import Path

N_PER_CORPUS = 250
SEEDS = [7101, 7102, 7103, 7104]

CORPUS = {
    "technical_ru": "Система распределяет нагрузку по отдельным линиям. Каждый участок имеет свой автомат и проверяется независимо. Кабель прокладывается параллельно, соединения выполняются в доступных коробках, а параметры защиты выбираются по току нагрузки и условиям отключения. Перед вводом в эксплуатацию проверяются непрерывность защитного проводника, сопротивление изоляции и работа устройств защиты.",
    "literary_ru": "Вечером город медленно затихал. Свет в окнах становился редким, дорога уходила за поворот и исчезала в темноте. Человек остановился у старого дома, прислушался и заметил, как ветер перебирает сухие ветви. Ничего особенного не происходило, но именно в этой тишине каждая маленькая перемена становилась заметной.",
    "structured_en": "Alpha connects to beta. Beta connects to gamma. Gamma connects to delta. Delta returns to alpha. A second loop begins at beta and reaches epsilon before returning to gamma. The two loops share a small number of transitions, so the same local pieces can participate in different larger paths. This sequence is deliberately regular enough to test whether local statistics determine the whole arrangement.",
    "randomish_en": "q7mZp2LxA9vK4rTn8cW3fHs6Jd1Qe5Uy0BgaP7sNx2VtR9kLm4Cw8Yj3Fh6Dq1Za5Xn0Gp7Ts2Vk9Rb4Mc8Wy3Lq6Hf1Jd5Pe0Xu7Ka2Zn9Bt4Rw8Vm3Cs6Yh1Qf5Ld0Ng7Xp2Tr9Vk4Ba8Wm3Jc6Hs1Qy5Df0Zp7Ln2Kx9Vt4Rg8Cb3Wm6Yh1Fs5Qd0Ja7Pn2Lx9Kc4Vr8Tb3Mg6Wy1Hs5Fq0Zd7D"
}

def build_adjacency(text):
    adj = defaultdict(list)
    for a, b, c in zip(text, text[1:], text[2:]): adj[(a, b)].append(c)
    return adj

def reconstruct(text, seed):
    rng = random.Random(seed)
    adj = build_adjacency(text)
    for values in adj.values(): rng.shuffle(values)
    stack = [(text[0], text[1])]; path = []
    while stack:
        v = stack[-1]
        if adj[v]: stack.append((v[1], adj[v].pop()))
        else: path.append(stack.pop())
    vertices = list(reversed(path))
    out = vertices[0][0] + vertices[0][1] + "".join(v[1] for v in vertices[1:])
    assert len(out) == len(text)
    assert Counter(out) == Counter(text)
    assert Counter(zip(out, out[1:], out[2:])) == Counter(zip(text, text[1:], text[2:]))
    return out

def run():
    result = {}
    for name, text in CORPUS.items():
        original = len(zlib.compress(text.encode("utf-8"), 9))
        rows, seen = [], set()
        for i in range(N_PER_CORPUS):
            seed = SEEDS[i % len(SEEDS)] * 100000 + i
            transformed = reconstruct(text, seed)
            seen.add(transformed)
            rows.append(len(zlib.compress(transformed.encode("utf-8"), 9)) - original)
        result[name] = {
            "length": len(text), "original_zlib": original,
            "n_reconstructions": len(rows), "distinct_reconstructions": len(seen),
            "mean_delta_zlib": statistics.mean(rows), "median_delta_zlib": statistics.median(rows),
            "sd_delta_zlib": statistics.stdev(rows), "min_delta_zlib": min(rows), "max_delta_zlib": max(rows),
            "positive_fraction": sum(x > 0 for x in rows) / len(rows),
            "negative_fraction": sum(x < 0 for x in rows) / len(rows),
            "zero_fraction": sum(x == 0 for x in rows) / len(rows),
        }
    return {"experiment":"Ω-INF-7","date":"2026-08-13","question":"Do trigram-preserving reconstruction effects remain stable across more texts and seeds?","runs_per_corpus":N_PER_CORPUS,"seeds":SEEDS,"results":result,"interpretation_limit":"No semantic claim; compression is one observable. This experiment tests robustness of the sampling procedure, not a universal law of information."}

if __name__ == "__main__":
    output = Path(__file__).with_name("RESULTS_Omega-INF-7.json")
    data = run()
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, ensure_ascii=False, indent=2))
