#Ejercicio 5.12: Comprar

import random

def comprar_figu(figus_total):
    return (random.randint(1,figus_total+1))

def main():
    cant_figus = 10
    print(comprar_figu(cant_figus))

main()
