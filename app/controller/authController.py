from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from pydantic import BaseModel
from app.service.authService import authenticate_user, create_access_token
from app.configuration.database import get_db

router = APIRouter()

class LoginSchema(BaseModel):
    cpf: str
    password: str

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    """Endpoint de login utilizando CPF e senha."""
    user = authenticate_user(db, cpf=data.cpf, password=data.password)
    if not user:
        raise HTTPException(status_code=400, detail="CPF ou senha incorretos")

    access_token = create_access_token(data={"sub": str(user.id)}, expires_delta=timedelta(minutes=60))
    return {"access_token": access_token, "token_type": "bearer"}
