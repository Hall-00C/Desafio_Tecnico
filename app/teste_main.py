from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_usuario():
    response = client.post("/usuarios", json={"nome": "João", "email": "joao@email.com", "idade": 30})
    assert response.status_code == 200
    assert response.json()["nome"] == "João"

def test_listar_usuarios():
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_buscar_usuario_por_id():
    # Primeiro, cria um usuário
    client.post("/usuarios", json={"nome": "Maria", "email": "maria@email.com", "idade": 25})
    
    # Depois, busca o usuário pelo ID
    response = client.get("/usuarios/1")
    assert response.status_code == 200
    assert response.json()["nome"] == "Maria"

    def test_deletar_usuario():
        # Primeiro, cria um usuário
        client.post("/usuarios", json={"nome": "Carlos", "email": "carlos@email.com", "idade": 40})
        
        # Depois, deleta o usuário pelo ID
        response = client.delete("/usuarios/1")
        assert response.status_code == 200
        
        # Verifica se o usuário foi removido
        response = client.get("/usuarios")
        assert len(response.json()) == 0