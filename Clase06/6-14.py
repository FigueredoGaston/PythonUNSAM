#Ejercicio 6.14: Búsqueda binaria

def donde_insertar(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve la posición de ese elemento en la lista (si se encuentra en la lista)
        o la posición donde se podría insertar el elemento para que la lista
        permanezca ordenada (si no está en la lista)
    '''
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            return medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return medio

if __name__=="__main__":
    print(donde_insertar([0,2,4,6], 5))