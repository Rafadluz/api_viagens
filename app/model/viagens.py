from sqlalchemy import Column, BigInteger, Integer, String, Date, DateTime, SmallInteger, CHAR, DECIMAL
from sqlalchemy.dialects.mysql import ENUM, YEAR
from app.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id_usuario = Column(BigInteger, primary_key=True, autoincrement=True)
    nome = Column(String(200), nullable=False)
    cpf = Column(CHAR(11), unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    senha = Column(CHAR(64), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    usuario = Column(String(50), unique=True, nullable=False)

    


class PassageiroModel(Base):
    __tablename__ = "passageiro"

    id_passageiro = Column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario = Column(BigInteger, nullable=False)
    media_avaliacao = Column(DECIMAL(3, 2))


class MotoristaModel(Base):
    __tablename__ = "motorista"

    id_motorista = Column(BigInteger, primary_key=True, autoincrement=True)
    id_usuario = Column(BigInteger, nullable=False)
    media_avaliacao = Column(DECIMAL(3, 2))
    experiencia = Column(String(100))
    cnh = Column(BigInteger, nullable=False)


class MotoristaVeiculoModel(Base):
    __tablename__ = "motorista_veiculo"

    id_motorista = Column(BigInteger, primary_key=True, nullable=False)
    id_veiculo = Column(BigInteger, primary_key=True, nullable=False)
    datahora_inicio = Column(DateTime, nullable=False)
    datahora_fim = Column(DateTime)


class CorridaModel(Base):
    __tablename__ = "corrida"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_passageiro = Column(BigInteger, nullable=False)
    id_motorista = Column(BigInteger, nullable=False)
    id_servico = Column(Integer, nullable=False)
    id_avaliacao = Column(BigInteger)
    datahora_inicio = Column(DateTime, nullable=False)
    datahora_fim = Column(DateTime)
    local_partida = Column(String(50), nullable=False)
    local_destino = Column(String(50), nullable=False)
    valor_estimado = Column(DECIMAL(10, 2))


class PagamentoModel(Base):
    __tablename__ = "pagamento"

    id_pagamento = Column(BigInteger, primary_key=True, autoincrement=True)
    id_corrida = Column(BigInteger, nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    id_metodo_pagamento = Column(SmallInteger, nullable=False)
    datahora_transacao = Column(DateTime, nullable=False)


class MetodoPagamentoModel(Base):
    __tablename__ = "metodo_pagamento"

    id_metodo_pagamento = Column(SmallInteger, primary_key=True, autoincrement=True)
    descricao = Column(String(45), nullable=False)
    nome_financeira = Column(String(45), nullable=False)


class AvaliacaoModel(Base):
    __tablename__ = "avaliacao"

    id_avaliacao = Column(BigInteger, primary_key=True, autoincrement=True)
    comentario = Column(String(45), nullable=False)
    nota = Column(SmallInteger, nullable=False)
    nota_passageiro = Column(SmallInteger, nullable=False)
    nota_motorista = Column(SmallInteger, nullable=False)
    datahora_limite = Column(DateTime, nullable=False)


class ServicoModel(Base):
    __tablename__ = "servico"

    id_servico = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(50), nullable=False)
    preco = Column(DECIMAL(10, 2), nullable=False)
    id_motorista = Column(BigInteger, nullable=False)



class VeiculoModel(Base):
    __tablename__ = "veiculo"

    id_veiculo = Column(BigInteger, primary_key=True, autoincrement=True)
    placa = Column(CHAR(7), nullable=False)
    id_modelo = Column(Integer, nullable=False)
    tem_seguro = Column(SmallInteger, nullable=False)
    id_classe = Column(Integer, nullable=False)


class ModeloVeiculoModel(Base):
    __tablename__ = "modelo_veiculo"

    id_modelo = Column(Integer, primary_key=True, autoincrement=True)
    nome_modelo = Column(String(45), nullable=False)
    cor = Column(String(45), nullable=False)
    fabricante = Column(String(45), nullable=False)
    ano = Column(YEAR, nullable=False)
    capacidade = Column(SmallInteger, nullable=False)
    propriedade = Column(ENUM("Próprio", "Alugado"), nullable=False)
    id_combustivel = Column(Integer, nullable=False)