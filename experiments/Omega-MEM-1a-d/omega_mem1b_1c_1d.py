# Ω-MEM-1b–1d: STRICT CAUSAL INTERVENTION, SIZE vs STRUCTURE, MINIMALITY
# Archived raw experimental code/results exactly as supplied in the research log.

# NOTE: This file preserves the supplied experimental implementation and output.
# It is an archival record, not a validated final analysis.

# ============================================================
# Ω-MEM-1b: STRICT CAUSAL INTERVENTION
# ============================================================
# One identical history; two trajectories; reset state=0 at step 5.
# The supplied implementation uses StructuredMemoryMachine and strict_intervention
# defined in the Ω-MEM-1a source file.

print("Ω-MEM-1b: STRICT CAUSAL INTERVENTION")

test_history_b = ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'X']
reset_step_b = 5

strict_results = {}
for S in PARAMS['sizes']:
    machine = StructuredMemoryMachine(S)
    result = strict_intervention(machine, test_history_b, reset_step_b)
    strict_results[S] = result
    print(f"M{S if S>1 else 0}: diff={result['diff']}/{result['total']}, "
          f"first_diff={result['first_diff']}, reconverge={result['reconverge']}, "
          f"state_at_reset={result['state_at_reset_A']}")

# ============================================================
# Ω-MEM-1c: SIZE vs STRUCTURE
# ============================================================
size_vs_structure = {}
for S in PARAMS['sizes']:
    if S == 1:
        continue
    struct_successes, rand_successes = [], []
    struct_diffs, rand_diffs = [], []
    for seed in PARAMS['seed_range']:
        history = generate_history(PARAMS['history_length'], seed)
        machine_s = StructuredMemoryMachine(S)
        res_s = strict_intervention(machine_s, history, PARAMS['intervention_step'])
        struct_successes.append(1 if res_s['diff'] > 0 else 0)
        struct_diffs.append(res_s['diff'])
        machine_r = RandomMemoryMachine(S, seed=S*1000 + seed)
        res_r = strict_intervention(machine_r, history, PARAMS['intervention_step'])
        rand_successes.append(1 if res_r['diff'] > 0 else 0)
        rand_diffs.append(res_r['diff'])
    size_vs_structure[S] = {
        'struct_success': np.mean(struct_successes),
        'rand_success': np.mean(rand_successes),
        'struct_diff_mean': np.mean(struct_diffs),
        'rand_diff_mean': np.mean(rand_diffs),
        'struct_diff_std': np.std(struct_diffs),
        'rand_diff_std': np.std(rand_diffs),
    }
    print(f"M{S}: Structured success={size_vs_structure[S]['struct_success']:.2%}, "
          f"Random success={size_vs_structure[S]['rand_success']:.2%}")

# ============================================================
# Ω-MEM-1d: MINIMALITY
# ============================================================
m1 = StructuredMemoryMachine(1)
print("S=1: only state 0; reset is identity.")
print("next_state(0,X)=", m1.next_state[(0,'X')])
print("next_state(0,Y)=", m1.next_state[(0,'Y')])

m2 = StructuredMemoryMachine(2)
for s in [0,1]:
    for inp in ['X','Y']:
        ns, out = m2.step(s, inp)
        print(f"({s},{inp}) -> state={ns}, output={out}")

s_after = 0
for inp in ['X','Y','Y']:
    s_after, _ = m2.step(s_after, inp)
_, out_no_reset = m2.step(s_after, 'X')
_, out_with_reset = m2.step(0, 'X')
print("Minimal counterexample:", out_no_reset, out_with_reset,
      "differ=", out_no_reset != out_with_reset)

# SUPPLIED OUTPUT SUMMARY
# M0: 0% causal effect.
# M2/M4/M8/M16: 54% repeatability; mean Δ=5.40/10.
# Strict intervention fixed history: M0 0/10; M2–M16 10/10.
# Size vs structure: M2 random 32%, M4 61%, M8 81%, M16 89%; structured 54%.
# Minimality: S=1 impossible in this architecture; S=2 possible.
