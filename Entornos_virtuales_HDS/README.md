# ENTORNOS VIRTUALES
## PYENV:
Es una herramienta que nos permite instalar diferentes versiones de Python y cambiar entre ellas según los requerimientos del proyecto con el cual necesitamos trabajar.
## PIPENV: 
Es un creador de entornos virtuales desfasado que ya no se utiliza actualmente.
## PIP:
Es un comando que permite instalar paquetes de python para nuestroas proyectos.
### para crear un entorno virtual.
1. Nos ubicamos en la carpeta que deseamos crear el entorno virtual. 
   ```bash
   cd <ruta del archivo>
   cd Entornos_Virtuales/Entorno_uno
   ```
2. Creamos el entorno virtual con el siguiente comando 
   ```bash
   python -m venv <nombre de nuestro entorno virtual>
   python -m venv mi_entorno
   ```
3. Para activar el entorno virtual con el gitbash como teminal predeterminada corremos el siguiente comando solo para windows
   ```bash
   sourse venv/Script/activate
   ```
### Observacion:
Para poder ejecutarlo en powershell como terminar predeterminado ejecutar el siguiente comando.
```powershell
venv\Scripts\Activate.psl
```
## Para instalar paquetes en nuestro entorno virtual
1. primero verificamos que no tengamos el paquete instalado y listamos con el siguiente comando.
#### Debemos tener activado nuestro entorno virtual primero.
```bash
pip list
```
2. Luego instalaremos con el siguiente comando.
```bash
pip install <nombre del paquete>```