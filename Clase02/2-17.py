### Ejercicio 2.17: Diccionarios como contenedores

import csv

fruit_dictionary = {}

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

fruit_dictionary = fruitPrice('../Data/precios.csv')
print(fruit_dictionary['Mandarina'])