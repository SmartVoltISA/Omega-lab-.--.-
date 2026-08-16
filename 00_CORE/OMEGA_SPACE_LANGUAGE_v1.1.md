# Ω-Space Language v1.1

## Extension: relation, information, quantity

SPACE messages must represent not only *what* is said, but how entities are connected, how much information is involved, and how many entities/events/relations are involved.

### 1. Relation is first-class

A semantic statement is not merely `subject -> value`. It is a typed relation with context:

```text
SOURCE
RELATION
TARGET
RELATION_TYPE
DIRECTION
STRENGTH
SCOPE
TEMPORAL_CONTEXT
SPATIAL_CONTEXT
PROVENANCE
```

The relation itself is an addressable object and may have its own memory, evidence, uncertainty and history.

### 2. Information is first-class

Each message separates:

```text
CONTENT        what is represented
MEANING        what it means
SOURCE         where it came from
PROVENANCE     how it was produced/transformed
CONFIDENCE     confidence in the claim
UNCERTAINTY    what is not known
FRESHNESS      how current it is
IMPORTANCE     semantic importance
```

The receiver must be able to request the information behind a conclusion rather than receiving only the conclusion.

### 3. Quantity is first-class

Whenever quantity is meaningful, the language carries:

```text
VALUE
UNIT
COUNT
RANGE
MIN
MAX
PRECISION
RATE
DURATION
FREQUENCY
AGGREGATION
```

`COUNT` and `VALUE` must never be conflated. A message can say both "7 events" and "2.4 seconds average duration" without ambiguity.

### 4. Cardinality and multiplicity

SPACE must represent:

- one-to-one;
- one-to-many;
- many-to-one;
- many-to-many;
- zero-or-more;
- exactly N;
- at-least N;
- at-most N.

This is necessary for groups, family spaces, sensor fusion, graph structures, memory clusters and SPACE-to-SPACE communication.

### 5. Graph-native meaning

A semantic message may contain a compact graph fragment:

```text
NODE A
  --RELATION--> NODE B
  --RELATION--> NODE C

CARDINALITY: 1:N
COUNT: 2
PROVENANCE: ...
UNCERTAINTY: ...
```

Existing graph nodes should normally be referenced rather than copied. Only the required delta is transmitted.

### 6. Semantic compression rule

The language should minimize transmitted resources without removing meaning:

```text
KNOWN NODE + KNOWN RELATION + DELTA
```

is preferred to transmitting the complete object again.

If the receiver lacks required context, it may request the missing relation, evidence or information explicitly.

### 7. Integrity rule

A compressed message must remain reconstructible enough for the receiver to distinguish:

```text
fact
inference
hypothesis
measurement
request
recommendation
decision
execution result
```

No compression is allowed to silently change one class into another.

### 8. Context and place

Meaning may depend on place. `PLACE` therefore remains first-class and may identify:

- graph location;
- organ/location inside SPACE;
- physical location;
- group/context;
- temporal position;
- task/workspace.

### 9. Feedback

Every consequential interaction may link:

```text
MESSAGE → ACTION → RESULT → FEEDBACK → MEMORY → GRAPH UPDATE
```

The feedback carries quantity where measurable: latency, count, duration, resource consumption, error rate, confidence change or other relevant metrics.

## Core law v1.1

> **Meaning is carried by entities and their relations; information carries provenance and uncertainty; quantity carries magnitude and cardinality; Memory preserves the history; Guardian controls authority.**

External research supports the use of entity-relation structures for semantic communication and shows that provenance, certainty and source metadata are important parts of machine-interpretable knowledge. These concepts are incorporated here without treating external standards as the SPACE language itself. citeturn0search0turn0search1turn0search7
