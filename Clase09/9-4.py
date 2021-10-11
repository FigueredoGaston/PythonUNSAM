#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 9.4: Usá tu clase

import costo_camion
import informe_final

print(costo_camion.costo_camion('../Data/camion.csv'))
informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv')
