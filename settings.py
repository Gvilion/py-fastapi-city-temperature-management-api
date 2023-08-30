from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Temperature management API"

    DATABASE_URL: str | None = "sqlite+aiosqlite:///./sql_app.db"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()