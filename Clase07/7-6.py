#!/usr/bin/env python3
#Ejercicio 7.6: De archivos a "objetos cual archivos"


import csv

def parse_csv(lines, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    registros = []
    filas = csv.reader(lines)

    if has_headers:
        # Lee los encabezados del archivo
        encabezados = next(filas)
        # Si se indicó un selector de columnas, buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            #Convertir los tipos si es necesario
            if types != None:
                fila = [func(val) for func, val in zip(types, fila) ]
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
    else:
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            #Convertir los tipos si es necesario
            if types != None:
                fila = tuple(func(val) for func, val in zip(types, fila))
            # Armar el diccionario
            registros.append(fila)

    return registros

if __name__=="__main__":
    lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
    print(parse_csv(lines, types=[str,int,float]))