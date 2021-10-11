#Ejercicio 4.15: Lectura de todos los árboles

import csv

arboleda = []

def leer_arboles(name_file):
    types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
    list = []
    dict_local = {}

    with open(name_file, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            try:
                converted = [func(val) for func, val in zip(types, row)]
                dict_local = dict(zip(headers, converted))
                list.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    return list

def main():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    print(arboleda)
