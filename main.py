#José Rojo
#Septiembre 25 de 2023
#App Menu de Hamburguesas Proyecto Final Python Avanzado

from pedido import Pedidos
from clientes import Clientes
from menu import Menu
 

class Aplicacion:
    """Clase Aplicación, con esta clase empezamos el programa y le damos vida a la app, creando mediante funciones los menus de navegación
    """
    
    def __init__(self):
        """Constructor donde definimos nuestro aplicativo mediante la función iniciarAplicacion()
        """
        self.iniciarAplicacion()
       
    
    def iniciarAplicacion(self):
        """Con esta función desplegamos el Menu Navegador Principal y damos la opción de elegir mediante el input a donde se desea navegar
        """
        print("------------------------------------")
        print("Bienvenido al sistema de Burger Bros")
        salir_programa = False
        while not salir_programa:
            print("Menú de Burger Bros")
            print(""" 
                1.- Pedidos
                2.- Clientes
                3.- Menu
                4.- Salir
                """)
            opcion = int(input("Indica una opción del menú "))
            if opcion == 1:
                self.iniciarPedidos()
            elif opcion == 2:
                self.iniciarClientes()
            elif opcion == 3:
                self.iniciarMenu()
            if opcion == 4:
                print("Salida del programa, hasta luego ")
                salir_programa = True
                
    def iniciarPedidos(self):
        """Inicia el Menú de navegación de Pedidos, mostrándonos las opciones para navegar, haciendo uso de funciones en otra clase de otro archivo
        """
        pedidos = Pedidos()
        salir_pedidos = False
        print("------------------------------------")
        while not salir_pedidos:
            print("Pedidos de Burger Bros")
            print(""" 
                1.- Lista de Pedidos
                2.- Agregar Pedido
                3.- Cancelar Pedido
                4.- Volver Menu Principal
                """)
            opcion = int(input("Indica una opción del menú Pedidos "))
            if opcion == 1:
                pedidos.mostrarListaPedidos()
            elif opcion == 2:
                pedidos.agregarPedido()
            elif opcion == 3:
                pedidos.cancelarPedido()
            if opcion == 4:
                print("Volver al inicio")
                salir_pedidos = True
               
    
    def iniciarClientes(self):
        """Iniciamos el Menú de Navegación de Clientes, el cual se mantendrá mientras el While permanezca verdadero de lo contrario regresará al Menú anterior"""
        clientes = Clientes()
        print("------------------------------------")
        salir_clientes = False
        while not salir_clientes:
            print("Clientes de Burger Bros")
            print(""" 
                1.- Lista de Clientes
                2.- Dar de alta a un Cliente
                3.- Editar un Cliente
                4.- Eliminar un Cliente
                5.- Volver Menu Principal
                """)
            opcion = int(input("Indica una opción del menú Clientes"))
            if opcion == 1:
                clientes.mostrarListaClientes()
            elif opcion == 2:
                clientes.agregarCliente()
            elif opcion == 3:
                clientes.modificarCliente()
            elif opcion == 4:
                clientes.eliminarCliente()
            if opcion == 5:
                print("Volver al inicio")
                salir_clientes = True
                
    def iniciarMenu(self):
        """Iniciamos el Menú de Navegación del Menú del Restaurante, con un while se mantiene vivo, al terminar, regresa al Menú anterior"""
        burgers = Menu()
        print("------------------------------------")
        salir_menu = False
        while not salir_menu:
            print("Menu de Hamburguesas de Burger Bros")
            print(""" 
                1.- Lista de Hamburguesas
                2.- Agregar Hamburguesa
                3.- Modificar Hamburguesa
                4.- Eliminar Hamburguesa
                5.- Volver Menu Principal
                """)
            opcion = int(input("Indica una opción del menú "))
            if opcion == 1:
                burgers.mostrarListaProductos()
            elif opcion == 2:
                burgers.agregarProducto()
            elif opcion == 3:
                burgers.modificarProducto()
            elif opcion == 4:
                burgers.eliminarProducto()
            if opcion == 5:
                print("Volver al inicio")
                salir_menu = True
    
                
sistema_burgers = Aplicacion()
