#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 10.15: Código simple.

import animal
import tablero
import mundo

if __name__ == '__main__':
    L = animal.Leon()
    A1 = animal.Antilope()
    A2 = animal.Antilope()
    vecinos = [(1, A1), (2, A2)]
    pos = L.alimentarse(vecinos)
    if pos:
        print(f'El león se come al antílope A{pos}')
    else:
        print(f'El león no come')
