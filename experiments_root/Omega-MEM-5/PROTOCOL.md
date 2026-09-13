# Ω-MEM-5 Protocol

**Status:** FIXED BEFORE EXECUTION  
**Question:** Does functional memory change the predictive partition of future transitions beyond raw memory capacity?

## 1. Primary hypothesis

For equal memory capacity and equal current observable state, histories encoded differently by memory can produce different sets/distributions of predictable next transitions.

Formal target:

`C(S,M1) != C(S,M2)`

with a corresponding measurable prediction difference.

## 2. Experimental design

Use controlled generators for which the predictive structure is known:

- Periodic-4;
- true Markov-2;
- Thue-Morse with a correct position/carry representation;
- two-state HMM;
- iid binary random control.

Each generator must have at least two histories that can converge to the same externally observed current symbol/state while retaining different internal predictive contexts.

## 3. Memory architectures

At minimum:

1. **No-memory baseline** — current observation only.
2. **State-memory** — stores a defined recent/internal state.
3. **Relation-memory** — stores the transition/context relation required by the generator.
4. **Mismatched memory** — same state budget but deliberately preserves an irrelevant distinction.
5. **Random FSM control** — same state budget, independently sampled transitions.

All architectures must actually use the requested state budget. No silent overwriting of `S` is permitted.

## 4. Capacity control

Sweep:

`S = 2, 4, 8, 16, 32, 64`

where meaningful.

For every primary comparison:

- same S;
- same sequence length;
- same train/test split;
- same number of seeds;
- same input alphabet;
- same parameter/state-transition accounting.

Random controls must use multiple independent FSMs per condition.

## 5. Measurements

### Primary

- next-transition prediction accuracy;
- conditional entropy `H(X_next | S,M)`;
- number of distinct next transitions observed from each memory state;
- predictive partition size;
- predictive partition entropy.

### Secondary

- reachable memory states;
- effective memory-state entropy;
- history-convergence cases where the same current observation is reached by different histories;
- divergence of future transition distributions after convergence;
- recovery after controlled memory intervention;
- per-seed paired differences;
- 95% confidence intervals.

## 6. Critical test

Construct matched pairs:

`H1 → S`  
`H2 → S`

where current external state `S` is the same but historical context differs.

Measure:

`P(X_next | S,M1)` versus `P(X_next | S,M2)`.

If the distributions differ reliably and the difference disappears when memory is destroyed, this is evidence that retained history changes the predictive partition.

## 7. Intervention

Intervene on memory only, without changing the current external observation.

Required measurements:

- immediate internal-state divergence;
- immediate next-transition distribution divergence;
- cumulative prediction loss;
- recovery time;
- repeated non-equivalent reset states.

A permutation test alone is not accepted as causal evidence.

## 8. Falsification

The hypothesis fails for a tested generator if, under valid equal-capacity control:

- history-specific memory states do not change the predictive distribution;
- destroying relevant memory does not change future prediction;
- predictive partition metrics provide no improvement beyond raw capacity;
- mismatched memory performs equivalently across all controlled cases.

A failure in one implementation is not a universal falsification. The implementation and structural correspondence must be audited.

## 9. Data integrity

Before interpretation, archive:

- executable code;
- fixed protocol;
- exact generator definitions;
- full per-seed raw data;
- machine-readable results;
- analysis script;
- plots;
- audit notes.

No post-hoc architecture changes are allowed after execution.

## 10. Interpretation rule

A positive result establishes only that the tested memory representation carries predictive information under the tested generator and controls.

It does not establish a universal law about memory, information, energy, physical reality, agency, or consciousness.
