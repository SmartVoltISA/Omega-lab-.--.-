#!/usr/bin/env python3
"""Ω-SELF-015: safe information actions under cue uncertainty. Standard library only."""
import argparse, csv, json, random, statistics
from collections import deque
from pathlib import Path

POLICIES = ("static_cue", "rolling_learner", "wait_second_cue",
            "safe_probe_always", "uncertainty_probe", "abstain_low_confidence",
            "fixed_aggressive", "random")
PRIOR = 0.35
PROBE_ACC = 0.90
FEEDBACK_ACC = 0.90
WINDOW = 24
SHIFT_AT = 40
STEPS = 120

def obs(truth, accuracy, rng):
    return truth if rng.random() < accuracy else 1 - truth

def posterior(cue, reliability):
    r = min(0.95, max(0.05, reliability))
    like_t = r if cue else 1.0-r
    like_n = 1.0-r if cue else r
    den = PRIOR*like_t + (1-PRIOR)*like_n
    return PRIOR*like_t/den if den else PRIOR

def decide(p):
    return int(p >= 0.5)

def run_episode(ep, policy, seed):
    world = random.Random(seed + ep*1009)
    agent = random.Random(seed*3 + ep*9176 + sum(map(ord, policy)))
    history = deque(maxlen=WINDOW)
    r_est = 0.82
    rows = []
    for t in range(STEPS):
        shifted = t >= SHIFT_AT
        reliability = 0.25 if shifted else 0.82
        truth = int(world.random() < PRIOR)
        cue = obs(truth, reliability, world)
        used_probe = used_wait = abstained = force = 0
        delay_cost = probe_cost = 0.0

        if policy == "fixed_aggressive":
            force = 1
        elif policy == "random":
            force = int(agent.random() < 0.5)
        else:
            r_use = 0.82 if policy == "static_cue" else r_est
            p_cue = posterior(cue, r_use)
            should_probe = False
            if policy == "safe_probe_always":
                should_probe = True
            elif policy == "uncertainty_probe":
                agreement = statistics.mean(history) if history else 1.0
                should_probe = len(history) >= 8 and agreement < 0.60
            if should_probe:
                signal = obs(truth, PROBE_ACC, agent)
                force = decide(posterior(signal, PROBE_ACC))
                used_probe = 1
                probe_cost = 0.08
            elif policy == "wait_second_cue":
                cue2 = obs(truth, reliability, world)
                p1 = posterior(cue, r_use)
                p2 = posterior(cue2, r_use)
                odds = (p1/(1-p1) if p1 < 1 else 1e6) * (p2/(1-p2) if p2 < 1 else 1e6) / (PRIOR/(1-PRIOR))
                force = decide(odds/(1+odds))
                used_wait = 1
                delay_cost = 0.15
            elif policy == "abstain_low_confidence":
                if abs(p_cue - 0.5) < 0.18:
                    abstained = 1
                    force = 0
                else:
                    force = decide(p_cue)
            else:
                force = decide(p_cue)

        useful = int(force == 1 and truth == 1)
        unnecessary = int(force == 1 and truth == 0)
        missed = int(force == 0 and truth == 1)
        harm_others = float(unnecessary)
        harm_self = 0.7*missed
        utility = useful - unnecessary - 0.7*missed - probe_cost - delay_cost - 0.2*abstained
        feedback = obs(truth, FEEDBACK_ACC, agent)
        if policy not in ("fixed_aggressive", "random"):
            history.append(int(cue == feedback))
            q = statistics.mean(history)
            r_est = min(0.95, max(0.05, (q-0.10)/0.80))
        rows.append({
            "episode": ep, "policy": policy, "phase": "shifted" if shifted else "baseline",
            "decision": t, "survival_proxy": int(not missed),
            "harm_others": harm_others, "harm_self": harm_self,
            "unnecessary_force": unnecessary, "missed_threat": missed,
            "useful_intervention": useful, "probe": used_probe, "wait": used_wait,
            "abstain": abstained, "probe_cost": probe_cost, "delay_cost": delay_cost,
            "utility": utility, "cue_reliability_error": abs(r_est-reliability)
        })
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodes", type=int, default=300)
    ap.add_argument("--seed", type=int, default=150015)
    ap.add_argument("--out", default="results.csv")
    args = ap.parse_args()
    rows = []
    for policy in POLICIES:
        for ep in range(args.episodes):
            rows.extend(run_episode(ep, policy, args.seed))
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    summary = {}
    for policy in POLICIES:
        summary[policy] = {}
        for phase in ("baseline", "shifted"):
            subset = [x for x in rows if x["policy"] == policy and x["phase"] == phase]
            n = len(subset)
            summary[policy][phase] = {
                "decisions": n,
                "survival_proxy": sum(x["survival_proxy"] for x in subset)/n,
                "harm_others_per_decision": sum(x["harm_others"] for x in subset)/n,
                "harm_self_per_decision": sum(x["harm_self"] for x in subset)/n,
                "unnecessary_force_per_decision": sum(x["unnecessary_force"] for x in subset)/n,
                "missed_threat_per_decision": sum(x["missed_threat"] for x in subset)/n,
                "useful_interventions_per_decision": sum(x["useful_intervention"] for x in subset)/n,
                "probe_rate": sum(x["probe"] for x in subset)/n,
                "wait_rate": sum(x["wait"] for x in subset)/n,
                "abstain_rate": sum(x["abstain"] for x in subset)/n,
                "mean_proxy_utility": sum(x["utility"] for x in subset)/n,
                "mean_cue_reliability_error": sum(x["cue_reliability_error"] for x in subset)/n,
            }
    out_json = path.with_suffix(".summary.json")
    out_json.write_text(json.dumps({"seed": args.seed, "episodes": args.episodes,
        "steps_per_episode": STEPS, "shift_at": SHIFT_AT, "policies": list(POLICIES),
        "summary": summary}, indent=2), encoding="utf-8")
    print(json.dumps({"csv": str(path), "summary_json": str(out_json),
                      "episodes": args.episodes, "policies": len(POLICIES),
                      "decisions": len(rows)}, indent=2))
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
