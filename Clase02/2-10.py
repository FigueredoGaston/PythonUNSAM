### Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros

import csv

total_cost = 0.0

def costTruck (name_file):
    with open(name_file, 'rt') as f:
            cost = 0.0
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                try:
                    cost += int(row[1]) * float(row[2])
                except:
                    print(f"Datos no válidos.")
    return cost

total_cost = costTruck('../Data/camion.csv')
print(f"Costo total: {round(total_cost, 2)}")