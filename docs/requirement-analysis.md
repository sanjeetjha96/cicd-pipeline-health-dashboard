# Requirement Analysis — CI/CD Pipeline Health Dashboard


## 1. Summary
Build a dockerized, production-ready dashboard that collects CI/CD metrics from GitHub Actions, visualizes them (success/failure rate, average build time, last build status), stores recent build logs, and sends alerts (Slack/Email) for failed builds. Include documentation of AI involvement.


## 2. Stakeholders
- DevOps Engineers (primary users)
- Developers (to see build health)
- SRE / Platform teams
- Project managers


## 3. Goals / Success Criteria
- Real-time (near real-time) visibility of GitHub Actions executions.
- Alerting for failing pipelines within configurable thresholds (immediate or aggregated).
- Easy deployment via Docker Compose.
- Clear documentation and prompt log of AI usage.


## 4. Metrics to collect
- Pipeline run success rate (time-windowed: 24h, 7d, 30d).
- Average build time (per workflow / repo / branch).
- Last build status for tracked workflows.
- Count of failed builds (by repo/branch/workflow).
- Recent build logs (last N runs, searchable).


## 5. Data sources & integration points
- GitHub Actions REST API v3/v4 (Actions): to fetch runs and logs.
- GitHub webhook (optional) to get events in near-real-time.
- Slack Incoming Webhooks / Emails via SMTP or transactional service (e.g., SendGrid) for alerts.


## 6. Non-functional requirements
- Dockerized, simple `docker-compose up` deployment.
- Configurable via environment variables (GitHub token(s), DB URL, Slack webhook, alert thresholds).
- Secure: store secrets in env only; support integration with vault later.
- Scalable components (stateless backend, Postgres database for persistence).
- Observability: logs + basic metrics endpoint for monitoring.


## 7. Constraints & Assumptions
- User will provide a GitHub personal access token (read: actions) with minimum scopes.
- The central instance will poll GitHub or receive webhooks; polling frequency configurable.
- For initial version, we support GitHub; later add GitLab/Bitbucket.


## 8. Acceptance criteria
- Docker Compose can bring up backend, frontend, and Postgres DB.
- Dashboard shows last build status and success rate for at least one repo/workflow.
- Failed-build Slack notifications are sent after a failed run.
- Prompt logs and AI-docs are included in repo.
