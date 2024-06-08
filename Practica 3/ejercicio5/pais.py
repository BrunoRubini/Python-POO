from provincia import Provincia
class Pais:
    def __init__(self,nombre) -> None:
        self.__nombre = nombre
        self.__provincias = []
    @property
    def get_nombre(self):
        return self.__nombre
    @property
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def __str__(self) -> str:
        return self.__nombre
    
    def get_provincias(self):
        return self.__provincias
    def get_provincia(self,indice):
        return self.__provincias[indice]
    def add_provincia(self,provincia:Provincia):
        if provincia not in self.__provincias:
            self.__provincias.append(provincia)
            print("Provincia agregada con exito")
        else:
            print("Ya se encuentra agregada dicha provincia")
    def remove_provincia(self,provincia:Provincia):
        if provincia in self.__provincias:
            self.__provincias.remove(provincia)
            print("Provincia eliminada con exito")
        else:
            print("No se ha encontrado dicha provincia")
        