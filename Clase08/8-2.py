#!/usr/bin/env python3
#Ejercicio 8.2: Cuánto falta

from datetime import datetime

def f_principal(parametros):
    b_day = datetime.strptime(parametros, '%d/%m/%Y')
    today = datetime.now()
    dif = b_day - today
    return dif.days

if __name__=="__main__":
    print(f'Faltan {f_principal("22/09/2022")} días para primavera!!')