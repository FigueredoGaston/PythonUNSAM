#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.9: Pascal

def pascal(n, k):
    if k in (0, n):
        return 1
    return pascal(n-1, k-1) + pascal(n-1, k)


if __name__ == '__main__':
    print(pascal(5, 2))
