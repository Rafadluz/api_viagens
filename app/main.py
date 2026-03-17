from fastapi import FastAPI
from app.database import Base, engine
from app.route.viagens import corrida

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(corrida)

@app.get("/")
async def health_check():
    return {"status": "API Online"}