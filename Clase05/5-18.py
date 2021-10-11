#Ejercicio 5.18:

import random
import numpy as np

def comprar_paquete(figus_total, figus_paquete):
    lista = []

    for i in range(figus_paquete):
        lista.append(random.randint(1,figus_total))
    return lista

def crear_album(figus_total):
    return (np.zeros(figus_total, dtype=np.int64))

def album_incompleto(A):
    return (False if 0 in A else True)

def cuantos_paquetes(figus_total, figus_paquete):
    cont = 0

    album = crear_album(figus_total)
    while not album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for i in paquete:
            album[i-1] += 1
        cont +=1
    return cont

def main():
    cant_figus = 670
    paq = 6
    print(cuantos_paquetes(cant_figus, paq))

main()