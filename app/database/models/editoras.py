from database.session import Base
from sqlalchemy import Column, Integer, String


class Editora(Base):
    __tablename__ = 'editoras'
    
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(254))
