from pydantic import BaseSettings

__all__ = ["Settings", "SMTPSettings", "JWTSettings"]


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


class JWTSettings(BaseSettings):
    class Config:
        env_prefix = "JWT_"

    client_id: str
    client_secret: str
    issuer: str
    algorithm: str
