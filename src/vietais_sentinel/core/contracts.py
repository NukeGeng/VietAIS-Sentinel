"""Versioned observations, not misconduct verdicts or SaaS authorization."""

from enum import StrEnum
from typing import Annotated, Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, StringConstraints, model_validator

Reference = Annotated[str, StringConstraints(min_length=1, max_length=128, strip_whitespace=True)]
Digest = Annotated[str, StringConstraints(pattern=r"^[a-f0-9]{64}$")]
Probability = Annotated[float, Field(ge=0, le=1, allow_inf_nan=False)]


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class AnalysisStatus(StrEnum):
    OK = "ok"
    INVALID_INPUT = "invalid_input"
    MODEL_UNAVAILABLE = "model_unavailable"
    ERROR = "error"
    OVERLOAD = "overload"
    DEADLINE_EXCEEDED = "deadline_exceeded"


class FrameContext(StrictModel):
    """Opaque references; never proof of identity, tenant membership or authorization."""

    attempt_ref: Reference
    source_ref: Reference
    connection_epoch: Reference
    sequence: int = Field(ge=0, strict=True)
    captured_at: AwareDatetime


class BoundingBox(StrictModel):
    """Normalized coordinates in the original, unmirrored image coordinate system."""

    x1: Probability
    y1: Probability
    x2: Probability
    y2: Probability

    @model_validator(mode="after")
    def require_positive_area(self) -> "BoundingBox":
        if self.x2 <= self.x1 or self.y2 <= self.y1:
            raise ValueError("Bounding box must have positive width and height")
        return self


class Detection(StrictModel):
    label: Literal["phone", "person"]
    confidence: Probability
    box: BoundingBox


class ModelProvenance(StrictModel):
    model_id: Reference
    weights_sha256: Digest
    pipeline_version: Reference
    config_sha256: Digest


class FrameObservation(StrictModel):
    schema_version: Literal["1.0"] = "1.0"
    context: FrameContext
    analyzed_at: AwareDatetime
    analysis_status: AnalysisStatus
    detections: list[Detection] = Field(default_factory=list)
    provenance: ModelProvenance | None = None

    @model_validator(mode="after")
    def prevent_error_as_success(self) -> "FrameObservation":
        if self.analysis_status == AnalysisStatus.OK and self.provenance is None:
            raise ValueError("Successful analysis requires model and config provenance")
        if self.analysis_status != AnalysisStatus.OK and self.detections:
            raise ValueError("Failed analysis cannot publish detections as successful observations")
        if self.analyzed_at < self.context.captured_at:
            raise ValueError("Analysis time cannot precede the normalized capture time")
        return self
