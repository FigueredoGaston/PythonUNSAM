#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.15: Peso específico

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
import requests
import io


def funct_principal():
    enlace = 'https://raw.githubusercontent.com/python-unsam/Programacion_en_Python_UNSAM/master/Notas/11_Recursion/longitudes_y_pesos.csv'
    r = requests.get(enlace).content
    data_lyp = pd.read_csv(io.StringIO(r.decode('utf-8')))

    print(data_lyp)

    """ data_deptos = pd.DataFrame(
        {'alquiler': alquiler, 'superficie': superficie, 'antigüedad': antigüedad})

    X = pd.concat([data_deptos.superficie, data_deptos.antigüedad], axis=1)

    ajuste_deptos = linear_model.LinearRegression()
    ajuste_deptos.fit(X, data_deptos.alquiler)

    errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
    print(errores)
    print("ECM:", (errores**2).mean())  # error cuadrático medio
    
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
    plt.show() """


if __name__ == '__main__':
    funct_principal()
