from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    username: str
    nombre: str
    rol: str
    estado: int

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: str
    nombre: str
    rol: str
    estado: str


    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje:str