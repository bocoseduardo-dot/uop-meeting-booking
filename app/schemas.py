from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator


class ProfessorRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class SlotBase(BaseModel):
    starts_at: datetime
    ends_at: datetime
    location: str = Field(min_length=1, max_length=100)

    @model_validator(mode="after")
    def check_dates(self):
        if self.ends_at <= self.starts_at:
            raise ValueError("ends_at must be after starts_at")
        return self


class SlotCreate(SlotBase):
    professor_id: int


class SlotRead(SlotBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    professor: ProfessorRead
