### Ejercicio 2.6

total_cost = 0.0

def costTruck (name_file):
    with open(name_file, 'rt') as f:
            cost = 0.0
            headers = next(f)
            for line in f:
                row = line.split(',')
                cost += int(row[1]) * float(row[2])
    return cost

total_cost = costTruck('Data/camion.csv')
print(f"Costo total: {round(total_cost, 2)}")