"""
Escribir un programa que pida al usuario su peso (en
kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en
una variable, y muestre por pantalla la frase Tu índice de masa
corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
print("Ingrese su peso(kg): ")
peso = int(input())
print("Ingrese su estatura(mts): ")
estatura = float(input())
imc = peso/(estatura**2)
imc = round(imc,2)
print(imc)








"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos
 y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
print("Ingrese cantidad de payasos vendidos: ")
payasos = int(input())
print("Ingrese cantidad de muñecas vendidas: ")
muñecas = int(input())
pesoPayasos = 112
pesoMuñecas = 75
pesoTotal = (payasos*pesoPayasos) + (muñecas*pesoMuñecas)
print("El peso total del pedido es: ",pesoTotal)









"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
 Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
 Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
 Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
Redondear cada cantidad a dos decimales.
"""

interesAnual = 0.04
print("Ingrese cantidad de dinero a depositar: ")
dinero = float(input())
interesGenerado = round(dinero * interesAnual,2)
dinero = round(dinero + interesGenerado,2)
print("Interes generado 1er año: ",interesGenerado," Dinero total: $",dinero)
interesGenerado = round(dinero * interesAnual,2)
dinero = round(dinero + interesGenerado,2)
print("Interes generado 2do año: ",interesGenerado," Dinero total: $",dinero)
interesGenerado = round(dinero * interesAnual,2)
dinero = round(dinero + interesGenerado,2)
print("Interes generado 3er año: ",interesGenerado," Dinero total: $",dinero)



"""
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
 donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
 y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
print("Ingrese su nombre: ")
nombre = input()
print("Su numbre es: " + nombre + "  Cantidad de letras: ",len(nombre))

print("Ingrese una frase: ")
frase = input()
print("Ingrese una vocal: ")
vocal = input()
nuevaFrase = ""
for letra in frase:
    if vocal == letra:
        letra = letra.upper()
    nuevaFrase += letra
print("Frase: " + nuevaFrase)


"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades
 y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros 
 y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

nombre = input("Ingrese nombre del producto: ")
precio = float(input("Ingrese precio del producto: "))
cantidadUnidades = int(input("Ingrese cantidad de unidades: "))
print(f'Nombre: {nombre} Precio Unitario: ${round(precio,2)} Cantidad Unidades: {cantidadUnidades} Costo Total: ${round(precio*cantidadUnidades,2)}')