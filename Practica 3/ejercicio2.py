from datetime import date
class Persona:
    def __init__(self,nombre:str,apellido:str,fecha_nacimiento,edad:int,nro_documento:int) -> None:
        self.__nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._edad = edad
        self._nro_documento = nro_documento
    def __str__(self) -> str:
        return f"PERSONA: Nombre: {self.__nombre} Apellido: {self._apellido} Edad: {self._edad} DNI: {self._nro_documento}"
    

class Usuario(Persona):
    def __init__(self, user_name: str, password: str, email: str,__nombre, apellido, fecha_nacimiento, edad, nro_documento) -> None:
        super().__init__(__nombre, apellido, fecha_nacimiento, edad, nro_documento)
        self.__user_name = user_name 
        self.estado = True 
        self.email = email
        self.password = password
        self.fecha_alta = date.today()
        self.fecha_baja = None

    def __str__(self) -> str:
        return f"User: {self.__user_name} Estado: {self.estado} Fecha alta: {self.fecha_alta} Fecha baja: {self.fecha_baja} Nombre: {self._nombre}"
    def validar_credenciales(self, usuario, passw):
        return self.__user_name == usuario and self.password == passw

    def baja_usuario(self):
        self.estado = False
        self.fecha_baja = date.today()

nuevo_usuario = Usuario('brunoUser', 'password', 'bruno@gmail.com','Bruno','Rubini',(1800-10-12),25,12345)
nuevo_usuario._nombre = "testttt"
print("DATOS USUARIO",nuevo_usuario)
print(nuevo_usuario.validar_credenciales('brunoUser', 'password'))  #DEVUELVE TRUE O FALSE
nuevo_usuario.baja_usuario()  
print("DATOS USUARIO",nuevo_usuario)

print("___"*25)
nueva_persona = Persona("nameTest","apellTEst",(1900-10-15),50,41492)
nueva_persona.__nombre = "changedName"
print(nueva_persona)