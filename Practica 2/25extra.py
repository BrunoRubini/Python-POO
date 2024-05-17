def filtrar_subcadena(lista_palabras,subcadena):
    lista_filtrada = list(filter(lambda x : subcadena in x,lista_palabras))
    return lista_filtrada
palabras = ["hola", "mundo", "python", "es", "un", "lenguaje", "de", "programación"]
print("Ingrese una subcadena para filtrar palabras: ")
subcadena = str(input())
print("Las palabras filtradas: " + ' '.join(filtrar_subcadena(palabras,subcadena)))