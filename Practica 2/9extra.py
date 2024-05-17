def eliminar_duplicados(lista):
    lista_filtrada = []
    for n in lista:
        if not n in lista_filtrada:
            lista_filtrada.append(n)
    return lista_filtrada
lista_numeros = [1, 1, 3, 3, 1, 1, 1, 2, 2, 2,4]
print(eliminar_duplicados(lista_numeros))