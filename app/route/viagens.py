from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.viagens import CorridaModel
from app.schema.viagens import CorridaSchema

@corrida.post("/")
async def criar_serie(dados: CorridaSchema, db: Session = Depends(get_db)):
    nova_corrida = CorridaModel(**dados.model_dump())
    db.add(nova_corrida)
    db.commit()
    db.refresh(nova_corrida)
    return nova_corrida