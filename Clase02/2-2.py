### Ejercicio 2.2

total_cost = 0.0

with open('Data/camion.csv', 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            total_cost += int(row[1]) * float(row[2])
print(f"Costo total: {round(total_cost, 2)}")