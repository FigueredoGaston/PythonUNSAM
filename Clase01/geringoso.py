# Ejercicio 1.18

string_in = input("Ingrese una palabra: ")
string_exit = ""

# Esto sirve para sacar tildes y diéresis a vocales
a,b = 'áéíóúü','aeiouu'
change = str.maketrans(a,b)

for c in string_in:
    if c.lower() in "aeiouáéíóúü":
        string_exit += c + "p" + c.lower().translate(change)
    else:
        string_exit += c
print(f"La palabra en geringoso: {string_exit}")
