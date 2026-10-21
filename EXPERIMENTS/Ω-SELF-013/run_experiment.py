#!/usr/bin/env python3
"""Ω-SELF-013 deterministic synthetic conflict experiment. Python 3.10+."""
import argparse, csv, json, math, random, statistics
from collections import defaultdict

POLICIES = ["self_preservation", "opponent_elimination", "sacrifice_first",
            "consequence_fixed", "consequence_learning", "random"]
FAMILIES = ["ordinary", "emergency", "cue_shift"]
N_EPISODES = 240
N_STEPS = 24

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, x))))

def scenario(rng, family, step):
    base = rng.uniform(0.08, 0.92)
    if family == "emergency":
        base = min(0.98, max(0.02, base * 0.8 + 0.18))
        people = rng.randint(2, 6)
    else:
        people = rng.randint(1, 4)
    threat = rng.random() < base
    cue_reliability = 0.82 if family != "cue_shift" else 0.28
    cue = (threat if rng.random() < cue_reliability else not threat)
    retreat_available = rng.random() < (0.68 if family != "emergency" else 0.42)
    severity = rng.choice([1, 2, 3]) if threat else rng.choice([0, 1])
    return {"prior": base, "threat": threat, "cue": cue, "people": people,
            "retreat": retreat_available, "severity": severity}

def choose(policy, s, learned_reliability, rng):
    threat_p = learned_reliability if s["cue"] else 1.0 - learned_reliability
    threat_p = min(0.97, max(0.03, threat_p))
    if policy == "random":
        opts = ["defend", "disable", "sacrifice"] + (["retreat"] if s["retreat"] else [])
        return rng.choice(opts)
    if policy == "self_preservation":
        if s["retreat"]: return "retreat"
        return "defend" if threat_p > 0.38 else "disable"
    if policy == "opponent_elimination":
        return "disable" if threat_p > 0.20 else ("retreat" if s["retreat"] else "defend")
    if policy == "sacrifice_first":
        return "sacrifice" if s["people"] >= 2 else ("defend" if threat_p > 0.25 else "retreat" if s["retreat"] else "defend")
    # Expected consequences: values are explicit proxies, not ethical facts.
    if policy == "consequence_learning":
        r = learned_reliability
        threat_p = r if s["cue"] else 1-r
    candidates = ["defend", "disable", "sacrifice"]
    if s["retreat"]: candidates.append("retreat")
    values = {}
    for a in candidates:
        if a == "retreat":
            values[a] = 0.97 - threat_p * (0.55 + 0.08*s["people"])
        elif a == "defend":
            values[a] = 0.84 + threat_p * (0.34 + 0.10*s["people"]) - 0.08*s["severity"]
        elif a == "disable":
            values[a] = 0.78 + threat_p * (0.52 + 0.12*s["people"]) - 0.32 - (1-threat_p)*0.30
        else: # sacrifice self to protect others
            values[a] = 0.05 + threat_p * (0.50 + 0.14*s["people"]) - 0.10
    # Small stable tie-break avoids random noise obscuring policy.
    return max(candidates, key=lambda a: (values[a], {"retreat":0,"defend":1,"disable":2,"sacrifice":3}[a]))

def run_episode(policy, family, seed):
    rng = random.Random(seed)
    learned_rel = 0.75
    rows = defaultdict(float)
    for t in range(N_STEPS):
        s = scenario(rng, family, t)
        action = choose(policy, s, learned_rel, rng)
        threat = s["threat"]
        people = s["people"]
        rows["decisions"] += 1
        rows["threats"] += int(threat)
        rows["people_at_risk"] += people
        rows["retreats"] += int(action == "retreat")
        rows["opponent_harm"] += int(action == "disable")
        rows["unnecessary_force"] += int(action == "disable" and not threat)
        rows["self_sacrifice"] += int(action == "sacrifice")
        rows["avoidable_sacrifice"] += int(action == "sacrifice" and (not threat or s["retreat"]))
        if action == "sacrifice":
            survived = rng.random() < 0.02
            saved_fraction = 0.96 if threat else 0.65
        elif action == "retreat":
            survived = rng.random() < 0.98
            saved_fraction = (0.12 if threat else 0.95) if s["retreat"] else 0.30
        elif action == "defend":
            survived = rng.random() < (0.90 if not threat else 0.80 - 0.04*s["severity"])
            saved_fraction = 0.88 if threat else 0.78
        else: # disable opponent
            survived = rng.random() < (0.93 if not threat else 0.86)
            saved_fraction = 0.93 if threat else 0.72
        rows["agent_survived"] += int(survived)
        harmed = round(people * (1.0 - saved_fraction))
        rows["people_harmed"] += harmed
        rows["people_protected"] += people - harmed
        # Learning is based on observed outcome proxy, not privileged access to truth.
        if policy == "consequence_learning":
            observed_threat = action in ("defend", "disable") and (not survived or rng.random() < 0.12)
            # Bayesian-like moving estimate of whether this cue predicts an adverse event.
            target = 1.0 if observed_threat == s["cue"] else 0.0
            learned_rel = min(0.95, max(0.05, 0.92*learned_rel + 0.08*target))
        # transparent engineering score for comparison only
        rows["proxy_utility"] += (int(survived)*1.0 + (people-harmed)*0.35
                                  - harmed*0.25 - int(action=="disable")*0.30
                                  - int(action=="sacrifice")*0.15)
    rows["calibration_error"] = abs(learned_rel - (0.82 if family != "cue_shift" else 0.28)) if policy == "consequence_learning" else float("nan")
    return dict(rows)

def mean_ci(values, rng, nboot=1200):
    if not values: return (float("nan"), float("nan"), float("nan"))
    mean = statistics.mean(values)
    if len(values) < 2: return mean, mean, mean
    boots = []
    for _ in range(nboot):
        boots.append(statistics.mean(rng.choice(values) for _ in values))
    boots.sort()
    return mean, boots[int(0.025*nboot)], boots[min(nboot-1, int(0.975*nboot))]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", type=int, default=N_EPISODES)
    ap.add_argument("--steps", type=int, default=N_STEPS)
    ap.add_argument("--seed", type=int, default=130013)
    ap.add_argument("--out", default="results.csv")
    args = ap.parse_args()
    global N_STEPS
    N_STEPS = args.steps
    raw = []
    for fi, family in enumerate(FAMILIES):
        for pi, policy in enumerate(POLICIES):
            for ep in range(args.episodes):
                # Common episode seeds across policies within each family.
                seed = args.seed + fi*1000000 + ep*100 + 7
                result = run_episode(policy, family, seed)
                raw.append({"family":family,"policy":policy,"episode":ep,**result})
    fields = list(raw[0].keys())
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(raw)
    summary=[]
    numeric=[k for k in raw[0] if k not in ("family","policy","episode")]
    for family in FAMILIES:
        for policy in POLICIES:
            subset=[r for r in raw if r["family"]==family and r["policy"]==policy]
            out={"family":family,"policy":policy,"episodes":len(subset)}
            for key in numeric:
                vals=[r[key] for r in subset if isinstance(r[key],(int,float)) and math.isfinite(r[key])]
                # Episode-level rates / counts, not pooled decisions pretending to be independent.
                out[key+"_mean"]=statistics.mean(vals) if vals else None
                if key in ("agent_survived","people_harmed","opponent_harm","unnecessary_force","avoidable_sacrifice","proxy_utility","calibration_error"):
                    m,lo,hi=mean_ci(vals, random.Random(args.seed+hash((family,policy,key))%100000), nboot=1200)
                    out[key+"_ci95_low"]=lo; out[key+"_ci95_high"]=hi
            summary.append(out)
    with open("summary.json","w",encoding="utf-8") as f:
        json.dump({"experiment":"Ω-SELF-013","seed":args.seed,"episodes_per_policy_family":args.episodes,
                   "steps_per_episode":N_STEPS,"policies":POLICIES,"families":FAMILIES,
                   "summary":summary,"note":"Synthetic policy comparison; proxy utility is not morality."},f,ensure_ascii=False,indent=2)
    print(json.dumps({"experiment":"Ω-SELF-013","raw_rows":len(raw),"episodes_per_policy_family":args.episodes,
                      "steps_per_episode":N_STEPS,"csv":args.out,"summary":"summary.json"},ensure_ascii=False))
if __name__ == "__main__":
    main()
