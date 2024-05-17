class Persona:
    def constructor(self,name,age):
        self.name = name
        self.age = age

    def identificarse(self):
        print(f"hola soy {self.name} y tengo {self.age} años")
juan = Persona()
juan.constructor("bruno",25)
juan.identificarse()

class Persona1:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def identificarse(self):
        print(f"hola soy {self.name} y tengo {self.age} años")
juan = Persona1("bruno",25)
juan.identificarse()

class Persona2:
    def __init__(self,nombre,edad):
        self.name = nombre
        self.age = edad

    def __str__(self):
        return f"hola soy {self.name} y tengo {self.age} años"
juan1 = Persona2("bruno",252)
print(juan1)

class Persona3:
    color = ""
    def __init__(self,name,age:int):
        self.name = name
        self.age = age
    def __del__(self):
        print("objeto eliminado")
    def identificarse(self):
        print(f"hola soy {self.name} y tengo {self.age} años")
juan1 = Persona3("bruno",2115)
juan1.identificarse()
del juan1



class Test:
    color = ""
    def _validate_and_set_name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("El nombre debe ser una cadena")
        self.nombre = name
    def __init__(self, name: str):
        self._validate_and_set_name(name)
    def saludar(self):
        print(f"NOMBRE: {self.nombre} - COLOR: {self.color}")
    
test = Test("aaa")
test.color = "red"
test.saludar()




