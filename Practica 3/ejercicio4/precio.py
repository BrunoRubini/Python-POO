import estadia
class Precio:
    def __init__(self) -> None:
        self.precio_hora = 1000
    def calcular_importe(self,cant_horas):
        return self.precio_hora * cant_horas.total_seconds() / 3600

precio = Precio()
print(estadia.estadia1)
estadia.estadia1.registrar_salida()
print("El precio es: " + str(precio.calcular_importe(estadia.estadia1.cant_horas)))
