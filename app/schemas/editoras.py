from pydantic import BaseModel


class EditoraSchema(BaseModel):
    id: int
    nome: str
    
    class Config:
        orm_mode = True