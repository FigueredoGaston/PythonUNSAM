#Ejercicio 4.6: Propagación

def propagar(lista):
    propagada = []
    i = 0
    while i < len(lista): # Recorro la lista
        if lista[i] == 1:
            propagada.append(lista[i])
            for j in range(i-1, -1, -1):
                if lista[j] == 0:
                    propagada[j] = 1
                else:
                    break
            while i+1 < len(lista) and lista[i+1] == 0:
                propagada.append(1)
                i += 1
        else:
            propagada.append(lista[i])
        i += 1
    return propagada

def main():
    print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
    print(propagar([ 0, 0, 0, 1, 0, 0]))
