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