#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 12.2

def ord_burbujeo(lista):
    for i in range(1, len(lista)):
        for j in range(0, len(lista)-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


if __name__ == '__main__':
    print(ord_burbujeo([1, 2, -3, 8, 1, 5]))
