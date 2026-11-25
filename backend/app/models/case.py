import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Numeric
from sqlmodel import Field, SQLModel

from app.models.base import utcnow


class Case(SQLModel, table=True):
    __tablename__ = "cases"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    status: str = "open"
    created_by: uuid.UUID | None = Field(default=None, foreign_key="users.id")
    created_at: datetime = Field(
        default_factory=utcnow, sa_type=DateTime(timezone=True)
    )
    # Victim complaint: trail yahin se shuru hota hai
    victim_utr: str | None = None
    victim_amount: Decimal | None = Field(default=None, sa_type=Numeric(14, 2))
    complaint_ts: datetime | None = Field(
        default=None, sa_type=DateTime(timezone=True)
    )
    description: str | None = None


class CaseMember(SQLModel, table=True):
    __tablename__ = "case_members"

    case_id: uuid.UUID = Field(foreign_key="cases.id", primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="users.id", primary_key=True)


class EvidenceFile(SQLModel, table=True):
    __tablename__ = "evidence_files"

    id: int | None = Field(default=None, primary_key=True)
    case_id: uuid.UUID = Field(foreign_key="cases.id")
    filename: str
    kind: str  # statement | complaint | intel_export | report
    sha256: str
    uploaded_by: uuid.UUID | None = Field(default=None, foreign_key="users.id")
    uploaded_at: datetime = Field(
        default_factory=utcnow, sa_type=DateTime(timezone=True)
    )