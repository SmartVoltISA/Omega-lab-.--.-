#!/usr/bin/env python3
"""Deterministic synthetic pilot for Ω-SELF-012. No real-world systems are touched."""
from __future__ import annotations
import csv, hashlib, json, math, random, statistics
from pathlib import Path

SEED = 12012
EPISODES_PER_FAMILY = 240
STEPS = 60
POLICIES = ["A_self_only", "B_fixed_prohibition", "C_total_outcome", "D_consequence_fairness", "E_uncertainty_aware", "F_random_control"]
FAMILIES = ["ordinary_scarcity", "emergency", "heldout_cue_shift"]
OUT = Path(__file__).resolve().parent

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, x))))

def run_episode(policy, family, seed):
    rng = random.Random(seed)
    own = 8.0
    others = [8.0, 8.0]
    useful = incidents = harm_others = probes = fairness_violations = revisions = 0
    previous_error = False
    known_risk = 0.5
    surprise_count = 0
    for step in range(STEPS):
        # Scenario family is held out by cue encoding, not by changing the abstract risk structure.
        event = rng.choices(["ordinary", "emergency", "recovery"], weights=[0.55, 0.25, 0.20])[0]
        latent_risk = rng.random()
        cue = latent_risk
        if family == "heldout_cue_shift":
            cue = 1.0 - latent_risk  # same underlying structure, inverted surface cue
        if event == "emergency":
            target = min(range(2), key=lambda i: others[i])
            emergency_severity = 1.0 if others[target] < 4.0 else 0.5
        else:
            target = min(range(2), key=lambda i: others[i])
            emergency_severity = 0.0
        # Agent's cue-based prediction may be wrong, especially on the held-out mapping.
        predicted_risk = cue if family != "heldout_cue_shift" else 1.0 - cue
        uncertainty = abs(predicted_risk - 0.5) * 2.0
        # Safe probe costs a small amount but reveals whether a risky/urgent transfer is warranted.
        do_probe = False
        if policy == "C_total_outcome":
            do_probe = False
        elif policy == "D_consequence_fairness":
            do_probe = uncertainty > 0.65 and latent_risk > 0.72
        elif policy == "E_uncertainty_aware":
            do_probe = uncertainty > 0.35 and (event == "emergency" or latent_risk > 0.6)
        elif policy == "F_random_control":
            do_probe = rng.random() < 0.30
        if do_probe:
            probes += 1
            own = max(0.0, own - 0.20)
            predicted_risk = latent_risk
        # Action choices encode policy differences, but no policy is labeled morally correct by definition.
        if policy == "F_random_control":
            action = rng.choice(["work", "take", "share", "rest"])
        elif policy == "A_self_only":
            action = "take" if own < 7.0 or rng.random() < 0.65 else "work"
        elif policy == "B_fixed_prohibition":
            action = "share" if event == "emergency" and others[target] < 3.0 and own > 4.0 else "work"
        elif policy == "C_total_outcome":
            # Approximate total-welfare choice: share in acute emergency, otherwise work; take only if it prevents imminent own failure.
            action = "share" if event == "emergency" and others[target] < 3.5 and own > 3.0 else ("take" if own < 1.5 else "work")
        elif policy == "D_consequence_fairness":
            inequality = abs(own - min(others))
            if event == "emergency" and others[target] < 4.0 and own > 3.0:
                action = "share"
            elif inequality > 5.0 and own > min(others) + 1.0:
                action = "share"
            elif own < 2.5:
                action = "take" if min(others) > 4.0 else "rest"
            else:
                action = "work"
        else:  # E: uncertainty-aware consequence + fairness
            if event == "emergency" and others[target] < 4.0 and own > 3.0 and predicted_risk > 0.25:
                action = "share"
            elif abs(own - min(others)) > 5.0 and own > min(others) + 1.0:
                action = "share"
            elif own < 2.5:
                action = "take" if min(others) > 4.0 else "rest"
            else:
                action = "work"
        if action == "work":
            if own >= 0.5:
                own -= 0.5
                useful += 1
            else:
                own += 0.15
        elif action == "take":
            # Stealing yields short-term task value but harms another agent; high latent risk can trigger an incident.
            amount = min(1.5, others[target])
            others[target] -= amount
            own += amount * 0.8
            useful += 1.2
            harm_others += amount
            if latent_risk > 0.72 or others[target] < 0.5:
                incidents += 1
                harm_others += 1.0
                own = max(0.0, own - 0.5)
                others[target] = max(0.0, others[target] - 0.5)
        elif action == "share":
            if own >= 0.5:
                own -= 0.5
                others[target] += 0.8
                # A transfer averts a simulated incident when a vulnerable agent is helped in an emergency.
                if event == "emergency" and others[target] >= 2.0:
                    useful += 0.8
                else:
                    useful += 0.2
            else:
                own += 0.1
        else:  # rest
            own += 0.6
        # The environment provides consequences; recovery means a subsequent non-harmful choice after an incident.
        if incidents > 0 and action != "take":
            revisions += 1
        own = min(15.0, max(0.0, own))
        others = [min(15.0, max(0.0, x)) for x in others]
        if own <= 0.05:
            # The agent can fail, but episode continues to measure external consequences.
            own = 0.0
    survival = 1 if own > 0 else 0
    inequality = statistics.pstdev([own] + others)
    # No composite morality score: these are separate observables.
    return {
        "policy": policy, "family": family, "seed": seed,
        "survival": survival, "incidents": incidents, "harm_others": round(harm_others, 5),
        "useful_work": round(useful, 5), "probes": probes, "resource_inequality": round(inequality, 5),
        "final_own_reserve": round(own, 5), "final_other_reserve_mean": round(statistics.mean(others), 5),
        "model_revisions_proxy": revisions
    }

def bootstrap_ci(values, seed, reps=4000):
    rng = random.Random(seed)
    means = []
    n = len(values)
    for _ in range(reps):
        means.append(statistics.mean(values[rng.randrange(n)] for __ in range(n)))
    means.sort()
    return [round(means[int(0.025 * reps)], 5), round(means[int(0.975 * reps)], 5)]

def main():
    rows = []
    for fi, family in enumerate(FAMILIES):
        for pi, policy in enumerate(POLICIES):
            for ep in range(EPISODES_PER_FAMILY):
                seed = SEED + fi * 1000000 + ep * 31
                rows.append(run_episode(policy, family, seed))
    csv_path = OUT / "results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    keys = ["survival", "incidents", "harm_others", "useful_work", "probes", "resource_inequality", "final_own_reserve", "final_other_reserve_mean"]
    summary = {}
    for policy in POLICIES:
        summary[policy] = {}
        for key in keys:
            vals = [r[key] for r in rows if r["policy"] == policy]
            summary[policy][key] = {"mean": round(statistics.mean(vals), 5), "ci95_independent_bootstrap": bootstrap_ci(vals, SEED + len(policy) + len(key))}
    family_summary = {}
    for family in FAMILIES:
        family_summary[family] = {}
        for policy in POLICIES:
            family_summary[family][policy] = {}
            for key in keys:
                vals = [r[key] for r in rows if r["family"] == family and r["policy"] == policy]
                family_summary[family][policy][key] = round(statistics.mean(vals), 5)
    metadata = {
        "experiment": "Ω-SELF-012",
        "seed_base": SEED,
        "episodes_per_policy_per_family": EPISODES_PER_FAMILY,
        "steps_per_episode": STEPS,
        "families": FAMILIES,
        "policies": POLICIES,
        "episode_count": len(rows),
        "bootstrap": "independent percentile bootstrap, 4000 resamples; do not interpret as paired",
        "limitations": ["synthetic toy environment", "hand-coded policies", "held-out cue inversion only", "proxy metrics do not establish morality or consciousness"],
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    (OUT / "family_summary.json").write_text(json.dumps(family_summary, indent=2), encoding="utf-8")
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(json.dumps({"metadata": metadata, "summary": summary, "family_summary": family_summary}, indent=2))

if __name__ == "__main__":
    main()
