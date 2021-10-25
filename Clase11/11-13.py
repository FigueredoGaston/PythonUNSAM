#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.13: Hojas ISO y recursión

def medidas_hoja_A(N):
    def doblez(a, b):
        return round(b/2), a

    ancho = 841
    largo = 1189
    if N == 0:
        return (ancho, largo)
    else:
        for i in range(N):
            ancho, largo = doblez(ancho, largo)
    return (ancho, largo)


if __name__ == '__main__':
    print(medidas_hoja_A(3))
