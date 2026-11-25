import uuid

from sqlalchemy import BigInteger
from sqlalchemy.dialects.postgresql import ARRAY
from sqlmodel import Field, SQLModel


class Account(SQLModel, table=True):
    __tablename__ = "accounts"

    id: int | None = Field(default=None, primary_key=True)
    case_id: uuid.UUID = Field(foreign_key="cases.id")
    acct_ref: str
    holder: str | None = None
    risk_score: int = 0


class Flag(SQLModel, table=True):
    __tablename__ = "flags"

    id: int | None = Field(default=None, primary_key=True)
    account_id: int = Field(foreign_key="accounts.id")
    rule_id: str
    weight: int
    evidence_txn_ids: list[int] = Field(
        default_factory=list, sa_type=ARRAY(BigInteger)
    )
    explanation: str