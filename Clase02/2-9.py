### Ejercicio 2.9: Funciones de la biblioteca

import csv

f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
for row in rows:
        print(row)
f.close()