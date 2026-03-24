from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.viagens import UsuarioModel, PassageiroModel, MotoristaModel
from app.schema.viagens import UsuarioSchema, PassageiroSchema, MotoristaSchema

usuario = APIRouter()


@usuario.post("/usuarios")
async def criar_usuario(dados: UsuarioSchema, db: Session = Depends(get_db)):
    novo_usuario = UsuarioModel(**dados.model_dump())
    db.add(novo_usuario)  # adicionar o objeto na sessão
    db.commit() # grava no banco
    db.refresh(novo_usuario) # atualiza o objeto com os dados salvos
    return novo_usuario

@usuario.get("/usuarios") # busca no banco de dados
async def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()


@usuario.post("/usuarios/{id}/passageiro")
async def criar_passageiro(id: int, dados: PassageiroSchema, db: Session = Depends(get_db)):
    usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id).first()
    if not usuario_existente:
        return {"mensagem": "Usuário não encontrado"}
    novo_passageiro = PassageiroModel(**dados.model_dump(), id_usuario=id)
    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)
    return novo_passageiro

@usuario.post("/usuarios/{id}/motorista")
async def criar_motorista(id: int, dados: MotoristaSchema, db: Session = Depends(get_db)):
    usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id).first()
    if not usuario_existente:
        return {"mensagem": "Usuário não encontrado"}
    novo_motorista = MotoristaModel(**dados.model_dump(), id_usuario=id)
    db.add(novo_motorista)
    db.commit()
    db.refresh(novo_motorista)
    return novo_motorista


@usuario.put("/usuarios/{id}/update") # atualiza os dados
async def atualizar_usuario(id: int, dados: UsuarioSchema, db: Session = Depends(get_db)):
    usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id).first()
    if not usuario_existente:
        return {"mensagem": "Usuário não encontrado"}
    for campo, valor in dados.model_dump().items():
        setattr(usuario_existente, campo, valor)
    db.commit()
    db.refresh(usuario_existente)
    return usuario_existente


@usuario.delete("/usuarios/{id}")
async def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario_existente = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == id).first()
    if not usuario_existente:
        return {"mensagem": "Usuário não encontrado"}
    db.delete(usuario_existente)
    db.commit()
    return {"mensagem": "Usuário deletado com sucesso"}
