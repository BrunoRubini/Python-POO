from localidad import Localidad
class Provincia:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__localidades = []

    @property
    def get_nombre(self):
        return self.__nombre

    def add_localidad(self, localidad: Localidad):
        self.__localidades.append(localidad)

    def remove_localidad(self, localidad: Localidad):
        self.__localidades.remove(localidad)

    def get_localidades(self):
        return self.__localidades
    def get_localidad(self,indice):
        return self.__localidades[indice]
    def __str__(self):
        return self.__nombre

        