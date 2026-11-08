#Terceiro codigo de Hash que escrevi, esse lê pastas e subpastas e cria o Hash de cada arquivo, bem legal.
import hashlib
from pathlib import Path

def hash_file(caminho):   

    h = hashlib.sha256()
    
    with open(caminho, "rb") as f:

        while True:
           
            conteudo = f.read(65536)

            h.update(conteudo)

            if conteudo == b"":

                break

    return h.hexdigest()

def scan(pasta):

    d = {}

    for p in Path(pasta).rglob("*"):

        if p.is_file():

            d[str(p)] = hash_file(p)

    return d

print (scan("teste"))