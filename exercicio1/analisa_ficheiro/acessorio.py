import json

def pede_nome(nome):
    try: 
        f= open(nome,'r')
        f.close()
        return nome
    except OSError:
        print("Não conseguiu abriu o ficheiro", nome)
def gera_nome(nome):
    dictStore = {}
    f = open(nome, 'r')
    dictStore.add(f.read)
    nomeJ= nome +".json"
    with open(nomeJ,'w') as json_file:
        json.dump(dictStore, json_file, indent=4)
    