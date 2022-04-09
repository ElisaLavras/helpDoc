from typing import Any, List
from pymongo import MongoClient
import util.stringUtil as stringUtil
import util.jsonUtil as jsonUtil

URL_BANCO ="mongodb://root:example@127.0.1:27017"

CATEGORIAS = "categorias_"
DOCUMENTADOS = "_documentado"

MENSAGEM_DEFAULT = "Desculpa, não entendi."

MENSAGEM_BD = "buscar_banco"

cliente = MongoClient(URL_BANCO)
meuBanco = cliente["botinho"]

def get_categorias(menssagem):
    menssagem = stringUtil.remover_categorias(menssagem)
    colecao=meuBanco[menssagem]
    documento = colecao.find_one()
    return jsonUtil.get_keys_name(documento)

def get_lista(texto:str, lista:List[Any])->str:
    return "\n".join([item[texto] for item in lista])

def get_elementos_documentados(mensagem):
    name = "name"
    menssagem = stringUtil.remover_documentado(menssagem)
    colecao = meuBanco[menssagem]
    lista = colecao.find({},{name:1,"_id":0})
    return get_lista(name,lista)

def get_opcoes(mensagem,resposta):
    if CATEGORIAS in mensagem:
        return resposta.replace(MENSAGEM_BD,get_categorias(mensagem))
    elif DOCUMENTADOS in mensagem:
        return resposta.replace(MENSAGEM_BD,get_elementos_documentados(mensagem))
    return ""

def get_documentaoes(mensagem,resposta):
    
    return

def get_resposta(mensagem,resposta):
    if resposta == MENSAGEM_DEFAULT:
        return get_documentaoes(mensagem,resposta)
    elif MENSAGEM_BD in resposta:   
        return get_opcoes(mensagem,resposta)
    return