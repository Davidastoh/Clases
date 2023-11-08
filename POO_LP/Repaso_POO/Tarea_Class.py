# // vehiculo 
# // omnibus y sua tatributos modelo color ruedas
# // y su funcion recoger pasajero
# // auto modelo sus tatributos modelo color ruedas
# // y su funcion  arrancar avanzar y retroceder

class Vehiculo:
    def __init__(self, color, modelo):
        self.color = color
        self.modelo = modelo

    def acelerar(self):
        print("El vehículo está acelerando.")

    def frenar(self):
        print("El vehículo está frenando.")

class Autobus(Vehiculo):
    def __init__(self, color, modelo):
        super().__init__(color, modelo)

    def abrir_puertas(self):
        print("Las puertas del autobús se están abriendo.")

    def cerrar_puertas(self):
        print("Las puertas del autobús se están cerrando.")

class Auto(Vehiculo):
    def __init__(self, color, modelo):
        super().__init__(color, modelo)

    def hacer_pito(self):
        print("El auto está haciendo pito.")

    def estacionar(self):
        print("El auto se está estacionando.")

# Ejemplo de uso:
autobus1 = Autobus("Rojo", "Mercedes-Benz")
auto1 = Auto("Azul", "Toyota")

print(autobus1.color, autobus1.modelo)  # Salida: Rojo Mercedes-Benz
print(auto1.color, auto1.modelo)  # Salida: Azul Toyota

autobus1.abrir_puertas()  # Salida: Las puertas del autobús se están abriendo.
auto1.acelerar()  # Salida: El vehículo está acelerando.