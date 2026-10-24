
from sqlalchemy import select

from app.database import Base, SessionLocal, engine
from app.models import Professor


def seed() -> None:
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        existing = db.scalar(select(Professor).where(Professor.email == "example.com"))
        if existing is None:
            db.add(Professor(name="Professor example", email="example.com"))
            db.commit()


if __name__ == "__main__":
    seed()
