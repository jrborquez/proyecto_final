class Autenticacion:
    """Esta es nuestra clase de Autenticación, donde se encuentra nuestra función, que verifica que el
    usuario y contraseña sean correctas, de ser así nos da acceso, de no ser así, nos arroja un Error
    """
    def verificarAutenticacion(self):
        """Función de Autenticación, que verifica que las variables de entrada de Usuario y Contraseña,
        sean correctas.
        """
        is_login = False
        while not is_login :
            usuario = input("Ingresar usuario: ")
            password = input("Ingresar contraseña: ")
            if usuario != 'admin' or password != '123':
                print("Error de login")
            else:
                is_login = True
                
    def verificarAutenticacionFlask(self, a, b):
        """esta función es para verificar la autenticidad en Flask"""
        is_login = False
        while not is_login :
            usuario = 'admin'
            password = '123'
            if usuario != a or password != b:
                print("Error de login")
            else:
                is_login = True