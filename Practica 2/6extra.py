# Crear un diccionario con claves string y valores enteros
diccionario = {
    "uno": 1,
    "dos": 2,
    3: 3,
    "cuatro": 4,
    "cinco": 5
}
for clave in diccionario.keys():
    if type(clave) == str:
        print(clave)
for key in diccionario:
    if isinstance(key, str):
        print(key)