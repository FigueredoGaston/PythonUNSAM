#Ejercicio 6.15: Insertar un elemento en una lista

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

def insertar(lista, x):
    '''Inserat dato en lista
    Precondición: la lista está ordenada
    Devuelve la posición de ese elemento en la lista (si se encuentra en la lista)
        o lo agrega y devuelve la posición donde se insertó el elemento para que la lista
        permanezca ordenada (si no está en la lista)
    '''

    posicion = donde_insertar(lista, x);
    if lista[posicion] == x:    #Si el dato ya está en la lista devuelvo la posición en la que está
        return posicion
    elif lista[posicion] < x:   #Si el dato es mas grande que el de la lista lo agrego en la posición contigua y devuelvo la posición en la que está
        lista.insert(posicion+1, x)
        return posicion+1
    else:   #Si el dato es mas chico que el de la lista lo agrego y devuelvo la posición en la que está
        lista.insert(posicion, x)
        return posicion


if __name__=="__main__":
    lista = [0,2,4,6]
    dato = -1
    pos = insertar(lista, dato)
    print(lista)
    print(pos)
