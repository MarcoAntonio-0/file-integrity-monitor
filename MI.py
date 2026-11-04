import hashlib


def hash_file(caminho):

    h = hashlib.sha256()
    
    with open(caminho, "rb") as f:

        conteudo = f.read()

        h.update(conteudo)

    return h.hexdigest()

print(hash_file("texto.txt"))