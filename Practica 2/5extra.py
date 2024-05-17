diccionario={}
claves = ('a','b','c','d','e')
valores = (5, 15, 25, 35, 45)
diccionario = dict(zip(claves,valores))
print(diccionario)

for clave, valor in zip(claves, valores):
    diccionario[clave] = valor
print(diccionario)

for i in range(len(claves)):
    clave = claves[i]
    valor = valores[i]
    diccionario[clave] = valor
print(diccionario)
test = list(zip(claves,valores)) # Lista de tuplas a partir de 2 tuplas
print(test)
numeros = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
nums = [0,1,2,3,4,5]
test1 = dict(zip(numeros,nums)) # diccionario de tuplas a partir de 2 listas
print(test1)