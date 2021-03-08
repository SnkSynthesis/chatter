import pytest
from fastapi.testclient import TestClient
import os
from chatter import app
from pathlib import Path


@pytest.fixture
def client():
    os.environ["DATABASE_URL_FASTAPI"] = "sqlite:///./test.db"
    with TestClient(app) as client:
        yield client
    
    # Delete file if it is there to reset database for next tests
    db_file = Path("./test.db")
    if db_file.is_file():
        db_file.unlink()
