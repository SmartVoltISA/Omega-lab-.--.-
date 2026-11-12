#!/usr/bin/env python3
"""EXP-009: local relational repair vs degree-product null; exploratory, not a test of universal autonomy."""
import argparse,json,random
import networkx as nx
import networkx.algorithms.community as community
from sklearn.metrics import normalized_mutual_info_score

def add_edges(G,count,mode,rng):
    nodes=list(G.nodes())
    for _ in range(count):
        edge=None
        if mode=="closure":
            cand=set()
            for w in nodes:
                ns=list(G.neighbors(w))
                if len(ns)>=2:
                    a,b=rng.sample(ns,2)
                    if a!=b and not G.has_edge(a,b): cand.add(tuple(sorted((a,b))))
            if cand: edge=rng.choice(sorted(cand))
        elif mode=="degree_null":
            weights=[G.degree(v)+1 for v in nodes]
            for _ in range(100):
                a,b=rng.choices(nodes,weights=weights,k=2)
                if a!=b and not G.has_edge(a,b): edge=tuple(sorted((a,b))); break
        else: raise ValueError(mode)
        if edge is None:
            available=[(a,b) for i,a in enumerate(nodes) for b in nodes[i+1:] if not G.has_edge(a,b)]
            if not available: break
            edge=rng.choice(available)
        G.add_edge(*edge)
    return G

def labels(G):
    groups=list(community.greedy_modularity_communities(G)); out={}
    for i,group in enumerate(groups):
        for v in group: out[v]=i
    return [out[v] for v in sorted(G.nodes())]

def measure(G,ref):
    comps=list(nx.connected_components(G))
    return {"transitivity":nx.transitivity(G),"avg_clustering":nx.average_clustering(G),
      "giant_fraction":max(map(len,comps))/len(G),"components":len(comps),
      "efficiency":nx.global_efficiency(G),
      "partition_nmi":normalized_mutual_info_score(ref,labels(G))}

def run(seeds):
    rows=[]
    for seed in range(seeds):
      for growth in ("closure","degree_null"):
        rg=random.Random(seed*1000+(0 if growth=="closure" else 1))
        G=nx.gnm_random_graph(100,160,seed=seed); add_edges(G,240,growth,rg)
        ref=labels(G); edges=list(G.edges()); rg.shuffle(edges)
        k=int(.20*len(edges)); G.remove_edges_from(edges[:k]); damaged=measure(G,ref)
        for repair in ("closure","degree_null"):
          rr=random.Random(seed*1000+10+(0 if repair=="closure" else 1))
          H=G.copy(); add_edges(H,k,repair,rr)
          rows.append({"seed":seed,"growth":growth,"repair":repair,"removed_edges":k,
                       "damaged":damaged,"repaired":measure(H,ref)})
    return rows

if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("--seeds",type=int,default=100)
 p.add_argument("--output",default="EXP-009_RESULTS.json"); a=p.parse_args()
 rows=run(a.seeds)
 with open(a.output,"w",encoding="utf-8") as f: json.dump({"experiment":"EXP-009","seeds":a.seeds,"records":rows},f,indent=2)
 print(f"Wrote {len(rows)} records to {a.output}")
