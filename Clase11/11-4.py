#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.4: Potencias

def es_potencia(n, b):
    if ((n / b) == 0) or n == 1:
        return True
    if (n % b) != 0:
        return False
    return es_potencia(n/b, b)


if __name__ == '__main__':
    print(es_potencia(1, 4))
