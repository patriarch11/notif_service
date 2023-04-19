from pydantic import BaseSettings

__all__ = ["Settings", "SMTPSettings"]


class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000


class SMTPSettings(BaseSettings):
    class Config:
        env_prefix = "SMTP_"

    server: str
    port: int
    username: str
    password: str
