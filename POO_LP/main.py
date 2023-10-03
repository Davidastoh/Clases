# El nombre siempre debera ser en singular y con la primera letra mayusculas 
# class perro:
#     nombre="boby"
#     edad="2 meses"
#     color="cheqche"
#     raza="chusterrier"

#     def ladrar():
#         return "guau guau mascota"
#     def corre(self,pasos):
#         return "Corristes {pasos}, pasos"
    
# respuesta=perro()
# print(respuesta.nombre)
# print(respuesta.ladrar())
# print(respuesta.corre(10))

# Haciendo uso de la POO crear un objeto para la entidad celular.
# class Celular:
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color

#     def llamar(self, numero):
#         print(f"Llamando al número {numero} desde un celular {self.marca} {self.modelo}")

#     def enviar_mensaje(self, numero, mensaje):
#         print(f"Enviando mensaje '{mensaje}' al número {numero} desde un celular {self.marca} {self.modelo}")

# mi_celular = Celular("Redmi", "Miui 10", "Negro")
# print(f"Marca: {mi_celular.marca}")
# print(f"Modelo: {mi_celular.modelo}")
# print(f"Color: {mi_celular.color}")
# mi_celular.llamar("932429423")
# mi_celular.enviar_mensaje("910323323", "¡Hola! ¿Cómo estás?")
# Haciendo uso de la POO crear un objeto para la entidad vehiculo.
# class Vehiculo:
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color

#     def acelerar(self):
#         print(f"El vehículo {self.marca} {self.modelo} está acelerando")

#     def frenar(self):
#         print(f"El vehículo {self.marca} {self.modelo} está frenando")
# mi_vehiculo = Vehiculo("Toyota", "Corolla", "Rojo")

# # Acceder a los atributos del objeto
# print(f"Marca: {mi_vehiculo.marca}")
# print(f"Modelo: {mi_vehiculo.modelo}")
# print(f"Color: {mi_vehiculo.color}")
# mi_vehiculo.acelerar()
# mi_vehiculo.frenar()
# Haciendo uso de la POO crear un objeto para la entidad avion.
class Avion:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def despegar(self):
        print(f"El avión de marca {self.marca}, modelo {self.modelo} y color {self.color} está despegando.")

    def aterrizar(self):
        print(f"El avión de marca {self.marca}, modelo {self.modelo} y color {self.color} está aterrizando.")

# Crear una instancia de Avion
avion1 = Avion("Boeing", "737", "blanco")

# Acceder a los atributos de la instancia
print(f"Marca del avión: {avion1.marca}")
print(f"Modelo del avión: {avion1.modelo}")
print(f"Color del avión: {avion1.color}")

# Llamar a los métodos de la instancia
avion1.despegar()
avion1.aterrizar()

# Haciendo uso de la POO crear un objeto para un heroe de dota2.
class Hero:
    def __init__(self, arma, velocidad, habilidad):
        self.arma = arma
        self.velocidad = velocidad
        self.habilidad = habilidad

    def atacar(self):
        print(f"El héroe ataca con {self.arma}.")

    def moverse(self):
        print(f"El héroe se mueve a una velocidad de {self.velocidad}.")

    def usar_habilidad(self):
        print(f"El héroe utiliza la habilidad: {self.habilidad}.")

# Crear una instancia de Hero
heroe1 = Hero("espada", "rápida", "invisibilidad")

# Acceder a los atributos de la instancia
print(f"Arma del héroe: {heroe1.arma}")
print(f"Velocidad del héroe: {heroe1.velocidad}")
print(f"Habilidad del héroe: {heroe1.habilidad}")

# Llamar a los métodos de la instancia
heroe1.atacar()
heroe1.moverse()
heroe1.usar_habilidad()

## ejemplo dos
class HeroeDota2:
    def __init__(self, nombre, atributo_principal, rol):
        self.nombre = nombre
        self.atributo_principal = atributo_principal
        self.rol = rol

    def atacar(self):
        print(f"El héroe {self.nombre} está atacando.")

    def usar_habilidad(self):
        print(f"El héroe {self.nombre} está usando una habilidad.")

# # Crear una instancia de HeroeDota2
heroe = HeroeDota2("Invoker", "Inteligencia", "Lanzador de hechizos")

# Acceder a los atributos de la instancia
print(f"Nombre del héroe: {heroe.nombre}")
print(f"Atributo principal del héroe: {heroe.atributo_principal}")
print(f"Rol del héroe: {heroe.rol}")

# Llamar a los métodos de la instancia
heroe.atacar()
heroe.usar_habilidad()
# haciendo uso de la POO crear un objeto para una PC
class PC:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def encender(self):
        print("La PC se está encendiendo.")

    def apagar(self):
        print("La PC se está apagando.")

# Crear una instancia de PC
pc1 = PC("HP", "Pavilion", "negro")

# Acceder a los atributos de la instancia
print(f"Marca de la PC: {pc1.marca}")
print(f"Modelo de la PC: {pc1.modelo}")
print(f"Color de la PC: {pc1.color}")

# Llamar a los métodos de la instancia
pc1.encender()
pc1.apagar()

# haciendo uso de la POO crear un objeto para una impresora
class Impresora:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def imprimir_documento(self, documento):
        print(f"Imprimiendo {documento} en la impresora {self.marca} {self.modelo}.")

    def escanear_documento(self):
        print(f"Escaneando un documento en la impresora {self.marca} {self.modelo}.")

# Crear una instancia de Impresora
impresora1 = Impresora("Epson", "L3150", "Negro")

# Acceder a los atributos de la instancia
print(f"Marca de la impresora: {impresora1.marca}")
print(f"Modelo de la impresora: {impresora1.modelo}")
print(f"Color de la impresora: {impresora1.color}")

# Llamar a los métodos de la instancia
impresora1.imprimir_documento("Informe.pdf")
impresora1.escanear_documento()

# haciendo uso de la POO crear un objeto para emitir una factura

class Factura:
    def __init__(self, numero_factura, nombre_cliente, monto_total):
        self.numero_factura = numero_factura
        self.nombre_cliente = nombre_cliente
        self.monto_total = monto_total

    def generar_factura(self):
        mensaje=f"""
            "Numero de Factura" : {self.numero_factura},
            "Nombre del Cliente" : {self.nombre_cliente},
            "Monto Total": s/.{self.monto_total}
        """
        return mensaje

# Crear una instancia de Factura
factura1 = Factura("FAC-001", "Max", 1000)

# Acceder a los atributos de la instancia
print(f"Número de Factura: {factura1.numero_factura}")
print(f"Nombre del Cliente: {factura1.nombre_cliente}")
print(f"Monto Total: s/.{factura1.monto_total}")

# Llamar al método para generar la factura
factura1.generar_factura()
