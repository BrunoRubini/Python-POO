from datetime import date
class Cliente:
    __nro_cliente_ant = 0

    def __init__(self, nombre_apellido: str, direccion: str):
        self.__nombre_apellido = nombre_apellido
        self.__direccion = direccion
        self.__nro_cliente = Cliente.__nro_cliente_ant
        Cliente.__nro_cliente_ant += 1
        self.__fecha_alta = date.today()
        self.__fecha_baja = None

    def get_nombre_apellido(self):
        return self.__nombre_apellido

    def get_direccion(self):
        return self.__direccion

    def get_nro_cliente(self):
        return self.__nro_cliente

    def get_fecha_alta(self):
        return self.__fecha_alta

    def get_fecha_baja(self):
        return self.__fecha_baja

    def eliminar_cliente(self):
        print("Cliente dado de baja")
        self.__fecha_baja = date.today()
    def reactivar_cliente(self):
        print("Cliente reactivado")
        self.__fecha_baja = None
    def __str__(self):
        return (f"{self.__nro_cliente}: {self.__nombre_apellido}, {self.__direccion}, "
                f"Alta: {self.__fecha_alta}, Baja: {self.__fecha_baja}")