import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_orden_compra_cambio_direccion_exito():
    request = { "orden_compra_id": 1,"direccion": "direccion_actualizada"}
    response = client.put("/orden_compra/direccion", content = json.dumps(request))
    assert response.status_code == 200
    assert response.json() == "direccion_actualizada"

def test_orden_compra_cambio_direccion_fallido():
    request = { }
    response = client.put("/orden_compra/direccion", content = json.dumps(request))
    assert response.status_code == 422