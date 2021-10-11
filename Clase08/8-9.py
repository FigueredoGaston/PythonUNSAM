#!/usr/bin/env python3
#Ejercicio 8.9: Comparando especies en parques y en veredas

import pandas as pd
import os
import matplotlib.pyplot as plt

def f_principal():
    '''Muestra graficos boxplot de un árbol en específico.
    '''
    cols_sel_p = ['altura_tot', 'diametro', 'nombre_cie']
    cols_sel_v = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']
    directorio = '../Data'
    archivo = 'arbolado-publico-lineal-2017-2018.csv'
    fname = os.path.join(directorio, archivo)
    df = pd.read_csv(fname)
    df_veredas = df[cols_sel_v].copy()
    archivo = 'arbolado-en-espacios-verdes.csv'
    fname = os.path.join(directorio, archivo)
    df = pd.read_csv(fname)
    df_parques = df[cols_sel_p].copy()
    df_tipas_parques = df_parques[df_parques['nombre_cie'].isin(['Tipuana Tipu'])]
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'].isin(['Tipuana tipu'])]
    df_tipas_veredas.columns = ['altura_tot', 'diametro', 'nombre_cie'] #Camio el nombre de las columnas
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    df_tipas.boxplot('diametro', by = 'nombre_cie')
    df_tipas.boxplot('altura_tot', by = 'nombre_cie')
    plt.show()

if __name__=="__main__":
    f_principal()