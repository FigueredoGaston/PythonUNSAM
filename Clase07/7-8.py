#!/usr/bin/env python3
#%%
#Ejercicio 7.8: Sumas

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    if hasta < desde:
        return 0
    sumatoria = desde
    for i in range(desde+1, hasta):
        sumatoria += i
    return sumatoria

if __name__=="__main__":
    print(sumar_enteros(2, 5))

#%%
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    if hasta < desde:
        return 0
    n = hasta - desde
    return int(((n*(n+1))/2)+n)

if __name__=="__main__":
    print(sumar_enteros(2, 5))

# %%
