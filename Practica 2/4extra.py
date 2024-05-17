numeros = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

for num in numeros:
    if num % 2 == 0:
        print(f"El numero: {num} es par")
pares = tuple([num for num in numeros if num % 2 == 0])
print(pares)