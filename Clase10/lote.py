#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 9.1: Objetos como estructura de datos..

class Lote:
    def __init__(self, nombre, cajones, precio):
        # Todo dato guardado en `self` es propio de esa instancia
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, ncajones):
        self.cajones -= ncajones

    def __repr__(self):
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"
