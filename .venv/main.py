from fastapi import FastAPI
from routes.financeiro_routes import router as financeiro_router

app = FastAPI(title="API Controle Financeiro")

app.include_router(financeiro_router)


@app.get("/")
def home():
    return {"mensagem": "Backend de Controle Fincanceiro com FastAPI"}