import sqlite3
from baseDatos import BaseDatos
from autenticacionBd import Autenticacion
   
class Clientes:
    """En esta clase administramos el comportamiento de los Clientes, desde su listado en la BD, la conexión dentro de su tabla, así como su manipulación
     mediante funciones que agregan, enlistan, editan y eliminan registros en la tabla de Clientes en nuestra BD
     Todos los querys a la BD son validados, tanto para saber si hay datos que desplegar o por si existe un error en la conexión
    """
    baseDatos = None
    autenticacionBd = None
    
    def __init__(self):
        """En el constructor invocamos la BD con la que vamos a trabajar y validamos que exista o que no, para crearla o trabajar con ella
        """
        self.baseDatos = BaseDatos('burgers.db')
        self.autenticacionBd = Autenticacion()
        
        if self.baseDatos.verificarBaseDatosExiste():
            self.autenticacionBd.verificarAutenticacion()
        else:
            self.baseDatos.crearBaseDatos()
            

    def mostrarListaClientes(self):
        """Muestra la lista de clientes de nuestra tabla Clientes en la BD burgers, con un query, el cual es validado, para cualquier error en la consulta
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")     
            clientes = cursor.fetchall()
            if len(clientes) > 0:
                print("Lista de Clientes de BurgerBros: ")
                print("------------------------------------")
                for id, clave, nombre, direccion, correo, telefono in clientes:
                    print('id: {}, clave: {}, nombre: {}, direccion: {}, correo:{}, telefono: {}'
                        .format(id, clave, nombre, direccion, correo, telefono))
                print("------------------------------------")
            
            else:
                print("No hay clientes dados de alta")
                print("------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los datos de la tabla clientes", error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
        
    
    def agregarCliente(self):
        """Agrega un nuevo Cliente, pasando los valores introducidos en el input, gracias a la función ingresarDatosCliente, para insertarlo en nuestra tabla de clientes
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            clave, nombre, direccion, correo, telefono = self.ingresarDatosCliente()
            valores = (clave, nombre, direccion, correo, telefono)
            sql = ''' INSERT INTO clientes (clave, nombre, direccion, correo, telefono)
                    VALUES(?,?,?,?,?) '''
            cursor.execute(sql,valores)
            conexion.commit()
            print("Cliente guardado exitosamente")
            print("------------------------------------")
        except sqlite3.Error as e:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
                    
    def modificarCliente(self):
        """De igual manera modificar toma los datos mediante un input pedido de la función ingresarDatosCliente, para despues ejecutar mediante el cursor un query a la base de datos, con la instrucción UPDATE 
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            
            cursor.execute("SELECT * FROM clientes")     
            clientes = cursor.fetchall()
            if len(clientes) > 0:
                
                print("Lista de clientes para modificar:")
                self.mostrarListaClientes()
                print("----------------------------------")
                id_cliente = self.ingresarID("Ingresa el id del cliente a modificar \n")
                
                encontrar_cliente = cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))    
                cliente = encontrar_cliente.fetchone()
                if cliente :
                    clave, nombre, direccion, correo, telefono = self.ingresarDatosCliente()
                    sql = ''' UPDATE clientes SET clave = ?, nombre = ?, direccion = ?, correo = ?, telefono = ? WHERE id = ? '''
                    datos_producto = (clave, nombre, direccion, correo, telefono,id_cliente)
                    cursor.execute(sql,datos_producto)
                    conexion.commit()
                    print("Registro modificado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            else:  
                print("No hay clientes para modificar")
                print("------------------------------------")
            
        except sqlite3.Error as e:
            print('Error al intentar modificar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()


    def eliminarCliente(self):
        """Con la instrucción DELETE del query a la BD, Eliminamos al Cliente cuyo ID elegimos mediante un input
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")     
            clientes = cursor.fetchall()
            if len(clientes) > 0:
            
                print("Lista de productos para eliminar:")
                self.mostrarListaClientes()
                print("------------------------------------")
                id_cliente = self.ingresarID("Ingresa el id del cliente a eliminar \n")
                encontrar_cliente = cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))     
                if len(encontrar_cliente.fetchall()) == 1:
                    sql = ''' DELETE FROM clientes WHERE id = ? '''
                    cursor.execute(sql,(id_cliente,))
                    conexion.commit()
                    print("Registro eliminado correctamente")
                    print("------------------------------------")
                else:
                    print("No hay registro con ese id")
                    print("------------------------------------")
            
            else:  
                print("No hay clientes para eliminar")
                print("------------------------------------")
                
        except sqlite3.Error as e:
            print('Error al intentar eliminar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    
    def ingresarID(self,mensaje):
        """Esta función nos sirve para que el Usuario puede digitar y validar el ID que identifica nuestros registros a manipular
        """
        id_cliente = 0
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                id_cliente = int(input( mensaje ))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar el id del producto: {}'.format(e))
                print('Intente de nuevo ingresar el id \n')
                datos_incorrectos = True
        return id_cliente


    def ingresarDatosCliente(self):
        """Como en las otras clases, esta función nos ayuda a pasar los datos introducidos por el Usuario, además de validarlos
        returnandonos la información en variables que usamos dentro del proceso"""
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                clave = input("Ingresa la clave del cliente \n")
                nombre = input("Ingresa el nombre del cliente \n")
                direccion = input("Ingresa la dirección del cliente \n")
                correo = input("Ingresa el correo del cliente \n")
                telefono = input("Ingresa el teléfono del clinte \n")
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar un dato: {}'.format(e))
                print('Intente de nuevo ingresar los datos \n')
                datos_incorrectos = True
        return clave, nombre, direccion, correo, telefono