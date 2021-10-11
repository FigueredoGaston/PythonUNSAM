#Ejercicio 4.5: Invertir una lista

def invertir_lista(lista):
    invertida = []
    for i in range(len(lista)): # Recorro la lista
        invertida.append(lista[-i-1])
    return invertida

def main():
    print(invertir_lista([1, 2, 3, 4, 5]))
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))

