#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.6: Paridad

def posiciones(a, b):

    def posicion(c, d):
        return True if c == d else False

    return [p for p in range(len(a)) if posicion(a[p:p+2], b)]


if __name__ == '__main__':
    print(posiciones('Un tete a tete con Tete', 'te'))
