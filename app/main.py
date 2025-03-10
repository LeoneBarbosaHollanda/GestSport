from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from app.controller import eventController, participantController, authController
from app.configuration.database import Base, engine
from app.exception.exceptionHandler import (
    http_exception_handler,
    integrity_error_handler,
    generic_exception_handler,
)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    debug=True,
    title="GSport application server"
)

# exceção
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(IntegrityError, integrity_error_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# controllers
app.include_router(authController.router)
app.include_router(eventController.router)
app.include_router(participantController.router)

@app.get("/")
def root():
    return {"message": "API de Gestão de Eventos Esportivos Rodando 🚀"}
