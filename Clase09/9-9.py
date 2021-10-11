#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 9.9: Mejor salida para objetos

from lote import Lote

peras = Lote('Pera', 100, 490.1)
pcc = Lote('Pera', 100, 490.1)
print(peras)
print(pcc)
print(id(peras))
print(id(pcc))
