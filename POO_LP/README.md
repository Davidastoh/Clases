# Programación Orientada a objetos(POO)
## En ingles es Object Orient Programing(OOP)
Es un paradigma de programacion
> **Paradigma** - es un modelo, patron o ejemplo que se debe seguir.
POO es un modelo de como programar
**Objeto** - El objetivo es organizar el codigo de manera que se asemeje a como pensamos en la vida real.

Se basa en objetos
y en la POO un objeto es toda entidad que se puede describir atraves de **atributos** y **funciones** que puede realizar la entidad.

### Ejemplo

- celulares
```python
class Celular:
```
- atributos tipo clase (atributo general)
- son iguales para todos, que se creen

```python
    familia="Smart Phone"
```
- atributos de instancia 
- son atributos propios del objeto
- creamos una funcion inicializadora
```python
    def __init__(self,marca,modelo,imei,nroCelular)
        self.marca=marca
        self.modelo=modelo
        self.imei=imei
        self.nroCelular=nroCelular
```
- funcionalidades:
```python
    def llamar(self,destino):
        return f"llamando a (destino)"
```   
- objeto celular Max:
```python
llamandoMax=Celular("poco","X5","946723647","976364747")  
```
- instanciando mi clasecreado al objeto celular
- objeto celular
```python
print(llamandoMax.marca)
print(llamandoMax.familia)
print(llamandoMax.llamar("Adan"))

```
- objeto celular David:
```python
llamandoDan=Celular("Alcatel","basico","974636627","963476765")
print(llamandoDan.marca)
print(llamandoDan.familia)
print(llamandoDan.llamar("Dan"))

```