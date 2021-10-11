#Ejercicio 5.11: Incompleto

import numpy as np

def crear_album(figus_total):
    return (np.zeros(figus_total, dtype=np.int64))

def album_incompleto(A):
    return (False if  0 in A else True)

def main():
    print(album_incompleto(crear_album(10)))

main()