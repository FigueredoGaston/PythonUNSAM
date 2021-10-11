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