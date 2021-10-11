#!/usr/bin/env python3
#Ejercicio 7.12: Caminatas al azar

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)
    return pasos.cumsum()

def f_principal(parametros):
    fig = plt.figure()

    plt.subplot(2, 1, 1, title="12: Caminatas al azar", xlabel="Tiempo",
                ylabel="Distancia al origen", ylim=(-1000.0, 1000.0),
                xticks=[])
    caminata = randomwalk(parametros[2])
    max = caminata
    min = caminata
    plt.plot(caminata, c=np.random.rand(3,))
    for i in range(parametros[1]-1):
        caminata = randomwalk(parametros[2])
        if abs(max[-1]) < abs(caminata[-1]):
            max = caminata[:]
        elif abs(min[-1]) > abs(caminata[-1]):
            min = caminata[:]
        plt.plot(caminata, c=np.random.rand(3,))

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
