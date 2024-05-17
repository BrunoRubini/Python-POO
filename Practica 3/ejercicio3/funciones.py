import datos
import clases

def alta_usuario()->clases.Usuario:
    # ● Se le solicita al usuario que ingrese: username, email, apellido, nombre, fecha de
    # nacimiento y número de documento.
    # nombre, apellido, fecha_nacimiento, edad, nro_documento
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    fecha_nacimiento = input("Ingrese fecha de nacimiento: ")
    
    print("Ingrese una de las siguientes opciones: ")
    print("Elija del 1 al 3: ")
    i = 1
    for doc in datos.lista_tipo_documentos:
        print(f"{i} - {doc.__str__()}")
        i += 1
    tipo_documento = input()
    nro_documento = input("Ingrese el nro de documento: ")
    user_name = input("Ingrese el User name: ")
    email = input("Ingrese el email: ")

    #     Luego se le solicita al usuario que ingrese su contraseña 2 veces, la misma debe
    # coincidir y tener longitud entre 8 y 10 caracteres y tener al menos un carácter
    # numérico.

    while True:
        contraseña1 = input("Ingrese una contraseña, la misma debe tener entre 8 y 10 caracteres y tener al menos un caracter numerico: ")
        if validar_contraseña(contraseña1):
            contraseña2 = input("Confirme su contraseña: ")
            if(validar_contraseña(contraseña2)):
                if contraseña1 == contraseña2:
                    break
                else:
                    print("No coincide la contraseña, intentelo nuevamente.")
            else:
                print("Hubo un error, intentelo nuevamente.")
        else:
            print("Formato de contraseña incorrecta, intenlo nuevamente.")

    

    # Se le solicita al usuario que ingrese si el usuario que está dando de alta es un usuario
    # administrador.
    isAdmin = int(input("Ingrese 1 si el usuario que esta dando de alta es administrador, 0 si no lo es: "))
    if isAdmin == 1:
        isAdmin = True
    else:
        isAdmin = False
    nuevoUsuario = clases.Usuario(nombre, apellido, fecha_nacimiento, nro_documento,tipo_documento,user_name,contraseña1, email)
    nuevoUsuario._administrador = isAdmin
    print("Usuario creado exitosamente.")
    return nuevoUsuario

def validar_contraseña(password)->bool:
    if(len(password) >= 8 and len(password) <= 10):
        if any(char.isdigit() for char in password):
            return True
    
    return False

def buscar_usuario():
    pass
def buscar_libro():
    pass