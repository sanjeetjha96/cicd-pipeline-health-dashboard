from fastapi import APIRouter, Header, Request, HTTPException, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_session
from ..models import WorkflowRun
from ..config import settings
import hmac, hashlib, datetime, httpx

router = APIRouter()

def verify_github_signature(body: bytes, signature_header: str | None) -> bool:
    if not settings.WEBHOOK_SECRET:
        return True
    if not signature_header:
        return False
    try:
        sha_name, signature = signature_header.split('=')
    except Exception:
        return False
    mac = hmac.new(settings.WEBHOOK_SECRET.encode(), msg=body, digestmod=hashlib.sha256)
    return hmac.compare_digest(mac.hexdigest(), signature)

async def send_slack_alert(text: str):
    if not settings.SLACK_WEBHOOK_URL:
        return
    async with httpx.AsyncClient() as client:
        await client.post(settings.SLACK_WEBHOOK_URL, json={'text': text})

@router.post('/webhook/github')
async def github_webhook(request: Request, background_tasks: BackgroundTasks, x_hub_signature_256: str | None = Header(None), session: AsyncSession = Depends(get_session)):
    body = await request.body()
    if not verify_github_signature(body, x_hub_signature_256):
        raise HTTPException(status_code=401, detail="Invalid signature")
    payload = await request.json()
    if payload.get('workflow_run'):
        wr = payload['workflow_run']
        started = wr.get('run_started_at')
        completed = wr.get('updated_at')
        duration = None
        try:
            if started and completed:
                s = datetime.datetime.fromisoformat(started.replace('Z','+00:00'))
                c = datetime.datetime.fromisoformat(completed.replace('Z','+00:00'))
                duration = int((c - s).total_seconds())
        except Exception:
            duration = None
        run = WorkflowRun(
            run_id=wr.get('id'),
            status=wr.get('status'),
            conclusion=wr.get('conclusion'),
            started_at=started,
            completed_at=completed,
            duration_seconds=duration,
            html_url=wr.get('html_url')
        )
        session.add(run)
        await session.commit()
        if run.conclusion and run.conclusion != 'success':
            background_tasks.add_task(send_slack_alert, f"Build failed: {run.html_url} (conclusion={run.conclusion})")
    return {"ok": True}
