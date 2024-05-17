lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def lista_pares():
    lista_filtrada = list(filter(lambda x : x % 2 == 0,lista_numeros))
    cantidad_pares = len(lista_filtrada)
    return lista_filtrada , cantidad_pares
print("Los numeros pares de la lista: " +", ".join(map(str, lista_numeros)))
lista_resultado = lista_pares()
lista_par , cantidad = lista_resultado
print("Resultado: " + ", ".join(map(str, lista_par)) + " \n Cantidad Pares:" + str(cantidad))