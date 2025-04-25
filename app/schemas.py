from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    email: str
    idade: int

class UsuarioCreate(UsuarioBase):
    pass