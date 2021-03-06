#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 9.3: Lista de instancias

import lote
import fileparse

with open('../Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
print(camion)
print(sum([c.costo() for c in camion]))
