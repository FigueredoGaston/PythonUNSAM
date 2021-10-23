#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.5: Monitoreo de datos en tiempo real.
# Ejercicio 10.6: Uso de un generador para producir datos.

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


if __name__ == '__main__':
    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
