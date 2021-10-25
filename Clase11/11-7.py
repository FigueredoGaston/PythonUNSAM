#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.7: Máximo

def maximo(lista):
    def mx(a, b):
        return a if a >= b else b
    return lista[0] if len(lista) == 1 else mx(maximo(lista[0:len(lista)-1]), lista[len(lista)-1])


if __name__ == '__main__':
    print(maximo([1, 20, 6]))
