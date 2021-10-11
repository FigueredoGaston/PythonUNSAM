#Ejercicio 5.17:

import random

def comprar_paquete(figus_total, figus_paquete):
    lista = []

    for i in range(figus_paquete):
        lista.append(random.randint(1,figus_total))
    return lista

def main():
    cant_figus = 670
    paq = 6
    print(comprar_paquete(cant_figus, paq))

main()