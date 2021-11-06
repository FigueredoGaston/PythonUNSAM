#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 12.7:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def generar_lista(N):
    import random
    lista = []
    for i in range(N):
        lista.append(random.randint(1, 1000))
    return lista


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    lista_aux = lista[:]
    cont = 0

    for i in range(len(lista_aux) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista_aux[i + 1] < lista_aux[i]:
            cont += reubicar(lista_aux, i + 1)
            cont += 1
    return cont


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    cont = 0
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        cont += 1

    lista[j] = v
    return cont


def ord_burbujeo(lista):
    lista_aux = lista[:]
    cont = 0
    for i in range(len(lista_aux)):
        for j in range(i+1, len(lista_aux)):
            cont += 1
            if lista_aux[i] > lista_aux[j]:
                lista_aux[i], lista_aux[j] = lista_aux[j], lista_aux[i]
    return cont


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    lista_aux = lista[:]
    cont = 0
    # posición final del segmento a tratar
    n = len(lista_aux) - 1
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista_aux, 0, n)
        cont += n
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista_aux[p], lista_aux[n] = lista_aux[n], lista_aux[p]
        #print("DEBUG: ", p, n, lista_aux)
        # reducir el segmento en 1
        n = n - 1
    return cont


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""

    if len(lista) < 2:
        lista_nueva = lista
        cont = 0
    else:
        medio = len(lista) // 2
        izq, cont_izq = merge_sort(lista[:medio])
        der, cont_der = merge_sort(lista[medio:])
        lista_nueva, cont_merge = merge(izq, der)
        cont = cont_izq + cont_der + cont_merge
    return lista_nueva, cont


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    cont = 0

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        cont += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, cont


def experimento(N, k):
    """Devuelve Devuelve el promedio de la cantidad
        de operaciones que realiza cada promedio
        Pre: Largo de la lista y cantidad de veces que se genera.
        Post: Tupla con los promedios en este orden:
            1 Método burbuja
            2 Método inserción
            3 Método selección
            4 Método merge"""

    m_burbuja = 0
    m_insercion = 0
    m_seleccion = 0
    m_merge_aux = 0

    for i in range(k):
        lista = generar_lista(N)
        m_burbuja += ord_burbujeo(lista.copy())
        m_insercion += ord_insercion(lista.copy())
        m_seleccion += ord_seleccion(lista.copy())
        m_merge = merge_sort(lista.copy())
        m_merge_aux += m_merge[1]
    return (m_burbuja/k, m_insercion/k, m_seleccion/k, m_merge_aux/k)


def experimento_vectores(Nmax):
    """Devuelve una lista con los resultados de los experimentos
       con N desde 1 hasta Nmax.
       Pre: Nmax es un número entero positivo.
       Post: Una lista con los resultados de los experimentos."""

    lista = []
    for N in range(1, Nmax + 1):
        lista.append(experimento(N, 100))
    comparaciones_burbujeo = np.array([i[0] for i in lista])
    comparaciones_insercion = np.array([i[1] for i in lista])
    comparaciones_seleccion = np.array([i[2] for i in lista])
    comparaciones_merge = np.array([i[3] for i in lista])
    return (comparaciones_burbujeo, comparaciones_insercion, comparaciones_seleccion, comparaciones_merge)


if __name__ == '__main__':
    exp = experimento_vectores(100)

    plt.plot(np.arange(1, 101), exp[0], label='Burbuja')
    plt.plot(np.arange(1, 101), exp[1], label='Inserción')
    plt.plot(np.arange(1, 101), exp[2], label='Selección')
    plt.plot(np.arange(1, 101), exp[3], label='Merge')
    plt.xlabel('Largo de la lista')
    plt.ylabel('Cantidad de comparaciones')
    plt.legend()
    plt.title('Comparación de ordenamientos')
    plt.show()
