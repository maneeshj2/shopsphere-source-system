import uuid
from datetime import date

from sqlalchemy import Date, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.mixins import AuditMixin


class Customer(AuditMixin, Base):
    __tablename__ = "customers"

    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    phone_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    date_of_birth: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    loyalty_points: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )