import hashlib


def hash_file(caminho):   

    h = hashlib.sha256()
    
    with open(caminho, "rb") as f:

        while True:
           
            conteudo = f.read(4)

            h.update(conteudo)

            if conteudo == b"":

                break

    return h.hexdigest()

print(hash_file("grande.bin"))