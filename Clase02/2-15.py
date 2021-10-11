### Ejercicio 2.15: Lista de tuplas

import csv

list_out = []

def readTruck (name_file):
    truck = []
    count = 0
    lot = ()
    cost = 0.0

    with open(name_file, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                count += 1
                try:
                    lot = (row[0], int(row[1]), float(row[2]))
                    cost += lot[1] * lot[2]
                    truck.append(lot)
                except:
                    print(f"Datos no válidos en la línea {count} del archivo.")
    return [truck,cost]

list_out = readTruck('../Data/camion.csv')
print(list_out[0])
print(f"Costo total: {round(list_out[1], 2)}")