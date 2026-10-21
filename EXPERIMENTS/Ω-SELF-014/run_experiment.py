#!/usr/bin/env python3
"""Ω-SELF-014: model-failure detection and alternative search.
Standard library only. Synthetic mechanism test, not a morality score.
"""
import argparse, csv, json, math, random, statistics
from collections import deque

POLICIES = ["static_model", "cumulative_learner", "rolling_learner",
            "change_detector", "fixed_aggressive", "random"]
N_EPISODES, BASELINE_STEPS, SHIFT_STEPS = 300, 40, 80
FEEDBACK_ACCURACY, BASELINE_RELIABILITY, SHIFT_RELIABILITY = 0.90, 0.82, 0.25
PRIOR_THREAT = 0.45
WINDOW, DETECT_RECENT, DETECT_PRIOR = 24, 12, 24

def clamp(x, lo=0.03, hi=0.97):
    return min(hi, max(lo, x))

def cue_probability(cue, reliability, prior=PRIOR_THREAT):
    r = clamp(reliability)
    if cue:
        a,b = r*prior, r*prior + (1-r)*(1-prior)
    else:
        a,b = (1-r)*prior, (1-r)*prior + r*(1-prior)
    return a/b if b else prior

def decode_match_rate(observed_match_rate):
    # If feedback is wrong with probability e, P(match observed)=e+(1-2e)*P(cue is truthful).
    e = 1.0 - FEEDBACK_ACCURACY
    return clamp((observed_match_rate-e)/(1-2*e))

def outcome(action, threat, people, rng):
    if action == "retreat":
        survival = 0.98
        saved = 0.12 if threat else 0.95
    elif action == "defend":
        survival = 0.80 if threat else 0.94
        saved = 0.88 if threat else 0.78
    elif action == "disable":
        survival = 0.88 if threat else 0.91
        saved = 0.93 if threat else 0.72
    else:
        survival = 0.02
        saved = 0.96 if threat else 0.65
    survived = rng.random() < survival
    harmed = round(people*(1-saved))
    utility = int(survived) + (people-harmed)*0.35 - harmed*0.25
    if action == "disable": utility -= 0.30
    if action == "sacrifice": utility -= 0.15
    return survived, harmed, utility

def expected_utility(action, p, people):
    v = 0.0
    for threat, prob in ((True,p),(False,1-p)):
        if action == "retreat":
            surv,saved = 0.98,(0.12 if threat else 0.95)
        elif action == "defend":
            surv,saved = (0.80 if threat else 0.94),(0.88 if threat else 0.78)
        elif action == "disable":
            surv,saved = (0.88 if threat else 0.91),(0.93 if threat else 0.72)
        else:
            surv,saved = 0.02,(0.96 if threat else 0.65)
        harmed = round(people*(1-saved))
        u = surv+(people-harmed)*0.35-harmed*0.25
        if action == "disable": u -= 0.30
        if action == "sacrifice": u -= 0.15
        v += prob*u
    return v

def choose(policy, cue, reliability, people, retreat, rng):
    p = cue_probability(cue,reliability)
    if policy == "random":
        return rng.choice(["defend","disable","sacrifice"] + (["retreat"] if retreat else []))
    if policy == "fixed_aggressive":
        return "disable" if p > 0.20 else ("retreat" if retreat else "defend")
    actions = ["defend","disable","sacrifice"] + (["retreat"] if retreat else [])
    # All remaining policies explicitly compare the same declared utility over alternatives.
    return max(actions,key=lambda a:(expected_utility(a,p,people),
                                     {"retreat":0,"defend":1,"disable":2,"sacrifice":3}[a]))

def update_estimate(matches, n):
    # Beta-like smoothing on true cue reliability, corrected for the known noisy feedback.
    observed = (matches + 2.0*0.75) / (n + 2.0)
    return decode_match_rate(observed)

def run_episode(policy, seed):
    scene_rng = random.Random(seed)
    action_rng = random.Random(seed+9000001)
    history = deque(maxlen=WINDOW)
    cumulative_matches, cumulative_n = 0,0
    reliability = 0.75
    detected = False
    detection_delay = None
    rows = []
    for t in range(BASELINE_STEPS+SHIFT_STEPS):
        shifted = t >= BASELINE_STEPS
        true_reliability = SHIFT_RELIABILITY if shifted else BASELINE_RELIABILITY
        threat = scene_rng.random() < PRIOR_THREAT
        cue = threat if scene_rng.random() < true_reliability else not threat
        people = scene_rng.randint(2,6) if scene_rng.random() < 0.35 else scene_rng.randint(1,4)
        retreat = scene_rng.random() < 0.60
        if policy == "static_model":
            decision_rel = BASELINE_RELIABILITY
        elif policy == "cumulative_learner":
            decision_rel = reliability
        elif policy == "rolling_learner":
            decision_rel = update_estimate(sum(history),len(history)) if history else 0.75
        elif policy == "change_detector":
            decision_rel = update_estimate(sum(history),len(history)) if history else 0.75
        else:
            decision_rel = BASELINE_RELIABILITY
        action = choose(policy,cue,decision_rel,people,retreat,action_rng)
        survived,harmed,utility = outcome(action,threat,people,action_rng)
        rows.append({"phase":"shifted" if shifted else "baseline",
                     "survived":int(survived),"people_harmed":harmed,
                     "opponent_harm":int(action=="disable"),
                     "unnecessary_force":int(action=="disable" and not threat),
                     "avoidable_sacrifice":int(action=="sacrifice" and (not threat or retreat)),
                     "retreat":int(action=="retreat"),"utility":utility,
                     "reliability_error":abs(decision_rel-true_reliability),
                     "decision_reliability":decision_rel})
        # No ground truth is exposed to the agent: only a noisy post-action feedback signal.
        feedback_threat = threat if action_rng.random() < FEEDBACK_ACCURACY else not threat
        match = int(cue == feedback_threat)
        history.append(match)
        cumulative_matches += match
        cumulative_n += 1
        reliability = update_estimate(cumulative_matches,cumulative_n)
        if policy == "change_detector" and t >= BASELINE_STEPS+DETECT_PRIOR+DETECT_RECENT:
            recent = list(history)[-DETECT_RECENT:]
            prior = list(history)[-WINDOW:-DETECT_RECENT]
            if len(prior) == DETECT_PRIOR and len(recent) == DETECT_RECENT:
                prior_rate = sum(prior)/len(prior)
                recent_rate = sum(recent)/len(recent)
                # Trigger on substantial observed deterioration; detector is intentionally explicit.
                if not detected and prior_rate-recent_rate >= 0.25:
                    detected = True
                    detection_delay = t-BASELINE_STEPS
    return rows,detection_delay

def ci95(values, seed, nboot=1500):
    if len(values)<2:
        m=statistics.mean(values) if values else float("nan")
        return m,m,m
    rng=random.Random(seed); n=len(values); boots=[]
    for _ in range(nboot):
        boots.append(statistics.mean(values[rng.randrange(n)] for _ in range(n)))
    boots.sort()
    return statistics.mean(values),boots[int(.025*nboot)],boots[min(nboot-1,int(.975*nboot))]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--episodes",type=int,default=N_EPISODES)
    ap.add_argument("--seed",type=int,default=140014)
    ap.add_argument("--out",default="results.csv")
    args=ap.parse_args()
    raw=[]
    delays={}
    for pi,policy in enumerate(POLICIES):
        policy_delays=[]
        for ep in range(args.episodes):
            seed=args.seed+ep*1000+19
            rows,delay=run_episode(policy,seed)
            if delay is not None: policy_delays.append(delay)
            for t,row in enumerate(rows):
                raw.append({"policy":policy,"episode":ep,"step":t,**row})
        delays[policy]=policy_delays
    with open(args.out,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(raw[0]));w.writeheader();w.writerows(raw)
    summary=[]
    metrics=["survived","people_harmed","opponent_harm","unnecessary_force",
             "avoidable_sacrifice","retreat","utility","reliability_error"]
    for policy in POLICIES:
        for phase in ("baseline","shifted"):
            epvals=[]
            for ep in range(args.episodes):
                subset=[r for r in raw if r["policy"]==policy and r["episode"]==ep and r["phase"]==phase]
                rec={"policy":policy,"phase":phase,"episode":ep}
                for m in metrics:
                    rec[m]=statistics.mean(r[m] for r in subset)
                epvals.append(rec)
            out={"policy":policy,"phase":phase,"episodes":args.episodes}
            for m in metrics:
                vals=[r[m] for r in epvals]
                mean,lo,hi=ci95(vals,args.seed+sum(map(ord,policy+phase+m)))
                out[m+"_mean"],out[m+"_ci95_low"],out[m+"_ci95_high"]=mean,lo,hi
            summary.append(out)
        if policy == "change_detector":
            out={"policy":policy,"phase":"change_detection"}
            out["detected_episodes"]=len(delays[policy])
            out["detection_rate"]=len(delays[policy])/args.episodes
            out["median_detection_delay"]=statistics.median(delays[policy]) if delays[policy] else None
            summary.append(out)
    with open("summary.json","w",encoding="utf-8") as f:
        json.dump({"experiment":"Ω-SELF-014","seed":args.seed,"episodes":args.episodes,
                   "steps_per_episode":BASELINE_STEPS+SHIFT_STEPS,"baseline_steps":BASELINE_STEPS,
                   "shifted_steps":SHIFT_STEPS,"policies":POLICIES,"summary":summary,
                   "limitations":"Synthetic, hand-designed policies; proxy utility is not morality."},
                  f,ensure_ascii=False,indent=2)
    print(json.dumps({"experiment":"Ω-SELF-014","episodes_per_policy":args.episodes,
                      "policy_count":len(POLICIES),"decisions":len(raw),"csv":args.out,
                      "summary":"summary.json"},ensure_ascii=False))
if __name__=="__main__":
    main()
