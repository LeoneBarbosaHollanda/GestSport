import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.model.participantModel import Participant
from app.security.auth import get_password_hash
from app.enumeration.roleEnum import RoleEnum


def create_test_participant(db: Session):
    hashed_password = get_password_hash("senha123")
    admin_participant = Participant(
        id=1,
        name="João Silva",
        email="joao@email.com",
        age=25,
        role="admin",
        CPF="12345678900",
        password=hashed_password,
        event_id=1
    )
    db.add(admin_participant)
    db.commit()
    return admin_participant


def test_list_participants(client: TestClient, db):
    create_test_participant(db)

    login_data = {"cpf": "12345678900", "password": "senha123"}
    response = client.post("/login", json=login_data)
    assert response.status_code == 200, f"Erro ao fazer login: {response.text}"

    token = response.json().get("access_token")
    assert token is not None, "Token de acesso não foi retornado"
    response = client.get(f"/participants/1?token={token}")

    assert response.status_code == 200, f"Erro ao listar participantes: {response.text}"
    assert isinstance(response.json(), list), "Resposta não é uma lista de participantes"
