#Ejercicio 6.5: Crear una función de alto nivel para la ejecución del programa.

import csv

def leer_precios(name_file):
    dict_local = {}

    with open(name_file, 'rt') as f:
        rows = csv.reader(f)
        for count, row in enumerate(rows):
            try:
                dict_local[row[0]] = float(row[1])
            except:
                #print(f"Datos no válidos en la línea {count+1} del archivo.") ###Con esto sé en que linea me genera un error
                continue
    return dict_local

def leer_camion(name_file):
    truck = []

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
                #print(f"Datos no válidos en la línea {count+1} del archivo.")
                continue
    return truck

def hacer_informe(camion, precios):
    lista = []

    for i in range(len(camion)):
        aux = (camion[i]['nombre'], camion[i]['cajones'], camion[i]['precio'], round(precios[camion[i]['nombre']]-camion[i]['precio'], 2))
        lista.append(aux)
    return lista

def imprimir_informe(informe):
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


if __name__=="__main__":
    informe_camion('../Data/camion.csv', '../Data/precios.csv')