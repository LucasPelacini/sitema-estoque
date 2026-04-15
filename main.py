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
