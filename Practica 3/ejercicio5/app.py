
from pais import Pais
from provincia import Provincia
from localidad import Localidad
from cliente import Cliente
import datos

def main():
    # Mostrar datos cargados
    for pais in datos.paises:
        print(f"País: {pais.get_nombre}")
        for provincia in pais.get_provincias():
            print(f"  Provincia: {provincia.get_nombre}")
            for localidad in provincia.get_localidades():
                print(f"    Localidad: {localidad}")

    
main()
def menu():
    return '1-Registrar cliente\n2-Buscar cliente\n3-Salir\n'
def menu1():
    return '1-Eliminar cliente\n2-Reactivar cliente\n'
def registrar_cliente():
    nombre = input("Ingrese nombre y apellido del cliente: ")
    print("Seleccione un pais: ")
    for i, pais in enumerate(datos.paises,start=1):
        print(f"{i}. {pais.get_nombre}")
    indice_pais = int(input())
    pais_seleccionado = datos.paises[indice_pais - 1]
    
    print("Seleccione una provincia: ")
    for i, provincia in enumerate(pais_seleccionado.get_provincias(),start=1):
        print(f"{i}. {provincia.get_nombre}")
    indice_provincia = int(input())
    provincia_seleccionada = pais_seleccionado.get_provincia(indice_provincia - 1)
    
    print("Seleccione localidad: ")
    for i, localidad in enumerate(provincia_seleccionada.get_localidades(),start=1):
        print(f"{i}. {localidad.get_nombre}")
    indice_localidad = int(input())
    localidad_seleccionada = provincia_seleccionada.get_localidad(indice_localidad - 1)
    
    direccion = input("Ingrese su domicilio: ")
    nuevo_cliente = Cliente(nombre,direccion)
def eliminar_cliente():
    pass
def reactivar_cliente():
    pass
while True:
    opcion = int(input(menu()))
    if opcion == 1:
        registrar_cliente()
    elif opcion == 2:
        encontrado = False
        nro_buscar = int(input("Ingrese nro de cliente a buscar: "))
        for cliente in datos.clientes:
            if nro_buscar == cliente.get_nro_cliente():
                print("Cliente encontrado")
                encontrado = True
                print(cliente)
        if encontrado==True:
            opcion1 = int(input(menu1()))
            if opcion1 == 1:
                cliente.eliminar_cliente()
            elif opcion1 == 2:
                cliente.reactivar_cliente()
            else:
                print("Opcion incorrecta")
        else:
            print("Cliente inexistente")
    elif opcion == 3:
        print("Hasta luego")
        break
    else:
        print("Opcion invalida")

