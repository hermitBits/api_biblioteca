from database.session import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Obra(Base):
    __tablename__ = 'obras' 
    
    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String(254))
    autor_id = Column(Integer, ForeignKey("autores.id"))
    editora_id = Column(Integer, ForeignKey("editoras.id"))