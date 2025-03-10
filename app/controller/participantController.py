from fastapi import APIRouter, Depends, HTTPException
from app.configuration.database import get_db
from ..schema.participantSchema import ParticipantSchema  
from sqlalchemy.orm import Session
from app.service.participantService import ParticipantService
from app.service.authService import get_current_admin

router = APIRouter()

@router.post("/participants/", response_model=ParticipantSchema) 
def create_participant(event: ParticipantSchema, db: Session = Depends(get_db)):
    return ParticipantService.create_participant(db=db, event=event)

@router.get("/participants/{event_id}", response_model=list[ParticipantSchema])
def list_participants_by_event(event_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return ParticipantService.list_participants_by_event(db, event_id)