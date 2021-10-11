#Ejercicio 5.8: Guardar temperaturas

import random
import numpy as np

def medir_temp(n):
    lista = []
    lista_np = []

    for i in range(n):
        lista.append(random.normalvariate(37.5, 0.2))
    lista.sort()
    lista_np = np.array(lista)
    np.save('../Data/temperaturas.npy', lista_np)
    return lista

def resumen_temp(n):
    maximo = 0.0
    minimo = 0.0
    prom = 0.0
    media = 0.0
    
    lista = medir_temp(n)
    maximo = max(lista)
    minimo = min(lista)
    prom = sum(lista)/n
    media = lista[round(n/2)]
    return (maximo, minimo, prom, media)

def main():
    print(resumen_temp(999))

main()
