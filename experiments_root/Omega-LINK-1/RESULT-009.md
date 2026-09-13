# Ω-LINK-1 — RESULT-009

**Status:** OBSERVED RESULT / controlled experimental construction
**Run:** #45
**Run ID:** 31783238279
**Commit:** de56968a38071b3c5917c167214a4627f53539ae
**Experiment:** DEEP-MEMORY-1

## History

### Before

RESULT-008 (MINIMAL-STATE-1) showed a construction in which one previous state was sufficient to remove next-step uncertainty. This raised a sharper question: can the required history depth itself be increased and measured?

### Experiment design

A controlled process was constructed so that the current state `B` alone is insufficient, and the last two states `(C,B)` are also insufficient. The distinguishing information appears only when a third state is included.

Representative histories:

- `A → C → B → A`
- `C → C → B → C`

Both histories share the same current state `B` and the same last-two-state suffix `C → B`, but have different next states.

### Execution

The experiment was executed by GitHub Actions as a real Python step:

`python experiments/Omega-LINK-1/deep_memory_link1.py > deep_memory_results.txt`

The workflow completed successfully. The result artifact was uploaded as `omega-link-1-results.zip` (artifact ID 9212481201).

### Result

Measured conditional next-state entropy:

- `H(next | current) = 1.0 bit`
- `H(next | last2) = 1.0 bit`
- `H(next | last3) = 0.0 bit`

Therefore, in this controlled construction:

`current` → insufficient

`last 2 states` → insufficient

`last 3 states` → sufficient

### Interpretation

The experiment demonstrates that the minimum sufficient history depth can be greater than one. Here the required depth is 2 previous steps, equivalently a 3-state observed window including the current state.

This supports treating memory depth as a measurable property of a transition process rather than as a binary yes/no attribute.

### Interpretation boundary

This does not establish that all systems possess finite memory depth, nor that memory is a separate fundamental entity. It establishes the behavior of the tested controlled construction and motivates systematic scaling tests.

## Research chain

`RESULT-007` → hidden history carries predictive information

`RESULT-008` → one-step history can be sufficient

`RESULT-009` → a construction can require deeper history

### Next question

Can the required memory depth be systematically scaled (1, 2, 3, ...), and does every tested process admit a finite minimal sufficient state representation?
