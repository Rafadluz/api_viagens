from pydantic import BaseModel
from typing import Optional

class CorridaSchema(BaseModel):
    caminho: str
    avaliacao: Optional[str] = None
    datahora_inicio: int
    datahora_fim: int
    local_partida: int
    local_destino: int
    valor_estimado: int

    class Config:
        from_attributes = True