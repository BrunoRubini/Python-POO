from datetime import date
import clases

lista_usuarios = []
user = clases.Usuario('bruno','rubini',date(1998, 10, 12),12345,'DNI','userBruno','123','br@test.com')
admin = clases.Usuario('adminName','adminApellido',date(2023, 5, 3),9999,'PASAPORTE','admin','123','admin@admin.com')
admin._administrador = True

print(user.mostrar_informacion())
print(admin.mostrar_informacion())
dni = clases.TipoDocumento('DNI')
licencia = clases.TipoDocumento('Licencia')
pasaporte = clases.TipoDocumento('Pasaporte')
lista_tipo_documentos = []
lista_tipo_documentos.append(dni)
lista_tipo_documentos.append(pasaporte)
lista_tipo_documentos.append(licencia)
print(' - '.join(str(tipo_documento) for tipo_documento in lista_tipo_documentos))

libro1 = clases.Libro("libro1", date(1950, 10, 15))
libro2 = clases.Libro("libro2", date(1900, 12, 25))
libro3 = clases.Libro("libro3", date(1700, 8, 5))
lista_libros = []
lista_libros.append(libro1)
lista_libros.append(libro2)
lista_libros.append(libro3)
print('\n'.join(str(libro) for libro in lista_libros))
def retornar_lista():
    lista_usuarios.append(user)
    lista_usuarios.append(admin)
    return lista_usuarios
