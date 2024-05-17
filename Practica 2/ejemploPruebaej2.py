lista_medicos = []
def registrar():
    medico = {
    'Nombre': [],
    'dni': 0,
    'titulos_realizados': ['Médico Clínico'],
    'cantidad_titulos' : 1
    }
    print("Ingrese nombre del médico: ")
    medico['Nombre'] = input()
    print("Ingrese DNI del médico:")
    documento = int(input())
    if validar_numero_documento(lista_medicos , documento) == False:  #Si la funcion me devuelve False es que no fue encontrado el dni, por lo tanto puedo hacer el registro
        medico['dni'] = documento
        lista_medicos.append(medico)
def validar_numero_documento(medicos: list, nro_doc: str) -> bool:   # ESTO VA EN UN MODULO APARTE
    for meds in medicos: #meds seria un diccionario que tengo en mi lista_medicos
       for meds in medicos:
        if nro_doc == meds['dni']:
            print("Error, ya se encuentra registrado")
            return True
    print("DNI Correcto, puede proceder")
    return False
def agregar_titulo():
    encontrado = False
    print("Ingrese DNI del médico a buscar: ")
    dni_buscado = int(input())
    for meds in lista_medicos:
        if dni_buscado == meds['dni']:
            encontrado = True
            print("Médico encontrado: " + meds['Nombre'])
            print("Ingrese titulo médico a agregar: ")
            titulo = input()
            meds['titulos_realizados'].append(titulo)
            meds['cantidad_titulos'] += 1
            return
    if encontrado == False:
        print("No hay un médico registrado con dni: " + str(dni_buscado))
def mostrar_resumen():
    i = 1
    for med in ordenar_cantidad_titulos():
        print(str(i))
        print(med['Nombre'] + " - Nro Doc:" + str(med['dni']))
        titulos_concatenados = ", ".join(med['titulos_realizados'])
        print("Títulos realizados: " + titulos_concatenados)
        print("Cantidad de títulos: " + str(med['cantidad_titulos']))
        i += 1
def ordenar_cantidad_titulos():
    lista_ordenada = sorted(lista_medicos, key=lambda x: x['cantidad_titulos'] , reverse=True) # en este caso x seria cada diccionario de mi lista, por lo tanto accedo a su cantidad de titulos
    return lista_ordenada
   
while True: #Se podria meter en una funcion
        print("\nMenu:")
        print("1. Registrar médico")
        print("2. Agregar título")
        print("3. Mostrar resumen")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            registrar()
        elif opcion == '2':
            agregar_titulo()
        elif opcion == '3':
            mostrar_resumen()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


