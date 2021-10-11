"""with open('Data/camion.csv', 'rt') as f:
        data = f.read()
print(data)

with open('Data/camion.csv', 'rt') as f:
        for line in f:
            print(line, end = '')

with open('Data/camion.csv', 'rt') as f:
        headers = next(f)
        print(headers)
        for line in f:
            print(line, end = '')"""

with open('Data/camion.csv', 'rt') as f:
        headers = next(f)
        print(headers)
        for line in f:
            row = line.split(',')
            print(row)
