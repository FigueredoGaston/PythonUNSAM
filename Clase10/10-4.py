#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.4: Un generador simple.

def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line


for line in open('../Data/camion.csv'):
    print(line, end='')

for line in filematch('../Data/camion.csv', 'Naranja'):
    print(line, end='')
