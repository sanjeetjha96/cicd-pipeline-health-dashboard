from fastapi import FastAPI
from .api import webhook, metrics, health
from .db import init_db

app = FastAPI(title="CI/CD Pipeline Health Dashboard - Backend")

app.include_router(webhook.router)
app.include_router(metrics.router)
app.include_router(health.router)

@app.on_event('startup')
async def startup_event():
    await init_db()

from fastapi import FastAPI

app = FastAPI(title="CI/CD Pipeline Health Dashboard")

@app.get("/")
async def root():
    return {"message": "CI/CD Pipeline Health Dashboard Backend is running"}

# existing imports and routes like /metrics, /health, /webhook/github
