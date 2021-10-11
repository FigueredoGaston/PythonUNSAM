### Ejercicio 2.13: Más operaciones con diccionarios

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
        for k in d:
            print(k, '=', d[k])
        items = d.items()
        for k, v in d.items():
            print(k, '=', v)
        print(f"Costo: {round(d['cajones'] * d['precio'], 2)}")
f.close()