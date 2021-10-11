# Ejercicio 3.17: Tablas de multiplicar

print(f'{"":>6}', end='')
for i in range(10):
    print('%7s' % i, end='')
print()
for i in range(11):
    print(f'{"":->7}', end='')
print()
for i in range(10):
    count = 0
    print(f'{str(i)+":":>7}', end='')
    for j in range(10):
        print(f'{count:>7}', end='')
        count+=i
    print()