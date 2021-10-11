#Ejercicio 4.14: Fijando ideas

import csv

types = [str, float, str, str, float, float, float, float, int]
date = [int, int, int]

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
date_1 = [func(val) for func, val in zip(date, str.split(record['date'], '/'))] #Con str.split('/') separo la cadena por /
f.close()

print(record)
print(date_1)