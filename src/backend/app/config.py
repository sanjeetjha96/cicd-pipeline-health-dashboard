from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://dashboard:dashboard@db:5432/cicd_dashboard"
    GITHUB_TOKEN: str | None = None
    SLACK_WEBHOOK_URL: str | None = None
    WEBHOOK_SECRET: str | None = None
    class Config:
        env_file = ".env"
settings = Settings()
