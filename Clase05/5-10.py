#Ejercicio 5.10: Crear

import numpy as np

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album

def main():
    print(crear_album(10))

main()