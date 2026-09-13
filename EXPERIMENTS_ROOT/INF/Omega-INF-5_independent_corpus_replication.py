"""Ω-INF-5 — independent corpus replication.

Replication of Ω-INF-4 on four independent short sequences. The exact trigram
multiset is preserved by randomized Eulerian traversal. No new n-gram order is
introduced and no semantic interpretation is attempted.
"""
import json, math, random, statistics, zlib
from collections import Counter, defaultdict
from pathlib import Path

SEED_START = 20260820
N_RUNS = 100
CORPUS = {
"technical": "Система распределяет нагрузку по отдельным линиям. Каждый участок имеет свой автомат и проверяется независимо. Кабель прокладывается параллельно, соединения выполняются в доступных коробках, а параметры защиты выбираются по току нагрузки и условиям отключения. Перед вводом в эксплуатацию проверяются непрерывность защитного проводника, сопротивление изоляции и работа устройств защиты.",
"literary": "Вечером город медленно затихал. Свет в окнах становился редким, дорога уходила за поворот и исчезала в темноте. Человек остановился у старого дома, прислушался и заметил, как ветер перебирает сухие ветви. Ничего особенного не происходило, но именно в этой тишине каждая маленькая перемена становилась заметной.",
"random_like": "q7mK2xP9vL4aN8sT3wZ6cR1hY5uB0dF8jQ2nX7pM4kS9eV3tA6gH1rW5zC0xD8mL2qP7vN4sJ9fK3bT6yU1cG5hR0wX8aZ2nM7pQ4dS9vL3kF6jB1tY5eC0rH8xW2mN7zP4qA9sD3vK6fJ1uT5gB0hX8cR2yM7lQ4pS9nV3dF6kZ1aC5tW0rH8jX2mN7qP4vL9sD3eK6bT1yU5gA0fR8cJ2zM7wQ4nP9",
"structured": "Alpha connects to beta. Beta connects to gamma. Gamma connects to delta. Delta returns to alpha. A second loop begins at beta and reaches epsilon before returning to gamma. The two loops share a small number of transitions, so the same local pieces can participate in different larger paths. This sequence is deliberately regular enough to test whether local statistics determine the whole arrangement."
}

def h(seq, order):
    if len(seq) <= order: return 0.0
    p=Counter(tuple(seq[i-order:i]) for i in range(order,len(seq)))
    e=Counter(tuple(seq[i-order:i+1]) for i in range(order,len(seq)))
    n=len(seq)-order
    return -sum(c/n*math.log2(c/p[x[:-1]]) for x,c in e.items())

def metrics(text):
    s=list(text)
    return {"n":len(s),"H0":-sum(c/len(s)*math.log2(c/len(s)) for c in Counter(s).values()),"H1":h(s,1),"H2":h(s,2),"H3":h(s,3),"unique_trigrams":len(Counter(zip(s,s[1:],s[2:]))),"zlib":len(zlib.compress(text.encode("utf-8"),9))}

def reconstruct(text, seed):
    rng=random.Random(seed); s=list(text); adj=defaultdict(list)
    for a,b,c in zip(s,s[1:],s[2:]): adj[(a,b)].append(c)
    for v in adj: rng.shuffle(adj[v])
    stack=[(s[0],s[1])]; path=[]
    while stack:
        v=stack[-1]
        if adj[v]: stack.append((v[1],adj[v].pop()))
        else: path.append(stack.pop())
    v=list(reversed(path)); out=v[0][0]+v[0][1]+"".join(x[1] for x in v[1:])
    assert len(out)==len(text) and Counter(out)==Counter(text)
    assert Counter(zip(out,out[1:],out[2:]))==Counter(zip(text,text[1:],text[2:]))
    return out

def run():
    result={}
    for name,text in CORPUS.items():
        original=metrics(text); runs=[metrics(reconstruct(text,SEED_START+i)) for i in range(N_RUNS)]
        result[name]={"length":len(text),"original":original,"mean_zlib":statistics.mean(x["zlib"] for x in runs),"sd_zlib":statistics.stdev(x["zlib"] for x in runs),"min_zlib":min(x["zlib"] for x in runs),"max_zlib":max(x["zlib"] for x in runs),"mean_H3":statistics.mean(x["H3"] for x in runs),"trigram_invariant":all(x["unique_trigrams"]==original["unique_trigrams"] for x in runs)}
    return {"experiment":"Ω-INF-5","date":"2026-08-13","seed_start":SEED_START,"runs_per_corpus":N_RUNS,"question":"Does the Ω-INF-4 observation replicate on independent texts?","results":result}

if __name__=="__main__":
    out=Path(__file__).with_name("RESULTS_Omega-INF-5.json"); out.write_text(json.dumps(run(),ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(run(),ensure_ascii=False,indent=2))
