from app.model.eventModel import EventModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.schema.eventSchema import EventSchema

class EventService:
    @staticmethod
    def create_event(db: Session, event: EventSchema):
        if event.max_participants <= 0:
            raise HTTPException(status_code=400, detail="O número máximo de participantes deve ser maior que zero.")
        try:
            db_event = EventModel(
                name=event.name,
                date=event.date,
                location=event.location,
                modality=event.modality,
                max_participants=event.max_participants
            )
            db.add(db_event)
            db.commit()
            db.refresh(db_event)
            return db_event
        
        except IntegrityError:
            db.rollback()
            raise IntegrityError 

    @staticmethod
    def list_events(db: Session):
        return db.query(EventModel).all()
