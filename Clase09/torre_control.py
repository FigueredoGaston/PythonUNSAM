#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 9.12: Torre de Control

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return len(self.items) == 0

class TorreDeControl:
    '''modelo el trabajo de una torre de control de un
    aeropuerto con una pista de aterrizaje
    '''

    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, arribo):
        self.arribos.encolar(arribo)

    def nueva_partida(self, partida):
        self.partidas.encolar(partida)

    def ver_estado(self):
        if not self.arribos.esta_vacia():
            print(f'Vuelos esperando para aterrizar:', end=' ')
            print(', '.join(self.arribos.items))
        if not self.partidas.esta_vacia():
            print(f'Vuelos esperando para despegar:', end=' ')
            print(', '.join(self.partidas.items))

    def asignar_pista(self):
        try:
            print(f'El vuelo {self.arribos.desencolar()} aterrizó con éxito.')
        except:
            try:
                print(f'El vuelo {self.partidas.desencolar()} aterrizó con éxito.')
            except:
                print('No hay vuelos en espera.')