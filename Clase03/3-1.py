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