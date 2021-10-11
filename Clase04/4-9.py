#Ejercicio 4.9: Consultas de datos

import csv

precios = {}
camion = []
costo = 0.0
valor = 0.0

def leer_precios(name_file):
    dict_local = {}

    with open(name_file, 'rt') as f:
        rows = csv.reader(f)
        for count, row in enumerate(rows):
            try:
                dict_local[row[0]] = float(row[1])
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.") ###Con esto sé en que linea me genera un error
    return dict_local

def leer_camion(name_file):
    truck = []
    dict_local = {}

    with open(name_file, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for count, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                dict_local = {
                        'nombre' : record['nombre'],
                        'precio' : float(record['precio']),
                        'cajones' : int(record['cajones'])
                        }
                truck.append(dict_local)
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.")
    return truck

def main():
    camion = leer_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    mas100 = [s for s in camion if s['cajones'] > 100]
    myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]
    costo10k = [s for s in camion if s['cajones'] * s['precio'] > 10000]
    print(mas100)
    print(myn)
    print(costo10k)
