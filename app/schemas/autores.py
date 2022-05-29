from pydantic import BaseModel


class AutorSchema(BaseModel):
    nome: str
 
    
class CreateAutorSchema(AutorSchema):
    nome: str
 
    
class ShowAutorSchema(AutorSchema):
    id: int
    nome: str
    
    class Config:
        orm_mode = True