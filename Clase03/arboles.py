#%%
# Ejercicio 3.18: Lectura de los árboles de un parque

import csv

tree_list = []
park_list = []

def readList (name_file):
    list = []

    with open(name_file, 'rt', encoding='utf8') as f:
        dict_local = {}
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                dict_local = {
                            headers[0] : float(record[headers[0]]),
                            headers[1] : float(record[headers[1]]),
                            headers[2] : int(record[headers[2]]),
                            headers[3] : int(record[headers[3]]),
                            headers[4] : int(record[headers[4]]),
                            headers[5] : int(record[headers[5]]),
                            headers[6] : int(record[headers[6]]),
                            headers[7] : record[headers[7]],
                            headers[8] : record[headers[8]],
                            headers[9] : record[headers[9]],
                            headers[10] : record[headers[10]],
                            headers[11] : record[headers[11]],
                            headers[12] : record[headers[12]],
                            headers[13] : record[headers[13]],
                            headers[14] : record[headers[14]],
                            headers[15] : float(record[headers[15]]),
                            headers[16] : float(record[headers[16]]),
                            }
                list.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    return list

def parkList(list, park_name):
    list_out = []
    for i in range(len(list)):
        if park_name.upper() == list[i]['espacio_ve']:
            list_out.append(list[i])
    return list_out

tree_list = readList('../Data/arbolado-en-espacios-verdes.csv')
park_list = parkList(tree_list, "GENERAL PAZ")

print(park_list)
print(f'Total de árboles: {len(park_list)}')

#%%
# Ejercicio 3.19: Determinar las especies en un parque

import csv

tree_list = []
species_list = []

def readList (name_file):
    list = []

    with open(name_file, 'rt', encoding='utf8') as f:
        dict_local = {}
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                dict_local = {
                            headers[0] : float(record[headers[0]]),
                            headers[1] : float(record[headers[1]]),
                            headers[2] : int(record[headers[2]]),
                            headers[3] : int(record[headers[3]]),
                            headers[4] : int(record[headers[4]]),
                            headers[5] : int(record[headers[5]]),
                            headers[6] : int(record[headers[6]]),
                            headers[7] : record[headers[7]],
                            headers[8] : record[headers[8]],
                            headers[9] : record[headers[9]],
                            headers[10] : record[headers[10]],
                            headers[11] : record[headers[11]],
                            headers[12] : record[headers[12]],
                            headers[13] : record[headers[13]],
                            headers[14] : record[headers[14]],
                            headers[15] : float(record[headers[15]]),
                            headers[16] : float(record[headers[16]]),
                            }
                list.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    return list

def setList(list, set_name):
    list_out = []
    for i in range(len(list)):
        list_out.append(list[i][set_name])
    list_out = set(list_out)
    return list_out

tree_list = readList('../Data/arbolado-en-espacios-verdes.csv')
set_list = setList(tree_list, 'nombre_com')

print(set_list)
print(f'Total de especies: {len(set_list)}')

#%%
# Ejercicio 3.20: Contar ejemplares por especie
import csv
from collections import Counter
from pprint import pprint

tree_list = []
park_list_1 = []
park_list_2 = []
park_list_3 = []
dict_1 ={}
dict_2 = {}
dict_3 = {}
park_label = ('GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO')
quanty_set = (5)

def readList (name_file):
    list = []

    with open(name_file, 'rt', encoding='utf8') as f:
        dict_local = {}
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                dict_local = {
                            headers[0] : float(record[headers[0]]),
                            headers[1] : float(record[headers[1]]),
                            headers[2] : int(record[headers[2]]),
                            headers[3] : int(record[headers[3]]),
                            headers[4] : int(record[headers[4]]),
                            headers[5] : int(record[headers[5]]),
                            headers[6] : int(record[headers[6]]),
                            headers[7] : record[headers[7]],
                            headers[8] : record[headers[8]],
                            headers[9] : record[headers[9]],
                            headers[10] : record[headers[10]],
                            headers[11] : record[headers[11]],
                            headers[12] : record[headers[12]],
                            headers[13] : record[headers[13]],
                            headers[14] : record[headers[14]],
                            headers[15] : float(record[headers[15]]),
                            headers[16] : float(record[headers[16]]),
                            }
                list.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    return list

def parkList(list, park_name):
    list_out = []
    for i in range(len(list)):
        if park_name.upper() == list[i]['espacio_ve']:
            list_out.append(list[i])
    return list_out

def count_tree(list, quanty):
    dictionary = {}
    tree_counts = Counter(d['nombre_com'] for d in list)
    tree_counts = tree_counts.most_common(quanty)
    for i in range(quanty):
        dict_aux = {
                        tree_counts[i][0] : tree_counts[i][1]
                    }
        dictionary.update(dict_aux)
    return dictionary

tree_list = readList('../Data/arbolado-en-espacios-verdes.csv')
park_list_1 = parkList(tree_list, park_label[0])
park_list_2 = parkList(tree_list, park_label[1])
park_list_3 = parkList(tree_list, park_label[2])

dict_1 = count_tree(park_list_1, quanty_set)
dict_2 = count_tree(park_list_2, quanty_set)
dict_3 = count_tree(park_list_3, quanty_set)

print('%20s' % park_label[0])
print(f'{" ":->21}')
pprint(dict_1)
print('%20s' % park_label[1])
print(f'{" ":->21}')
pprint(dict_2)
print('%20s' % park_label[2])
print(f'{" ":->21}')
pprint(dict_3)

#%%
# Ejercicio 3.21: Alturas de una especie en una lista

import csv
from collections import Counter
from pprint import pprint

tree_list = []
park_list_1 = []
park_list_2 = []
park_list_3 = []
list_1 = []
list_2 = []
list_3 = []
park_label = ('GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO')
tree = 'Jacarandá'

def readList (name_file):
    list = []

    with open(name_file, 'rt', encoding='utf8') as f:
        dict_local = {}
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                dict_local = {
                            headers[0] : float(record[headers[0]]),
                            headers[1] : float(record[headers[1]]),
                            headers[2] : int(record[headers[2]]),
                            headers[3] : int(record[headers[3]]),
                            headers[4] : int(record[headers[4]]),
                            headers[5] : int(record[headers[5]]),
                            headers[6] : int(record[headers[6]]),
                            headers[7] : record[headers[7]],
                            headers[8] : record[headers[8]],
                            headers[9] : record[headers[9]],
                            headers[10] : record[headers[10]],
                            headers[11] : record[headers[11]],
                            headers[12] : record[headers[12]],
                            headers[13] : record[headers[13]],
                            headers[14] : record[headers[14]],
                            headers[15] : float(record[headers[15]]),
                            headers[16] : float(record[headers[16]]),
                            }
                list.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    return list

def parkList(list, park_name):
    list_out = []
    for i in range(len(list)):
        if park_name.upper() == list[i]['espacio_ve']:
            list_out.append(list[i])
    return list_out

def count_tree(list, specie):
    list_aux = []
    for i in range(len(list)):
        if specie == list[i]['nombre_com']:
            d = (specie, list[i]['altura_tot'])
            list_aux.append(d)
    return list_aux

tree_list = readList('../Data/arbolado-en-espacios-verdes.csv')
park_list_1 = parkList(tree_list, park_label[0])
park_list_2 = parkList(tree_list, park_label[1])
park_list_3 = parkList(tree_list, park_label[2])

list_1 = count_tree(park_list_1, tree)
list_2 = count_tree(park_list_2, tree)
list_3 = count_tree(park_list_3, tree)

print(park_label[0])
max_1 = max(list_1)
prom_1 = 0
for i in list_1:
    prom_1 += i[1]
prom_1 = round(prom_1/len(list_1), 2)
print(f'El valor máximo es: {max_1[1]}')
print(f'El promedio es: {prom_1}')
print(park_label[1])
max_1 = max(list_2)
prom_1 = 0
for i in list_2:
    prom_1 += i[1]
prom_1 = round(prom_1/len(list_2), 2)
print(f'El valor máximo es: {max_1[1]}')
print(f'El promedio es: {prom_1}')
print(park_label[2])
max_1 = max(list_3)
prom_1 = 0
for i in list_3:
    prom_1 += i[1]
prom_1 = round(prom_1/len(list_3), 2)
print(f'El valor máximo es: {max_1[1]}')
print(f'El promedio es: {prom_1}')

#%%
# Ejercicio 3.22: Inclinaciones por especie de una lista

import csv
from collections import Counter
from pprint import pprint

tree_list = []
park_list_1 = []
park_list_2 = []
park_list_3 = []
list_1 = []
list_2 = []
list_3 = []
park_label = ('GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO')
tree = 'Jacarandá'

def readList (name_file):
    list = []

    with open(name_file, 'rt', encoding='utf8') as f:
        dict_local = {}
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                dict_local = {
                            headers[0] : float(record[headers[0]]),
                            headers[1] : float(record[headers[1]]),
                            headers[2] : int(record[headers[2]]),
                            headers[3] : int(record[headers[3]]),
                            headers[4] : int(record[headers[4]]),
                            headers[5] : int(record[headers[5]]),
                            headers[6] : int(record[headers[6]]),
                            headers[7] : record[headers[7]],
                            headers[8] : record[headers[8]],
                            headers[9] : record[headers[9]],
                            headers[10] : record[headers[10]],
                            headers[11] : record[headers[11]],
                            headers[12] : record[headers[12]],
                            headers[13] : record[headers[13]],
                            headers[14] : record[headers[14]],
                            headers[15] : float(record[headers[15]]),
                            headers[16] : float(record[headers[16]]),
                            }
                list.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    return list

def parkList(list, park_name):
    list_out = []
    for i in range(len(list)):
        if park_name.upper() == list[i]['espacio_ve']:
            list_out.append(list[i])
    return list_out

def get_inclinations(list, specie):
    list_aux = []
    for i in range(len(list)):
        if specie == list[i]['nombre_com']:
            d = (specie, list[i]['inclinacio'])
            list_aux.append(d)
    return list_aux

tree_list = readList('../Data/arbolado-en-espacios-verdes.csv')
park_list_1 = parkList(tree_list, park_label[0])
park_list_2 = parkList(tree_list, park_label[1])
park_list_3 = parkList(tree_list, park_label[2])

list_1 = get_inclinations(park_list_1, tree)
list_2 = get_inclinations(park_list_2, tree)
list_3 = get_inclinations(park_list_3, tree)

print(park_label[0])
print(list_1)
print(park_label[1])
print(list_2)
print(park_label[2])
print(list_3)

#%%
# Ejercicio 3.23: Especie con el ejemplar más inclinado

import csv
from collections import Counter
from pprint import pprint

tree_list = []
park_list_1 = []
park_list_2 = []
park_list_3 = []
list_1 = []
list_2 = []
list_3 = []
park_label = ('GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO')

def readList (name_file):
    list = []

    with open(name_file, 'rt', encoding='utf8') as f:
        dict_local = {}
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                dict_local = {
                            headers[0] : float(record[headers[0]]),
                            headers[1] : float(record[headers[1]]),
                            headers[2] : int(record[headers[2]]),
                            headers[3] : int(record[headers[3]]),
                            headers[4] : int(record[headers[4]]),
                            headers[5] : int(record[headers[5]]),
                            headers[6] : int(record[headers[6]]),
                            headers[7] : record[headers[7]],
                            headers[8] : record[headers[8]],
                            headers[9] : record[headers[9]],
                            headers[10] : record[headers[10]],
                            headers[11] : record[headers[11]],
                            headers[12] : record[headers[12]],
                            headers[13] : record[headers[13]],
                            headers[14] : record[headers[14]],
                            headers[15] : float(record[headers[15]]),
                            headers[16] : float(record[headers[16]]),
                            }
                list.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    return list

def parkList(list, park_name):
    list_out = []
    for i in range(len(list)):
        if park_name.upper() == list[i]['espacio_ve']:
            list_out.append(list[i])
    return list_out

def more_inclined_specimen(list):
    list_aux = []
    for i in range(len(list)):
        d = (list[i]['nombre_com'], list[i]['inclinacio'])
        list_aux.append(d)
    return max(list_aux, key=lambda item:item[1])

tree_list = readList('../Data/arbolado-en-espacios-verdes.csv')
park_list_1 = parkList(tree_list, park_label[0])
park_list_2 = parkList(tree_list, park_label[1])
park_list_3 = parkList(tree_list, park_label[2])

list_1 = more_inclined_specimen(park_list_1)
list_2 = more_inclined_specimen(park_list_2)
list_3 = more_inclined_specimen(park_list_3)

print(park_label[0])
print(list_1)
print(park_label[1])
print(list_2)
print(park_label[2])
print(list_3)

#%%
#Ejercicio 3.24: Especie más inclinada en promedio

import csv
from collections import Counter

tree_list = []
park_list_1 = []
park_list_2 = []
park_list_3 = []
list_1 = []
list_2 = []
list_3 = []
park_label = ('GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO')

def readList (name_file):
    list = []

    with open(name_file, 'rt', encoding='utf8') as f:
        dict_local = {}
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                dict_local = {
                            headers[0] : float(record[headers[0]]),
                            headers[1] : float(record[headers[1]]),
                            headers[2] : int(record[headers[2]]),
                            headers[3] : int(record[headers[3]]),
                            headers[4] : int(record[headers[4]]),
                            headers[5] : int(record[headers[5]]),
                            headers[6] : int(record[headers[6]]),
                            headers[7] : record[headers[7]],
                            headers[8] : record[headers[8]],
                            headers[9] : record[headers[9]],
                            headers[10] : record[headers[10]],
                            headers[11] : record[headers[11]],
                            headers[12] : record[headers[12]],
                            headers[13] : record[headers[13]],
                            headers[14] : record[headers[14]],
                            headers[15] : float(record[headers[15]]),
                            headers[16] : float(record[headers[16]]),
                            }
                list.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    return list

def parkList(list, park_name):
    list_out = []
    for i in range(len(list)):
        if park_name.upper() == list[i]['espacio_ve']:
            list_out.append(list[i])
    return list_out

def mean_species_most_inclined(list):
    list_aux1 = []
    list_aux2 = []
    for i in range(len(list)):
        list_aux1.append(list[i]['nombre_com'])
        list_aux2.append(list[i]['inclinacio'])
    res = dict.fromkeys(list_aux1, 0)
    tree_counts = Counter(d for d in list_aux1)
    for a, b in zip(list_aux1, list_aux2):
        if tree_counts[a] != 0:
            res[a] += round(b / tree_counts[a], 2)
        else:
            res[a] += b
    return max(res, key=lambda item:item[1])

tree_list = readList('../Data/arbolado-en-espacios-verdes.csv')
park_list_1 = parkList(tree_list, park_label[0])
park_list_2 = parkList(tree_list, park_label[1])
park_list_3 = parkList(tree_list, park_label[2])

list_1 = mean_species_most_inclined(park_list_1)
list_2 = mean_species_most_inclined(park_list_2)
list_3 = mean_species_most_inclined(park_list_3)

print()
print(list_1)
print(list_2)
print(list_3)
