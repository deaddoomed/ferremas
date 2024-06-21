from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
    
def test_server_running_exito():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "API is running"