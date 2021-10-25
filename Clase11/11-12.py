#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 11.12: Envolviendo a Fibonacci

def fibonacci(n):
    """
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    """

    def fib(n):
        """Precondición: n >= 0.
        Devuelve: el número de Fibonacci número n."""
        if n == 0:
            res = 0
        elif n == 1:
            res = 1
        else:
            res = fib(n - 1) + fib(n - 2)
        return res

    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            F = dict_fibo[n]
        else:
            F = fib(n)
            dict_fibo[n] = F
        return F, dict_fibo

    dict_fibo = {0: 0, 1: 1}
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F


if __name__ == '__main__':
    print(fibonacci(7))
