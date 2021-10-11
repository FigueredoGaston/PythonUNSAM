### Ejercicio 2.18: Balances

import csv

fruit_dictionary = {}
list_out = []
total_cost= 0.0
i = 0
aux = ""

def fruitPrice(name_file):
    dict_local = {}

    with open(name_file, 'rt') as f:
        rows = csv.reader(f)
        for count, row in enumerate(rows):
            try:
                dict_local[row[0]] = float(row[1])
            except:
                print(f"Datos no válidos en la línea {count+1} del archivo.") ###Con esto sé en que linea me genera un error
    return dict_local

def readTruck (name_file):
    truck = []
    count = 0
    cost = 0.0

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
                    cost += dict_local['cajones'] * dict_local['precio']
                    truck.append(dict_local)
                except:
                    print(f"Datos no válidos en la línea {count+1} del archivo.")
    return [truck,cost, count]

list_out = readTruck('../Data/camion.csv')
fruit_dictionary = fruitPrice('../Data/precios.csv')

while i < list_out[2]:
    aux = list_out[0][i]['nombre']
    if aux in fruit_dictionary.keys():
        total_cost += list_out[0][i]['cajones'] * fruit_dictionary[aux]
    i += 1
print(f"El valor total del camión es: ${list_out[1]}")
print(f"Total recaudado de la venta total: ${total_cost}")
print(f"El balance arroja un saldo de: ${round(total_cost-list_out[1], 2)}")
