def numeros_cuadrados(lista_numeros):
    cuadrados = list(map(lambda x : x**2 , lista_numeros))
    return cuadrados
lista_numeros = []
while True:
    print("Ingrese 1 para agregar numeros a la lista , 0 para salir: \n")
    opcion = int(input())
    if opcion == 1:
        print("Ingrese numeros para agregar a la lista y mostrar sus cuadrados: ")
        agregar = int(input())
        lista_numeros.append(agregar)
        print(numeros_cuadrados(lista_numeros))
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opcion incorrecta, por favor ingrese 1 para agregar o 0 para salir")
