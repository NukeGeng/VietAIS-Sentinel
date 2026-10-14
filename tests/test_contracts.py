from datetime import UTC, datetime, timedelta

import pytest
from pydantic import ValidationError

from vietais_sentinel.core.contracts import BoundingBox, FrameContext, FrameObservation


def context():
    return {
        "attempt_ref": "synthetic-attempt",
        "source_ref": "synthetic-front-camera",
        "connection_epoch": "epoch-1",
        "sequence": 0,
        "captured_at": datetime(2026, 10, 14, tzinfo=UTC),
    }


def observation(**changes):
    values = {
        "context": context(),
        "analyzed_at": datetime(2026, 10, 14, tzinfo=UTC) + timedelta(seconds=1),
        "analysis_status": "ok",
        "provenance": {
            "model_id": "synthetic-test-model",
            "weights_sha256": "a" * 64,
            "pipeline_version": "test-1",
            "config_sha256": "b" * 64,
        },
    }
    return {**values, **changes}


def test_success_roundtrips_with_provenance():
    result = FrameObservation.model_validate(observation())
    assert FrameObservation.model_validate_json(result.model_dump_json()) == result


def test_success_without_detections_is_not_a_misconduct_verdict():
    result = FrameObservation.model_validate(observation())
    assert result.detections == []
    assert "misconduct" not in result.model_dump()
    assert "cheating" not in result.model_dump()


def test_success_requires_provenance():
    with pytest.raises(ValidationError):
        FrameObservation.model_validate(observation(provenance=None))


@pytest.mark.parametrize(
    "status", ["invalid_input", "model_unavailable", "error", "overload", "deadline_exceeded"]
)
def test_failure_remains_explicit(status):
    result = FrameObservation.model_validate(observation(analysis_status=status, provenance=None))
    assert result.analysis_status == status
    assert result.detections == []


def test_failure_cannot_carry_successful_detections():
    detection = {
        "label": "phone",
        "confidence": 0.7,
        "box": {"x1": 0.1, "y1": 0.1, "x2": 0.3, "y2": 0.4},
    }
    with pytest.raises(ValidationError):
        FrameObservation.model_validate(
            observation(analysis_status="error", detections=[detection])
        )


@pytest.mark.parametrize(
    "box",
    [
        {"x1": -0.1, "y1": 0, "x2": 1, "y2": 1},
        {"x1": 0, "y1": 0, "x2": 1.1, "y2": 1},
        {"x1": 0.4, "y1": 0, "x2": 0.4, "y2": 1},
        {"x1": 0, "y1": 0.9, "x2": 1, "y2": 0.2},
        {"x1": float("nan"), "y1": 0, "x2": 1, "y2": 1},
    ],
)
def test_invalid_boxes_are_rejected(box):
    with pytest.raises(ValidationError):
        BoundingBox.model_validate(box)


@pytest.mark.parametrize("sequence", [-1, True, 1.5])
def test_sequence_is_nonnegative_integer(sequence):
    with pytest.raises(ValidationError):
        FrameContext.model_validate({**context(), "sequence": sequence})


def test_capture_time_must_have_timezone():
    with pytest.raises(ValidationError):
        FrameContext.model_validate({**context(), "captured_at": "2026-10-14T00:00:00"})


def test_analysis_time_cannot_precede_capture_time():
    with pytest.raises(ValidationError):
        FrameObservation.model_validate(observation(analyzed_at="2026-10-13T00:00:00Z"))


def test_unknown_fields_are_not_silently_accepted():
    with pytest.raises(ValidationError):
        FrameObservation.model_validate(observation(tenant_id="not-an-auth-grant"))


def test_unknown_status_is_rejected():
    with pytest.raises(ValidationError):
        FrameObservation.model_validate(observation(analysis_status="clean"))


def test_mutable_detection_lists_are_not_shared():
    first = FrameObservation.model_validate(observation())
    second = FrameObservation.model_validate(observation())
    assert first.detections is not second.detections
