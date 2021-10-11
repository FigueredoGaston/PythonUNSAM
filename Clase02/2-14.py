### Ejercicio 2.14: Diccionario geringoso.

dictionary = {}

def geringoso (list_in):
    a,b = 'áéíóúü','aeiouu'
    change = str.maketrans(a,b)
    dict_out = {}

    for string in list_in:
        string_out = ""
        for c in string:
            if c.lower() in "aeiouáéíóúü":
                string_out += c + "p" + c.lower().translate(change) ### Esto sirve para sacar tildes y diéresis a vocales
            else:
                string_out += c
        dict_out[string] = string_out
    return dict_out

list = ['banana', 'manzana', 'mandarina']
print(list)
dictionary = geringoso(list)
for k in dictionary:
    print(k, '=', dictionary[k])
