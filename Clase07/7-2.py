#Ejercicio 7.2: Atrapemos excepciones

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''

    with open(nombre_archivo) as f:
        registros = []
        filas = csv.reader(f)

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
            for i, fila in enumerate(filas):
                try:
                    # Filtrar la fila si se especificaron columnas
                    if indices:
                        fila = [fila[index] for index in indices]
                    #Convertir los tipos si es necesario
                    if types != None:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    # Armar el diccionario
                    registro = dict(zip(encabezados, fila))
                    registros.append(registro)
                except ValueError as e:
                    print(f'Fila {i+1}: No pude convertir {fila}')
                    print(f'Fila {i+1}: Motivo: {e}')
        else:
            for i, fila in enumerate(filas):
                try:
                    #Convertir los tipos si es necesario
                    if types != None:
                        fila = tuple(func(val) for func, val in zip(types, fila))
                    # Armar el diccionario
                    registros.append(fila)
                except ValueError as e:
                    print(f'Fila {i+1}: No pude convertir {fila}')
                    print(f'Fila {i+1}: Motivo: {e}')

    return registros

if __name__=="__main__":
    print(parse_csv('../Data/missing.csv', types = [str, int, float]))
