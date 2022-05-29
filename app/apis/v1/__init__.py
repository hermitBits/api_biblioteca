from . import autores

from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(autores.router, prefix="/autores", tags=["autores"])
