#tarea crear una lista con 10 objetos que contengan los datos de las tiendas comerciales
#ejemplo
# tiendas
## ```
# Tiendas=[
#     {
#         "nombre":"el pichilon",
#         "categoria":["bodega"],
#         "horario_atencion":(
#             "dia" : 7 am -12 pm,
#             "tarde": 2 pm - 8 pm
#         ),
#         "gerente":"nadine"

#     }
# ]
## ```
# observacion: las categorias sera: abarrotes farmacia, bodega, restaurante
# los gerentes solo seran los siguientes: Edwin,china,cristhian, nadine
# 1. crear un metodo que me filtre las tiendas que tiene cada gerente 
# 2. crear un metodo que nos muestre ls negocios que tienen mas de dos categorias 
# 3. crear un metodo que me muestre solo el nombre y ruc de las tiendas 


class Tienda_Comercial:


    def tienda_gerente(self, bd_negocios, nombre_gerente):
        respuesta = list(filter(lambda el: el["gerente"] == nombre_gerente, bd_negocios))
        return respuesta

    def tienda_mas_categorias(self, bd_negocios):
        negocios_mas_categorias = list(filter(lambda el: len(el["categoria"].split(", ")) > 2, bd_negocios))
        return negocios_mas_categorias

    def ruc_nombre(self, bd_negocios):
        nombre_ruc = [(el["nombre"], el["ruc"]) for el in bd_negocios]
        return nombre_ruc

    def mostrar_todo(self, bd_negocios):
        for el in bd_negocios:
            print("Nombre:", el["nombre"])
            print("Categoría:", el["categoria"])
            print("Gerente:", el["gerente"])
            print("RUC:", el["ruc"])
            print("----------------------")

# Crear una lista con 10 objetos de tiendas comerciales
negocios = [
    {"nombre": "Tienda 1", "categoria": "Abarrotes", "gerente": "Edwin", "ruc": "12345678901"},
    {"nombre": "Tienda 2", "categoria": "Farmacia", "gerente": "China", "ruc": "23456789012"},
    {"nombre": "Tienda 3", "categoria": "Bodega", "gerente": "Cristian", "ruc": "34567890123"},
    {"nombre": "Tienda 4", "categoria": "Restaurantes", "gerente": "Nadine", "ruc": "45678901234"},
    {"nombre": "Tienda 5", "categoria": "Abarrotes, Farmacia", "gerente": "Edwin", "ruc": "56789012345"},
    {"nombre": "Tienda 6", "categoria": "Bodega, Restaurantes", "gerente": "China", "ruc": "67890123456"},
    {"nombre": "Tienda 7", "categoria": "Farmacia, Bodega", "gerente": "Cristian", "ruc": "78901234567"},
    {"nombre": "Tienda 8", "categoria": "Abarrotes, Restaurantes", "gerente": "Nadine", "ruc": "89012345678"},
    {"nombre": "Tienda 9", "categoria": "Farmacia, Restaurantes", "gerente": "Edwin", "ruc": "90123456789"},
    {"nombre": "Tienda 10", "categoria": "Abarrotes, Bodega", "gerente": "China", "ruc": "01234567890"}
]

gerente = Tienda_Comercial()
print("Tiendas del gerente China:")
tiendas_china = gerente.tienda_gerente(negocios, "China")
for tienda in tiendas_china:
    print(tienda["nombre"])

print("\nNegocios con más de dos categorías:")
negocios_mas_categorias = gerente.tienda_mas_categorias(negocios)
for negocio in negocios_mas_categorias:
    print(negocio["nombre"])

print("\nNombre y RUC de las tiendas:")
nombre_ruc = gerente.ruc_nombre(negocios)
for tienda in nombre_ruc:
    print(f"Nombre: {tienda[0]}, RUC: {tienda[1]}")

print("\nMostrar todos los datos de las tiendas:")
gerente.mostrar_todo(negocios)
