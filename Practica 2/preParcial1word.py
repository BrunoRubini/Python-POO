lista_empleados = []
lista_cursos = ['PHP', 'Python', 'C#', 'HTML_CSS', 'Java', 'JS', 'Ruby', 'Git']


def registrar_empleado():
    empleado = {
        "nombre": '',
        "legajo": 0,
        "cursos_realizados": [],
        "antiguedad": 0
    }
    nombre = input("Ingrese el nombre del empleado a registrar: ")
    legajo = int(input("Ingrese legajo del empleado: "))
    while True:
        antiguedad = int(input("Ingrese antiguedad del empleado: "))
        if antiguedad < 6:
            print("La antiguedad no puede ser menor a 6 meses.")
        else:
            break

    empleado["nombre"] = nombre
    empleado["legajo"] = legajo
    empleado["antiguedad"] = antiguedad
    lista_empleados.append(empleado)


def agregar_curso():
    legajo_buscado = int(input("Ingrese legajo del empleado a buscar: "))
    for emp in lista_empleados:
        if legajo_buscado == emp['legajo']:
            print("Empleado encontrado: " + emp['nombre'])
            while True:
                curso_elegido = seleccionar_curso()
                if curso_elegido in emp['cursos_realizados']:
                    print("Error, el empleado ya cuenta con ese curso registrado")
                elif curso_elegido != False:
                    emp['cursos_realizados'].append(curso_elegido)
                    print("Se ha agregado: " + curso_elegido)
                seguir = int(input("Desea agregar otro curso? 1-Si 0-No: "))
                while seguir != 1 and seguir != 0:
                    print(
                        "Opción inválida, por favor ingrese 1 para continuar o 0 para salir")
                    seguir = int(input())
                if seguir == 0:
                    print("Saliendo...")
                    return
    print("No se ha encontra un empleado con legajo: " + str(legajo_buscado))


def seleccionar_curso():
    print("Cursos Disponibles: ")
    while True:
        print("1-PHP 2-Python 3-C# 4-HTML_CSS 5-Java 6-JS 7-Ruby 8-Git")
        opcion = int(
            input("Ingrese el nro de Curso que desea agregar o 0 para cancelar operación: "))
        if opcion == 0:
            print("Operación Cancelada")
            return False
        elif opcion < 1 or opcion > 8:
            print("Opción inválida, seleccione entre 1 y 8")
        else:
            return lista_cursos[opcion-1]


def mostrar_resumen():
    lista_ordenada = sorted(lista_empleados, key=lambda x: len(
        x['cursos_realizados']), reverse=True)
    for emp in lista_ordenada:
        print("Empleado: " + emp['nombre'] + " - Legajo: " +
              str(emp['legajo']) + " - Antiguedad: " + str(emp['antiguedad']))
        print(f"Cursos realizados: {' - '.join(emp['cursos_realizados'])}")
        print("Cantidad de cursos: " + str(len(emp['cursos_realizados'])))


while True:
    print(" 1- Registrar empleado 2- Agregar nuevo curso 3- Mostrar resumen 4- Salir: ")
    try:
        menu = int(input())
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número entero.")
        continue
    if menu == 1:
        registrar_empleado()
    elif menu == 2:
        agregar_curso()
    elif menu == 3:
        mostrar_resumen()
    elif menu == 4:
        print("Hasta luego")
        break
    else:
        print("Opción inválida , ingrese un numero entre 1 y 4")
