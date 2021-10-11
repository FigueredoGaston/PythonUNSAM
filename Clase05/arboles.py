#Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás

import csv
import numpy as np
import matplotlib.pyplot as plt

def lista_pares(lista):
    arboleda = []
    tree = ['Jacarandá']

    arboleda = [(float(arbol['altura_tot']), float(arbol['diametro']), ) for arbol in lista if arbol['nombre_com'] in tree]
    return arboleda

def leer_arboles(name_file):
    types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
    lista = []
    dict_local = {}

    with open(name_file, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            try:
                converted = [func(val) for func, val in zip(types, row)]
                dict_local = dict(zip(headers, converted))
                lista.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    lista = lista_pares(lista)
    return lista

def scatter_hd(lista_de_pares):
    d = np.array(list(i[0] for i in lista_de_pares), dtype=np.int64)
    h = np.array(list(i[1] for i in lista_de_pares), dtype=np.int64)
    plt.scatter(d,h, c=np.random.rand(len(h)), alpha=0.5)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()


def main():
   scatter_hd(leer_arboles('../Data/arbolado-en-espacios-verdes.csv'))
