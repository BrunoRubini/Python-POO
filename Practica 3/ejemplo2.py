"""DataClasses y Sobrecarga de operadores."""

from dataclasses import dataclass
from typing import List


"""Una carrera tiene varias materias, la "longitud" de una carrera hace
referencia a cuantas materias tiene.

Cada materia tiene un nombre.

Escribir una estructura de clases que refleje lo anterior.

Restricciones:
    - Utilizar Dataclasses
    - Utilizar 2 clases
    - Utilizar 1 variables de instancia en cada clase
    - Utilizar 1 método mágico
    - No utilizar variables de clase
    - No utilizar métodos de clase
    - No utilizar métodos de instancia
    - No utilizar properties
    - Utilizar Type Hints en todos los métodos y variables
"""
@dataclass
class Materia:
    nombre: str
@dataclass
class Carrera:
    materias: List[Materia]

    def __str__(self):
        return f"Carrera(materias={self.materias})"
materia1 = Materia("matemática")
materia2 = Materia("test2")
materia2.nombre = ("change")
ciclo_basico = Carrera([materia1, materia2])
print(ciclo_basico)