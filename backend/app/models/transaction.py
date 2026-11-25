import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Numeric
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, SQLModel


class Transaction(SQLModel, table=True):
    __tablename__ = "transactions"

    id: int | None = Field(default=None, primary_key=True)
    case_id: uuid.UUID = Field(foreign_key="cases.id")
    account_id: int = Field(foreign_key="accounts.id")
    ts: datetime = Field(sa_type=DateTime(timezone=True))  # UTC
    tz_original: str | None = None  # e.g. 'Asia/Kolkata'
    type: str  # 'DEBIT' | 'CREDIT'
    amount: Decimal = Field(sa_type=Numeric(14, 2))
    balance: Decimal | None = Field(default=None, sa_type=Numeric(14, 2))
    counterparty: str | None = None
    counterparty_acct: str | None = None
    utr: str | None = None
    narration: str | None = None
    source_file: str | None = None
    raw: dict | None = Field(default=None, sa_type=JSONB)
    balance_ok: bool | None = None