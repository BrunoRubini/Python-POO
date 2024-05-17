def ordenar_palabras(lista_palabras):
    lista_palabras = list(map(lambda x: x.upper(), palabras))
    lista_ordenada = sorted(lista_palabras,reverse= True)
    return lista_ordenada
palabras = ["hola", "mundo", "python", "es", "un", "lenguaje", "de", "programación"]
print("Las palabras ordenadas: " + ' '.join(ordenar_palabras(palabras)))