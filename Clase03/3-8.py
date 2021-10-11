### Ejercicio 3.8: Un ejemplo práctico de enumerate()

import csv

total_cost = 0.0

def costTruck (name_file):
    with open(name_file, 'rt') as f:
            cost = 0.0
            rows = csv.reader(f)
            headers = next(rows)
            for count, row in enumerate(rows):
                try:
                    cost += int(row[1]) * float(row[2])
                except:
                    print(f"Datos no válidos en la línea {count} del archivo.")
    return cost

total_cost = costTruck('../Data/missing.csv')
print(f"Costo total: {round(total_cost, 2)}")