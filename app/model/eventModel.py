from app.configuration.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.orm import relationship
from app.model.participantModel import Participant 

class EventModel(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    modality = Column(String, nullable=False)
    max_participants = Column(Integer, nullable=False)

    
    participants = relationship("Participant", back_populates="event")

    __table_args__ = {'extend_existing': True}

