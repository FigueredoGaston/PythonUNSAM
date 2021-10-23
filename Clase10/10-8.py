#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.8: Configuremos un pipeline simple

import os
import time


def vigilar(root):
    f = open(root)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    naranjas = filematch(lines, 'Naranja')
    for line in naranjas:
        print(line)
