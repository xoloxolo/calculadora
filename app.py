# Importamos la libería Flask para crear nuestra aplicación web
from flask import Flask
# Importamos las funciones del programa
from .src.utils import area_of_circle, area_of_triangle, perimeter_of_triangle

"""
Creamos una instancia de la clase Flask, que representa nuestra aplicación web. 
El argumento __name__ indica el nombre del módulo actual.
"""
app = Flask(__name__)


# Este es el punto de entrada de nuestra aplicación web
if __name__ == '__main__':
    # Iniciamos la aplicación web
    app.run(debug=True)