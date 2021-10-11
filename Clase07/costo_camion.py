#!/usr/bin/env python3
#Ejercicio 7.4: Función principal
import informe_final
import sys

def costo_camion(name_file):
    cost = 0.0
    lista = informe_final.leer_camion(name_file)
    for i in lista:
        cost += i['cajones'] * i['precio']
    return cost

def f_principal(parametros):
    total_cost = costo_camion(parametros[1])
    print(f"Costo total: {round(total_cost, 2)}")

if __name__=="__main__":
    f_principal(['informe_final.py', '../Data/camion.csv', '../Data/precios.csv'])