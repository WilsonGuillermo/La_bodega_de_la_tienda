""" Modulo Cocina """
""" Version 4, proyecto ANYEA """
""" WgMg Python ChatPT """
""" Agregando los ingredientes """
""" Agregamos las tablas de referencia """
""" Verificamos si la requete se realizo correctamente """
""" Modificacion de la tabla de ingredientes -> modificacion interrogaciones """
""" Pasamos a nombre unico del fichero """

### Session de imports
import mysql.connector as base

class mi_base(object):
    # Conectarse a la BDD
    def __init__(self):
        
        self.conexion = base.connect(
            host = "localhost",
            user = "majo",
            password = "WilsonMemo_1964",
            database = "boutique"
        )

        # Crear un cursor para ejecutar consultas "
        self.cursor = self.conexion.cursor()

    # Ejecutar insercion
    #def insercion(self):
    #    consulta = "insert into ingredientes (nombre, cantidad, fecha_vencimiento, tipo) values ('Arroz', '5', '2026-04-14', 'cereales');"
    #    self.cursor.execute(consulta)
    #    validacion="commit;"
    #    self.cursor.execute(validacion)

    # Ejecutar insercion: Agregar un producto
    def agregar(self, producto):
        """ Agregando ingrediente """
        agregando = ("insert into ingredientes (nombre, cantidad, fecha_vencimiento) "
        "VALUES ('%s', %s, '2027-12-12')"
        )
        
        data = producto

        requete=(agregando%data)
        print("el producto recibido para agregar es: ", data)
        print("la requete es: ", requete)

        self.ejecutar_requete(requete)

    # Ejecutar consulta: recuperar la lista de productos
    def consultacion(self):
        consulta = "select * from ingredientes"

        self.ejecutar_requete(consulta)

        # Obtener los resultados
        resultados = self.cursor.fetchall() # a voir!!!
        for fila in resultados:
            print(fila)

    def consultacion_generique(self, interrogation):
        consulta = "select * from ingredientes"

        self.ejecutar_requete(interrogation)

        # Obtener los resultados
        resultados = self.cursor.fetchall() # a voir!!!

        return resultados

    # Ejecutar consulta simple
    def consultacion_bis(self, producto):
        consulta = "select nombre from ingredientes where nombre = '%s'"
        print("la consultacion es :", consulta%producto)
        self.cursor.execute(consulta%producto)

        resultado = self.cursor.fetchone()
        print("lo q encontro es: ",resultado)
        if resultado is None:
            print("el producto: ",producto," no esta en la tabla ingredientes, lo agregaremos")
            return False
        else:
            print("el producto: ",producto," si esta en la tabla ingredientes, lo pondremos al dia")
            return True
    
    # Ejecutar consulta simple
    def consultacion_usuario(self, producto):
        print("la consultacion es :", producto)
        self.ejecutar_requete(producto)
        #self.cursor.execute(producto)

        resultado = self.cursor.fetchone()
        print("lo q encontro es: ",resultado)
        if resultado is None:
            print("la interrogacion: ",producto," no esta")
            return False
        else:
            print("la interrogacion: ",producto," si esta")

            print("le rol es: ",resultado[3])
            #return True
            return resultado[3]
        
    # Ejecutar consulta simple
    def consultacion_referencial(self, producto):
        consulta = "select nombre from referencia_ingredientes where nombre = '%s'"%producto
        print("la consultacion es :", consulta)
        self.cursor.execute(consulta)

        resultado = self.cursor.fetchone()
        print("Si se encontro en el referencial el producto: ",resultado)
        if resultado is None:
            return False
        else:
            return True
    
    def consultacion_ter(self, producto):
        """ Si el producto existe, regresamos la cantidad"""
        consulta = "select cantidad from ingredientes where nombre = '%s'"%producto
        print("la consultacion es :", consulta)
        self.cursor.execute(consulta)

        cantidad = self.cursor.fetchone()[0]
        print("lo q encontro es: ",cantidad)
        
        return cantidad

    # Ejecutar maj
    def update(self, producto):
        """ Actualizando ingrediente """
        data = producto
        print("el producto recibido es: ", data[1],"y ",data[0])

        actualizando = "update ingredientes set cantidad = %3i, fecha_vencimiento = '2028-10-10' where nombre = '%s'"
        
        requete = actualizando%(int(data[1]),data[0])
        print("la requete es: ", requete)
        self.ejecutar_requete(requete)
        self.ejecutar_requete("commit")
        
    # Ejecutar requete y verificar sino hay error
    def ejecutar_requete(self, interrogacion ):
        """ Funcion que nos va a ejecutar las requetes y
            nos va a verificar si hay un error o no """
        
        try:
            self.cursor.execute(interrogacion)
        except base.Error as e:
            print("Error al ejecutar la consulta", e)

    def fin(self):
        self.cursor.close()
        self.conexion.close()


### Session principal
if __name__ == "__main__" :
    #controlando = Kontrolador()
    probando = mi_base()
    probando.insercion()
    probando.update()
    probando.consultacion()
    probando.fin()
    #probando.gestion_del_menu()
    
