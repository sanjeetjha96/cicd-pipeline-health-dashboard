# Tech Design — CI/CD Pipeline Health Dashboard


## 1. Chosen stack (recommended)
- Backend: **FastAPI** (Python 3.11+) for async HTTP, performance, auto docs.
- Frontend: **React** + Vite + Tailwind CSS (modern, fast dev experience).
- Database: **Postgres** (docker-compose). For lightweight demo, SQLite option available.
- Message / cache: optional **Redis** for rate-limiting and caching (not required initially).
- Deployment: Docker & Docker Compose.
- Alerts: Slack Incoming Webhook (primary), SMTP (optional).


## 2. High-level architecture (textual)
