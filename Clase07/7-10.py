#!/usr/bin/env python3
#Ejercicio 7.10: Funciones y documentación

def valor_absoluto(n):
    '''Retorna la distancia desde cero y un número, en una recta numérica.

    Pre: n debes ser un valor nuérico.
    Pos: Se devuelve el valor numérico sin signo.
    '''

    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    '''De una lista numérica suma los valores pares,
    si ninguno es par devuleve cero.

    Pre: l debes ser una lista de números.
    Pos: Se devuelve la sumatoria de todos los pares de la lista,
        si no contiene valores pares devuelve cero.
    '''

    res = 0 #Invariante de ciclo
    for e in l:
        if e % 2 ==0:   #Si el resto es 0 es par y lo suma, si no sigue con el siguiente nro.
            res += e
        else:
            res += 0
    
    '''Res tiene que partir de cero por si la lista
        no contiene valores pares'''
    return res

def veces(a, b):
    '''Suma el valor "a", "b" veces.

    Pre: a y b tienen que ser números enteros y b >= que 0.
    Pos: Se devuelve la sumatoria de "a", "b" veces.
    '''

    res = 0 #Invariante de ciclo
    nb = b  #Invariante de ciclo
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1

    '''res debe partir de cero por si se tiene que repetir
    cero veces el valor de "a" y "nb" toma el valor de "b" para
    no modificar el valor de la variable original.
    '''
    return res

def collatz(n):
    '''Devuelve la cantidad de veces que se procesa un número hasta llegar a 1
    (conjetura de Collaz).

    Pre: n tiene que un número entero y mayor que 0.
    Pos: Se devuelve la sumatoria de veces que se procesa un número.
    '''

    res = 1 #Invariante de ciclo

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    '''res debe partir de uno por si el número ingresado es uno.
    '''
    return res

if __name__=="__main__":
    print(collatz(13))