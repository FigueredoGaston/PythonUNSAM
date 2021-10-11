#!/usr/bin/env python3
#Ejercicio 8.13: Otros puertos

from scipy import signal # para procesar señales
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

def calcular_fft(y, freq_sampleo = 24.0):
    '''y debe ser un vector con números reales
    representando datos de una serie temporal.
    freq_sampleo está seteado para considerar 24 datos por unidad.
    Devuelve dos vectores, uno de frecuencias 
    y otro con la transformada propiamente.
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran

def f_principal():
    df=pd.read_csv('../Data/OBS_Zarate_2013A.csv',index_col=['Time'],parse_dates=True)
    inicio = '2012-07'
    fin = '2013-06'
    alturas_zr = df[inicio:fin]['H_Zarate'].to_numpy()
    freq_zr, fft_zr = calcular_fft(alturas_zr)
    pico_zr = signal.find_peaks(np.abs(fft_zr), prominence = 5)[0][-1]
    ang_zr = np.abs(np.angle(fft_zr)[pico_zr])
    ret_zr = ang_zr * 24 / (2 * np.pi * freq_zr[350])
    td = timedelta(hours=ret_zr)
    dt = datetime.min + td
    print("Tiempo (expresado en horas y minutos) que le toma a la onda de marea llegar de Buenos Aires a Zárate: {:%H:%M}".format(dt))

if __name__=="__main__":
    f_principal()