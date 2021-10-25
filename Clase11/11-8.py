#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.8: Replicar

def replicar(lista, n):
    return [p for p in lista if replicar()]


if __name__ == '__main__':
    print(replicar([1, 3, 3, 7], 2))
