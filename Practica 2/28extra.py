lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 , 21 , 23 , 24]
def cantidad_impares():
    cantidad = len(list(filter(lambda x : x % 2 != 0,lista_numeros)))
    return cantidad
print("La cantidad de impares que tiene la lista son: " + str(cantidad_impares()))