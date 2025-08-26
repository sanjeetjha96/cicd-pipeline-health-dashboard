from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class WorkflowRun(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    run_id: int
    status: str
    conclusion: Optional[str] = None
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    duration_seconds: Optional[int] = None
    html_url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
