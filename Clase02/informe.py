### Ejercicio 2.18: Balances

import csv

fruit_dictionary = {}
list_out = []
total_cost= 0.0
i = 0
aux = ""

def fruitPrice(name_file):
    count = 0
    dict = {}

    with open(name_file, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            count += 1
            try:
                dict[row[0]] = float(row[1])
            except:
                '''print(f"Datos no válidos en la línea {count} del archivo.")''' ###Con esto sé en que linea me genera un error
    return dict

def readTruck (name_file):
    truck = []
    count = 0
    cost = 0.0

    with open(name_file, 'rt') as f:
            dict = {}
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                count += 1
                try:
                    dict = {
                            'nombre' : row[0],
                            'precio' : float(row[2]),
                            'cajones' : int(row[1])
                            }
                    cost += dict['cajones'] * dict['precio']
                    truck.append(dict)
                except:
                    print(f"Datos no válidos en la línea {count} del archivo.")
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
