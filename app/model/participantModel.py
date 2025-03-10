from app.configuration.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.enumeration.roleEnum import RoleEnum 

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False) 
    CPF = Column(String, nullable=False, unique=True)  
    password = Column(String, nullable=False) 
    event_id = Column(Integer, ForeignKey("events.id"))

    event = relationship("EventModel", back_populates="participants")
