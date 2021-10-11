### Ejercicio 2.9: Funciones de la biblioteca

import csv

f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
for row in rows:
        t = (row[0], 2*int(row[1]), float(row[2]))
        print(t)
f.close()