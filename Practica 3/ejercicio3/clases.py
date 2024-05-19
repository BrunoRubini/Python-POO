
from datetime import date
import datos
import random
import string
class Libro:
    def __init__(self,nombre:str,fecha_lanzamiento: date) -> None:
        self.nombre = nombre
        self.autor = "Unknow"
        self.fecha_lanzamiento = fecha_lanzamiento
        self.__isbn = self.generar_ISBN()
    def generar_ISBN(self) ->str:
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod
    def __str__(self) -> str:
        return 'Nombre Libro: ' + self.nombre +' Autor: '+ self.autor + ' Fecha: ' + str(self.fecha_lanzamiento) + ' ISBN: '+ str(self.__isbn)
    
    @property
    def isbn(self):
        return self.__isbn
class TipoDocumento:
    def __init__(self, tipo_documento):
        self._tipo_documento = tipo_documento

    @property
    def tipo_documento(self):
        return self._tipo_documento
    
    def __str__(self):
        return self.tipo_documento

class Persona():
    def __init__(self, nombre, apellido, fecha_nacimiento, nro_documento, tipo_documento):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._nro_documento = nro_documento
        self._tipo_documento = tipo_documento

    @property
    def edad(self):
        today = date.today()
        fecha_nacimiento = self._fecha_nacimiento
        edad = today.year - fecha_nacimiento.year
        if (today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1
        return edad

    def mostrar_informacion(self):
        pass


class Usuario(Persona):
    def __init__(self, nombre, apellido, fecha_nacimiento, nro_documento, tipo_documento, user_name,password, email):
        super().__init__(nombre, apellido, fecha_nacimiento, nro_documento, tipo_documento)
        self._user_name = user_name
        self._password = password
        self._email = email
        self._estado = True
        self._administrador = False
        self._fecha_alta = date.today()
        self._fecha_baja = None
        self.libros_leidos = []

    @property
    def user_name(self):
        return self._user_name
    @property
    def password(self):
        return self._password
    def leyo_libro(self, isbn):
        
        pass

    def validar_credenciales(self, username, password):
        if (username == self.user_name and password == self.password):
            return True
        return False
        

    def baja_usuario(self):
        self._estado = False
        self._fecha_baja = date.today()

    
    def add_libro(self):
        i = 0
        print("Seleccione un libro de la lista para agregar a tu coleccion: ")
        for l in datos.lista_libros:
            print(str(i) + "- Libro: " + l.nombre + " ISBN: " + str(l.isbn))
            i+=1
        opcion = int(input("Ingrese numero de libro: "))
        l = datos.lista_libros[opcion]
        self.libros_leidos.append(l)
        return self.libros_leidos

    def remove_libro(self, l):
        #self.libros_leidos.pop(l)
        #del self.libros_leidos[l]
        self.libros_leidos.remove(l)
        pass

    def mostrar_informacion(self):
        return {
        'Nombre': self._nombre,
        'Apellido': self._apellido,
        'Fecha_nacimiento': self._fecha_nacimiento,
        'Nro_doc': self._nro_documento,
        'Tipo_doc': self._tipo_documento,
        'User_name': self._user_name,
        'Password': self._password,
        'Email': self._email,
        'Edad' : self.edad
    }
    def mostrar_libros_leidos(self):
        i = 0
        print(f"Libros leidos por {self._nombre} {self._apellido}")
        for libro in self.libros_leidos:
            print (f"{i} - Libro: {libro.nombre}, Autor: {libro.autor}, Fecha lanzamiento: {libro.fecha_lanzamiento}, isbn: {libro.isbn}")
            i += 1


