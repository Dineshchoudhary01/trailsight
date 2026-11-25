import uuid

from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, SQLModel


class Entity(SQLModel, table=True):
    __tablename__ = "entities"

    id: int | None = Field(default=None, primary_key=True)
    case_id: uuid.UUID = Field(foreign_key="cases.id")
    type: str  # account|domain|ip|ns|registrar|asn|upi|phone
    value: str
    props: dict = Field(default_factory=dict, sa_type=JSONB)


class Edge(SQLModel, table=True):
    __tablename__ = "edges"

    id: int | None = Field(default=None, primary_key=True)
    case_id: uuid.UUID = Field(foreign_key="cases.id")
    from_id: int = Field(foreign_key="entities.id")
    to_id: int = Field(foreign_key="entities.id")
    type: str  # RESOLVES_TO | USES_NS | PAID_TO | ...
    evidence: dict = Field(default_factory=dict, sa_type=JSONB)