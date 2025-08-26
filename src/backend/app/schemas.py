from pydantic import BaseModel
from typing import Optional
class MetricsOut(BaseModel):
    total_runs: int
    success_count: int
    failure_count: int
    avg_duration_seconds: Optional[float]
