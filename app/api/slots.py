from fastapi import APIRouter, HTTPException

from app.api.dependecies import SessionDep
from app.errors import ProfessorNotFoundError
from app.schemas import SlotCreate, SlotRead
from app.services import slots as slot_service

router = APIRouter(prefix="/slots")


@router.post("", response_model=SlotRead, status_code=201)
def create_slot(slot_in: SlotCreate, db: SessionDep):
    try:
        return slot_service.publish_slot(db, slot_in)
    except ProfessorNotFoundError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error


@router.get("", response_model=list[SlotRead])
def list_slots(db: SessionDep):
    return slot_service.ret_list(db)
