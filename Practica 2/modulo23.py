def longitud_mayor_queX(lista_palabras,largo):
    lista_filtrada = list(filter(lambda x:len(x)>largo ,lista_palabras))
    return lista_filtrada