#!/usr/bin/env python3
#Ejercicio 8.3: Fecha de reincorporación

from datetime import datetime, timedelta

def f_principal():
    return datetime.strptime('26/09/2020', '%d/%m/%Y') + timedelta(200)

if __name__=="__main__":
    print(f'Se reincorpora el  {f_principal()}')