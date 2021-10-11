#Ejercicio 5.13: Cantidad de compras

import random
import numpy as np

def comprar_figu(figus_total):
    return (random.randint(1,figus_total))

def crear_album(figus_total):
    return (np.zeros(figus_total, dtype=np.int64))

def album_incompleto(A):
    return (False if 0 in A else True)

def cuantas_figus(figus_total):
    cont = 0

    album = crear_album(figus_total)
    while not album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu-1] += 1
        cont +=1
    return cont

def main():
    cant_figus = 6
    print(cuantas_figus(cant_figus))

main()