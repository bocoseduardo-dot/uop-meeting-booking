from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Slot


def add(db: Session, slot: Slot) -> Slot:
    db.add(slot)
    db.flush()
    return slot


def list_all(db: Session) -> list[Slot]:
    return list(db.scalars(select(Slot)).all())
