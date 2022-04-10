import re 

CATEGORIAS = "categorias"
DOCUMENTADOS = "documentados"
DOCUMENTADAS = "documentadas"

def remover_caractares(texto):
    return re.sub(r"[^a-zA-Z0-9]"," ",texto).strip()

def remover_categorias(texto:str) -> str:
    return texto.replace(CATEGORIAS,"").strip()

def remover_documentado(texto:str)->str:
    return texto.replace(DOCUMENTADAS,"").replace(DOCUMENTADOS,"").strip()

def get_palavras(texto):
    return texto.split(" ")