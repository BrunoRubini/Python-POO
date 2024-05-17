#Escribe un programa que pida al usuario ingresar su edad y luego imprima un mensaje
#indicando si es mayor de edad o no
while True:
    try:
        print("Ingrese su edad")
        edad = int(input())
        if type(edad) == str or type(edad) == bool:
            raise ValueError("Debes ingresar un numero")
        else:
            break
    except ValueError as error:
        print(error)
if edad < 18:
    print("Es menor de edad")
else:
    print("Es mayor de edad")

while True:
    print("Ingrese su edad")    
    try:
        edad = int(input())
        if edad >= 18:
            print("Es mayor de edad")
            break
        elif edad < 0:
            print("La edad no puede ser negativa")
        else:
            print("Es menor de edad")
            break
    except ValueError as error:
        print("Por favor ingrese un numero")