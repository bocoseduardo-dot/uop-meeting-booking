from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.api.slots import router as slots_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(title="uop-meeting-booking", version="0.1.0")
app.include_router(slots_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
def index():
    return FileResponse("static/index.html")
