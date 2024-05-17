class Materia:
    def __init__(self,nombre:str) -> None:
        self.nombre:str = nombre
        pass
class Carrera:
    def __init__(self, materias) -> None:
        self.lista = []  
        self.lista.extend(materias)
    def __str__(self) -> str:
        materias_str = ", ".join(materia.nombre for materia in self.lista)
        return f"Carrera(materias=[{materias_str}])"
    def __len__(self) -> int:
        return len(self.lista)

matematica = Materia("Matemática")
estadistica = Materia(nombre="Estadística")
ciclo_basico = Carrera([matematica, estadistica])
print(ciclo_basico)

str(ciclo_basico) == "Carrera(materias=[Materia(nombre='Matemática'), Materia(nombre='Estadística')])"  


print(len(ciclo_basico) == 2)
def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        numeros = [i for i in range(a, b+1)]
    else:
        numeros = [i for i in range(b, a+1)]
    return sum(numeros)
print(get_sum(0,-1))