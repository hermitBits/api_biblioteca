from pydantic import BaseModel


class ObraSchema(BaseModel):
    id: int
    titulo: int
    autor: int
    editora: int
    foto: str
    
    class Config:
        orm_mode = True