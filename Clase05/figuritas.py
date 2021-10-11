#%%
#Ejercicio 5.15:

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
    cant_figus = 670
    rep = 100
    print(experimento_figus(rep, cant_figus))

#%%
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

#%%
#Ejercicio 5.19:

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

def experimento_figus(n_repeticiones, figus_total, figus_paquete):
    lista = list(cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones))
    return np.mean(lista)

def main():
    repeticiones = 100
    cant_figus = 670
    paq = 5
    print(experimento_figus(repeticiones, cant_figus, paq))

#%%
#Ejercicio 5.20:

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

def experimento_figus(n_repeticiones, figus_total, figus_paquete):
    lista = list(cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones))
    return (np.array(lista) <= 850).sum()/n_repeticiones
    #return len(list(i for i in lista if i <= 850))/n_repeticiones

def main():
    repeticiones = 100
    cant_figus = 670
    paq = 5
    print(experimento_figus(repeticiones, cant_figus, paq))

