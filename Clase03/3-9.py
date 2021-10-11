### Ejercicio 3.9: La función zip()

import csv

total_cost = 0.0

def costTruck (name_file):
    cost = 0.0

    with open(name_file, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for count, row in enumerate(rows):
                record = dict(zip(headers, row))
                try:
                    cost += int(record['cajones']) * float(record['precio'])
                except:
                    print(f"Datos no válidos en la línea {count} del archivo.")
    return cost

total_cost = costTruck('../Data/fecha_camion.csv')
print(f"Costo total: {round(total_cost, 2)}")