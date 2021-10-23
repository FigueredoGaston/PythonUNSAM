#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.16: Volviendo a ordenar imágenes.

import os


def archivos_png(directorio):
    '''Genera una lista con todos los archivos .png del directorio.

    Pre: se debe pasar el directorio a recorrer.
    Pos: se devuelve una lista con nombre de archivos.
    '''

    os.chdir(directorio)
    list = []
    for root, dirs, files in os.walk('./'):
        list.append((root, name)for name in files
                    if os.path.isfile(os.path.join(root, name)) and name.endswith('.png'))
        list.append((root, name)for name in dirs
                    if os.path.isfile(os.path.join(root, name)) and name.endswith('.png'))
    return list


if __name__ == "__main__":
    for i in archivos_png('../Data/ordenar/'):
        i
