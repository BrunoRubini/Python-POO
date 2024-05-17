diccionario = {}
contar_letras = 0
def contador_letras(frase):
    contar_letras = 0
    frase = frase.replace(" ", "")
    frase = frase.lower()
    for i in range(len(frase)):
        letra = frase[i]
        for j in frase:
            if j == letra:
                contar_letras+=1
        diccionario[letra] = contar_letras
        contar_letras = 0
    return diccionario

frase = "hola mundkonnnnnYyy"
print(contador_letras(frase))

def contador_letras(cadena):

    diccionario = {}
    for letra in cadena:
        if letra in diccionario.keys():
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    lista_letras_duplicadas = list(diccionario.keys())
    return lista_letras_duplicadas
cadena = "hola mundooooo"
resultado = contador_letras(cadena)
print(resultado)