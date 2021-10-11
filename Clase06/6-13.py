#Ejercicio 6.13: Búsqueda lineal sobre listas ordenadas.


def busqueda_lineal_lordenada(lista, e):
    pos = -1
    for i, z in enumerate(lista):
        if z == e:
            return i
        if z > e:
            break
    return pos

if __name__=="__main__":
    print(busqueda_lineal_lordenada([1,2,3,2,3,4],1))
    print(busqueda_lineal_lordenada([1,2,3,2,3,4],2))
    print(busqueda_lineal_lordenada([1,2,3,2,3,4],3))
    print(busqueda_lineal_lordenada([1,2,3,2,3,4],5))
