from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.viagens import VeiculoModel, ModeloVeiculoModel
from app.schema.viagens import VeiculoSchema, ModeloVeiculoSchema


veiculo = APIRouter()

@veiculo.post("/")
async def criar_veiculo(dados_veiculo: VeiculoSchema, dados_modelo: ModeloVeiculoSchema, db: Session = Depends(get_db)):
    novo_modelo = ModeloVeiculoModel(**dados_modelo.model_dump())
    db.add(novo_modelo)
    db.commit()
    db.refresh(novo_modelo)

    novo_veiculo = VeiculoModel(**dados_veiculo.model_dump(), id_modelo=novo_modelo.id_modelo)
    db.add(novo_veiculo)
    db.commit() 
    db.refresh(novo_veiculo) 
    return {"veiculo": novo_veiculo, "modelo": novo_modelo}


@veiculo.get("/veiculos") 
async def listar_veiculos(db: Session = Depends(get_db)):
    veiculos = db.query(VeiculoModel).all()
    modelos = db.query(ModeloVeiculoModel).all()
    return {"veiculos": veiculos, "modelos": modelos}


@veiculo.put("/veiculos/{id}/update") 
async def atualizar_veiculo(id: int, dados_veiculo: VeiculoSchema, dados_modelo: ModeloVeiculoSchema, db: Session = Depends(get_db)):
    veiculo_existente = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id).first()
    if not veiculo_existente:
        return {"mensagem": "Veículo não encontrado"}

    modelo_existente = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id_modelo == veiculo_existente.id_modelo).first()

    for campo, valor in dados_veiculo.model_dump().items():
        setattr(veiculo_existente, campo, valor)

    for campo, valor in dados_modelo.model_dump().items():
        setattr(modelo_existente, campo, valor)

    db.commit()
    db.refresh(veiculo_existente)
    db.refresh(modelo_existente)
    return {"veiculo": veiculo_existente, "modelo": modelo_existente}


@veiculo.delete("/veiculos/{id}")
async def deletar_veiculo(id: int, db: Session = Depends(get_db)):
    veiculo_existente = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id).first()
    if not veiculo_existente:
        return {"mensagem": "Veículo não encontrado"}
    db.delete(veiculo_existente)
    db.commit()
    return {"mensagem": "Veículo deletado com sucesso"}