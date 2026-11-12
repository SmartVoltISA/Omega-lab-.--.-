"""EXP-007: reconstructed relation-endpoint coalescence test.
This is a new operationalization inspired by archival description, NOT recovered original code.
NumPy only. Run: python EXP-007_RELATION_ENDPOINT_COALESCENCE_RECONSTRUCTION.py
"""
import json
import numpy as np

N_REL = 150
STEPS = 500
BOX = 10.0
MOVE = 0.08
SEEDS = range(20261112, 20261152)
THRESHOLDS = (0.05, 0.10, 0.20)

def root(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def metrics(parent):
    n = 2 * N_REL
    roots = np.array([root(parent, i) for i in range(n)])
    _, inv = np.unique(roots, return_inverse=True)
    nv = int(inv.max()) + 1
    edges = [(int(inv[2*k]), int(inv[2*k+1])) for k in range(N_REL)]
    adj = [set() for _ in range(nv)]
    loops = 0
    for a, b in edges:
        if a == b:
            loops += 1
        else:
            adj[a].add(b); adj[b].add(a)
    seen, sizes = set(), []
    for v in range(nv):
        if v in seen: continue
        stack, size = [v], 0
        seen.add(v)
        while stack:
            x = stack.pop(); size += 1
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        sizes.append(size)
    triangles = 0
    for i in range(nv):
        for j in adj[i]:
            if j > i:
                triangles += sum(1 for k in (adj[i] & adj[j]) if k > j)
    components = len(sizes)
    return {
        "vertices": nv, "edges": N_REL, "components": components,
        "cycle_rank": N_REL - nv + components, "self_loops": loops,
        "triangles": triangles, "giant_fraction": max(sizes)/nv,
        "mean_degree": float(np.mean([len(a) for a in adj]))
    }

def spatial(seed, threshold, steps=STEPS, move=MOVE):
    rng = np.random.default_rng(seed)
    n = 2 * N_REL
    pos = rng.random((n, 2)) * BOX
    parent = np.arange(n)
    merges = 0
    for _ in range(steps):
        roots = np.unique([root(parent, i) for i in range(n)])
        pos[roots] = (pos[roots] + rng.normal(0, move, (len(roots), 2))) % BOX
        if len(roots) < 2: continue
        p = pos[roots]
        d = np.abs(p[:, None, :] - p[None, :, :])
        d = np.minimum(d, BOX - d)
        ii, jj = np.where(np.triu((d*d).sum(2) < threshold*threshold, 1))
        for a, b in zip(ii, jj):
            ra, rb = root(parent, int(roots[a])), root(parent, int(roots[b]))
            if ra != rb:
                parent[rb] = ra
                merges += 1
    out = metrics(parent)
    out.update(seed=seed, condition="spatial", threshold=threshold, merges=merges)
    return out

def matched_random(seed, merges, threshold):
    rng = np.random.default_rng(seed + 900000)
    parent = np.arange(2 * N_REL)
    for _ in range(merges):
        roots = list(set(root(parent, i) for i in range(2 * N_REL)))
        if len(roots) < 2: break
        a, b = rng.choice(roots, 2, replace=False)
        parent[int(b)] = int(a)
    out = metrics(parent)
    out.update(seed=seed, condition="random_matched", threshold=threshold, merges=merges)
    return out

def summarize(rows):
    result = {}
    for th in THRESHOLDS:
        result[str(th)] = {}
        for condition in ("spatial", "random_matched"):
            group = [r for r in rows if r["threshold"] == th and r["condition"] == condition]
            result[str(th)][condition] = {}
            for key in ("vertices", "components", "cycle_rank", "self_loops",
                        "triangles", "giant_fraction", "mean_degree", "merges"):
                vals = np.array([r[key] for r in group], float)
                result[str(th)][condition][key] = {
                    "mean": float(vals.mean()),
                    "sd": float(vals.std(ddof=1))
                }
        a = {r["seed"]: r for r in rows if r["threshold"] == th and r["condition"] == "spatial"}
        b = {r["seed"]: r for r in rows if r["threshold"] == th and r["condition"] == "random_matched"}
        result[str(th)]["paired_delta_spatial_minus_random"] = {}
        rng = np.random.default_rng(771 + int(th*1000))
        for key in ("components", "cycle_rank", "self_loops", "triangles", "giant_fraction"):
            d = np.array([a[s][key] - b[s][key] for s in sorted(a)], float)
            boot = np.array([rng.choice(d, len(d), replace=True).mean() for _ in range(10000)])
            result[str(th)]["paired_delta_spatial_minus_random"][key] = {
                "mean": float(d.mean()),
                "bootstrap_95pct_ci": [float(np.quantile(boot, .025)), float(np.quantile(boot, .975))]
            }
    return result

def main():
    rows = []
    for th in THRESHOLDS:
        for seed in SEEDS:
            s = spatial(seed, th)
            r = matched_random(seed, s["merges"], th)
            rows.extend([s, r])
    payload = {
        "experiment": "EXP-007 relation endpoint coalescence reconstruction",
        "status": "executed reconstructed operationalization; not exact historical replication",
        "parameters": {"relations": N_REL, "initial_endpoints": 2*N_REL,
                       "steps": STEPS, "box": BOX, "movement_sd": MOVE,
                       "thresholds": list(THRESHOLDS), "seeds": [min(SEEDS), max(SEEDS)],
                       "runs_per_condition_threshold": len(SEEDS)},
        "summary": summarize(rows), "raw": rows
    }
    with open("EXP-007_RELATION_ENDPOINT_COALESCENCE_RESULTS.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(json.dumps(payload["summary"], indent=2))

if __name__ == "__main__":
    main()
