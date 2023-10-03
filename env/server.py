#José Rojo
#Septiembre 25 de 2023
#App Menu de Hamburguesas Proyecto Final Python Avanzado

from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def paginaPrincipal():
    return render_template('index.html')
    """Con esta función con decorador, empezamos nuestra App, renderiza un template de html que será nuestra página de inicio
    
    !!!!!! En este espacio Documentaremos el app de arriba por los errores que genera, es con lo que inicia nuestra app en Flask
    
    !!!!!! Este DocString está en esta posición, por los errores que marca al estar debajo de la función, o entre el decorador y la función.

    Returns:
        html: Renderiza cualquier página que será nuestra página de inicio 
    """


@app.route('/info',methods=['POST'])
def imprimirInfo():
    
    """esta función nos renderiza nuestra página info.html, pero aún más importante, es donde jalamos la variable id_pedido, para buscarla
    en nuestra base de datos, nos arroje el resultado de su búsqueda y nos ayude a renderizar una tabla con el resultado.
    
    El print de la excepción debió ser cambiado por una variable que arroje el resultado de haber la excepción, pero el Flask, nos arroja un
    error en consola, ya que no obtiene un valor, sino hasta que la excepción se activa.  Para efectos funcionales, así se queda.

    Returns:
        _type_: _description_
    """
    
    id_pedido = request.form['id_pedido']
    
    try:
        con = sql.connect('/Users/JR/Documents/GitHub/Python/proyecto_final/burgers.db')
        con.row_factory = sql.Row
    
        cur = con.cursor()
        cur.execute("SELECT * FROM pedidos WHERE pedido = ?", (id_pedido))
    
        rows = cur.fetchall();
    
    
    except Exception as e:
        print ('Error al conectar a la Base de datos: {}'.format(e))
    
    finally:
        if con:
            cur.close()
            con.close()
            

    
    return render_template("info.html", rows = rows)
    
    
    
                

