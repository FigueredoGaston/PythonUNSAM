#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 9.10: Ejemplo de getattr()

import lote
c = lote.Lote('Peras', 100, 490.1)
columnas = ['nombre', 'cajones']
for colname in columnas:
        print(colname, '=', getattr(c, colname))

