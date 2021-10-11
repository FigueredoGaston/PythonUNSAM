#Ejercicio 4.4: Búsqueda de máximo y mínimo

def maximo(lista):
    m = lista[0]
    for e in lista[1:]: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def minimo(lista):
    m = lista[0]
    for e in lista[1:]: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m

def main():
    print(maximo([1,2,7,2,3,4]))
    print(maximo([1,2,3,4]))
    print(maximo([-5,4]))
    print(maximo([-5,-4]))

    print(minimo([1,2,7,2,3,4]))
    print(minimo([1,2,3,4]))
    print(minimo([-5,4]))
    print(minimo([-5,-4]))
