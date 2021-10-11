#!/usr/bin/env python3
#Ejercicio 7.4: Función principal

import fileparse
import sys

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        dict_local = {}
        local = fileparse.parse_csv(f, types = [str, float], has_headers = False)
        for row in local:
            dict_local[row[0]] = float(row[1])
    return dict_local

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        truck = fileparse.parse_csv(f, select = ['nombre', 'precio', 'cajones'], types = [str, float, int]) 
    return truck

def hacer_informe(camion, precios):
    lista = []
    for i in range(len(camion)):
        aux = (camion[i]['nombre'], camion[i]['cajones'], camion[i]['precio'], round(precios[camion[i]['nombre']]-camion[i]['precio'], 2))
        lista.append(aux)
    return lista

def imprimir_informe(informe):
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

def f_principal(parametros):
    informe_camion(parametros[1], parametros[2])

if __name__=="__main__":
    f_principal(['informe_final.py', '../Data/camion.csv', '../Data/precios.csv'])