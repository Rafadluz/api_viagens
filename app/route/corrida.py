from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.viagens import CorridaModel
from app.schema.viagens import CorridaSchema

corrida = APIRouter()

@corrida.post("/")
async def criar_corrida(dados: CorridaSchema, db: Session = Depends(get_db)):
    nova_corrida = CorridaModel(**dados.model_dump())
    db.add(nova_corrida)
    db.commit()
    db.refresh(nova_corrida)
    return nova_corrida

@corrida.get("/corridas")
async def listar_corridas(db: Session = Depends(get_db)):
    return db.query(CorridaModel).all()

@corrida.put("/corridas/{id}/update")
async def atualizar_corrida(id: int, dados: CorridaSchema, db: Session = Depends(get_db)):
    corrida_existente = db.query(CorridaModel).filter(CorridaModel.id == id).first()
    if not corrida_existente:
        return {"mensagem": "Corrida não encontrada"}
    for campo, valor in dados.model_dump().items():
        setattr(corrida_existente, campo, valor)
    db.commit()
    db.refresh(corrida_existente)
    return corrida_existente

@corrida.delete("/corridas/{id}")
async def deletar_corrida(id: int, db: Session = Depends(get_db)):
    corrida_existente = db.query(CorridaModel).filter(CorridaModel.id_corrida == id).first()
    if not corrida_existente:
        return {"mensagem": "Corrida não encontrada"}
    db.delete(corrida_existente)
    db.commit()
    return {"mensagem": "Corrida deletada com sucesso"}