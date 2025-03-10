import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.configuration.database import get_db, Base
from app.main import app 

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db():
    """ Configuração do banco de dados para os testes """
    Base.metadata.create_all(bind=engine)  

    session = TestingSessionLocal()
    try:
        yield session 
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine) 
@pytest.fixture
def client(db):
    """ Configuração do cliente de testes com sobrescrita do banco de dados """
    def override_get_db():
        try:
            yield db
        finally:
            pass 

    app.dependency_overrides[get_db] = override_get_db
    test_client = TestClient(app)

    yield test_client

    app.dependency_overrides.clear() 

def test_check_tables_exist(db):
    tables = db.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    assert ("events",) in tables  
