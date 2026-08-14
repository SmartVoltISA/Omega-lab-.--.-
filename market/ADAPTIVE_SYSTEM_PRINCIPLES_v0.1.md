# Ω-MARKET — ADAPTIVE SYSTEM PRINCIPLES v0.1

**Date:** 2026-08-14
**Status:** architecture principle / working specification

## 1. Core analogy

The market is treated as a **living river**.

Its channel, flow, slope, obstacles, pressure and turbulence change over time. A system designed to operate in that environment must adapt to the current river rather than force one permanent strategy onto every regime.

The trading system is therefore treated as a **living adaptive system**, not as one universal indicator or one immutable strategy.

## 2. Wheel / gear principle

A single strategy or indicator is only a **wheel / gear** inside the larger machine.

A gear can work correctly and still fail to produce a working vehicle if the surrounding system is absent or the operating conditions have changed.

Therefore:

> Never evaluate an isolated tool as if it were the whole system.

Each tool must have:
- a purpose;
- activation conditions;
- invalidation conditions;
- compatible market states;
- expected behavior;
- measured performance;
- failure modes;
- a place in the larger architecture.

## 3. Adaptive operating loop

```text
MARKET
  ↓
STATE ESTIMATION
  ↓
REGIME / TERRAIN IDENTIFICATION
  ↓
TRANSITION DETECTION
  ↓
SELECT APPROPRIATE TOOL / MODULE
  ↓
CHECK MODULE CONDITIONS
  ↓
SIGNAL or WAIT
  ↓
RISK / MONEY MANAGEMENT
  ↓
OUTCOME
  ↓
ERROR / SUCCESS ANALYSIS
  ↓
FEEDBACK
  ↓
UPDATED STATE ESTIMATION
```

## 4. River navigation principle

The system should generally move **with the market flow**.

Going against the flow is allowed only under specifically detected conditions where the expected advantage compensates for the additional risk and resource consumption.

Analogy:
- current direction = dominant market direction;
- channel = structural constraints / support-resistance context;
- slope = directional pressure;
- turbulence = volatility;
- obstacles = liquidity zones / trapped positions / abrupt events;
- depth = available liquidity;
- speed = rate of price displacement;
- eddies = countertrend rotations;
- waterfall = high-energy transition / liquidation event.

The system must therefore ask:

> What kind of river are we currently in, and which maneuver is appropriate here?

Not:

> Which single indicator should always be used?

## 5. Tool selection

Candidate modules include:

- trend / structure module;
- impulse module;
- compression / breakout module;
- balance / range module;
- OI pressure module;
- funding / crowding module;
- liquidation / squeeze module;
- volume / taker-flow module;
- multi-timeframe alignment module;
- reversal / absorption module;
- correlation / external-market module;
- volatility regime module.

A module is activated only when its conditions match the detected market state.

## 6. Transition detection

Transitions are first-class objects in the system.

Examples:

```text
balance → expansion
expansion → continuation
expansion → absorption
absorption → reversal
trend → compression
compression → breakout
crowding → liquidation
```

The system must detect not only the current state, but also the **direction and speed of state change**.

## 7. Universal tool principle

A useful tool should be reusable across different market conditions, but its **mode of operation may change with the regime**.

The analogy is a paddle:
- left/right stroke;
- acceleration/deceleration;
- steering;
- braking;
- maneuvering around obstacles.

The objective is not to find one perfect paddle stroke. The objective is to build a tool that can be used appropriately under changing conditions.

## 8. Testing discipline

The working cycle is intentionally short:

```text
IDEA
 ↓
IMPLEMENT
 ↓
RUN
 ↓
MEASURE
 ↓
COMPARE
 ↓
RECORD
 ↓
KEEP / MODIFY / ARCHIVE
 ↓
NEXT TEST
```

Do not spend excessive time refining an untested idea.

A failed experiment is a useful result if its failure mode is recorded.

## 9. Result categories

Every tested component receives one of these statuses:

- **PASS** — demonstrated useful advantage under defined conditions;
- **CONDITIONAL** — works only in identified regimes;
- **FILTER** — useful for confirming/rejecting another signal, but insufficient alone;
- **FAIL** — no useful advantage under tested conditions;
- **UNKNOWN** — insufficient data or unresolved mechanism;
- **REWORK** — promising but requires modification;
- **ARCHIVE** — retained for historical comparison but not active.

## 10. Error analysis

For every failed prediction, record:

1. what the system predicted;
2. what actually happened;
3. which state was detected;
4. whether the state classification was wrong;
5. whether the selected tool was wrong;
6. whether activation conditions were incomplete;
7. whether a transition was missed;
8. whether the market changed regime during the prediction horizon;
9. whether risk management should have prevented activation.

For every successful prediction, record the same information to determine **why it worked**, not merely that it worked.

## 11. No permanent loyalty to a strategy

A strategy is not protected because it worked previously.

If the river changes and the strategy loses its advantage, the system must be able to:

```text
DETECT CHANGE
   ↓
REDUCE / DISABLE MODULE
   ↓
SELECT ANOTHER MODULE
   ↓
RETEST
```

## 12. Research philosophy

The project is not trying to prove that one indicator, one formula or one market law explains everything.

The objective is to construct a practical adaptive architecture through repeated empirical testing.

The final system must be capable of saying:

> **This is the current state. These are the available tools. These conditions are satisfied. This module has historically worked here. This module has failed here. Therefore act / wait / reduce risk.**

## 13. Connection to Ω-Lab

The MARKET architecture follows the same working discipline as Ω-Lab:

**node → relation → graph → state → transition → experiment → result → memory → feedback.**

The market project applies that methodology to a changing external system.

## 14. Operational rule

Do not ask repeatedly for permission to test an obvious next hypothesis.

When an idea is sufficiently defined:

**test it → record it → compare it → continue.**

Escalate to the user only when a decision genuinely requires human judgment, resources, risk acceptance, or interpretation beyond the available data.
