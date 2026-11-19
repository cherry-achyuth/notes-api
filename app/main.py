
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database import get_db
from app.schemas import NoteCreate, NoteResponse, NoteUpdate
from app.model import Note
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Notes CRUD API")


@app.get("/")
def home():
    return {"message": "Welcome to Notes API"}


# Get all notes
@app.get("/notes", response_model=list[NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    statement = select(Note).order_by(Note.id.desc())
    result = db.execute(statement)
    notes = result.scalars().all()

    return notes


# Get note by ID
@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note_by_id(note_id: int, db: Session = Depends(get_db)):
    statement = select(Note).where(Note.id == note_id)
    note = db.execute(statement).scalars().first()

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    return note


# Create a note
@app.post(
    "/insert-data",
    response_model=NoteResponse,
    status_code=status.HTTP_201_CREATED
)
def post_notes(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(**note.model_dump())

    try:
        db.add(db_note)
        db.commit()
        db.refresh(db_note)

        logger.info("Note created successfully: ID %s", db_note.id)
        return db_note

    except Exception:
        db.rollback()
        logger.exception("Failed to create note")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create note"
        )


# Update a note
@app.put("/update-data/{note_id}", response_model=NoteResponse)
def update_notes(
    note_id: int,
    note_data: NoteUpdate,
    db: Session = Depends(get_db)
):
    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    updated_data = note_data.model_dump(exclude_unset=True)

    for field, value in updated_data.items():
        setattr(note, field, value)

    try:
        db.commit()
        db.refresh(note)

        logger.info("Note updated successfully: ID %s", note_id)
        return note

    except Exception:
        db.rollback()
        logger.exception("Failed to update note")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update note"
        )


# Delete a note
@app.delete("/delete-note/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    try:
        db.delete(note)
        db.commit()

        logger.info("Note deleted successfully: ID %s", note_id)
        return {"message": "Note deleted successfully"}

    except Exception:
        db.rollback()
        logger.exception("Failed to delete note")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete note"
        )
