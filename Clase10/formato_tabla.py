#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 9.5: Un problema de extensibilidad


class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print(f'<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
        #print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        print(f'<tr>', end='')
        for d in data_fila:
            print(f'<th>{d}</th>', end='')
        print('</tr>')

def crear_formateador(nombre):
    if nombre == 'txt':
        return FormatoTablaTXT()
    elif nombre == 'csv':
        return FormatoTablaCSV()
    elif nombre == 'html':
        return FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {nombre}')