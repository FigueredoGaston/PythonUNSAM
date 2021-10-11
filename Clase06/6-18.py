#Ejercicio 6.18: Un ejemplo más complejo

from copy import copy

def incrementar(s):
    carry = 1
    l = len(s)
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

def listar_secuencias(n):
    aux = [0]*n
    lista = [copy(aux)]
    for i in range((2**n)-1):
        lista.append(copy(incrementar(aux)))
    return lista

if __name__=="__main__":
    print(listar_secuencias(4))
