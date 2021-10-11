#Ejercicio 6.10: Importar módulos

import fileparse

print(fileparse.parse_csv('../Data/precios.csv', types = [str, float], has_headers = False))