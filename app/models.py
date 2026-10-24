from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Professor(Base):
    __tablename__ = "professors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    slots: Mapped[list["Slot"]] = relationship(
        back_populates="professor", cascade="all, delete-orphan"
    )


class Slot(Base):
    __tablename__ = "slots"
    id: Mapped[int] = mapped_column(primary_key=True)
    professor_id: Mapped[int] = mapped_column(ForeignKey("professors.id"))
    starts_at: Mapped[datetime]
    ends_at: Mapped[datetime]
    location: Mapped[str] = mapped_column(String(100))
    professor: Mapped["Professor"] = relationship(back_populates="slots")
