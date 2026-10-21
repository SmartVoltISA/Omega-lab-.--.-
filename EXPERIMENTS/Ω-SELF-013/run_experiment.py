#!/usr/bin/env python3
"""Ω-SELF-013 v2: conflict, self-preservation, and sacrifice.
Synthetic policy comparison. Proxy utility is not a moral score.
"""
import argparse, csv, json, math, random, statistics
from collections import defaultdict

POLICIES = ["self_preservation", "opponent_elimination", "sacrifice_first",
            "consequence_fixed", "consequence_learning", "random"]
FAMILIES = ["ordinary", "emergency", "cue_shift"]
N_EPISODES, N_STEPS, N_CALIBRATION = 240, 24, 80
FEEDBACK_ACCURACY = 0.90
FIXED_RELIABILITY = 0.82

def scenario(rng, family, cue_reliability):
    prior = 0.68 if family == "emergency" else 0.45
    threat = rng.random() < prior
    cue = threat if rng.random() < cue_reliability else not threat
    people = rng.randint(2, 6) if family == "emergency" else rng.randint(1, 4)
    retreat = rng.random() < (0.42 if family == "emergency" else 0.68)
    return {"threat": threat, "cue": cue, "people": people, "retreat": retreat}

def threat_probability(cue, reliability, prior):
    r = min(0.97, max(0.03, reliability))
    if cue:
        num, den = r*prior, r*prior + (1-r)*(1-prior)
    else:
        num, den = (1-r)*prior, (1-r)*prior + r*(1-prior)
    return num / den if den else prior

def action_outcomes(action, threat):
    if action == "retreat":
        return (0.98, 0.12 if threat else 0.95)
    if action == "defend":
        return (0.80 if threat else 0.94, 0.88 if threat else 0.78)
    if action == "disable":
        return (0.88 if threat else 0.91, 0.93 if threat else 0.72)
    return (0.02, 0.96 if threat else 0.65)

def expected_utility(action, p_threat, people, retreat):
    if action == "retreat" and not retreat:
        return -1e9
    val = 0.0
    for threat, p in ((True,p_threat),(False,1-p_threat)):
        survive, saved = action_outcomes(action, threat)
        v = survive + people*saved*0.35 - people*(1-saved)*0.25
        if action == "disable": v -= 0.30
        if action == "sacrifice": v -= 0.15
        val += p*v
    return val

def choose(policy, s, reliability, rng, prior):
    p = threat_probability(s["cue"], reliability, prior)
    if policy == "random":
        options = ["defend","disable","sacrifice"] + (["retreat"] if s["retreat"] else [])
        return rng.choice(options)
    if policy == "self_preservation":
        candidates = ["defend","disable"] + (["retreat"] if s["retreat"] else [])
        def surv(a):
            return p*(action_outcomes(a,True)[0]) + (1-p)*action_outcomes(a,False)[0]
        return max(candidates, key=lambda a:(surv(a), {"retreat":2,"defend":1,"disable":0}.get(a,0)))
    if policy == "opponent_elimination":
        return "disable" if p > 0.20 else ("retreat" if s["retreat"] else "defend")
    if policy == "sacrifice_first":
        return "sacrifice" if s["people"] >= 2 else ("retreat" if s["retreat"] else "defend")
    candidates = ["defend","disable","sacrifice"] + (["retreat"] if s["retreat"] else [])
    return max(candidates, key=lambda a:(expected_utility(a,p,s["people"],s["retreat"]),
                                           {"retreat":0,"defend":1,"disable":2,"sacrifice":3}[a]))

def update_reliability(stats, cue, feedback):
    matches, n = stats
    matches += int(cue == feedback); n += 1
    prior_n, prior_r = 4.0, 0.75
    prior_match_rate = (1-FEEDBACK_ACCURACY) + (2*FEEDBACK_ACCURACY-1)*prior_r
    observed_match_rate = (prior_n*prior_match_rate + matches) / (prior_n+n)
    estimate = (observed_match_rate - (1-FEEDBACK_ACCURACY)) / (2*FEEDBACK_ACCURACY-1)
    return (matches,n), min(0.97,max(0.03,estimate))

def run_episode(policy, family, seed):
    scenario_rng = random.Random(seed)
    action_rng = random.Random(seed+50000000)
    prior = 0.68 if family == "emergency" else 0.45
    reliability = 0.75
    stats = (0,0)
    for _ in range(N_CALIBRATION):
        s = scenario(scenario_rng, family, FIXED_RELIABILITY)
        feedback = s["threat"] if action_rng.random() < FEEDBACK_ACCURACY else not s["threat"]
        if policy == "consequence_learning":
            stats,reliability = update_reliability(stats,s["cue"],feedback)
    eval_reliability = 0.28 if family == "cue_shift" else FIXED_RELIABILITY
    rows = defaultdict(float)
    for _ in range(N_STEPS):
        s = scenario(scenario_rng, family, eval_reliability)
        decision_reliability = reliability if policy == "consequence_learning" else FIXED_RELIABILITY
        action = choose(policy,s,decision_reliability,action_rng,prior)
        rows["decisions"] += 1
        rows["retreats"] += int(action=="retreat")
        rows["opponent_harm"] += int(action=="disable")
        rows["unnecessary_force"] += int(action=="disable" and not s["threat"])
        rows["self_sacrifice"] += int(action=="sacrifice")
        rows["avoidable_sacrifice"] += int(action=="sacrifice" and (not s["threat"] or s["retreat"]))
        survive_p,saved = action_outcomes(action,s["threat"])
        survived = action_rng.random() < survive_p
        harmed = round(s["people"]*(1-saved))
        rows["agent_survived"] += int(survived)
        rows["people_harmed"] += harmed
        rows["proxy_utility"] += (int(survived)+(s["people"]-harmed)*0.35-harmed*0.25
                                  -int(action=="disable")*0.30-int(action=="sacrifice")*0.15)
        feedback = s["threat"] if action_rng.random() < FEEDBACK_ACCURACY else not s["threat"]
        if policy == "consequence_learning":
            stats,reliability = update_reliability(stats,s["cue"],feedback)
        rows["reliability_estimate_sum"] += reliability
        rows["reliability_error_sum"] += abs(reliability-eval_reliability)
    rows["reliability_estimate"] = rows["reliability_estimate_sum"]/N_STEPS
    rows["reliability_error"] = rows["reliability_error_sum"]/N_STEPS
    return dict(rows)

def bootstrap_ci(values, seed, nboot=2000):
    if len(values)<2: return (statistics.mean(values),)*3
    rng=random.Random(seed); n=len(values); means=[]
    for _ in range(nboot):
        means.append(statistics.mean(values[rng.randrange(n)] for _ in range(n)))
    means.sort()
    return statistics.mean(values),means[int(.025*nboot)],means[min(nboot-1,int(.975*nboot))]

def main():
    global N_EPISODES,N_STEPS,N_CALIBRATION
    ap=argparse.ArgumentParser()
    ap.add_argument("--episodes",type=int,default=N_EPISODES)
    ap.add_argument("--steps",type=int,default=N_STEPS)
    ap.add_argument("--calibration",type=int,default=N_CALIBRATION)
    ap.add_argument("--seed",type=int,default=130013)
    ap.add_argument("--out",default="results.csv")
    args=ap.parse_args()
    N_EPISODES,N_STEPS,N_CALIBRATION=args.episodes,args.steps,args.calibration
    raw=[]
    for fi,family in enumerate(FAMILIES):
        for pi,policy in enumerate(POLICIES):
            for ep in range(args.episodes):
                seed=args.seed+fi*1000000+ep*100+7
                raw.append({"family":family,"policy":policy,"episode":ep,
                            **run_episode(policy,family,seed)})
    with open(args.out,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(raw[0]));w.writeheader();w.writerows(raw)
    numeric=[k for k in raw[0] if k not in ("family","policy","episode")]
    summary=[]
    for family in FAMILIES:
        for policy in POLICIES:
            subset=[r for r in raw if r["family"]==family and r["policy"]==policy]
            rec={"family":family,"policy":policy,"episodes":len(subset)}
            for key in numeric:
                vals=[r[key] for r in subset if math.isfinite(r[key])]
                rec[key+"_mean"]=statistics.mean(vals)
                if key in ("agent_survived","people_harmed","opponent_harm","unnecessary_force",
                           "avoidable_sacrifice","proxy_utility","reliability_error"):
                    m,lo,hi=bootstrap_ci(vals,args.seed+sum(map(ord,family+policy+key)))
                    rec[key+"_ci95_low"],rec[key+"_ci95_high"]=lo,hi
            summary.append(rec)
    with open("summary.json","w",encoding="utf-8") as f:
        json.dump({"experiment":"Ω-SELF-013-v2","seed":args.seed,"episodes_per_policy_family":args.episodes,
                   "calibration_steps":N_CALIBRATION,"evaluation_steps":N_STEPS,
                   "policies":POLICIES,"families":FAMILIES,"summary":summary,
                   "note":"Synthetic policy comparison; proxy utility is not morality."},f,ensure_ascii=False,indent=2)
    print(json.dumps({"experiment":"Ω-SELF-013-v2","raw_rows":len(raw),"decisions":len(raw)*N_STEPS,
                      "calibration_steps_per_episode":N_CALIBRATION,"summary":"summary.json"}))
if __name__=="__main__":
    main()
