from space.core.semantic_codec import Quantity, Relation, SemanticMessage, decode, encode


def test_round_trip_preserves_relations_information_and_quantity():
    original = SemanticMessage(
        message_id="M1",
        kind="measurement",
        meaning="two sensors observed movement",
        relations=(
            Relation(
                source="sensor:imu",
                relation_type="supports",
                target="event:movement",
                place="body/phone",
            ),
        ),
        quantities=(
            Quantity(value=2, unit="events", count=2, duration=1.5),
        ),
        source="sensor-fusion",
        provenance=("sensor:imu", "sensor:gyro"),
        confidence=0.91,
        uncertainty=0.09,
        place="phone",
        reference="event:movement",
        delta={"state": "moving"},
    )

    restored = decode(encode(original))

    assert restored.relations == original.relations
    assert restored.quantities == original.quantities
    assert restored.provenance == original.provenance
    assert restored.uncertainty == original.uncertainty
    assert restored.delta == original.delta


def test_count_is_not_value():
    message = SemanticMessage(
        message_id="M2",
        kind="measurement",
        meaning="average duration",
        quantities=(Quantity(value=2.4, unit="seconds", count=7),),
    )
    restored = decode(encode(message))
    quantity = restored.quantities[0]
    assert quantity.value == 2.4
    assert quantity.count == 7
    assert quantity.value != quantity.count


def test_invalid_kind_is_rejected():
    message = SemanticMessage(message_id="M3", kind="command", meaning="execute")
    try:
        encode(message)
    except ValueError:
        return
    raise AssertionError("unknown semantic kind must be rejected")
