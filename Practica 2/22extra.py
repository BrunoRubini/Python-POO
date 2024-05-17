def filtrar_longitud_mayor_5(lista):
    filtrados = list(filter(lambda x: len(x) > 5, lista))
    return filtrados

lista = ["hola","mundo","asdddad","te","mate","cafeeee","5letra"]
print(filtrar_longitud_mayor_5(lista))