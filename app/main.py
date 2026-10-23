from fastapi import FastAPI

from app.database import Base, engine
from app import models  # noqa: F401

Base.metadata.create_all(bind=engine)
app = FastAPI(title="uop-meeting-booking", version="0.1.0")


@app.get("/health")
def health_check():
    return {"status": "ok"}
