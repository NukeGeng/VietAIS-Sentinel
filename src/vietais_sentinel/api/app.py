"""Bootstrap API. No model download, fake inference, or SaaS dependencies."""

from fastapi import FastAPI, status
from pydantic import BaseModel, ConfigDict

from vietais_sentinel import __version__


class Capabilities(BaseModel):
    model_config = ConfigDict(extra="forbid")

    api_version: str = "v1"
    engine_version: str = __version__
    stage: str = "foundation"
    object_detection: bool = False
    face_landmarks: bool = False
    temporal_behavior: bool = False


class Readiness(BaseModel):
    ready: bool = False
    reason: str = "Inference adapters have not been implemented"


def create_app() -> FastAPI:
    app = FastAPI(
        title="VietAIS Sentinel",
        version=__version__,
        description="Foundation API only; not ready for exam analysis.",
    )

    @app.get("/health/live")
    def live() -> dict[str, str]:
        return {"status": "alive", "engine_version": __version__}

    @app.get(
        "/health/ready",
        response_model=Readiness,
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
    )
    def ready() -> Readiness:
        return Readiness()

    @app.get("/v1/capabilities", response_model=Capabilities)
    def capabilities() -> Capabilities:
        return Capabilities()

    return app


app = create_app()
