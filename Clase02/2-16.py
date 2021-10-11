### Ejercicio 2.16: Lista de diccionarios

import csv

list_out = []

def readTruck (name_file):
    truck = []
    count = 0
    cost = 0.0

    with open(name_file, 'rt') as f:
            dict = {}
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                count += 1
                try:
                    dict = {
                            'nombre' : row[0],
                            'precio' : float(row[2]),
                            'cajones' : int(row[1])
                            }
                    cost += dict['cajones'] * dict['precio']
                    truck.append(dict)
                except:
                    print(f"Datos no válidos en la línea {count} del archivo.")
    return [truck,cost]

list_out = readTruck('../Data/camion.csv')
for k in list_out[0]:
    print(k)
print(f"Costo total: {round(list_out[1], 2)}")