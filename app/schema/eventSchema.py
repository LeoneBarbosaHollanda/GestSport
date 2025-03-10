# app/schemas/eventSchema.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

class EventSchema(BaseModel):
    id: Optional[int]  # O id será opcional na criação, mas será preenchido ao retornar do banco de dados
    name: str
    date: date
    location: str
    modality: str
    max_participants: int


    class Config:
        from_attributes = True  # Isso diz ao Pydantic para trabalhar com SQLAlchemy models
