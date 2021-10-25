#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.5: Subcadenas

def posiciones(a, b):
    lista = []

    def posicion(a, b):
        if a[-2:-1] == b:
            return len(a)-1


if __name__ == '__main__':
    print(posiciones('Un tete a tete con Tete', 'te'))
