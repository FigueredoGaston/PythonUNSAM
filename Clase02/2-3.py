### Ejercicio 2.3: Precio de la naranja

total_cost = 0.0

with open('Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        if row[0] == "Naranja":
            total_cost = float(row[1])
if total_cost != 0.0:
    print(f"El precio de la naranja es: {round(total_cost, 2)}")
else:
    print("No hay naranjas en la lista.")