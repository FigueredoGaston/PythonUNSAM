#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()

""" def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell') """

#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':     #Convertir a minúscula y no necesito el "else" del "if" ya que si no saldría siempre después de leer la primera letra
            return True
        i += 1
    return False    #Si no retorno nada el valor es "NONE"

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente

""" def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell') """

#    A continuación va el código corregido

def tiene_a(expresion):     #Falta ":"
    n = len(expresion)
    i = 0
    while i<n:  #Falta ":"
        if expresion[i].lower() == 'a':   #Si pongo "=" es asignación, corresponde "==", falta ":" y lo convierto a minúscula
            return True
        i += 1
    return False    #No es Falso es "False"

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%
#Ejercicio 3.3. Función tiene_uno()

""" def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984) """

#   A continuación va el código corregido

def tiene_uno(expresion):
    string = str(expresion)    #Convierto la expersión a una cadena
    n = len(string)      #Al ingresar 1984 como entero no sirve la función len()
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if string[i] == '1':
            tiene = True
        i += 1
    return tiene

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

#%%
#Ejercicio 3.4. Función suma()

""" def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")"""

#   A continuación va el código corregido

def suma(a,b):
       return a + b     #LA función no retorna nada, por eso la variable se se impreme como "NONE"
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5 Función leer_camion()

""" import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
"""
#   Lo que está haciendo es asignar valores al mismo espacio de memoria.
#   Lo corregí generando un diccionario por cada hilera
#   A continuación va el código corregido


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    i=0
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        registro={}
        for fila in filas:
            registro = {    
                        encabezado[0] : fila[0],
                        encabezado[1] : int(fila[1]),
                        encabezado[2] : float(fila[2])
                        }
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)