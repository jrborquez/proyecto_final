#José Rojo
#Septiembre 25 de 2023
#App Menu de Hamburguesas Proyecto Final Python Avanzado

from flask import Flask, render_template
from baseDatos import *

app = Flask(__name__)



@app.route('/')
def introducePedido():
    encabezado = 'Bienvenido a Burger Bros'
    titulo = 'Burger Bros'
    return render_template('index.html', encabezado=encabezado, titulo=titulo)



@app.route('/infoPedido')
def imprimirInfo():
    return render_template('infoPedido.html')




