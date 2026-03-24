from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional



class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    cpf: int
    data_nascimento: date
    usuario: str

    class Config:
        from_attributes = True



class PassageiroSchema(BaseModel):
    media_avaliacao: Optional[int] = None
    class Config:
        from_attributes = True



class MotoristaSchema(BaseModel):
    cnh: int
    experiencia: Optional[str] = None
    media_avaliacao: Optional[int] = None
    class Config:
        from_attributes = True


        


class ModeloVeiculoSchema(BaseModel):
    fabricante: str
    cor: str
    nome_modelo: str
    ano: int

    class Config:
        from_attributes = True


class VeiculoSchema(BaseModel):
    placa: str
    id_motorista: int
    id_combustivel: int

    class Config:
        from_attributes = True



class TipoCombustivelSchema(BaseModel):
    nome: str

    class Config:
        from_attributes = True



class CorridaSchema(BaseModel):
    origem: str
    destino: str
    distancia_km: float
    valor: float
    id_passageiro: int
    id_motorista: int
    id_veiculo: int

    class Config:
        from_attributes = True


class ServicoSchema(BaseModel):
    descricao: str
    preco: float
    id_motorista: int

    class Config:
        from_attributes = True



class AvaliacaoSchema(BaseModel):
    nota: int
    comentario: Optional[str] = None
    id_servico: int
    id_passageiro: int
    nota_passageiro: int
    nota_motorista: int
    datahora_limite: datetime

    class Config:
        from_attributes = True


class PagamentoSchema(BaseModel):
    valor: float
    data: str
    id_usuario: int
    id_metodo: int

    class Config:
        from_attributes = True


class MetodoPagamentoSchema(BaseModel):
    tipo: str