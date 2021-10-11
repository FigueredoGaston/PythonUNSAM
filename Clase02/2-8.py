### Ejercicio 2.8: Administración de errores

total_cost = 0.0

def costTruck (name_file):
    with open(name_file, 'rt') as f:
            cost = 0.0
            headers = next(f)
            for line in f:
                try:
                    row = line.split(',')
                    cost += int(row[1]) * float(row[2])
                except:
                    print(f"Datos no válidos.")
    return cost

total_cost = costTruck('Data/missing.csv')
print(f"Costo total: {round(total_cost, 2)}")