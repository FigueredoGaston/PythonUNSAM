#!/usr/bin/env python3
#Ejercicio 8.1: Segundos vividos

from datetime import datetime

def vida_en_segundos(fecha_nac):
    b_day = datetime.strptime(fecha_nac, '%d/%m/%Y')
    today = datetime.now()
    dif = today - b_day
    return dif.total_seconds()

if __name__=="__main__":
    print(f'Viviste {vida_en_segundos("18/01/1985")} segundos!!')