#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.14: precio_alquiler ~ superficie

import pandas as pd
from sklearn import linear_model
import numpy as np


def ajuste_lineal_simple(x, y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


def funct_principal():
    superficie = np.array([150.0, 120.0, 170.0, 80.0])
    alquiler = np.array([35.0, 29.6, 37.4, 21.0])
    antigüedad = [50.0, 5.0, 25.0, 70.0]

    data_deptos = pd.DataFrame(
        {'alquiler': alquiler, 'superficie': superficie, 'antigüedad': antigüedad})

    X = pd.concat([data_deptos.superficie, data_deptos.antigüedad], axis=1)

    ajuste_deptos = linear_model.LinearRegression()
    ajuste_deptos.fit(X, data_deptos.alquiler)

    errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
    print(errores)
    print("ECM:", (errores**2).mean())  # error cuadrático medio


if __name__ == '__main__':
    funct_principal()
