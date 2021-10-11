# Ejercicio 5.4: Envido

import random

def mano_truco():
    tirada=[]
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]

    tirada.append(random.sample(naipes,k=3))
    return tirada

def probabilidad_30(tirada):
    repetidos = list(tirada.count(i) for i in tirada if tirada.count(i)>1)
    return len(repetidos)/cant

print(mano_truco())