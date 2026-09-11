from fastapi import FastAPI

app = FastAPI(
    title="CI Test Intelligence",
    description="A fictional API for analyzing automated test runs.",
    version="0.1.0",
)

@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "healthy"}