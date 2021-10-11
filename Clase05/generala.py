# Ejercicio 5.2: Generala no necesariamente servida

from collections import Counter
import random

def tirar(cant=5):
    tirada=[]
    for i in range(cant):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    if len(set(tirada)) == 1:
        return True
    return False

def volver_a_tirar(tirada):
    counter = [(0,0)]
    aux = []
    for i in range(2):
        aux = aux + (tirada(5-counter[0][1]))
        counter = Counter(aux)
        counter = counter.most_common()
        aux = []
        for j in range(counter[0][1]):
                aux.append(counter[0][0])
    aux = aux + (tirada(5-counter[0][1]))
    return aux

def prob_generala(N):
    G = 0
    G = sum([es_generala(volver_a_tirar(tirar)) for i in range(N)])
    return G/N

def main():
    Nro = 100000
    probab = 0.0
    probab = prob_generala(Nro)
    print(f'Podemos estimar la probabilidad de sacar generala mediante {probab:.6f}.')

