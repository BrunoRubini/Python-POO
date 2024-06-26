import datos
import clases
import funciones
listaUsuarios = datos.retornar_lista() # traigo la lista de mi Datos.py

def login():
    user = input("Ingrese nombre de usuario: ")
    passw = input("Ingrese contraseña: ")
    for usuario in listaUsuarios:
        if usuario._user_name == user:
            if usuario.validar_credenciales(user, passw):
                Menu(usuario)
                return
            else:
                print("Datos incorrectos.")
                return
    print("Usuario no encontrado")


def Menu(usuario: clases.Usuario):
    
    while True:
        print()
        print("Menú: ")
            #en este caso usamos de ejemplo al admin
        if usuario._administrador:
            #si devuelve true significa que el usuario es administrador, por lo tanto mostramos el menu para administradores
            print("1-Nuevo usuario")
            print("2-Buscar usuario")
        print("3-Buscar libro")
        print("4-Ver libros")
        print("5-Agregar libro a mi coleccion")
        print("6-Eliminar libro de mi coleccion")
        print("7-Cerrar sesión")
        print()
        opcion_menu = int(input("Ingrese una de las opciones: "))
        if opcion_menu == 1:
            listaUsuarios.append(funciones.alta_usuario())
        elif opcion_menu == 2:
            funciones.buscar_usuario()
        elif opcion_menu == 3:
            funciones.buscar_libro()
        elif opcion_menu == 4:
            #pedir un user_name para buscar sus libros
            usuario.mostrar_libros_leidos() # pasar como parametro un user_name
        elif opcion_menu == 5:

            usuario.add_libro()
        elif opcion_menu == 6:
            i = 0
            for l in usuario.libros_leidos:
                print("Opción: "+str(i) +" - Libro: " + l.nombre + " Autor: " + l.autor + " ISBN: " + str(l.isbn))
                i+=1
            opcion = int(input("Ingrese numero de libro a eliminar: "))
            l = usuario.libros_leidos[opcion]
            usuario.remove_libro(l)
        elif opcion_menu == 7:
            print("Cerrando sesion.")
            login()
            break
        else:
            print("Opción incorrecta.")
while True:  
    login()