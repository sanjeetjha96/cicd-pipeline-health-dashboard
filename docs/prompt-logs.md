# prompt-logs.md


## Entry 001 — Initial project request (from user)
**Date:** 2025-08-26
**Prompt / Request:**
We are an expert DevOps Engineer. I need your help in building CI/CD Pipeline Health Dashboard.


Here are the key requirements:


Metrics Collection – Collect and visualize CI/CD pipeline metrics from GitHub Actions (success/failure rate, average build time, last build status).


Alerting – Implement Slack/Email alerts for failed builds.


UI – Provide a simple dashboard to display metrics and recent build logs.


Deployment – Solution must be dockerized and easy to deploy.


AI-Native Requirement – Document how AI was used in the design and build process.


Expected Deliverables (must be generated and refined step by step):


prompt-logs.md → Logs of all prompts used during solution creation.


requirement-analysis.md → Detailed requirement analysis.


tech-design.md → High-level and low-level architecture (data flow, integrations, tools, APIs).


src/ → Complete source code of the dashboard (backend + frontend + alerting integration).


docker-compose.yml or Dockerfile → For deployment.


README.md → Setup instructions + summary of AI usage.


Your task:


Guide me step by step through building this project.


At each step, produce the required artifacts (documents, diagrams, and code).


Ensure the solution is production-ready, modular, and clearly explained.


Help me keep prompt-logs.md updated with all prompts used.


**Assistant action (planned):** Create project skeleton, requirement and design docs, then implement code in small iterations (backend → frontend → alerting → deployment) with Docker Compose.
