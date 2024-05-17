import moduloPreparcial1
lista_empleados = []
def registrar_empleado():
    empleado = { 
             'nombre': '',
             'legajo': '',
             'cursos_realizados': [],
             'cantidad_cursos': 0,
             'antiguedad_meses': 0
             }
    print("Ingrese nombre del empleado: ")
    nombre_empleado = input()
    empleado["nombre"] = nombre_empleado
    print("Ingrese legajo: ")
    legajo_empleado = int(input())
    while(len(str(legajo_empleado)) < 5):
        print("El legajo debe ser mayor a 5 caracteres. Vuelva a ingresar legajo: ")
        legajo_empleado = int(input())
    empleado["legajo"] = legajo_empleado
    print("Ingrese antiguedad en meses del empleado: ")
    antiguedad_empleado = input()
    empleado["antiguedad_meses"] = antiguedad_empleado
    lista_empleados.append(empleado)
def agregar_nuevo_curso():
    print("Ingrese legajo del empleado a buscar: ")
    legajo_buscado = int(input())
    for emp in lista_empleados:
        if emp['legajo'] == legajo_buscado:
            print("Empleado encontrado: " + str(emp['nombre']))
            print("Ingrese curso a agregar: ")
            curso_agregar = input()
            emp['cursos_realizados'].append(curso_agregar)
            emp['cantidad_cursos'] += 1
            print("El curso " + curso_agregar + " ha sido agregado correctamente")
            return
    print("El empleado de legajo: " + str(legajo_buscado) + " no ha sido encontrado")

def ordenar_por_cantidad_cursos():
    lista_ordenada = sorted (lista_empleados , key = lambda x : x['cantidad_cursos'] , reverse=True)
    return lista_ordenada

def mostrar_resumen(): 
    for emp in ordenar_por_cantidad_cursos():
        print(str(emp['nombre']) + ' - Legajo: ' + str(emp['legajo']) + ' - Antiguedad: ' + str(emp['antiguedad_meses']) + ' meses.')
        print("Cursos: " + ' - '.join(emp['cursos_realizados']))
        print("Cantidad de cursos: " + str(emp['cantidad_cursos']))
        if moduloPreparcial1.validar_estandar_conocimiento(int(emp['cantidad_cursos']) , int(emp['antiguedad_meses'])):
            print("Cumple con el estandar")
        else:
            print("No cumple con el estandar")
while True:
    print("Ingrese una opcion: ")
    print("1-Registrar empleado 2-Agregar nuevo curso 3-Mostrar resumen 4-Salir")
    opcion = int(input())
    if opcion == 1:
        registrar_empleado()
    elif opcion == 2:
        agregar_nuevo_curso()
    elif opcion == 3:
        mostrar_resumen()
    elif opcion == 4:
        print("Hasta luego")
        break
    else:
        print("Opcion Incorrecta")