from fastapi import FastAPI
from datetime import datetime
from fastapi import HTTPException
app = FastAPI()


@app.get("/")
async def root():
    return {"/": "Seja bem vindo ao sistema de estoque"}

@app.get("/estoque")
async def listar_estoque():
    return estoque_produtos

# Simula um banco de dados
estoque_produtos = [
    {"Id": 1, "nome":"coca cola mini", "quantidade": 24, "validade": "15-03-2027"},
    {"Id": 2, "nome":"coca cola lata", "quantidade": 12, "validade": "12-04-2026"},
    {"Id": 3, "nome":"coca cola 600ml", "quantidade": 8, "validade": "18-04-2026"},
    {"Id": 4, "nome":"coca cola 2litros", "quantidade": 10, "validade": "15-07-2027"}
]

@app.get("/estoque/status")
def verificar_status():
    hoje = datetime.now()
    relatorio = []

    for item in estoque_produtos:
        data_validade = datetime.strptime(item["validade"], "%d-%m-%Y")
        dias_restantes = (data_validade - hoje).days

        if dias_restantes < 0:
            status = "O produto esta vencido, deve ser descartado imediatamente."
        elif dias_restantes <= 5:
            status = "Cuidado - O produto esta proximo da sua data de validade."
        else:
            status = "O prdduto esta com sua data de validade em dia."

        item_analisado = item.copy()
        item_analisado["status"] = status
        relatorio.append(item_analisado)

    return relatorio

@app.post("/estoque/adicionar")
def adicionar_item(nome: str, quantidade: int, validade: str):
    if quantidade < 0:
        raise HTTPException(status_code=400, detail="A quantidade não pode ser negativa.")

    novo_id = len(estoque_produtos) + 1
    novo_item = {
        "Id": novo_id,
        "nome": nome,
        "quantidade": quantidade,
        "validade": validade,
    }
    estoque_produtos.append(novo_item)
    return {"Mensagem": "Item adicionado com sucesso.", "item": novo_item}