#Ejercicio 5.9: Empezando a plotear


import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=25)
    plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.

def main():
    print(plotear_temperaturas())
