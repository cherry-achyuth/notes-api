
from app.database import Base
from datetime import datetime

from sqlalchemy import Text, String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    context: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    created_datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
