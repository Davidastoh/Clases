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
    
    def eliminar_tienda(self, bd_negocios, nombre_tienda):
        bd_negocios = list(filter(lambda el: el["nombre"] != nombre_tienda, bd_negocios))
        return bd_negocios
    
    def actualizar_tienda(self, bd_negocios, nombre_tienda, nueva_categoria, nuevo_gerente, nuevo_ruc):
        for el in bd_negocios:
            if el["nombre"] == nombre_tienda:
                el["categoria"] = nueva_categoria
                el["gerente"] = nuevo_gerente
                el["ruc"] = nuevo_ruc
        return bd_negocios
    
    def crear_producto(self, bd_negocios, nombre_tienda, nuevo_producto):
        for el in bd_negocios:
            if el["nombre"] == nombre_tienda:
                if "productos" not in el:
                    el["productos"] = []
                el["productos"].append(nuevo_producto)
        return bd_negocios
    
    def actualizar_horario(self, bd_negocios, nombre_tienda, nuevo_horario):
        for el in bd_negocios:
            if el["nombre"] == nombre_tienda:
                el["horario"] = nuevo_horario
        return bd_negocios
        
# "horario_atencion":("Mañana": "8.00 am - 12.00", "Tarde: "1.00 pm - 6:00 pm "

# Crear una lista con 10 objetos de tiendas comerciales
negocios = [
    {
        "nombre": "Tienda 1",
        "categoria": "Abarrotes",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00,
        #     "Tarde ": 1:00 pm - 6:00 pm
        #     ),
        "gerente": "Edwin",
        "ruc": "12345678901"
    },
    {
        "nombre": "Tienda 2", 
        "categoria": "Farmacia",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00, 
        #     "Tarde ": 1:00 pm - 6:00 pm
        #     ),
        "gerente": "China",
        "ruc": "23456789012"
    },
    {
        "nombre": "Tienda 3", 
        "categoria": "Bodega",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00, 
        #     "Tarde ": 1:00 pm - 6:00 pm
        #     ),
        "gerente": "Cristian", 
        "ruc": "34567890123"
    },
    {
        "nombre": "Tienda 4", 
        "categoria": "Restaurantes",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00, 
        #     "Tarde ": 1:00 pm - 6:00 pm
        #     ), 
        "gerente": "Nadine", 
        "ruc": "45678901234"
    },
    {
        "nombre": "Tienda 5", 
        "categoria": "Abarrotes, Farmacia",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00, 
        #     "Tarde ": 1:00 pm - 6:00 pm
        #     ), 
        "gerente": "Edwin", 
        "ruc": "56789012345"
    },
    {
        "nombre": "Tienda 6",
        "categoria": "Bodega, Restaurantes",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00, 
        #     "Tarde ": 1:00 pm - 6:00 p
        #     ), 
        "gerente": "China", 
        "ruc": "67890123456"
    },
    {
        "nombre": "Tienda 7", 
        "categoria": "Farmacia, Bodega",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00, 
        #     "Tarde ": 1:00 pm - 6:00 pm
        #     ), 
        "gerente": "Cristian", 
        "ruc": "78901234567"
    },
    {
        "nombre": "Tienda 8", 
        "categoria": "Abarrotes, Restaurantes",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00, 
        #     "Tarde ": 1:00 pm - 6:00 pm
        #     ), 
        "gerente": "Nadine", 
        "ruc": "89012345678"
    },
    {
        "nombre": "Tienda 9", 
        "categoria": "Farmacia, Restaurantes",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00, 
        #     "Tarde ": 1:00 pm - 6:00 pm
        #     ), 
        "gerente": "Edwin", 
        "ruc": "90123456789"
    },
    {
        "nombre": "Tienda 10", 
        "categoria": "Abarrotes, Bodega",
        # "horario_atencion":(
        #     "Mañana": 8:00 am - 12.00, 
        #     "Tarde ": 1:00 pm - 6:00 pm
        #     ), 
        "gerente": "China", 
        "ruc": "01234567890"
    }
]

gerente = Tienda_Comercial()

# Crear un nuevo producto en una tienda específica
negocios = gerente.crear_producto(negocios, "Tienda 1", "Nuevo producto 1")
negocios = gerente.crear_producto(negocios, "Tienda 1", "Nuevo producto 2")

# Actualizar una tienda
negocios = gerente.actualizar_tienda(negocios, "Tienda 2", "Nueva categoría", "Nuevo gerente", "09876543210")

# Actualizar el horario de atención de una tienda
negocios = gerente.actualizar_horario(negocios, "Tienda 3", "8:00 AM - 6:00 PM")

# Mostrar todos los datos actualizados de las tiendas
gerente.mostrar_todo(negocios)