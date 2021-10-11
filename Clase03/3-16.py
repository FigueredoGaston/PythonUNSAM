# Ejercicio 3.13: Recolectar datos

import csv

fruit_dictionary = {}
list_truck = []
list_final = []
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

def fruitPrice(name_file):
    dict_local = {}

    with open(name_file, 'rt') as f:
        rows = csv.reader(f)
        for count, row in enumerate(rows):
            try:
                dict_local[row[0]] = float(row[1])
            except:
                '''print(f"Datos no válidos en la línea {count+1} del archivo.")''' ###Con esto sé en que linea me genera un error
    return dict_local

def readTruck (name_file):
    truck = []

    with open(name_file, 'rt') as f:
            dict_local = {}
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
                    '''print(f"Datos no válidos en la línea {count+1} del archivo.")'''
    return truck

def make_report(truck, fruit):
    list = []
    aux = ()

    for i in range(len(truck)):
        aux = (truck[i]['nombre'], truck[i]['cajones'], truck[i]['precio'], round(fruit[truck[i]['nombre']]-truck[i]['precio'], 2))
        list.append(aux)
    return list

list_truck = readTruck('../Data/camion.csv')
fruit_dictionary = fruitPrice('../Data/precios.csv')
list_final = make_report(list_truck, fruit_dictionary)
for i in headers:
    print('%10s' % i, end='')
print()
for i in headers:
    print(f'{" ":->11}', end='')
print()
for i in list_final:
    print(f'{i[0]:>10} {i[1]:>10} {"$ "+str(i[2]):>9} {"$ "+str(i[3]):>10}')
