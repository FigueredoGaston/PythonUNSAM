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