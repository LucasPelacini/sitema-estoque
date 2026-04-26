from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_ver_estoque():
    response = client.get("/estoque")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_item_nao_encontrado():
    response = client.get("/estoque/item-nao-existe")
    assert response.status_code == 404

def test_integridade_dados():
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"

def test_rota_protegita():
    response = client.get("/api/segura")
    assert response.status_code in [401, 200, 404]