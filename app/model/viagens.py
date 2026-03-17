from sqlalchemy import Column, Integer, String
from app.database import Base

class CorridaModel(Base):
    __tablename__ = "corrida"

    id = Column(Integer, primary_key=True, autoincrement=True)
    caminho = Column(String(100), nullable=False)
    avaliacao = Column(String(255))
    datahora_inicio = Column(Integer)
    datahora_fim = Column(Integer)
    local_partida = Column(String(255))
    local_destino = Column(String(255))
    valor_estimado = Column(Integer)