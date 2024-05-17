print("Helloooaoa mundo")
#Aritmética básica
#1 Calcular el área del cuadrado usando las variables disponibles.
#Restricción: Usar el operador de multiplicación
print("#1")
lado_cuadrado = 5
area_cuadrado = lado_cuadrado*lado_cuadrado
print(area_cuadrado)

#2 Re-Escribir usando el operador de potencia.
print("#2")
area_cuadrado = (lado_cuadrado ** 2)
print(area_cuadrado)

#3 Re-Escribir usando la función pow.
print("#3")
area_cuadrado = pow(lado_cuadrado,2)
print(area_cuadrado)

#4 Calcular la cantidad de unidades a comprar.
#Restricción: Usar el operador de división entera.
print("#4")
precio = 3.74
presupuesto_disponible = 10
cantidad_a_comprar=int(presupuesto_disponible//precio)
print(cantidad_a_comprar)

#Determinar si el número de la variable es divisible por 7.
#Restricción: Usar el operador módulo.
print("#5")  
numero_incalculable = 2 ** 54 - 1
es_divisible_por_siete = numero_incalculable % 7 == 0
print(es_divisible_por_siete)
#print(1<0<1/0)
precio=5
nombre="test"
texto="{1} debe pagar ${0}".format(precio,nombre)
print(texto)
#input()