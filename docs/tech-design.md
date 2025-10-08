Technical Design Document — CI/CD Pipeline Health Dashboard
1. Introduction

This document defines the technical design for the CI/CD Pipeline Health Dashboard — a dockerized, production-ready system that collects, stores, analyzes, visualizes, and alerts on CI/CD pipeline runs (initially GitHub Actions). It covers architecture, data flow, database schema, APIs, alerting, deployment, scaling, security, observability, and operational runbook items.

2. Goals
Near-real-time visibility of GitHub Actions runs (last status, success/failure rate, average build time).

Store recent build logs and allow searching / drill-down.

Slack and Email alerting for failed pipelines (configurable rules).

Easy deploy via docker-compose and configurable with environment variables.

Modular, testable, and production-ready design.

3. High-level architecture

Components:

Frontend — React + Vite + Tailwind. Visualizations (charts, lists), filters, log viewer, alert management.

Backend API — FastAPI (Python 3.11+) with async workers. Exposes REST APIs for UI, webhook endpoints, metrics ingestion, and admin.

Scheduler / Worker — Background tasks to poll GitHub (if webhook not used), fetch logs, run alert rules. Implemented using asyncio background tasks or Celery/Redis for heavier needs.

Database — PostgreSQL for persistence.

Optional Cache/Queue — Redis (caching, rate limiting, optional Celery broker).

Alerting Integrations — Slack Incoming Webhooks, SMTP (or SendGrid), optional MS Teams.

Reverse Proxy / Ingress — Nginx (optional) for TLS termination.

Monitoring — metrics endpoint and structured logs.

Diagram
[GitHub Actions] --> (Webhook) --> [Backend API /webhook]
                            \
                             --> [Worker] --> [Postgres]
[Backend API] <--> [Frontend (React)]
[Worker] --> [Alerting Services (Slack/SMTP)]
[Backend] --> /metrics


4. Data Flow
Webhook Mode (preferred)

GitHub sends workflow_run events to POST /webhook/github.

Backend validates signature, enqueues processing job, persists run + jobs metadata, optionally downloads logs and stores them.

Trigger alert evaluation.

ERD (simplified)
repositories (1) --- (N) workflow_runs (1) --- (N) jobs (1) --- (N) steps
workflow_runs (1) --- (N) alerts
jobs (1) --- (N) logs

5. API Design (examples)

Base: GET /api/v1/... | JSON

Public / Frontend APIs

GET /api/v1/repos — list repos (with basic metrics)

POST /api/v1/repos — register repo to track (owner/name + webhook secret or token)

GET /api/v1/repos/{repo}/workflows — list workflows for repo

GET /api/v1/repos/{repo}/runs?from=...&to=...&status=... — list runs (pagination)

GET /api/v1/runs/{run_id} — run details (with jobs)

GET /api/v1/jobs/{job_id}/logs — fetch logs (or presigned S3 URL)

GET /api/v1/metrics?repo=...&window=24h — compute success rate, avg build time

GET /api/v1/alerts?repo=... — list alerts

Ingestion / Admin

POST /webhook/github — GitHub webhook receiver (verify X-Hub-Signature-256)

POST /api/v1/poll/run — trigger poll (admin)

POST /api/v1/settings/alerts — update alert rules

Auth & Security

Admin endpoints protected by API key / JWT.

Frontend uses session / JWT (for multi-user support).

6. Alerting & Rules
Types of alerts

Instant Failure Alert — a workflow run with conclusion=failure triggers immediate alert.

Flapping Alert — N failures within M runs/time window (e.g., 3 failures in 30 min).

Regression Alert — success rate drop below threshold in window (e.g., success rate < 80% for 24h).

Slow Build Alert — average build duration > threshold (e.g., > 20 min) per workflow.

7. Project structure & deliverables

Suggested repo layout:

/ .
  /backend
    app/
    Dockerfile
    requirements.txt
  /worker
    tasks/
  /frontend
    src/
    Dockerfile
  /deploy
    docker-compose.yml
    tls/
  /docs
    requirement-analysis.md
    tech-design.md  <-- this doc
    prompt-logs.md
 README.md


Data Flow Diagram (DFD)
     +--------------------+
     |  GitHub Actions    |
     |  (CI/CD Provider)  |
     +--------------------+
               |
        (Webhook / API)
               |
               v
     +--------------------+
     |  Backend (FastAPI) |
     |--------------------|
     | - Receives webhook |
     | - Validates event  |
     | - Processes data   |
     | - Stores in DB     |
     | - Evaluates alerts |
     +--------------------+
               |
               |  (Insert/Update)
               v
     +--------------------+
     |   PostgreSQL DB    |
     |--------------------|
     | Tables:            |
     | - Repositories     |
     | - Workflow_Runs    |
     | - Jobs, Steps      |
     | - Logs, Alerts     |
     +--------------------+
               |
               |  (API Query)
               v
     +--------------------+
     | Frontend (React)   |
     |--------------------|
     | - Fetch metrics    |
     | - Render charts    |
     | - Show logs/runs   |
     | - Manage alerts    |
     +--------------------+
               |
               |  (View alerts / logs)
               v
     +--------------------+
     | Notification Layer |
     |--------------------|
     | - Slack Webhook    |
     | - Email (SMTP)     |
     +--------------------+



Entity Relationship Diagram (ERD)
+----------------+        +-------------------+
|  Repositories  |1------∞|   Workflow_Runs   |
| repo_id (PK)   |        | run_id (PK)       |
| name           |        | repo_id (FK)      |
| owner          |        | workflow_name     |
| full_name      |        | status            |
| created_at     |        | conclusion        |
+----------------+        | started_at        |
                          | completed_at      |
                          | duration_seconds  |
                          | html_url          |
                          +-------------------+
                                  |
                                  |1
                                  ∞
                          +-------------------+
                          |       Jobs        |
                          | job_id (PK)       |
                          | run_id (FK)       |
                          | name              |
                          | status            |
                          | conclusion        |
                          | started_at        |
                          | completed_at      |
                          | duration_seconds  |
                          +-------------------+
                                  |
                                  |1
                                  ∞
                          +-------------------+
                          |       Steps       |
                          | step_id (PK)      |
                          | job_id (FK)       |
                          | name              |
                          | status            |
                          | number            |
                          | started_at        |
                          | completed_at      |
                          +-------------------+
                                  |
                                  |1
                                  ∞
                          +-------------------+
                          |       Logs        |
                          | log_id (PK)       |
                          | step_id (FK)      |
                          | log_text          |
                          | log_size_bytes    |
                          | captured_at       |
                          +-------------------+
                                  |
                                  |1
                                  ∞
                          +-------------------+
                          |      Alerts       |
                          | alert_id (PK)     |
                          | run_id (FK)       |
                          | repo_id (FK)      |
                          | severity          |
                          | channel           |
                          | message           |
                          | created_at        |
                          | resolved_at       |
                          +-------------------+
