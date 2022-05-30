from database.models import Autor
from schemas import CreateAutorSchema

from fastapi import HTTPException

from sqlalchemy.exc import *
from sqlalchemy.orm import Session


def criar_autor(autor: CreateAutorSchema, db: Session):
    try:
        autor_obj = Autor(**autor.dict())
        db.add(autor_obj)
        db.commit()
        db.refresh(autor_obj)
        return autor_obj
    except IntegrityError as e:
        errorInfo = e.orig.args[1]
        raise HTTPException(status_code=400, 
                            detail=errorInfo)


def procurar_autor(id: int, db: Session):
    autor = db.query(Autor).filter(Autor.id == id).first()
    return autor


def listar_autores(db: Session, nome: str = None):
    if nome is None:
        autores = db.query(Autor).all()
    else: 
        autores= db.query(Autor).filter(Autor.nome.in_([nome])).all() 
    return autores


def atualizar_autor_by_id(id: int, autor: CreateAutorSchema, db: Session):
    autor_obj = db.query(Autor).filter(Autor.id == id)
    if not autor_obj.first():
        return 0
    autor_obj.update(autor.dict())
    db.commit()
    return 1


def apagar_autor_by_id(id: int, db: Session):
    autor_obj = db.query(Autor).filter(Autor.id == id)
    if not autor_obj.first():
        return 0
    autor_obj.delete()
    db.commit()
    return 1