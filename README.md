# CI/CD Pipeline Health Dashboard

## Overview
A dashboard to collect and visualize GitHub Actions pipeline metrics and alert on failures.

## Quick start (development)
1. Copy `.env` files and fill values (GITHUB_TOKEN, SLACK_WEBHOOK_URL) if you plan to connect GitHub/Slack.
2. Run: `docker compose up --build`
3. Frontend: http://localhost:5173
4. Backend API (FastAPI): http://localhost:8000/docs

## Seeder / Demo data
A small seeder is included (`src/backend/seed_data.py`) to populate demo pipeline runs so the UI shows data after first start.
