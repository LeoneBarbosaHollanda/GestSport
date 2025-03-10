from sqlalchemy.orm import Session
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.model.participantModel import Participant
from app.model.eventModel import EventModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class ParticipantService:
    @staticmethod
    def create_participant(db: Session, event):
        if not event.name or not event.email or not event.password or not event.CPF:
            raise HTTPException(status_code=400, detail="Nome, e-mail, senha e CPF são obrigatórios.")

        if "@" not in event.email:
            raise HTTPException(status_code=400, detail="E-mail inválido.")

        if len(event.password) < 6:
            raise HTTPException(status_code=400, detail="A senha deve ter pelo menos 6 caracteres.")

        if len(event.CPF) != 11 or not event.CPF.isdigit():
            raise HTTPException(status_code=400, detail="CPF inválido. Deve conter 11 dígitos numéricos.")

        if event.age < 0 or event.age > 120:
            raise HTTPException(status_code=400, detail="Idade inválida.")
        
        if event.event_id == 0:
            raise HTTPException(status_code=400, detail="Insira o id de um evento cadastrado.")
        
        event_exists = db.query(EventModel).filter(EventModel.id == event.event_id).first()
        if not event_exists:
            raise HTTPException(status_code=404, detail="Evento não encontrado.")

        existing_user = db.query(Participant).filter(
            (Participant.email == event.email) | (Participant.CPF == event.CPF)
        ).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Já existe um participante com esse e-mail ou CPF.")

        try:
            hashed_password = pwd_context.hash(event.password)  

            new_participant = Participant(
                name=event.name,
                email=event.email, 
                age=event.age, 
                role=event.role,
                CPF=event.CPF,
                password=hashed_password, 
                event_id=event.event_id
            )

            db.add(new_participant)
            db.commit()
            db.refresh(new_participant)
            return new_participant
        
        except IntegrityError:
            db.rollback()
            raise IntegrityError 

    @staticmethod
    def list_participants_by_event(db: Session, event_id: int):
        return db.query(Participant).filter(Participant.event_id == event_id).all()
