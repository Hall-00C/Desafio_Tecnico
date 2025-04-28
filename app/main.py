from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Banco de dados "fake" em memória (para evitar PostgreSQL por enquanto)
db_usuarios = []

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    idade: int

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    idade: int

# GET /usuarios
@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios():
    return db_usuarios

# POST /usuarios
@app.post("/usuarios", response_model=Usuario)
def criar_usuario(usuario: UsuarioCreate):
    novo_usuario = Usuario(
        id=len(db_usuarios) + 1,
        nome=usuario.nome,
        email=usuario.email,
        idade=usuario.idade
    )
    db_usuarios.append(novo_usuario)
    return novo_usuario

# GET /usuarios/{id}
@app.get("/usuarios/{usuario_id}", response_model=Usuario)
def buscar_usuario(usuario_id: int):
    for usuario in db_usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# PUT /usuarios/{id}
@app.put("/usuarios/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: int, usuario: UsuarioCreate):
    for index, user in enumerate(db_usuarios):
        if user.id == usuario_id:
            db_usuarios[index] = Usuario(
                id=usuario_id,
                nome=usuario.nome,
                email=usuario.email,
                idade=usuario.idade
            )
            return db_usuarios[index]
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# DELETE /usuarios/{id}
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for index, user in enumerate(db_usuarios):
        if user.id == usuario_id:
            db_usuarios.pop(index)
            return {"message": "Usuário deletado"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")