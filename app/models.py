from datetime import datetime
from pydantic import BaseModel

class TestRun(BaseModel):
    test_name: str
    status: str
    duration_seconds: float
    run_id: str
    executed_id: datetime
