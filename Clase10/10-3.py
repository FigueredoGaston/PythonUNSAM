#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.3: Un iterador adecuado.

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def __repr__(self):
        return f'Camion({self.lotes})'

    def __str__(self):
        t = [f'Camion con {self.__len__()} lotes:']
        for obj in self.lotes:
            s = f"Lote de {obj.cajones} cajones de '{obj.nombre}', pagados a ${obj.precio} cada uno."
            t.append(s)
        return '\n'.join(t)

    def __len__(self):
        return len(self.lotes)

    def __getitem__(self, position):
        return self.lotes[position]

    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
