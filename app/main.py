from fastapi import FastAPI
from app.database import Base, engine
from app.route.usuario import usuario
from app.route.veiculo import veiculo
from app.route.corrida import corrida
from app.route.servico import servico
from app.route.pagamento import pagamento


Base.metadata.create_all(bind=engine) # cria todas as tabelas definidas e executa no banco


app = FastAPI(title="Viagens API")


app.include_router(usuario, prefix="/api", tags=["Usuários"])
app.include_router(veiculo, prefix="/api", tags=["Veículos"])
app.include_router(corrida, prefix="/api", tags=["Corridas"])
app.include_router(servico, prefix="/api", tags=["Serviços"])
app.include_router(pagamento, prefix="/api", tags=["Pagamentos"])


@app.get("/")
async def health_check():
    return {"status": "API Online"}