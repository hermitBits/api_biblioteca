from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
