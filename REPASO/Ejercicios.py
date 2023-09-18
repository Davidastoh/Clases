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

numero_premiado = 2468
condicion=True
while condicion:

    numero_ingresado = int(input("Ingresa el número: "))
    if numero_ingresado == numero_premiado:
        print("¡Felicidades! haz ganado el premio.")
        condicion=False
    else:
        print("Sigue intentando.")
