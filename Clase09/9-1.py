#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 9.1: Objetos como estructura de datos.

import lote

a = lote.Lote('Pera', 100, 490.10)
b = lote.Lote('Manzana', 50, 122.34)
c = lote.Lote('Naranja', 75, 91.75)
b.cajones * b.precio
c.cajones * c.precio
lotes = [a, b, c]
print(lotes)
for c in lotes:
    print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
