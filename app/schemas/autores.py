from pydantic import BaseModel


class AutorSchema(BaseModel):
    id: int
    nome: str
    
    class Config:
        orm_mode = True