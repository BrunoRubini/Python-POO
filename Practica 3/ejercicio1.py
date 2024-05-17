from datetime import date

class Usuario:
    def __init__(self, user_name, email, password, nombre, apellido):
        self.__user_name = user_name  # readonly attribute
        self.estado = True  
        self.email = email
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_alta = date.today()
        self.fecha_baja = None
    def __str__(self) -> str:
        return f"user: {self.__user_name} estado: {self.estado} fecha alta: {self.fecha_alta} fecha baja: {self.fecha_baja}"
    def validar_credenciales(self, usuario, passw):
        return self.__user_name == usuario and self.password == passw

    def baja_usuario(self):
        self.estado = False
        self.fecha_baja = date.today()

nuevo_usuario = Usuario('brunoUser ', 'bruno@gmail.com', '123', 'bruno', 'test')
print(nuevo_usuario.validar_credenciales('bruno', '123'))  
nuevo_usuario.baja_usuario()  
print(nuevo_usuario)