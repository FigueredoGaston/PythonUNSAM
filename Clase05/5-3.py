# Ejercicio 5.3: Cocumpleaños

import random

def tirar(cant=30):
    tirada=[]
    for i in range(cant):
        tirada.append(random.randint(1,365))
    return tirada

def cantidad_cumpleaños_mismo_dia(tirada, cant):
    repetidos = list(tirada.count(i) for i in tirada if tirada.count(i)>1)
    return len(repetidos)/cant

def main():
    retorno = 0.0
    cant_personas = 30
    retorno = cantidad_cumpleaños_mismo_dia(tirar(cant_personas), cant_personas)
    print(f'Podemos estimar la probabilidad de encontrar dos personas de {cant_personas}, cumplan el mismo día en: {retorno:.6f}.')

main()