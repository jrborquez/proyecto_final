import sqlite3 
import os
from autenticacionBd import Autenticacion

class BaseDatos:
    """Clase para acceder a nuestra Base de datos, crearla y/o manipularla
    """
    def __init__(self, nombreBaseDatos):
        """Nuestro constructor, donde recibe un argumento, el nombre de nuestra base de datos.

        Args:
            nombreBaseDatos (string): Nombre de nuestra base de datos, el que le queramos dar.
        """
        self.nombreBaseDatos = nombreBaseDatos
        self.autenticacionBd = Autenticacion()
        

    def crearBaseDatos(self):
        """Crea nuestra base de datos, al igual que hace el llamado a las funciones para crear las tablas que lleva dentro
        """
        try:
            conn = sqlite3.connect(self.nombreBaseDatos)
            self.crearTablaPedidos()
            self.crearTablaClientes()
            self.crearTablaMenu() 
        except Exception as e:
            print('Error al crear la Base de datos: {}'.format(e))


    def verificarBaseDatosExiste(self):
        """Verifica si ya existe el archivo de la base de datos

        Returns:
            Boleano: solo verifica, lanza un verdadero o falso, para la siguiente etapa de otra función que la llama.
        """
        if os.path.isfile(self.nombreBaseDatos):
            return True
        else:
            return False

    def crearTablaPedidos(self):
        """crea la tabla de Pedidos
        """
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE pedidos
                (pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                producto TEXT NOT NULL,
                precio FLOAT NOT NULL
                );''')
        
        conexion.close()
            
            
    def crearTablaClientes(self):
        """crea nuestra tabla de clientes
        """
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
        """crea nuestra tabla de menú de productos
        """
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE menu
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            clave TEXT NOT NULL,
            nombre_producto TEXT NOT NULL,
            precio FLOAT NOT NULL
            );''')
        
        conexion.close()
    
        
    def abrirConexion(self):
        """abre la conexión con nuestra base de datos

        Returns:
            variable: la variable es la conexión a nuestra base de datos
        """
        try:
            conexion = sqlite3.connect(self.nombreBaseDatos) 
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))

