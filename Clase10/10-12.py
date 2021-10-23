#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.12: El pipeline ensamblado.

from vigilante import vigilar
import csv
from formato_tabla import crear_formateador
import informe_final


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows


def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio)
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
    #data_informe = informe_final.hacer_informe(camion, rows)
    imprimir_informe(rows, formateador)


if __name__ == '__main__':
    ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')
