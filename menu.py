import sqlite3
from baseDatos import BaseDatos
from autenticacionBd import Autenticacion

class Menu:
    """Es la clase que administra el Menú de Hamburguesas del Restaurante, la cual agrupa funciones de desplegar, agregar, editar y eliminar registros de nuestra tabla
    en nuestra base de datos.
    Todos los querys a la BD son validados, tanto para saber si hay datos que desplegar o por si existe un error en la conexión
    """
    baseDatos = None
    autenticacionBd = None
    
    def __init__(self):
        """Nuestro constructor de la Clase Menu
        """
        self.baseDatos = BaseDatos('burgers.db')
        self.autenticacionBd = Autenticacion()
        
        if self.baseDatos.verificarBaseDatosExiste():
            self.autenticacionBd.verificarAutenticacion()
        else:
            self.baseDatos.crearBaseDatos()
            

    def mostrarListaProductos(self):
        """Muestra el listado del producto mediante un query validado a la BD"""
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM menu")     
            productos = cursor.fetchall()
            if len(productos) > 0:
                print("Lista de productos disponibles: ")
                print("------------------------------------")
                for id, clave, nombre_producto,precio in productos:
                    print('id: {}, clave: {}, nombre del producto: {}, precio: {}'
                        .format(id, clave, nombre_producto, precio))
                print("------------------------------------")
            
            else:
                print("No hay productos que mostrar")
                print("------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los datos de la tabla productos", error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
        
    
    def agregarProducto(self):
        """Agregamos productos al menu mediante la conexión y queries a nuestra BD 
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            clave,nombre_producto,precio = self.ingresarDatosProducto()
            valores = (clave, nombre_producto, precio)
            sql = ''' INSERT INTO menu (clave, nombre_producto, precio)
                    VALUES(?,?,?) '''
            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")
            print("------------------------------------")
        except sqlite3.Error as e:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                    
    def modificarProducto(self):
        """Nos ayuda a modificar un Producto, trayendolo de la tabla Menu, BD Burgers, y dándole un UPDATE a los datos introducidos por el usuario
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            
            cursor.execute("SELECT * FROM menu")     
            productos = cursor.fetchall()
            if len(productos) > 0:
                
                print("Lista de productos para modificar:")
                self.mostrarListaProductos()
                print("----------------------------------")
                id_producto = self.ingresarID("Ingresa el id del producto a modificar \n")
                
                encontrar_producto = cursor.execute("SELECT * FROM menu WHERE id = ?", (id_producto,))    
                producto = encontrar_producto.fetchone()
                if producto :
                    clave,nombre_producto,precio = self.ingresarDatosProducto()
                    sql = ''' UPDATE menu SET clave = ?, nombre_producto = ?, precio = ? WHERE id = ? '''
                    datos_producto = (clave,nombre_producto,precio,id_producto)
                    cursor.execute(sql,datos_producto)
                    conexion.commit()
                    print("Registro modificado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            else:  
                print("No hay productos para modificar")
                print("------------------------------------")
            
        except sqlite3.Error as e:
            print('Error al intentar modificar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()


    def eliminarProducto(self):
        """Eliminamos un producto, mostrando la lista de la tabla menu, ejecutando una función del cursor, para luego elegir mediante el ID el producto a eliminar
        y dando la instrucción mediante un Query"""
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM menu")     
            productos = cursor.fetchall()
            if len(productos) > 0:
            
                print("Lista de productos para eliminar:")
                self.mostrarListaProductos()
                print("------------------------------------")
                id_producto = self.ingresarID("Ingresa el id del producto a eliminar \n")
                
                encontrar_producto = cursor.execute("SELECT * FROM menu WHERE id = ?", (id_producto,))     
                if len(encontrar_producto.fetchall()) == 1:
                    sql = ''' DELETE FROM menu WHERE id = ? '''
                    cursor.execute(sql,(id_producto,))
                    conexion.commit()
                    print("Registro eliminado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            
            else:  
                print("No hay productos para eliminar")
                print("------------------------------------")
                
        except sqlite3.Error as e:
            print('Error al intentar eliminar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    
    def ingresarID(self,mensaje):
        """ejecutamos esta función, para usar el número introducido, como instrucción en las funciones anteriores
        tomamos el mensaje como parámetro y retornamos una variable con el número que elegimos
        """
        id_producto = 0
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                id_producto = int(input( mensaje ))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar el id del producto: {}'.format(e))
                print('Intente de nuevo ingresar el id \n')
                datos_incorrectos = True
        return id_producto


    def ingresarDatosProducto(self):
        """Tal como en las otras Clases, pedimos la info al Usuario por medio de inputs, y nos retorna esta info en variables que usaremos en otras funciones de forma automática
        """
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                clave = input("Ingresa la clave del producto \n")
                nombre_producto = input("Ingresa el nombre del producto \n")
                precio = float(input("Ingresa el precio del producto \n"))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar un dato: {}'.format(e))
                print('Intente de nuevo ingresar los datos \n')
                datos_incorrectos = True
        return clave,nombre_producto,precio