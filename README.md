# flask_roja

## Ejercicios de Flask Cinta Roja B12 Dev.F

1.- Activar su entorno virtual
```
source env/bin/activate   linux y mac
env\Scripts\activate      windows
```
2.- En el archivo requirements.txt se encuentran las librerias que deben tener instaladas para que el proyecto corra
```
pip freeze  # Con este comando pueden revisar que librerias tienen instaladas
```
3.- Si les faltan algunas librerias instalarlas directamente del archivo requirements.txt
```
pip install -r requirements.txt  # Instalar todas las librerias que están en el archivo
```
4.- Configurar su proyecto de Flask
```
export FLASK_APP=archivo.py   linux y mac  # deben de estar a la altura de su archivo.py que es su archivo principal
set FLASK_APP=archivo.py      windows

flask run
```
