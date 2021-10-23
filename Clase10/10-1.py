#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.1: Iteradores, un ejemplo.

f = open('../Data/camion.csv')
f.__iter__()    # Notar que esto apunta al método...
# ...que accede al archivo mismo.
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
