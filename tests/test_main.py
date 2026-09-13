from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Get test
def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# Posr test
def test_create_test_run() -> None:
    payload = {
        "test_name": "test_checkout_with_valid_card",
        "status": "failed",
        "duration_seconds": 12.4,
        "run_id": "run-2026-001",
        "executed_id": "2026-09-12T18:30:00Z",
    }

    response = client.post("/test-runs", json=payload)

    assert response.status_code == 201, response.json()
    assert response.json() == payload

    list_response = client.get("/test-runs")

    assert list_response.status_code == 200
    assert list_response.json() == [payload]