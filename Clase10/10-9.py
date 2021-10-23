#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.9: Un pipeline más en serio

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
    from vigilante import vigilar
    import csv

    lines = vigilar('../Data/mercadolog.csv')
    rows = csv.reader(lines)
    for row in rows:
        print(row)
