#Ejercicio 4.13: Diccionarios

import csv

types = [str, int, float]


f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
r = list(zip(types, row))
converted = []
''' for func, val in zip(types, row):
    converted.append(func(val))
'''
converted = [func(val) for func, val in zip(types, row)]

f.close()

print(converted)
print(converted[1] * converted[2])
print(dict(zip(headers, converted)))
print({ name: func(val) for name, func, val in zip(headers, types, row) })