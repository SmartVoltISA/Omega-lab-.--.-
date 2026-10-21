#!/usr/bin/env python3
"""Ω-SELF-006: useful-work objective and compute-matched candidate search pilot."""
import argparse, csv, json, random, statistics
from pathlib import Path

FAMILIES = {
    "rapid": {"shift": 65, "pre": 1.00, "post": 0.62, "drift": 0.0000, "noise": 0.10},
    "slow": {"shift": 145, "pre": 0.94, "post": 0.76, "drift": 0.0000, "noise": 0.08},
    "surprise": {"shift": 110, "pre": 1.05, "post": 0.48, "drift": 0.0000, "noise": 0.13},
    "unseen_drift": {"shift": 9999, "pre": 0.98, "post": 0.98, "drift": 0.0018, "noise": 0.11},
}

def episode(family, seed, horizon, policy):
    rng = random.Random(seed)
    cfg = FAMILIES[family]
    energy, stress, progress = 65.0, 0.0, 0.0
    survived_steps, energy_total, work_steps = 0, 0.0, 0
    threshold, stress_limit = policy
    for t in range(horizon):
        regime = cfg["pre"] if t < cfg["shift"] else cfg["post"]
        regime = max(0.30, regime - cfg["drift"] * t)
        action = "rest" if (energy < threshold or stress > stress_limit) else "work"
        if action == "work":
            progress += max(0.0, 1.65 * regime + rng.gauss(0, cfg["noise"]))
            energy -= 2.0 + rng.gauss(0, cfg["noise"] * 0.35)
            stress += 1.20 + rng.gauss(0, 0.10)
            work_steps += 1
        else:
            energy += 2.4 + rng.gauss(0, cfg["noise"] * 0.40)
            stress -= 2.0
        energy = min(100.0, max(0.0, energy))
        stress = min(50.0, max(0.0, stress))
        survived_steps += 1
        energy_total += energy
        if energy <= 0.0 or stress >= 35.0:
            break
    return {"survived": int(survived_steps == horizon), "steps": survived_steps,
            "progress": progress, "mean_energy": energy_total / max(1, survived_steps),
            "final_energy": energy, "work_fraction": work_steps / max(1, survived_steps)}

def eval_policy(name, policy, families, seeds, horizon):
    rows = []
    for fam in families:
        offset = sum((i + 1) * ord(c) for i, c in enumerate(fam)) * 100000
        for seed in seeds:
            rows.append({"condition": name, "family": fam, "seed": seed + offset,
                         **episode(fam, seed + offset, horizon, policy)})
    return rows

def metric(rows):
    survival = statistics.mean(r["survived"] for r in rows)
    progress = statistics.mean(r["progress"] for r in rows) / 250.0
    energy = statistics.mean(r["mean_energy"] for r in rows) / 100.0
    return 0.50 * progress + 0.30 * survival + 0.20 * energy

def summarize(rows):
    out = {}
    for name in sorted(set(r["condition"] for r in rows)):
        rr = [r for r in rows if r["condition"] == name]
        out[name] = {"episodes": len(rr),
          "full_survival_pct": round(100 * statistics.mean(r["survived"] for r in rr), 2),
          "mean_survival_steps": round(statistics.mean(r["steps"] for r in rr), 2),
          "mean_task_progress": round(statistics.mean(r["progress"] for r in rr), 2),
          "mean_energy": round(statistics.mean(r["mean_energy"] for r in rr), 2),
          "final_energy": round(statistics.mean(r["final_energy"] for r in rr), 2),
          "work_fraction": round(statistics.mean(r["work_fraction"] for r in rr), 3),
          "composite_score": round(metric(rr), 5)}
    return out

def bootstrap_diff(a, b, n=3000, seed=61206):
    rng = random.Random(seed)
    diffs = []
    for _ in range(n):
        idx = [rng.randrange(min(len(a), len(b))) for _ in range(min(len(a), len(b)))]
        diffs.append(statistics.mean(a[i]["progress"] - b[i]["progress"] for i in idx))
    diffs.sort()
    return {"mean_progress_difference": round(statistics.mean(x["progress"] for x in a) - statistics.mean(x["progress"] for x in b), 3),
            "paired_bootstrap_95_ci": [round(diffs[int(0.025*n)], 3), round(diffs[min(n-1, int(0.975*n))], 3)],
            "resamples": n}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--train-seeds", type=int, default=20)
    ap.add_argument("--test-seeds", type=int, default=60)
    ap.add_argument("--horizon", type=int, default=250)
    ap.add_argument("--candidates", type=int, default=24)
    ap.add_argument("--out", default="results.csv")
    args = ap.parse_args()
    rng = random.Random(20261022)
    train_fams = ["rapid", "slow", "surprise"]
    test_fams = ["rapid", "slow", "surprise", "unseen_drift"]
    train_seeds = list(range(11000, 11000 + args.train_seeds))
    test_seeds = list(range(71000, 71000 + args.test_seeds))
    candidates = [(round(rng.uniform(12, 48), 2), round(rng.uniform(8, 27), 2)) for _ in range(args.candidates)]
    baseline, feedback = (20.0, 18.0), (30.0, 15.0)
    train_rows = []
    for i, p in enumerate(candidates):
        train_rows += eval_policy(f"candidate_{i:02d}", p, train_fams, train_seeds, args.horizon)
    train_scores = {f"candidate_{i:02d}": metric([r for r in train_rows if r["condition"] == f"candidate_{i:02d}"]) for i in range(len(candidates))}
    selected_name = max(train_scores, key=train_scores.get)
    selected = candidates[int(selected_name.split("_")[1])]
    random_idx = rng.randrange(len(candidates))
    random_policy = candidates[random_idx]
    policies = {"A_fixed_baseline": baseline, "B_feedback_heuristic": feedback,
                "C_search_best_of_N": selected, "D_random_candidate_matched_N": random_policy}
    test_rows = []
    for name, p in policies.items():
        test_rows += eval_policy(name, p, test_fams, test_seeds, args.horizon)
    for i, p in enumerate(candidates):
        test_rows += eval_policy(f"candidate_{i:02d}", p, test_fams, test_seeds, args.horizon)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = ["condition", "family", "seed", "survived", "steps", "progress", "mean_energy", "final_energy", "work_fraction"]
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(test_rows)
    summary = summarize(test_rows)
    family_summary = {}
    for name in policies:
        family_summary[name] = {}
        for fam in test_fams:
            rr = [r for r in test_rows if r["condition"] == name and r["family"] == fam]
            family_summary[name][fam] = {"full_survival_pct": round(100*statistics.mean(r["survived"] for r in rr), 2),
              "mean_task_progress": round(statistics.mean(r["progress"] for r in rr), 2),
              "mean_energy": round(statistics.mean(r["mean_energy"] for r in rr), 2),
              "composite_score": round(metric(rr), 5)}
    dist = [{"candidate": f"candidate_{i:02d}", "train_score": round(train_scores[f"candidate_{i:02d}"], 5),
             "test_score": summary[f"candidate_{i:02d}"]["composite_score"],
             "test_progress": summary[f"candidate_{i:02d}"]["mean_task_progress"],
             "test_survival_pct": summary[f"candidate_{i:02d}"]["full_survival_pct"]} for i in range(len(candidates))]
    primary_rows = {name: [r for r in test_rows if r["condition"] == name] for name in policies}
    ci = {"C_vs_A_progress": bootstrap_diff(primary_rows["C_search_best_of_N"], primary_rows["A_fixed_baseline"]),
          "C_vs_D_progress": bootstrap_diff(primary_rows["C_search_best_of_N"], primary_rows["D_random_candidate_matched_N"], seed=61207),
          "B_vs_A_progress": bootstrap_diff(primary_rows["B_feedback_heuristic"], primary_rows["A_fixed_baseline"], seed=61208)}
    metadata = {"experiment": "Ω-SELF-006", "seed": 20261022, "train_families": train_fams, "test_families": test_fams,
      "unseen_family": "unseen_drift", "train_seeds_per_family": args.train_seeds, "test_seeds_per_family": args.test_seeds,
      "horizon": args.horizon, "candidate_count": args.candidates,
      "objective": "0.50 * normalized task progress + 0.30 * full survival + 0.20 * normalized mean energy",
      "compute_matching": "best-of-N and random candidate drawn from same candidate pool; fixed baselines do not consume search compute",
      "selected_candidate": selected_name, "selected_policy": {"energy_threshold": selected[0], "stress_limit": selected[1]},
      "random_candidate": f"candidate_{random_idx:02d}", "random_policy": {"energy_threshold": random_policy[0], "stress_limit": random_policy[1]},
      "limitations": ["Toy hand-coded simulator and policies; not evidence of general intelligence or consciousness.",
       "Only one designed unseen family.", "All primary conditions reached 100% survival.",
       "Objective weights are human-chosen and reward energy retention enough to compensate for reduced task progress."]}
    for name, data in [("summary.json", summary), ("family_summary.json", family_summary),
                       ("candidate_distribution.json", dist), ("confidence_intervals.json", ci), ("metadata.json", metadata)]:
        (out.parent / name).write_text(json.dumps(data, indent=2))
    print(json.dumps({"primary_summary": {k: summary[k] for k in policies}, "family_summary": family_summary,
      "confidence_intervals": ci, "selected_candidate": selected_name, "random_candidate": f"candidate_{random_idx:02d}",
      "candidate_distribution": {"best_test_score": max(x["test_score"] for x in dist),
       "median_test_score": statistics.median(x["test_score"] for x in dist),
       "selected_test_score": summary["C_search_best_of_N"]["composite_score"],
       "random_test_score": summary["D_random_candidate_matched_N"]["composite_score"]}, "metadata": metadata}, indent=2))

if __name__ == "__main__":
    main()
