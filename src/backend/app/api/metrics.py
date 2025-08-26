from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from ..db import get_session
from ..models import WorkflowRun
from ..schemas import MetricsOut

router = APIRouter()

@router.get('/api/metrics', response_model=MetricsOut)
async def get_metrics(session: AsyncSession = Depends(get_session)):
    q_total = await session.execute(select(func.count(WorkflowRun.id)))
    total = q_total.scalar_one() or 0

    q_success = await session.execute(select(func.count(WorkflowRun.id)).where(WorkflowRun.conclusion == 'success'))
    success = q_success.scalar_one() or 0

    q_fail = await session.execute(select(func.count(WorkflowRun.id)).where(WorkflowRun.conclusion != 'success'))
    failure = q_fail.scalar_one() or 0

    q_avg = await session.execute(select(func.avg(WorkflowRun.duration_seconds)))
    avg_dur = q_avg.scalar_one()

    return MetricsOut(total_runs=total, success_count=success, failure_count=failure, avg_duration_seconds=avg_dur)
