### Ejercicio 2.2
### Ejercicio 2.8: Administración de errores
### Ejercicio 2.9: Funciones de la biblioteca

import csv

total_cost = 0.0

def costTruck (name_file):
    with open(name_file, 'rt') as f:
            cost = 0.0
            count = 0
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                count += 1
                try:
                    cost += int(row[1]) * float(row[2])
                except:
                    print(f"Datos no válidos en la línea {count} del archivo.")
    return cost

total_cost = costTruck('../Data/camion.csv')
print(f"Costo total: {round(total_cost, 2)}")