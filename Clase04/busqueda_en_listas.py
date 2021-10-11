#%%
#Ejercicio 4.3: Búsquedas de un elemento

def buscar_u_elemento(lista, e):
    pos = -1
    i = 0
    for z in lista:
        if z == e:
            pos = i
        i += 1
    return pos

def main():
    print(buscar_u_elemento([1,2,3,2,3,4],1))
    print(buscar_u_elemento([1,2,3,2,3,4],2))
    print(buscar_u_elemento([1,2,3,2,3,4],3))
    print(buscar_u_elemento([1,2,3,2,3,4],5))

main()

#%%
#Ejercicio 4.4: Búsqueda de máximo y mínimo

def maximo(lista):
    m = lista[0]
    for e in lista[1:]: # Recorro la lista y voy guardando el mayor, a partir de la segunda posición
        if e > m:
            m = e
    return m

def minimo(lista):
    m = lista[0]
    for e in lista[1:]: # Recorro la lista y voy guardando el menor, a partir de la segunda posición
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
