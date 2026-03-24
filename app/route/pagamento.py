from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.viagens import PagamentoModel, MetodoPagamentoModel
from app.schema.viagens import PagamentoSchema, MetodoPagamentoSchema

pagamento = APIRouter()


@pagamento.post("/pagamentos")
async def criar_pagamento(dados_pagamento: PagamentoSchema, dados_metodo: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    novo_metodo = MetodoPagamentoModel(**dados_metodo.model_dump())
    db.add(novo_metodo)
    db.commit()
    db.refresh(novo_metodo)

    novo_pagamento = PagamentoModel(**dados_pagamento.model_dump(), id_metodo=novo_metodo.id_metodo)
    db.add(novo_pagamento)
    db.commit()
    db.refresh(novo_pagamento)
    return {"pagamento": novo_pagamento, "metodo": novo_metodo}

@pagamento.get("/pagamentos")
async def listar_pagamentos(db: Session = Depends(get_db)):
    pagamentos = db.query(PagamentoModel).all()
    metodos = db.query(MetodoPagamentoModel).all()
    return {"pagamentos": pagamentos, "metodos": metodos}

@pagamento.put("/pagamentos/{id}/update")
async def atualizar_pagamento(id: int, dados_pagamento: PagamentoSchema, dados_metodo: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    pagamento_existente = db.query(PagamentoModel).filter(PagamentoModel.id_pagamento == id).first()
    if not pagamento_existente:
        return {"mensagem": "Pagamento não encontrado"}

    metodo_existente = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo == pagamento_existente.id_metodo).first()

    for campo, valor in dados_pagamento.model_dump().items():
        setattr(pagamento_existente, campo, valor)

    for campo, valor in dados_metodo.model_dump().items():
        setattr(metodo_existente, campo, valor)

    db.commit()
    db.refresh(pagamento_existente)
    db.refresh(metodo_existente)
    return {"pagamento": pagamento_existente, "metodo": metodo_existente}

@pagamento.delete("/pagamentos/{id}")
async def deletar_pagamento(id: int, db: Session = Depends(get_db)):
    pagamento_existente = db.query(PagamentoModel).filter(PagamentoModel.id_pagamento == id).first()
    if not pagamento_existente:
        return {"mensagem": "Pagamento não encontrado"}
    db.delete(pagamento_existente)
    db.commit()
    return {"mensagem": "Pagamento deletado com sucesso"}