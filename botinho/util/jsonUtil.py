import json
from sqlite3 import Cursor

def get_keys_name(dados:dict)->str:
    return "\n".join(dados.keys())

def get_values(dados:dict):
    retorno = ""
    for categorias, elementos in dados.items():
        texto = []
        retorno += f"{categorias.capitalize()}\n"
        for elemento in elementos:
            for key, val in elemento.intems():
                texto.append(f"{key.capitalize()}:{val}")
        retorno += ", ".join(texto)
    return retorno