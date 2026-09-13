from datetime import datetime
from pydantic import BaseModel
from typing import Literal

class TestRun(BaseModel):
    test_name: str
    status: Literal["passed", "failed"]
    duration_seconds: float
    run_id: str
    executed_id: datetime
