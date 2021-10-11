### Ejercicio 2.7: Buscar precios

fruit_name = ""
exist_article = []

def fruitPrice(article):
    cost = 0.0
    with open('../Data/precios.csv', 'rt') as f:
        for line in f:
            row = line.split(',')
            if row[0].lower() == article.lower():  ### Paso los datos a minúsculas para unificar la búsqueda
                cost = float(row[1])
                return [True,cost]  ###Retorno una lista si existe el artículo y el precio
    return [False,cost]

fruit_name = input("Ingrese una fruta: ")
exist_article = fruitPrice(fruit_name)
if exist_article[0]:
    print(f"El precio de la {fruit_name.lower()} es: {round(exist_article[1], 2)}")
else:
    print(f"No hay {fruit_name.lower()} en la lista.")