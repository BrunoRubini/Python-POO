from datetime import datetime

class Estadia:
    def __init__(self,nro_patente:str,) -> None:
        self.nro_patente = nro_patente
        self.fecha = datetime.now().date()
        now = datetime.now()
        self.hora_entrada = now.strftime("%H:%M")
        self.hora_salida = None
        self.estado = 'Activo'
        self.pagado = False


        
    def __str__(self) -> str:
        return (f'fecha: {self.fecha} patente: {self.nro_patente} hora entrada: {self.hora_entrada} hora salida: {self.hora_salida} pagado: {self.pagado}')
    
    def registrar_salida(self):
        #now = datetime.now()
        #self.hora_salida = now.strftime("%H:%M")
        self.hora_salida = '18:50'
        self.estado = 'Pagado'
        self.pagado = True
        # Convertir las horas de entrada y salida a objetos datetime
        hora_entrada_dt = datetime.strptime(self.hora_entrada, "%H:%M")
        hora_salida_dt = datetime.strptime(self.hora_salida, "%H:%M")
        # Calcular la cantidad de horas
        self.cant_horas = hora_salida_dt - hora_entrada_dt
estadia1 = Estadia('ABC123')