#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.14: precio_alquiler ~ superficie

import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x, y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


def funct_principal():
    N = 50
    minx = 0
    maxx = 250
    x = np.array([150.0, 120.0, 170.0, 80.0])
    y = np.array([35.0, 29.6, 37.4, 21.0])
    a, b = ajuste_lineal_simple(x, y)
    grilla_x = np.linspace(start=minx, stop=maxx, num=1000)
    grilla_y = grilla_x*a + b
    g = plt.scatter(x=x, y=y)
    plt.title('y ajuste lineal')
    plt.plot(grilla_x, grilla_y, c='green')
    plt.xlabel('x')
    plt.ylabel('y')
    errores = y - (a*x + b)
    print(errores)
    print("ECM:", (errores**2).mean())
    plt.show()


if __name__ == '__main__':
    funct_principal()
