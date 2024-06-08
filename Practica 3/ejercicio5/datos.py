from cliente import Cliente
from pais import Pais
from provincia import Provincia
from localidad import Localidad
# Crear localidades
localidad1 = Localidad("Totoras", 1000)
localidad2 = Localidad("Rosario", 2000)
localidad3 = Localidad("Mar del Plata", 3000)

# Crear provincias y agregar localidades
provincia1 = Provincia("Santa Fe")
provincia1.add_localidad(localidad1)
provincia1.add_localidad(localidad2)

provincia2 = Provincia("Buenos Aires")
provincia2.add_localidad(localidad3)

# Crear país y agregar provincias
pais = Pais("Argentina")
pais.add_provincia(provincia1)
pais.add_provincia(provincia2)



# Crear localidades
localidad4 = Localidad("Localidad4", 1000)
localidad5 = Localidad("Localidad5", 2000)
localidad6 = Localidad("Localidad6", 3000)

# Crear provincias y agregar localidades
provincia3 = Provincia("Sao Paulo")
provincia3.add_localidad(localidad4)
provincia3.add_localidad(localidad5)

provincia4 = Provincia("Brasilia")
provincia4.add_localidad(localidad6)

# Crear país y agregar provincias
pais1 = Pais("Brasil")
pais1.add_provincia(provincia3)
pais1.add_provincia(provincia4)


# Lista de países
paises = [pais, pais1]

# Crear cliente
cliente1 = Cliente("Juan Perez", "Calle Falsa 123")
print(cliente1)

# Eliminar cliente
#cliente1.eliminar_cliente()
#print(cliente1)

cliente2 = Cliente("test lcien","stret 100")
clientes = [cliente1]