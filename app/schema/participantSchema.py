from pydantic import BaseModel
from app.enumeration.roleEnum import RoleEnum  # Certifique-se de importar corretamente

class ParticipantSchema(BaseModel):
    id: int
    name: str
    email: str
    age: int
    role: RoleEnum  # Agora está vinculado ao Enum RoleEnum
    CPF: str
    password: str
    event_id: int

    class Config:
        from_attributes = True
