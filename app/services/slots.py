from sqlalchemy.orm import Session

from app.errors import ProfessorNotFoundError
from app.models import Slot
from app.repositories import professors as professor_repository
from app.repositories import slots as slot_repository
from app.schemas import SlotCreate


def publish_slot(db: Session, slot_c: SlotCreate) -> Slot:
    if professor_repository.get_by_id(db, slot_c.professor_id) is None:
        raise ProfessorNotFoundError(
            f"Professor with ID:{slot_c.professor_id} does not exist"
        )
    slot_f = Slot(**slot_c.model_dump())
    slot_repository.add(db, slot_f)
    db.commit()
    db.refresh(slot_f)
    return slot_f


def ret_list(db: Session) -> list[Slot]:
    return slot_repository.list_all(db)
