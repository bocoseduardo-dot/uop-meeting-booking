import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app
from app.models import Professor

test_engine = create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)
testing_sesionlocal = sessionmaker(bind=test_engine)


@pytest.fixture
def client():
    Base.metadata.create_all(bind=test_engine)
    with testing_sesionlocal() as db:
        db.add(Professor(name="Test_Professor", email="Professor@Exalmple.com"))
        db.commit()

    def override_get_db():
        with testing_sesionlocal() as db:
            yield db

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)


def test_created_Slot_apears_in_list(client):
    payload = {
        "professor_id": 1,
        "starts_at": "2026-10-26T10:00:00",
        "ends_at": "2026-10-26T11:00:00",
        "location": "Office 12",
    }
    response = client.post("/slots", json=payload)

    assert response.status_code == 201
    assert response.json()["professor"]["name"] == "Test_Professor"
    assert len(client.get("/slots").json()) == 1
