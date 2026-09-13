"""Ω-MEM-5 deterministic runner.

Implements the fixed protocol with equal nominal memory budget S=4,
controlled generators, relevant/mismatched/random memory encodings,
predictive-partition metrics, and a single memory intervention check.
"""
import json, math
from collections import Counter, defaultdict
import numpy as np

N=20_000
SEEDS=range(10)


def periodic4(n, seed=0):
    p=[0,1,1,0]
    return np.array([p[i%4] for i in range(n)], dtype=int)


def markov2(n, seed=0):
    x=[0,1]
    for _ in range(2,n): x.append(x[-1]^x[-2])
    return np.array(x, dtype=int)


def thue_morse(n, seed=0):
    return np.array([i.bit_count()%2 for i in range(n)], dtype=int)


def hmm(n, seed):
    rng=np.random.default_rng(seed); h=0; xs=[]; hs=[]
    for _ in range(n):
        h = h if rng.random()<0.85 else 1-h
        p=0.15 if h==0 else 0.85
        xs.append(int(rng.random()<p)); hs.append(h)
    return np.array(xs), np.array(hs)


def iid(n, seed):
    return np.random.default_rng(seed).integers(0,2,size=n)


def trailing_ones_parity(i):
    k=0
    while i & 1:
        k += 1; i >>= 1
    return k%2


def noise_bit(i):
    z=(i*0x9E3779B1+0x85EBCA77)&0xffffffff
    z ^= z>>16; z=(z*0x7feb352d)&0xffffffff; z ^= z>>15
    return z&1


def key(gen, x, h, i, memory):
    if memory=='none': return (int(x[i]),)
    if memory=='relevant':
        if gen=='HMM': return (int(h[i]),)
        if gen=='Markov-2': return (int(x[i-1]), int(x[i]))
        if gen=='Thue-Morse': return (int(x[i]), trailing_ones_parity(i))
        if gen=='Periodic-4': return (i%4,)
        return (int(x[i]),)
    # Deliberately irrelevant but equal nominal 4-way capacity when paired with current symbol.
    if memory in ('mismatched','random'):
        return ((int(x[i])<<1) | noise_bit(i),)
    raise ValueError(memory)


def metrics(keys, ys):
    d=defaultdict(list)
    for k,y in zip(keys,ys): d[k].append(int(y))
    total=len(ys); H=0.; acc=0.; choices=[]
    for vals in d.values():
        c=Counter(vals); n=len(vals)
        H += n/total * (-sum((v/n)*math.log2(v/n) for v in c.values()))
        acc += max(c.values()); choices.append(len(c))
    return {
        'accuracy':acc/total,
        'conditional_entropy':H,
        'predictive_partition_size':len(d),
        'mean_distinct_next_choices':float(np.mean(choices)),
        'max_distinct_next_choices':int(max(choices)),
    }


def evaluate(gen, x, h, memory):
    keys=[key(gen,x,h,i,memory) for i in range(1,len(x)-1)]
    return metrics(keys, x[2:])


def intervention(gen, x, h):
    keys=[key(gen,x,h,i,'relevant') for i in range(1,len(x)-1)]
    ys=x[2:]; model=defaultdict(list)
    for k,y in zip(keys,ys): model[k].append(int(y))
    pred={k:Counter(v).most_common(1)[0][0] for k,v in model.items()}
    j=len(keys)//2; original=keys[j]; normal=pred[original]
    alternatives=[k for k,v in pred.items() if v!=normal]
    if not alternatives: return {'prediction_changed':False}
    altered=alternatives[0]
    return {
        'index':j+1,
        'external_state':int(x[j+1]),
        'original_memory':str(original),
        'intervened_memory':str(altered),
        'normal_prediction':normal,
        'intervened_prediction':pred[altered],
        'prediction_changed':pred[altered]!=normal,
    }


def main():
    generators={'Periodic-4':periodic4,'Markov-2':markov2,'Thue-Morse':thue_morse,'HMM':hmm,'IID':iid}
    rows=[]; interventions=[]
    for gen,fn in generators.items():
        for seed in SEEDS:
            if gen=='HMM': x,h=fn(N,seed)
            else: x,h=fn(N,seed),None
            for memory in ('none','relevant','mismatched','random'):
                rows.append({'generator':gen,'seed':seed,'memory':memory,'S':4,**evaluate(gen,x,h,memory)})
            if gen!='IID': interventions.append({'generator':gen,'seed':seed,**intervention(gen,x,h)})
    with open('RAW_RESULTS.json','w',encoding='utf-8') as f: json.dump({'N':N,'seeds':list(SEEDS),'rows':rows,'interventions':interventions},f,indent=2)
    print('Wrote RAW_RESULTS.json')

if __name__=='__main__': main()
