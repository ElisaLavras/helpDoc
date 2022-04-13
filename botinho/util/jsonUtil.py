import json
from sqlite3 import Cursor
from typing import Type

def get_keys_name(dados:dict)->str:
    return "\n".join(dados.keys())

def get_values(dados:dict):
    retorno = ""
    for categorias, elementos in dados.items():
        if type(elementos) == list:
            texto = []
            retorno += f"{categorias.capitalize()}\n"
            for elemento in elementos:
                if type(elemento) == dict:
                    for key, val in elemento.items():
                        texto.append(f"{key.capitalize()}:{val}")
                elif type(elemento) == str:
                    texto.append(elemento.capitalize())
            retorno += "\n ".join(texto)
        elif type(elementos) == str:
            retorno += f"{categorias.capitalize()}: {elementos.capitalize()}"

    return retorno

    {"status" : "producao"}