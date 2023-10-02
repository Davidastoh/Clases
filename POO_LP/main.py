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
class Celular:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def llamar(self, numero):
        print(f"Llamando al número {numero} desde un celular {self.marca} {self.modelo}")

    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje '{mensaje}' al número {numero} desde un celular {self.marca} {self.modelo}")

mi_celular = Celular("Redmi", "Miui 10", "Negro")
print(f"Marca: {mi_celular.marca}")
print(f"Modelo: {mi_celular.modelo}")
print(f"Color: {mi_celular.color}")
mi_celular.llamar("932429423")
mi_celular.enviar_mensaje("910323323", "¡Hola! ¿Cómo estás?")
# Haciendo uso de la POO crear un objeto para la entidad vehiculo.
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El vehículo {self.marca} {self.modelo} está acelerando")

    def frenar(self):
        print(f"El vehículo {self.marca} {self.modelo} está frenando")
mi_vehiculo = Vehiculo("Toyota", "Corolla", "Rojo")

# Acceder a los atributos del objeto
print(f"Marca: {mi_vehiculo.marca}")
print(f"Modelo: {mi_vehiculo.modelo}")
print(f"Color: {mi_vehiculo.color}")
mi_vehiculo.acelerar()
mi_vehiculo.frenar()
# Haciendo uso de la POO crear un objeto para la entidad avion.
# Haciendo uso de la POO crear un objeto para un heroe de dota2.

## TKINTER - Libreria de python para la creacion de interfaces graficas.