#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.11: Búsqueda binaria

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = True
        elif lista[medio] > e:
            res = bbinaria_rec(lista[:medio], e)
        else:
            res = bbinaria_rec(lista[medio:], e)
    return res


if __name__ == '__main__':
    print(bbinaria_rec([1, 2, 3, 4, 5], 4))
