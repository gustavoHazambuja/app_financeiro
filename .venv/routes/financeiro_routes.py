#CRIANDO AS ROTAS PARA AS REQUISIÇÕES HTTP

from fastapi import APIRouter
from controllers.financeiro_controller import(
    listar_transacoes,
    criar_transacao,
    calculcar_saldo
)

from models.transacao_model import Transacao

router = APIRouter(prefix="/financeiro", tags=["Financeiro"])

@router.get("/transacoes")
def get_transacoes():
    return listar_transacoes()


@router.post("/transacoes")
def post_transacoes(transacao: Transacao):
    return criar_transacao(transacao)


@router.get("/saldo")
def get_saldo():
    return calculcar_saldo()