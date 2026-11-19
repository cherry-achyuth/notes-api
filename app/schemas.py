
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    context: str = Field(min_length=1)
    category: str = Field(min_length=1, max_length=50)


class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=150)
    context: str | None = Field(default=None, min_length=1)
    category: str | None = Field(default=None, min_length=1, max_length=50)


class NoteResponse(BaseModel):
    id: int
    title: str
    context: str
    category: str
    created_datetime: datetime
    updated_datetime: datetime

    model_config = ConfigDict(from_attributes=True)
