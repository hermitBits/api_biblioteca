from database.models import Autor
from schemas import CreateAutorSchema

from sqlalchemy.orm import Session

def criar_autor(autor: CreateAutorSchema, db: Session):
    autor_obj = Autor(**autor.dict())
    db.add(autor_obj)
    db.commit()
    db.refresh(autor_obj)
    return autor_obj