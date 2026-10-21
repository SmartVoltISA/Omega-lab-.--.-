#!/usr/bin/env python3
"""Omega SELF-009: test whether learned experience transfers to a structurally analogous task."""
import argparse, csv, json, random, statistics, math
from pathlib import Path

CONDITIONS = ["A_no_transfer", "B_episode_replay", "C_abstract_rule", "D_random_rule"]

def episode(seed, condition, family, horizon=180):
    rng = random.Random(seed)
    risk = rng.uniform(.18, .42)
    score = 0.0
    violations = 0
    safe_actions = 0
    total_actions = 0
    abstract_threshold = .62
    replay_threshold = .62 if family == "heat" else .42
    for t in range(horizon):
        seasonal = .12 * (1 + math.sin(t / 13.0))
        risk = max(0.0, min(1.0, risk + seasonal * .08 + rng.gauss(0, .055)))
        cue = max(0.0, min(1.0, risk * .70 + .16 + rng.gauss(0, .025))) if family == "battery" else max(0.0, min(1.0, risk + rng.gauss(0, .025)))
        if condition == "A_no_transfer":
            intervene = cue > .75
        elif condition == "B_episode_replay":
            intervene = cue > replay_threshold
        elif condition == "C_abstract_rule":
            normalized = max(0.0, min(1.0, (cue - .16) / .70)) if family == "battery" else cue
            intervene = normalized > abstract_threshold
        else:
            intervene = rng.random() < .35
        total_actions += 1
        if intervene:
            safe_actions += 1
            score -= .20
            risk = max(0.0, risk - .22 + rng.gauss(0, .025))
        else:
            score += 1.0
            risk = min(1.0, risk + .055 + rng.gauss(0, .025))
        if risk > .86:
            violations += 1
            score -= 2.0
            risk = max(0.0, risk - .18)
    return {"condition": condition, "family": family, "seed": seed, "score": score,
            "violations": violations, "safe_action_rate": safe_actions / max(1,total_actions),
            "final_risk": risk}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--seeds',type=int,default=250)
    ap.add_argument('--horizon',type=int,default=180)
    ap.add_argument('--out',default='results.csv')
    args=ap.parse_args()
    rows=[]
    for cond in CONDITIONS:
        for family in ['heat','battery']:
            for i in range(args.seeds):
                seed=900900 + i + (0 if family=='heat' else 100000)
                rows.append(episode(seed,cond,family,args.horizon))
    out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    summary={}
    for cond in CONDITIONS:
        rr=[r for r in rows if r['condition']==cond]
        summary[cond]={}
        for fam in ['heat','battery']:
            fr=[r for r in rr if r['family']==fam]
            summary[cond][fam]={k:round(statistics.mean(x[k] for x in fr),4) for k in ['score','violations','safe_action_rate','final_risk']}
        summary[cond]['transfer_gap_score']=round(summary[cond]['heat']['score']-summary[cond]['battery']['score'],4)
    meta={'experiment':'Ω-SELF-009','seeds_per_family':args.seeds,'steps_per_episode':args.horizon,'episodes_per_condition':2*args.seeds,
          'conditions':CONDITIONS,'train_family':'heat','transfer_test_family':'battery',
          'hypothesis':'A portable abstract risk rule transfers better than surface-level episode replay to a structurally analogous task.',
          'primary_metrics':['battery score','battery violations','battery final risk'],
          'limitations':['Toy simulator with stochastic noise','Abstract-rule normalization is explicitly provided, so this tests rule transfer rather than autonomous abstraction discovery','No evidence of general intelligence or consciousness']}
    (out.parent/'summary.json').write_text(json.dumps(summary,indent=2))
    (out.parent/'metadata.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps({'summary':summary,'metadata':meta},indent=2))
if __name__=='__main__': main()
