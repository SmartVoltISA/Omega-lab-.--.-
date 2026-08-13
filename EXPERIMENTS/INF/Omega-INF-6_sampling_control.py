"""Ω-INF-6 — sampling control for trigram-preserving reconstructions.

Question: is the observed variation a property of the trigram-equivalence class,
or an artifact of one randomized Eulerian traversal procedure?

This first control compares multiple traversal policies using the same exact
trigram multiset. It does not increase n-gram order and makes no semantic claim.
"""
import json, random, statistics, zlib
from collections import Counter, defaultdict
from pathlib import Path

SEED = 20260830
N_RUNS = 100
CORPUS = {
    "technical": "Система распределяет нагрузку по отдельным линиям. Каждый участок имеет свой автомат и проверяется независимо. Кабель прокладывается параллельно, соединения выполняются в доступных коробках, а параметры защиты выбираются по току нагрузки и условиям отключения. Перед вводом в эксплуатацию проверяются непрерывность защитного проводника, сопротивление изоляции и работа устройств защиты.",
    "literary": "Вечером город медленно затихал. Свет в окнах становился редким, дорога уходила за поворот и исчезала в темноте. Человек остановился у старого дома, прислушался и заметил, как ветер перебирает сухие ветви. Ничего особенного не происходило, но именно в этой тишине каждая маленькая перемена становилась заметной.",
    "structured": "Alpha connects to beta. Beta connects to gamma. Gamma connects to delta. Delta returns to alpha. A second loop begins at beta and reaches epsilon before returning to gamma. The two loops share a small number of transitions, so the same local pieces can participate in different larger paths. This sequence is deliberately regular enough to test whether local statistics determine the whole arrangement."
}

def reconstruct(text, seed, policy):
    rng = random.Random(seed)
    s=list(text); adj=defaultdict(list)
    for a,b,c in zip(s,s[1:],s[2:]): adj[(a,b)].append(c)
    for v, vals in adj.items():
        if policy == "shuffle": rng.shuffle(vals)
        elif policy == "reverse": vals.reverse()
        elif policy == "sorted": vals.sort()
    stack=[(s[0],s[1])]; path=[]
    while stack:
        v=stack[-1]
        if adj[v]: stack.append((v[1], adj[v].pop()))
        else: path.append(stack.pop())
    vertices=list(reversed(path))
    out=vertices[0][0]+vertices[0][1]+"".join(v[1] for v in vertices[1:])
    assert len(out)==len(text)
    assert Counter(out)==Counter(text)
    assert Counter(zip(out,out[1:],out[2:]))==Counter(zip(text,text[1:],text[2:]))
    return out

def run():
    result={}
    for name,text in CORPUS.items():
        original=len(zlib.compress(text.encode('utf-8'),9))
        result[name]={}
        for policy in ('shuffle','reverse','sorted'):
            vals=[len(zlib.compress(reconstruct(text,SEED+i,policy).encode('utf-8'),9)) for i in range(N_RUNS)]
            distinct={reconstruct(text,SEED+i,policy) for i in range(N_RUNS)}
            result[name][policy]={
                'original_zlib': original,
                'mean_zlib': statistics.mean(vals),
                'sd_zlib': statistics.stdev(vals),
                'min_zlib': min(vals), 'max_zlib': max(vals),
                'delta_mean': statistics.mean(vals)-original,
                'distinct_reconstructions': len(distinct)
            }
    return {'experiment':'Ω-INF-6','date':'2026-08-13','seed':SEED,'runs_per_policy':N_RUNS,'question':'Is the Ω-INF-5 variation dependent on the reconstruction sampling policy?','result':result,'interpretation_limit':'This is a sampling-method control. It does not establish semantic information or a universal hierarchy.'}

if __name__=='__main__':
    out=Path(__file__).with_name('RESULTS_Omega-INF-6.json')
    out.write_text(json.dumps(run(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(run(),ensure_ascii=False,indent=2))
