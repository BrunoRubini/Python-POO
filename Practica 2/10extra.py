def encontrar_mayor(lista):
    mayor = lista[0]
    for n in range(1 , len(lista)):
        if lista[n] > mayor:
            mayor = lista[n]
    return mayor
lista = [1, 1, 1, 1, 6, 1, 1, 2, 2, 9]
print(encontrar_mayor(lista))
def encontrar_may(lista):
    return max([x for x in lista])
print(encontrar_may(lista))