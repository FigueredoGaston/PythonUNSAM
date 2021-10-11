#Ejercicio 4.18: Diccionario con medidas

import csv

arboleda = []
H = []
tree = ['Jacarandá']

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

def medidas_de_especies(especies,arboleda):
    especie0 = [(float(arbol['altura_tot']), float(arbol['diametro']), ) for arbol in arboleda if arbol['nombre_com'] in especies[0]]
    especie1 = [(float(arbol['altura_tot']), float(arbol['diametro']), ) for arbol in arboleda if arbol['nombre_com'] in especies[1]]
    especie2 = [(float(arbol['altura_tot']), float(arbol['diametro']), ) for arbol in arboleda if arbol['nombre_com'] in especies[2]]
    dic_1 = {especies[0]:i for i in especie0}
    print(dic_1)
    #return dict(zip(especies, (especie0, especie1, especie2)))

def main():
    especies_m = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    arboles = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    medidas_de_especies(especies_m, arboles)

main()
