import asyncio, datetime, random
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from app.models import WorkflowRun
from app.config import settings

async def seed():
    engine = create_async_engine(settings.DATABASE_URL, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    async with AsyncSession(engine) as session:
        now = datetime.datetime.utcnow()
        samples = []
        for i in range(1, 21):
            started = now - datetime.timedelta(minutes=10*i)
            completed = started + datetime.timedelta(minutes=random.randint(1,10))
            samples.append(WorkflowRun(
                run_id=1000+i,
                status='completed',
                conclusion=random.choice(['success','failure','cancelled']),
                started_at=started.isoformat() + 'Z',
                completed_at=completed.isoformat() + 'Z',
                duration_seconds=int((completed - started).total_seconds()),
                html_url=f"https://github.com/example/repo/actions/runs/{1000+i}"
            ))
        session.add_all(samples)
        await session.commit()
    print('Seeded demo data')

if __name__ == '__main__':
    asyncio.run(seed())
