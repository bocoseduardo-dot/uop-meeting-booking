from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Professor, Slot
from app.schemas import SlotCreate, SlotRead

SettingsDep = Annotated[Session, Depends(get_db)]

Base.metadata.create_all(bind=engine)
app = FastAPI(title="uop-meeting-booking", version="0.1.0")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/slots", response_model=SlotRead, status_code=201)
def create_slot(slot_in: SlotCreate, db: SettingsDep):
    professor = db.get(Professor, slot_in.professor_id)
    if professor is None:
        raise HTTPException(status_code=422, detail="Professor not found")
    slot = Slot(**slot_in.model_dump())
    db.add(slot)
    db.commit()
    db.refresh(slot)
    return slot


@app.get("/slots", response_model=list[SlotRead])
def list_slots(db: SettingsDep):
    return db.scalars(select(Slot)).all()
