from fastapi import FastAPI
from app.models import TestRun

app = FastAPI(
    title="CI Test Intelligence",
    description="A fictional API for analyzing automated test runs.",
    version="0.1.0",
)

test_runs: list[TestRun] = []

@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "healthy"}

@app.post("/test-runs", status_code=201)
def create_test_run(test_run: TestRun) -> TestRun:
    test_runs.append(test_run)
    return test_run

@app.get("/test-runs")
def list_test_runs() -> list[TestRun]:
    return test_runs