#José Rojo
#Septiembre 25 de 2023
#App Menu de Hamburguesas Proyecto Final Python Avanzado

from flask import Flask, render_template
from baseDatos import *

app = Flask(__name__)



@app.route('/', methods=["GET","POST"])
def introducePedido():
    encabezado = 'Bienvenido a Burger Bros'
    titulo = 'Burger Bros'
    if request.method == 'GET':
        if request.form['id'] == post_id:
            ()
    post_id = request.form.get('id')
    
    return render_template('index.html', encabezado=encabezado, titulo=titulo)



@app.route('/infoPedido')
def imprimirInfo():
   @app.route('/', methods=["GET","POST"])
   def home():    
    if request.method == 'POST':
        if request.form['delete'] == post_id:
            (my sql login/cursor stuff....)
            sql = "DELETE FROM test_table WHERE post_id = ?"
            c.execute(sql, (post_id,))
            return redirect("/")

    

    return render_template('infoPedido.html')

