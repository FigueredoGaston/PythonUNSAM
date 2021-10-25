#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.3: Dígitos

def cant_digitos(n):
    if (n // 10) == 0:
        return 1
    return 1 + cant_digitos(n // 10)


if __name__ == '__main__':
    print(cant_digitos(3596))
