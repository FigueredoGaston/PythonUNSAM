#Ejercicio 5.14:

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

def experimento_figus(n_repeticiones, figus_total):
    lista = list(cuantas_figus(figus_total) for i in range(n_repeticiones))
    return np.mean(lista)

def main():
    cant_figus = 6
    rep = 1000
    print(experimento_figus(rep, cant_figus))

main()