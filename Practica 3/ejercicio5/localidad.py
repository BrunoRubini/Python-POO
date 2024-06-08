
class Localidad:
    def __init__(self, nombre: str, cod_postal: int):
        self.__nombre = nombre
        self.__cod_postal = cod_postal

    @property
    def get_nombre(self):
        return self.__nombre

    def get_cod_postal(self):
        return self.__cod_postal

    def __str__(self):
        return f"{self.__nombre} (CP: {self.__cod_postal})"