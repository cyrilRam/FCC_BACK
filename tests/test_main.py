import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_formation():
    response = client.get("/api/formations")
    assert response.status_code == 200
