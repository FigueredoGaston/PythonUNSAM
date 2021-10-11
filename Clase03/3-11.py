### Ejercicio 3.11: Contadores

import csv
from collections import Counter

list_out = []
list_out2 = []

def readTruck (name_file):
    truck = []
    count = 0
    cost = 0.0

    with open(name_file, 'rt') as f:
            dict_local = {}
            rows = csv.reader(f)
            headers = next(rows)
            for count, row in enumerate(rows):
                record = dict(zip(headers, row))
                try:
                    dict_local = {
                            'nombre' : record['nombre'],
                            'precio' : float(record['precio']),
                            'cajones' : int(record['cajones'])
                            }
                    cost += dict_local['cajones'] * dict_local['precio']
                    truck.append(dict_local)
                except:
                    print(f"Datos no válidos en la línea {count+1} del archivo.")
    return [truck,cost, count]

list_out = readTruck('../Data/camion.csv')

tenencias = Counter()
for s in list_out[0]:
    tenencias[s['nombre']] += s['cajones']
print(tenencias)
print(tenencias['Naranja'])
print(tenencias.most_common(3)) # Las 3 frutas con más cajones

list_out2 = readTruck('../Data/camion2.csv')

tenencias2 = Counter()
for s in list_out2[0]:
    tenencias2[s['nombre']] += s['cajones']
print(tenencias2)
print(tenencias2['Durazno'])
print(tenencias2.most_common(3)) # Las 3 frutas con más cajones

print(list_out + list_out2)