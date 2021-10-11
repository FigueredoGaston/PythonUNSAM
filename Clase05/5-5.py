# Ejercicio 5.5: Calcular pi

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def aproximar_pi(punto, N):
    lista = []
    for i in range(N):
        lista.append(punto())
    M = list(i for i in lista if (i[0]**2 + i[1]**2)<1)
    return 4*len(M)/N

def main():
    print(aproximar_pi(generar_punto, 100000))

main()