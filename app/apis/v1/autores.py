from typing import List

from database.session import get_db

from fastapi import APIRouter
from fastapi import Depends

from schemas import ShowAutorSchema 
from schemas import CreateAutorSchema

from sqlalchemy.orm import Session

from database.repository import criar_autor
from database.repository import listar_autores
from database.repository import procurar_autor


router = APIRouter()


@router.post("/criar_autor/", response_model=ShowAutorSchema)
def create_autor(
    autor: CreateAutorSchema, 
    db: Session = Depends(get_db)
):
    autor = criar_autor(
        autor=autor,
        db=db
    )
    return autor
    

@router.get("/autores", response_model=List[ShowAutorSchema])
def list_autores(
    db: Session = Depends(get_db),
    nome: str = None
):
    autores = listar_autores(db, nome)
    return autores