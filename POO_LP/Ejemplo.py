# crear un sistema para gestion control de stock de productos 
# casos de productos 
# historias de usuario 
# producto ower
# baclog
# prototipos de mierda
#entidad o entitis (la base de datos sobre la q ue voy a trbajar)

productos=[
    {  
        "id":1,
        "nombre":"arroz",
        "descripcion":"costeño costal por 100 kg",
        "stock":5,
        "unidad": "costales",
        "precio":125,
        "moneda":"soles",
    }
]
#casos de uso
class Producto:
#atributos de instancia
    def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
        self.nombre=nombre,
        self.descripcion=descripcion,
        self.stock=stock,
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda
# creacion de metodos
    def mostrar_producto(self):
        mensaje=f"""
        tienes(len{productos}) productos
        los productos son:
        {productos}
        """
        return mensaje
    def registrar_producto(self):
        nuevo_id=len(producto)+1
        producto_nuevo={
            "id":nuevo_id,
            "nombre":self.nombre,
            "descripcion":self.descripcion,
            "stock":self.stock,
            "unidad":self.unidad,
            "precio":self.precio,
            "moneda":self.moneda
        }
        registro_producto=productos.append(producto_nuevo)
        return f"El siguiente producto se rergistro exitosamente {producto_nuevo}"
    def mostrar_producto(self,id):
        producto_buscar=producto[id,1]
        return producto_buscar

    def eliminar_producto(self,id):
        producto_eliminar=producto[id-1]
        return f"El siguiente producto fue eliminado {producto_eliminar}" 

    # def actualizar_producto (self,id,clave,valor):
    #     producto_actualizar=list(filter(lambda obj: obj[clave]==id, producto))

    def actualizar_producto (self,id,clave,valor):
        ol=valor
        producto_actualizar=list(filter(lambda obj:obj[clave]==id,productos))[0].update
        ({clave:valor})
        return "se actualizo"

#list funcion para crear lista 
# programacion orientada a python
# metodo funcional filter retorna una lista con el elemento 
# 
# 

prod=Producto("aceite","extra virgen",1,"botella x litro",12.50)
print(prod.registrar_producto())
print(prod.mostrar_producto())
print(prod.mostrar_producto(1))
print(prod.eliminar_producto(2))
print(prod.mostrar_producto())
# print(prod.actualizar_producto("2023-A","codigo","cualquier cosa"))
print(prod.actualizar_producto(125,"precio",130))
# casos de uso de estudiante




