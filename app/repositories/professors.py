from sqlalchemy.orm import Session

from app.models import Professor


def get_by_id(db: Session, Professor_id: int):
    return db.get(Professor, Professor_id)
