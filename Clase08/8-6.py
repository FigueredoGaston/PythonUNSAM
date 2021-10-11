#!/usr/bin/env python3
#Ejercicio 8.6: Ordenar el árbol de archivos (optativo)

import os
import sys
from datetime import datetime

def crear_carpeta(directorio):
    '''Crea una carpeta

    Pre: se debe pasar el directorio crear.
    Pos: si no existe crea la carpeta si no retorna mensaje.
    '''

    if os.path.isdir(directorio):
        print('La carpeta destino ya existe.');
    else:
        os.mkdir(directorio)

def procesar_nombre(fname) :
    '''Toma un nombre y lo devuelve acortado y la fecha que contiene.

    Pre: se debe pasar un string con el nombre a modificar.
    Pos: se devuelve un nombre nuevo y la fecha que contenía.
    '''

    aux_name = fname[:-13]+fname[-4:]
    #renombro el archivo desde la posición encadenando dos partes de la cadena original
    aux_date = datetime.strptime(fname[-12:-4], '%Y%m%d')
    #Tomo la fecha de modificación del nombre del archivo
    return aux_name, aux_date

def manejo_rutas(root):
    '''Verifica qsi una ruta es relativa o absoluta.

    Pre: se debe pasar su nombre de ruta de acceso.
    Pos: se devuelve una ruta absoluta.
    '''

    if os.path.isabs(root):
        return root
    else:
        return os.path.abspath(os.path.join(os.getcwd(), root))

def procesar(root, name, nroot):
    '''Procesa el archivo que es pasado a travez de su nombre y
    su ruta de acceso.

    Pre: se debe pasar su nombre y su ruta de acceso actual y
        la nueva a la que se mueve.
    Pos: se mueve el archivo, se renombra y se setea la fecha de última modificación.
    '''

    aux_date = procesar_nombre(name)
    os.rename(os.path.join(root, name), os.path.join(nroot, aux_date[0]))
    #Muevo y renombro el archivo desde la posición encadenando dos partes de la cadena original
    os.utime(os.path.join(nroot, aux_date[0]), (aux_date[1].timestamp(), aux_date[1].timestamp()))
    #Cambio el atributo del archivo

def eliminar_carpetas(droot):
    '''Elimina carpeta vacias paertiendo del la ruta especificada.

    Pre: se debe pasar una ruta de acceso .
    Pos: se eliminan las carpetas vacias a partir de una ruta.
    '''

    for root, dirs, files in os.walk(droot, topdown=False):
        if not files and not dirs:
            os.rmdir(root)

def f_principal(paramateros):
    '''Genera una lista con todos los archivos .png del directorio.

    Pre: se debe pasar el directorio a recorrer.
    Pos: se devuelve una lista con nombre de archivos.
    '''

    crear_carpeta(paramateros[2])
    aux_root = manejo_rutas(paramateros[1])
    aux_nroot = manejo_rutas(paramateros[2])
    #Si la ruta es relativa la vuelvo absoluta
    os.chdir(aux_root)
    for root, dirs, files in os.walk("."):
        for name in files:
            img = os.path.join(root, name)
            if os.path.isfile(img) and name.endswith('.png'):
            #Pregunto si es un archivo y si es .png
                procesar(root, name, aux_nroot)
        for name in dirs:
            img = os.path.join(root, name)
            if os.path.isfile(img) and name.endswith('.png'):
                procesar(root, name, aux_nroot)
    eliminar_carpetas(aux_root)

if __name__=="__main__":
    f_principal(['informe_final.py', '../Data/ordenar/', '../Data/imgs_procesadas/'])
    #f_principal(sys.argv)