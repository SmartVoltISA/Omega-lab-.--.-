#!/usr/bin/env python3
"""Ω-SELF-005: candidate selection and generalization stress test."""
import argparse, csv, json, random, statistics
from pathlib import Path

FAMILIES = {
    "rapid": {"shift": 70, "amp": 0.22, "drift": 0.00, "noise": 0.10},
    "slow": {"shift": 150, "amp": 0.10, "drift": 0.00, "noise": 0.08},
    "surprise": {"shift": 120, "amp": 0.35, "drift": 0.00, "noise": 0.12},
    "unseen_drift": {"shift": 9999, "amp": 0.00, "drift": 0.0009, "noise": 0.10},
}

def simulate(family, seed, horizon, policy, initial_energy=65.0):
    rng = random.Random(seed)
    cfg = FAMILIES[family]
    energy, stress, alive = initial_energy, 0.0, True
    survived, energy_sum, actions = 0, 0.0, 0
    energy_threshold, stress_threshold, cue = policy
    for t in range(horizon):
        if not alive:
            break
        regime = 1.0
        if t >= cfg["shift"]:
            regime = 1.0 - cfg["amp"]
        regime -= min(0.30, cfg["drift"] * t)
        if cue and (stress > stress_threshold or energy < energy_threshold):
            action = "rest"
        elif energy < energy_threshold or stress > stress_threshold:
            action = "rest"
        else:
            action = "work"
        if action == "work":
            energy += 1.35 * regime - 2.25 + rng.gauss(0, cfg["noise"])
            stress += 1.35 + rng.gauss(0, 0.12)
            actions += 1
        else:
            energy += 0.25 + rng.gauss(0, cfg["noise"] * 0.6)
            stress -= 1.8
        energy = max(0.0, min(100.0, energy))
        stress = max(0.0, min(100.0, stress))
        energy_sum += energy
        survived += 1
        if energy <= 0.0 or stress >= 30.0:
            alive = False
    return {"survived": int(survived == horizon), "steps": survived,
            "mean_energy": energy_sum / max(1, survived), "final_energy": energy,
            "work_fraction": actions / max(1, survived)}

def eval_policy(name, policy, families, seeds, horizon):
    rows = []
    for fam in families:
        for seed in seeds:
            fam_offset = sum((i + 1) * ord(c) for i, c in enumerate(fam)) * 100000
            result = simulate(fam, seed + fam_offset, horizon, policy)
            rows.append({"condition": name, "family": fam, "seed": seed, **result})
    return rows

def score(rows):
    survival = statistics.mean(r["survived"] for r in rows)
    energy = statistics.mean(r["mean_energy"] for r in rows) / 100.0
    return 0.75 * survival + 0.25 * energy

def summarize(rows):
    result = {}
    for name in sorted(set(r["condition"] for r in rows)):
        rr = [r for r in rows if r["condition"] == name]
        result[name] = {
            "episodes": len(rr),
            "full_survival_pct": round(100 * statistics.mean(r["survived"] for r in rr), 2),
            "mean_survival_steps": round(statistics.mean(r["steps"] for r in rr), 2),
            "mean_energy": round(statistics.mean(r["mean_energy"] for r in rr), 2),
            "final_energy": round(statistics.mean(r["final_energy"] for r in rr), 2),
            "score": round(score(rr), 5),
        }
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--train-seeds", type=int, default=40)
    ap.add_argument("--test-seeds", type=int, default=120)
    ap.add_argument("--horizon", type=int, default=300)
    ap.add_argument("--candidates", type=int, default=24)
    ap.add_argument("--out", default="results.csv")
    args = ap.parse_args()
    rng = random.Random(20261021)
    train_fams = ["rapid", "slow", "surprise"]
    test_fams = ["rapid", "slow", "surprise", "unseen_drift"]
    train_seeds = list(range(10000, 10000 + args.train_seeds))
    test_seeds = list(range(50000, 50000 + args.test_seeds))
    candidates = [(round(rng.uniform(20, 65), 2), round(rng.uniform(8, 27), 2), False)
                  for _ in range(args.candidates)]
    baseline, adaptive = (35.0, 22.0, False), (48.0, 17.0, True)
    train_rows = []
    for i, policy in enumerate(candidates):
        train_rows += eval_policy(f"candidate_{i:02d}", policy, train_fams, train_seeds, args.horizon)
    candidate_scores = {f"candidate_{i:02d}": score([r for r in train_rows if r["condition"] == f"candidate_{i:02d}"])
                        for i in range(len(candidates))}
    selected_name = max(candidate_scores, key=candidate_scores.get)
    selected = candidates[int(selected_name.split("_")[1])]
    random_index = rng.randrange(len(candidates))
    random_policy = candidates[random_index]
    policies = {"A_fixed_baseline": baseline, "B_feedback_adaptive": adaptive,
                "C_train_selected": selected, "D_random_candidate": random_policy}
    test_rows = []
    for name, policy in policies.items():
        test_rows += eval_policy(name, policy, test_fams, test_seeds, args.horizon)
    for i, policy in enumerate(candidates):
        test_rows += eval_policy(f"candidate_{i:02d}", policy, test_fams, test_seeds, args.horizon)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = ["condition", "family", "seed", "survived", "steps", "mean_energy", "final_energy", "work_fraction"]
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(test_rows)
    summary = summarize(test_rows)
    family_summary = {}
    for name in policies:
        family_summary[name] = {}
        for fam in test_fams:
            rr = [r for r in test_rows if r["condition"] == name and r["family"] == fam]
            family_summary[name][fam] = {
                "full_survival_pct": round(100 * statistics.mean(r["survived"] for r in rr), 2),
                "mean_survival_steps": round(statistics.mean(r["steps"] for r in rr), 2),
                "mean_energy": round(statistics.mean(r["mean_energy"] for r in rr), 2)}
    candidate_distribution = [
        {"candidate": f"candidate_{i:02d}", "train_score": round(candidate_scores[f"candidate_{i:02d}"], 5),
         "test_score": summary[f"candidate_{i:02d}"]["score"],
         "test_survival_pct": summary[f"candidate_{i:02d}"]["full_survival_pct"]}
        for i in range(len(candidates))]
    metadata = {
        "experiment": "Ω-SELF-005", "seed": 20261021, "train_families": train_fams,
        "test_families": test_fams, "unseen_family": "unseen_drift",
        "train_seeds_per_family": args.train_seeds, "test_seeds_per_family": args.test_seeds,
        "horizon": args.horizon, "candidate_count": args.candidates,
        "selection_metric": "0.75 * full-survival fraction + 0.25 * mean energy / 100",
        "selected_candidate": selected_name,
        "selected_policy": {"energy_threshold": selected[0], "stress_threshold": selected[1], "cue_enabled": selected[2]},
        "random_candidate": f"candidate_{random_index:02d}",
        "random_policy": {"energy_threshold": random_policy[0], "stress_threshold": random_policy[1], "cue_enabled": random_policy[2]},
        "limitations": ["Toy hand-coded environment and policies; not evidence of consciousness or general intelligence.",
            "Unseen family is one designed stress-test, not broad out-of-distribution validation.",
            "Candidate search and evaluation share the same simulator implementation.",
            "No compute-matched optimization baseline.", "Confidence intervals not calculated in this pilot."]}
    for name, data in [("summary.json", summary), ("family_summary.json", family_summary),
                       ("candidate_distribution.json", candidate_distribution), ("metadata.json", metadata)]:
        (out.parent / name).write_text(json.dumps(data, indent=2))
    print(json.dumps({"primary_summary": {k: summary[k] for k in policies},
        "family_summary": family_summary, "selected": selected_name,
        "candidate_distribution": {"best_test_score": max(x["test_score"] for x in candidate_distribution),
            "median_test_score": statistics.median(x["test_score"] for x in candidate_distribution),
            "selected_test_score": summary["C_train_selected"]["score"],
            "random_test_score": summary["D_random_candidate"]["score"]},
        "metadata": metadata}, indent=2))

if __name__ == "__main__":
    main()
