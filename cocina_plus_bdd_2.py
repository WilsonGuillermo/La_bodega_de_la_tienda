""" Modulo Cocina """
""" Version 7, proyecto ANYEA """
""" WgMg Python ChatPT """
""" Vamos a salvar el stock """
""" si el stock existe, lo cargamos """
""" Agregamos el menu """
""" nuevo menu affichar la lista """
""" Tenemos cuenta del referencial """

### Session de imports
import pickle as saumure
import os.path as camino
from gestion_bdd_4 import mi_base


### Session de constantes
NOMBRE_FIC_GRABADO = "stockage.pickle"

class eureka(object):
    # Conectarse a la BDD
    def __init__(self):
        
        conexion = base.connect(
            host = "localhost",
            user = "majo",
            password = "WilsonMemo_1964",
            database = "boutique"
        )

        # Crear un cursor para ejecutar consultas "
        cursor = conexion.cursor()

        # Ejecutar insercion
        consulta = "insert into usuarios (nombre_usuario, contrasena, rol) values ('Alejandro', 'WilsonMemo_1964', 'Mesero')";
        cursor.execute(consulta)
        validacion="commit;"
        cursor.execute(validacion)

        # Ejecutar consulta
        consulta = "select * from usuarios"
        cursor.execute(consulta)

        # Obtener los resultados
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)

        # Cerrar cursor y conexion
        cursor.close()
        conexion.close()

class ingrediente(object):
    """ definicion del stockage """

    def __init__(self):
        """ Gestion del stock de ingredientes """

        self.mibase = mi_base()
        
        #self.stock = { 'harina': 100, 'huevos': 50, 'leche': 30, 'mantequilla': 32 }

        #self.stock = self.cargar()

        
        
        self.gestion_del_menu()

    def agregar_ingrediente( self ):
        """ funcion q va nos servir para agregar un
            ingrediente a nuestro stockage """

        print("1________")

        k = input("El nombre, por favor? ")
        if k == "q":
            print("Abandonamos")
            return
        if self.mibase.consultacion_bis(k):
            """ El producto existe, hacemos una actualizacion"""
            v = int(input("La cantidad, por favor? "))
            if v == "q":
                print("Abandonamos")
                return
            nueva_cantidad = int(self.mibase.consultacion_ter(k)) + v
            # aumentamos la cantidad del producto
            print("la cantidad nueva es :",nueva_cantidad)
            producto_al_dia = ( nueva_cantidad, k ) # Enviamos en el otro sentido
            print("el producto al dia: ",producto_al_dia)
            self.mibase.update(producto_al_dia)
        elif self.mibase.consultacion_referencial(k):
            # el producto no existe, antes de agregarlo, verificamos si hace parte del referente
            
            v = input("La cantidad, por favor? ")
            if v == "q":
                print("Abandonamos")
                return
            tipo = input("El tipo (cereal,legumbre, abarrote), por favor? ")
            if tipo == "q":
                print("Abandonamos")
                return
            vencimiento = input("la fecha de vencimiento en formato 'AAAA-MM-DD', por favor? ")
            if vencimiento == "q":
                print("Abandonamos")
                return
            
            producto = ( k, v, tipo, vencimiento)
            print("el producto a insertar es: ",producto)
            self.mibase.agregar(producto)

        print("despues de agregar, tenemos... ")
        # Ejecutar consulta
        self.mibase.consultacion()
        
        return

    def ingrediente_out( self ):
        """ funcion q va nos servir para dsiminuir
            la cantidad de un ingrediente
            sea porque se acabo, sea porque se vencio """
        """ Primera version, basada en la cantidad y no en la fecha """
        clave = self.stock.keys()
        print("1________")
        print(clave)

        k = input("El nombre, por favor? ")
        if k == "q":
            print("Abandonamos")
            return
        v = int(input("La cantidad, por favor? "))
        if v == "q":
            print("Abandonamos")
            return
        
        if k in self.stock:
            if self.stock[k] >= v:
                self.stock[k] -= v
                print("despues de disminuir, tenemos... ", self.stock)
                self.salvar_stock()
            else:
                print("ATENCION: cantidad insuficiente de: ", k )
        else:
            print("ATENCION: no tenemos: ", k )


    def verificar_ingrediente( self, ingrediente, cantidad ):
        """ funcion q va nos servir para saber
            si tenemos un ingrediente y si tenemos
            la cantidad necesaria para el pedido realizado """

        clave = self.stock.keys()
        print("vi________")
        print(clave)

        k = input("El nombre, por favor? ")
        if k == "q":
            print("Abandonamos")
            return
        v = int(input("La cantidad, por favor? "))
        if v == "q":
            print("Abandonamos")
            return

        if k in self.stock:
            if self.stock[k] >= v:
                return True
            else:
                return False
        else:
            return False

    def salvar_stock(self):
        """ funcion q va nos servir para grabar el stock en un fichero """

        print("pasamos por aqui")
        with open( NOMBRE_FIC_GRABADO, 'wb' ) as ficherow:
            saumure.dump( self, ficherow )

        #probamos q el fichero ha sido bien guardado
        with open( NOMBRE_FIC_GRABADO, 'rb' ) as ficor:
                #self.stock = saumure.load(ficor)
                print("el stockage salvado contiene... ")
                print(ficor.read())
                
        return

    def cargar(self):
        """ funcion que nos va ayudar a cargar la clase/objeto """

        print("y pasamos por aqui tambien")
        if camino.exists(NOMBRE_FIC_GRABADO):
            with open( NOMBRE_FIC_GRABADO, 'rb' ) as ficor:
                self.stock = saumure.load(ficor)
                print("el stockage contiene... ", self.stock)

        else:
            print("no hay nada para cargar")
            return None

    def afichar_lista(self):
        
        #for x in self.stock:
        #    print( "tenemos %s de %s "%(self.stock[x],x))

        productos = self.stock.items()
        print(productos)
        
    def dar_datos(self):
        
        producto = input("El nombre, por favor? ")
        if producto == "q":
            print("Abandonamos")
            return
        cantidad = input("La cantidad, por favor? ")
        if cantidad == "q":
            print("Abandonamos")
            return

        return (str(producto), int(cantidad))
    
    def gestion_del_menu(self):
        "Vamos a leer cada instrucion y segun ella vamos a una parte del codigo """

        MENSAJE = "Con los ingredientes, que desea hacer: (a)gregar, (c)onfirmar, (d)isminuir, (S)alir, (l)ista, (V)olver: \n"

        escoja = input(MENSAJE)
        
        while True:
            if escoja == "A" or escoja == "a":
                print("agregar ingrediente y la cantidad")

                self.agregar_ingrediente()
                return
                
            elif escoja == "c" or escoja == "C":
                print("ingrediente y cantidad à verificar")
               
                if self.verificar_ingrediente():
                    print("tenemos lo suficiente")
                else:
                    print("atencion, problema!!!")
                    break
                return
            elif escoja == "l" or escoja == "L":
                self.afichar_lista()
                return
            elif escoja == "V" or escoja == "v":
                print(INSTRUCIONES)
            elif escoja == "D" or escoja == "d":
                self.ingrediente_out()
            elif escoja == "S" or escoja == "s":
                if confirmar_salir():
                    print("grabacion del anuario")
                    self.salvar_stock()
                    print("Final del programa")
                    break
            else:
                modelo = "Tecla enviada desconocida, %s "
                print(modelo%MENSAJE)
                return
    

### Session principal
if __name__ == "__main__" :
    #controlando = Kontrolador()
    probando = ingrediente()
    #probando.gestion_del_menu()
    
