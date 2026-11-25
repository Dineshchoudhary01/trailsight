import uuid
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, SQLModel

from app.models.base import utcnow


class IntelCache(SQLModel, table=True):
    __tablename__ = "intel_cache"

    key: str = Field(primary_key=True)
    payload: dict = Field(sa_type=JSONB)
    expires_at: datetime = Field(sa_type=DateTime(timezone=True))


class AuditLog(SQLModel, table=True):
    __tablename__ = "audit_logs"

    id: int | None = Field(default=None, primary_key=True)
    user_id: uuid.UUID | None = Field(default=None, foreign_key="users.id")
    case_id: uuid.UUID | None = Field(default=None, foreign_key="cases.id")
    action: str
    meta: dict = Field(default_factory=dict, sa_type=JSONB)
    at: datetime = Field(default_factory=utcnow, sa_type=DateTime(timezone=True))