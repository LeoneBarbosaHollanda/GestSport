from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schema.eventSchema import EventSchema 
from app.service.eventService import EventService
from app.configuration.database import get_db

router = APIRouter()

@router.post("/events/", response_model=EventSchema)
def create_event(event: EventSchema, db: Session = Depends(get_db)):
    return EventService.create_event(db=db, event=event)


@router.get("/events/", response_model=list[EventSchema])
def list_events(db: Session = Depends(get_db)):
    return EventService.list_events(db)