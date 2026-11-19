
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app import model


TEST_DATABASE_URL = (
    "postgresql+psycopg://postgres:root@localhost:5432/notes_test_db"
)

test_engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    bind=test_engine,
    autoflush=False,
    expire_on_commit=False
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def setup_function():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)


def teardown_function():
    Base.metadata.drop_all(bind=test_engine)


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_note():
    response = client.post(
        "/insert-data",
        json={
            "title": "Learn FastAPI",
            "context": "Practice API development",
            "category": "Learning"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn FastAPI"
    assert "id" in response.json()


def test_get_all_notes():
    client.post(
        "/insert-data",
        json={
            "title": "Python",
            "context": "Learn Python",
            "category": "Programming"
        }
    )

    response = client.get("/notes")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_note():
    created = client.post(
        "/insert-data",
        json={
            "title": "Old title",
            "context": "Content",
            "category": "Study"
        }
    )

    note_id = created.json()["id"]

    response = client.put(
        f"/update-data/{note_id}",
        json={"title": "Updated title"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"


def test_delete_note():
    created = client.post(
        "/insert-data",
        json={
            "title": "Delete me",
            "context": "Temporary note",
            "category": "Test"
        }
    )

    note_id = created.json()["id"]

    response = client.delete(f"/delete-note/{note_id}")

    assert response.status_code == 200

    missing = client.get(f"/notes/{note_id}")
    assert missing.status_code == 404


def test_note_not_found():
    response = client.get("/notes/99999")

    assert response.status_code == 404


def test_invalid_note():
    response = client.post(
        "/insert-data",
        json={
            "title": "",
            "context": "Some context",
            "category": "Test"
        }
    )

    assert response.status_code == 422
