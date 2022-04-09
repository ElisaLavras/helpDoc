import re 

CATEGORIAS = "categorias_"
DOCUMENTADOS = "_documentado"

def remover_caractares(texto):
    return re.sub(r"[^a-zA-Z0-9]"," ",texto)

def remover_categorias(texto):
    return re.sub(CATEGORIAS,texto)

def remover_documentado(texto):
    return re.sub(DOCUMENTADOS,texto)

def get_palavras(texto):
    return texto.split(" ")