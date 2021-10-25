#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.2: Números triangulares

def triangular(n):
    if n == 1:
        return 1
    return n + triangular(n-1)


if __name__ == '__main__':
    print(triangular(3))
