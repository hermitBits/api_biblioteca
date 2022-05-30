from database.session import Base
from sqlalchemy import Column, Integer, String


class Autor(Base):
    __tablename__ = 'autores'
    
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(254), unique=True)
