from enum import Enum

from pydantic import BaseModel


class EmailBodyType(str, Enum):
    plain = "plain"
    html = "html"


class EmailNotification(BaseModel):
    from_: str
    subject: str
    body: str
    to: list[str, ...]
    cc: list[str, ...] = []
    bcc: list[str, ...] = []
    body_type: EmailBodyType
