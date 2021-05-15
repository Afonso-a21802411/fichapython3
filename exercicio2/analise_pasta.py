import json
import csv
import os
from typing import Counter

def pede_pasta(caminho) :
    if os.path.isdir(caminho)==True:
        caminhoPasta= caminho
    else:
        print("Não é o caminho para uma pasta")
def faz_calculos():
    listaFicheiros = os.listdir(caminhoPasta)
    volumeTotal= 0
    count= len(listaFicheiros)
    my_dict = {}
    my_dict_values = {
        "volume": 0,
        "quantidade": 0
    }
    for x in listaFicheiros:
        name, extension = os.path.splitext(os.path.join(caminhoPasta, x))
        if extension in dict:
             my_dict_values["volume"] += ((os.path.getsize(x))/1024)
             my_dict_values["quantidade"] += 1
        else:
            my_dict[extension] = my_dict_values

def guarda_resultados():
    try:
        csv_columns = ["Tipo","Volume","Quantidade"]
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in my_dict:
                writer.writerow(data)
    except IOError:
        print("IO ERROR")

def faz_graficos_queijos():
    

