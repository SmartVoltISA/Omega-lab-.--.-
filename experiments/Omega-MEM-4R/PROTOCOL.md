# Ω-MEM-4R Protocol

**Fixed before execution:** 2026-08-10  
**Hypothesis:** H-MEM-2.2  
**Question:** При одинаковой эффективной ёмкости памяти действительно ли структурно соответствующая архитектура имеет преимущество над структурно несоответствующей?

## Parameters

- sequence length: 2000
- burn-in: 100
- train: 1000
- test: 1000
- seeds: 30, range 0–29
- S sweep: 2, 4, 8, 16, 32, 64
- intervention step: 500
- permutation trials: 100
- random ensemble: 10 independent FSMs

## Processes

P1 Periodic-4; P2 true second-order Markov process; P3 Thue-Morse; P4 two-state HMM; P5 iid binary random control.

## Architectures

Baseline; Context-1; Context-2; Context-3; Counter; Random; Matched.

Context-2 and Context-3 are shift registers. Random uses independent FSMs. Matched is process-specific and must be interpreted as an implementation, not as a universal definition of structural correspondence.

## Metrics

- test prediction accuracy;
- conditional entropy H(X_next | state);
- reachable states;
- effective training states;
- intervention accuracy drop;
- recovery at horizons 1, 2, 4, 8, 16, 32, 64, 128;
- state→prediction permutation contrast;
- per-seed accuracy values.

## Success criteria

1. Matched > Mismatched at equal S for structured processes.
2. Context-k should improve when additional context is genuinely predictive.
3. Random ensemble mean should be below Matched at equal S where structural matching is informative.
4. Random-iid should remain at baseline.

## Failure criteria

- Matched ≤ Mismatched;
- Random ≥ Matched at equal S;
- advantage on Random-iid;
- permutation fails to remove predictive mapping advantage.

## Validation performed before execution

Context-2 state trace was explicitly checked on `X Y X X Y` and reached all four intended states. Context-3 trace was checked on the same sequence. Equal-capacity construction was checked for Matched P1 S=4 versus Counter S=4.

## Protocol limitations

P1 Matched uses a phase counter and therefore enforces S≥4 internally. The S=2 P1 Matched result must not be interpreted as a valid equal-S comparison. This exception is explicitly recorded rather than hidden.

## Interpretation rule

A predictive result is not automatically a causal-memory result. Intervention is required for causal claims. A matched architecture that fails is evidence about that implementation and its capacity, not proof that structural correspondence is irrelevant in general.
