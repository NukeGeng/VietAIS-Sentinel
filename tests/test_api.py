from fastapi.testclient import TestClient

from vietais_sentinel import __version__
from vietais_sentinel.api.app import create_app


def test_process_liveness_is_not_inference_readiness():
    with TestClient(create_app()) as client:
        assert client.get("/health/live").json() == {
            "status": "alive",
            "engine_version": __version__,
        }
        response = client.get("/health/ready")
        assert response.status_code == 503
        assert response.json()["ready"] is False


def test_capabilities_do_not_claim_unimplemented_models():
    with TestClient(create_app()) as client:
        assert client.get("/v1/capabilities").json() == {
            "api_version": "v1",
            "engine_version": __version__,
            "stage": "foundation",
            "object_detection": False,
            "face_landmarks": False,
            "temporal_behavior": False,
        }


def test_no_fake_analysis_endpoint():
    with TestClient(create_app()) as client:
        assert client.post("/v1/analyze", json={}).status_code == 404


def test_openapi_documents_readiness_failure():
    with TestClient(create_app()) as client:
        document = client.get("/openapi.json").json()
        assert "503" in document["paths"]["/health/ready"]["get"]["responses"]
