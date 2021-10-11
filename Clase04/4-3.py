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
