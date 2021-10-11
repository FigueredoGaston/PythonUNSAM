### Ejercicio 2.12: Diccionarios como estructuras de datos

import csv

f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
for row in rows:
        d = {
            'nombre' : row[0],
            'cajones' : int(row[1]),
            'precio' : float(row[2]),
            'cuenta' : 12345
        }
        print(d)
        print(f"Costo: {round(d['cajones'] * d['precio'], 2)}")
f.close()