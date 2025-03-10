import pytest
from fastapi.testclient import TestClient
from app.schema.eventSchema import EventSchema

from fastapi.testclient import TestClient

def test_create_event(client: TestClient, db):
    response = client.post("/events", json={
        "id":1,
        "name": "testee",
        "date": "2025-03-09",
        "location": "string",
        "modality":"string",
        "max_participants": 3
                                             })
    assert response.status_code == 200
    assert response.json()["name"] == "testee"

def test_list_events(client: TestClient, db):
    response = client.get("/events/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
