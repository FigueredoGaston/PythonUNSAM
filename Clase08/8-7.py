#!/usr/bin/env python3
#Ejercicio 8.7: Lectura y selección

import pandas as pd
import os

def f_principal():
    directorio = '../Data'
    archivo = 'arbolado-publico-lineal-2017-2018.csv'
    fname = os.path.join(directorio, archivo)
    df = pd.read_csv(fname, dtype = 'unicode')
    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    df_lineal = df[cols_sel]
    df_lineal_nombre = df_lineal['nombre_cientifico'].value_counts()
    df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
    print(df_lineal_nombre.head(10))
    print(df_lineal_seleccion.head(10))

if __name__=="__main__":
    f_principal()