import sqlite3 
import os
from autenticacionBd import Autenticacion

class BaseDatos:
    
    def __init__(self, nombreBaseDatos):
        self.nombreBaseDatos = nombreBaseDatos
        self.autenticacionBd = Autenticacion()
        

    def crearBaseDatos(self):
        try:
            conn = sqlite3.connect(self.nombreBaseDatos)
            self.crearTablaPedidos()
            self.crearTablaClientes()
            self.crearTablaMenu() 
        except Exception as e:
            print('Error al crear la Base de datos: {}'.format(e))


    def verificarBaseDatosExiste(self):
        if os.path.isfile(self.nombreBaseDatos):
            return True
        else:
            return False

    def crearTablaPedidos(self):
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE pedidos
                (pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                producto TEXT NOT NULL,
                precio FLOAT NOT NULL
                );''')
        
        conexion.close()
            
            
    def crearTablaClientes(self):
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE clientes
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            clave TEXT NOT NULL,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            correo TEXT NOT NULL,
            telefono TEXT NOT NULL
            );''')
        
        conexion.close()
        
            
    def crearTablaMenu(self):
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE menu
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            clave TEXT NOT NULL,
            nombre_producto TEXT NOT NULL,
            precio FLOAT NOT NULL
            );''')
        
        conexion.close()
    
        
    def abrirConexion(self):
        try:
            conexion = sqlite3.connect(self.nombreBaseDatos) 
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))

