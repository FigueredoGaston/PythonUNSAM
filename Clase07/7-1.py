#Ejercicio 7.1: Lancemos excepciones

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    if select != None and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    else:
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
    print(parse_csv('../Data/precios.csv', select = ['nombre','precio'], has_headers = False))
