import modulo23
palabras = ["hola", "mundo", "python", "es", "un", "lenguaje", "de", "programación"]
print("Ingrese longitud de palabras para filtrar: ")
largo = int(input())
print("Las palabras con longitud mayor a "+ str(largo) + " son: " + ' '.join(modulo23.longitud_mayor_queX(palabras,largo)))