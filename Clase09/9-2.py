#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 9.2: Agregá algunos métodos

import lote

s = lote.Lote('Pera', 100, 490.10)
print(s.costo())
print(s.cajones)
s.vender(25)
print(s.cajones)
print(s.costo())
