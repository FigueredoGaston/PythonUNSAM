#!/usr/bin/env python3
#Ejercicio 8.5: Recorrer el árbol de archivos

import os

def archivos_png(directorio):
    '''Genera una lista con todos los archivos .png del directorio.

    Pre: se debe pasar el directorio a recorrer.
    Pos: se devuelve una lista con nombre de archivos.
    '''

    os.chdir(directorio)
    for root, dirs, files in os.walk('./'):
        for name in files:
            img = os.path.join(root, name)
            if os.path.isfile(img) and name.endswith('.png'):
            #Pregunto si es un archivo y si es .png
                print(name)
        for name in dirs:
            img = os.path.join(root, name)
            if os.path.isfile(img) and name.endswith('.png'):
                print(name)

if __name__=="__main__":
    archivos_png('../Data/ordenar/')