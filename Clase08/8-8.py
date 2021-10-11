#!/usr/bin/env python3
#Ejercicio 8.8: Boxplots

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

def f_principal():
    directorio = '../Data'
    archivo = 'arbolado-publico-lineal-2017-2018.csv'
    fname = os.path.join(directorio, archivo)
    df = pd.read_csv(fname)#dtype = 'unicode', dtype=object
    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    df_lineal = df[cols_sel]
    df_lineal_nombre = df_lineal['nombre_cientifico'].value_counts()
    df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
    df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
    #sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
    plt.show()

if __name__=="__main__":
    f_principal()