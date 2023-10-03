import sqlite3
from baseDatos import BaseDatos
from autenticacionBd import Autenticacion

class Pedidos:
    """Clase de Pedidos, donde podemos administrar nuestros pedidos, Ver la lista de pedidos, Agregar y Cancelar Pedidos
    Todos los querys a la BD son validados, tanto para saber si hay datos que desplegar o por si existe un error en la conexión
    """
    baseDatos = None
    autenticacionBd = None
    
    def __init__(self):
        """Definimos nuestro constructor de la clase Pedidos invocando los métodos para conectarnos a nuestra BD
        """
        self.baseDatos = BaseDatos('burgers.db')
        self.autenticacionBd = Autenticacion()
        
        if self.baseDatos.verificarBaseDatosExiste():
            self.autenticacionBd.verificarAutenticacion()
        else:
            self.baseDatos.crearBaseDatos()
            
   
    def mostrarListaPedidos(self):
        """Mandamos llamar todos los registros de la BD Tabla Pedidos para visualizar cuales pedidos tenemos
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM pedidos")     
            pedidos = cursor.fetchall()
            if len(pedidos) > 0:
                print("Lista de pedidos disponibles: ")
                print("------------------------------------")
                for pedido, cliente, producto, precio in pedidos:
                    print('pedido: {}, cliente: {}, producto: {}, precio: {}'
                        .format(pedido, cliente, producto, precio))
                print("------------------------------------")
            
            else:
                print("No hay pedidos que mostrar")
                print("------------------------------------")
        except sqlite3.Error as error:
            print("Error al mostrar los datos de la tabla pedidos", error)
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    

    def agregarPedido(self):
        """Invocamos la función ingresarDatosPedido, para por medio de input insertar la info a los campos de la BD
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cliente, producto, precio = self.ingresarDatosPedido()
            valores = (cliente, producto, precio)  
            sql = ''' INSERT INTO pedidos (cliente, producto, precio)
                    VALUES(?,?,?) '''
            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")
            self.imprimirTicket()
            print("------------------------------------")
        except sqlite3.Error as e:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def imprimirTicket(self):
        """Esta función genera un ticket en automático al generar un pedido, al traer los valores de la BD y acomodarlos en un archivo TXT al igual que imprimirlo en la consola.
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            
            pedido = cursor.execute("SELECT pedido FROM pedidos ORDER BY pedido DESC LIMIT 1")
            pedido = cursor.fetchone()
            cliente = cursor.execute("SELECT cliente FROM pedidos ORDER BY pedido DESC LIMIT 1")
            cliente = cursor.fetchone()
            producto = cursor.execute("SELECT producto FROM pedidos ORDER BY pedido DESC LIMIT 1")
            producto = cursor.fetchone()
            precio = cursor.execute("SELECT precio FROM pedidos ORDER BY pedido DESC LIMIT 1")
            precio = cursor.fetchone()
            
            datos = f"Burger Bros\n =======================\n Ticket de Venta\n Pedido No. {pedido}\n Cliente: {cliente}\n=======================\n {producto}\n  {precio}"
            print(datos)
            ticket = open(f'./tickets/ticketNo{pedido}.txt', 'w')
            ticket.write(datos)
           
                    
                
        except sqlite3.Error as e:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()   
                    
    def cancelarPedido(self):
        """Cancela el Pedido, al darle el número de Pedido lo elimina de la BD
        """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM pedidos")     
            pedidos = cursor.fetchall()
            if len(pedidos) > 0:
                print("Lista de Pedidos para cancelar:")
                self.mostrarListaPedidos()
                print("------------------------------------")
                id_pedido = self.ingresarID("Ingresa el Número del pedido a cancelar \n")
                encontrar_pedido = cursor.execute("SELECT * FROM pedidos WHERE pedido = ?", (id_pedido,))     
                if len(encontrar_pedido.fetchall()) == 1:
                    sql = ''' DELETE FROM pedidos WHERE pedido = ? '''
                    cursor.execute(sql,(id_pedido,))
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
        """Validamos el número que nos manda como argumento al ejecutar la función

        Args:
            mensaje (int): Es el número que pedimos como input, en la función modificar o eliminar/cancelar

        Returns:
            Variable int: se regresa como variable de número int
        """
        id_pedido = 0
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                id_pedido = int(input( mensaje ))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar el número del pedido: {}'.format(e))
                print('Intente de nuevo ingresar el id \n')
                datos_incorrectos = True
        return id_pedido
       

    
    def ingresarDatosPedido(self):
        """Le pedimos que ingrese a manera de input los datos del pedido

        Returns:
            cliente,producto,precio: nos regresa los campos de cliente, producto y precio como variables
        """
        datos_incorrectos = True
        while datos_incorrectos:
            try:
                cliente = input("Ingresa el nombre del Cliente \n")
                producto = input("Ingresa la Hamburguesa que deseas \n")
                precio = float(input("Ingresa el precio del producto \n"))
                datos_incorrectos = False
            except Exception as e:
                print('Error al capturar un dato: {}'.format(e))
                print('Intente de nuevo ingresar los datos \n')
                datos_incorrectos = True
        return cliente, producto, precio