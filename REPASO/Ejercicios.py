## crea un programa que te pidala edad de una persona si la edad es mayor o 
# igual a 18 que me muetsre un mesaje "eres mayor de edad caso contrario 
# que nos muestre un mensaje "eres menor de edad" ...

# Edad = int(input("Ingresa tu edad: "))
# if Edad >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("Eres menor de edad.")

## una tienda dese hcer un descuento del 20%, crea un programa que determine
# si el cliente zse hace acreedor del descuentro teniendo en cuenta
# lo siguientre si elo clienete realiza una compra de 1000 soles mostrar
# un mensaje que diga "ganaste el descuento del 20%" ahora pagaras, 
# <mostrar el total de la compra menos el descuento> en caso que 
# la compra no supere los 1000 soles, entonces mostrar que diga 
# "no aplicas el descuento" y mostrar el monto de la compra.

# Compra = float(input("Ingrese el monto de la compra: "))

# if Compra >= 1000:
#     descuento = Compra * 0.2
#     total = Compra - descuento
#     print("¡Ganaste el descuento del 20%! Ahora pagarás:", total, "soles.")
# else:
#     print("No aplicas el descuento. El monto de la compra es de:", Compra, "soles.")

# crea un programa que me pida 5 veces un nombre y por cada vez
# que lo pida muestre la cantidad de veces que ingreso el nombre 

# for n in range (1,6):
#     nombre=input("ingrese un nombre:" )
#     print(f"ingresate {n} veces el nombre")
    
#  crea un programa que pida un numero y lo evalue con el numero premiado 
#  si el numero ingresado es el premiado, el programa finaliza si el numero
#  ingresado es el incorrecto el programa seguira pidiendo el numero premiado

# numero_premiado = 2468

# while True:
#     numero_ingresado = int(input("Ingresa el número: "))
#     if numero_ingresado == numero_premiado:
#         print("¡Felicidades! haz ganado el premio.")
#         break
#     else:
#         print("Sigue intentando.")

# numero_premiado = 2468
# condicion=True
# while condicion:

#     numero_ingresado = int(input("Ingresa el número: "))
#     if numero_ingresado == numero_premiado:
#         print("¡Felicidades! haz ganado el premio.")
#         condicion=False
#     else:
#         print("Sigue intentando.")
        
# crear una funcion por cada operador aritmetico que reciva 
# dos parametros y retorne el resultado de la operacion. 
#  Crear una funcion que nos permita imprimir el resultado.

def mi_print(texto):
    print(texto)

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    return x / y

mi_print(suma(4,5))
mi_print(resta(4,5))
mi_print(multiplicacion(4,5))
mi_print(division(4,5))

# 6
# Escribe una funcion de Python que reciba 
# un numero entero positivo y devueva su factorial. 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
numero = 5
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)
# 7
# Escribe una funcion de Pythonque reciba como parametro
# una lista de numeros y retorne una nueva lista 
# con el cuadrado de cada numero de la lista ingresada.
def calcular_cuadrados(lista):
    cuadrados = []
    for numero in lista:
        cuadrado = numero ** 2
        cuadrados.append(cuadrado)
    return cuadrados

numeros = [1, 2, 3, 4, 5]
resultado = calcular_cuadrados(numeros)
print("La lista de cuadrados es:", resultado)

# escribe un programa de python que reciba una cadena caracteres
# y devuelva un objeto con cada palabra que contiene y su frecuencia

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

cadena = input("Ingresa una cadena de caracteres: ")
resultado = contar_palabras(cadena)
print(resultado)