#!/usr/bin/env python3
#Ejercicio 7.12: Caminatas al azar

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    '''Genera una lista de "largo", cantidad de números enteros.

    Pre: largo debe ser un número entero y positivo.
    Pos: se devuelve una lista de números enteros.
    '''

    pasos=np.random.randint(-1,2,largo)
    return pasos.cumsum()

def f_principal(parametros):
    '''Grafica una N cantidad de listas reprentadas por gráfico.

    Pre: los parámetros deben ser un número de caminatas y el número de
        pasos de cada caminata.
    Pos: Se devuelven tres gráficas, la primera con todas las caminatas y las
        otras dos grafica la más lejana y la más cercana.
    '''

    #Genero el diagrama de gráficos
    fig = plt.figure()

    plt.subplot(2, 1, 1, title="12: Caminatas al azar", xlabel="Tiempo",
                ylabel="Distancia al origen", ylim=(-1000.0, 1000.0),
                xticks=[])
    #Genero la primera caminata y la tomo como máximo y mínimo
    caminata = randomwalk(parametros[2])
    plt.plot(caminata, c=np.random.rand(3,))
    max = caminata
    min = caminata
    max_distancia = np.amax(np.abs(caminata))   #Transformo el array a su valor absoluto y busco el máximo
    min_distancia = np.amax(np.abs(caminata))

    #Luego genero las demás y busco la más y menos alejada
    for i in range(parametros[1]-1):
        caminata = randomwalk(parametros[2])
        plt.plot(caminata, c=np.random.rand(3,))
        aux = np.amax(np.abs(caminata))
        if max_distancia < aux:
            max = caminata[:]
            max_distancia = aux
        elif min_distancia > aux:
            min = caminata[:]
            min_distancia = aux

    plt.subplot(2, 2, 3, title="La caminata que más se aleja", xlabel="Tiempo",
                ylabel="Distancia al origen", ylim=(-1000.0, 1000.0),
                xticks=[])
    plt.plot(max)

    plt.subplot(2, 2, 4, title="La caminata que menos se aleja", xlabel="Tiempo",
                ylabel="Distancia al origen", ylim=(-1000.0, 1000.0),
                xticks=[])
    plt.plot(min)

    plt.show()

if __name__=="__main__":
    f_principal(['random_walk.py', 12, 100000])