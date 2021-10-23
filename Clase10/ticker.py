#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.15: Código simple.

from vigilante import vigilar
import csv
from formato_tabla import crear_formateador
import informe_final


def elegir_columnas(rows, indices):
    return ((row[index] for index in indices) for row in rows)


def cambiar_tipo(rows, types):
    return((func(val) for func, val in zip(types, row)) for row in rows)


def hace_dicts(rows, headers):
    return((dict(zip(headers, row))) for row in rows)


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows


def filtrar_datos(rows, nombres):
    return ((row) for row in rows if row['nombre'] in nombres)


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, precio, volumenes)
    '''
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in data_informe:
        rowdata = [row['nombre'], f"{row['precio']}", f"{row['volumen']}"]
        formateador.fila(rowdata)


def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    formateador = crear_formateador(fmt)
    imprimir_informe(rows, formateador)


if __name__ == '__main__':
    ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')
