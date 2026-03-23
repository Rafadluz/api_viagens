from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.viagens import ServicoModel, AvaliacaoModel
from app.schema.viagens import ServicoSchema, AvaliacaoSchema

servico = APIRouter()

@servico.post("/servicos")
async def criar_servico(dados: ServicoSchema, db: Session = Depends(get_db)):
    novo_servico = ServicoModel(**dados.model_dump())
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico

@servico.get("/servicos")
async def listar_servicos(db: Session = Depends(get_db)):
    return db.query(ServicoModel).all()

@servico.put("/servicos/{id}/update")
async def atualizar_servico(id: int, dados: ServicoSchema, db: Session = Depends(get_db)):
    servico_existente = db.query(ServicoModel).filter(ServicoModel.id_servico == id).first()
    if not servico_existente:
        return {"mensagem": "Serviço não encontrado"}
    for campo, valor in dados.model_dump().items():
        setattr(servico_existente, campo, valor)
    db.commit()
    db.refresh(servico_existente)
    return servico_existente


@servico.post("/servicos/{id}/avaliacoes")
async def criar_avaliacao(id: int, dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    servico_existente = db.query(ServicoModel).filter(ServicoModel.id_servico == id).first()
    if not servico_existente:
        return {"mensagem": "Serviço não encontrado"}
    nova_avaliacao = AvaliacaoModel(**dados.model_dump(), id_servico=id)
    db.add(nova_avaliacao)
    db.commit()
    db.refresh(nova_avaliacao)
    return nova_avaliacao

@servico.get("/servicos/{id}/avaliacoes")
async def listar_avaliacoes(id: int, db: Session = Depends(get_db)):
    return db.query(AvaliacaoModel).filter(AvaliacaoModel.id_servico == id).all()

@servico.put("/servicos/{id}/avaliacoes/{id_avaliacao}/update")
async def atualizar_avaliacao(id: int, id_avaliacao: int, dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    avaliacao_existente = db.query(AvaliacaoModel).filter(
        AvaliacaoModel.id_avaliacao == id_avaliacao,
        AvaliacaoModel.id_servico == id
    ).first()
    if not avaliacao_existente:
        return {"mensagem": "Avaliação não encontrada"}
    for campo, valor in dados.model_dump().items():
        setattr(avaliacao_existente, campo, valor)
    db.commit()
    db.refresh(avaliacao_existente)
    return avaliacao_existente