""" Modulo Cocina """
""" Version 3, proyecto ANYEA """
""" WgMg Python ChatPT """
""" Vamos a salvar el stock """
""" si el stock existe, lo cargamos """

### Session de imports
import pickle as saumure
import os.path as camino

### Session de constantes
NOMBRE_FIC_GRABADO = "stockage.pickle"

class ingrediente(object):
    """ definicion del stockage """

    def __init__(self):
        """ Gestion del stock de ingredientes """

        #self.stock = { 'harina': 100, 'huevos': 50, 'leche': 30, 'mantequilla': 32 }
        self.stock = {}

    def agregar_ingrediente( self, ingrediente, cantidad ):
        """ funcion q va nos servir para agregar un
            ingrediente a nuestro stockage """

        if ingrediente in self.stock:
            self.stock[ingrediente] += cantidad
        else:
            self.stock[ingrediente] = cantidad

        print("despues de agregar, tenemos... ", self.stock)

        self.salvar_stock()

    def ingrediente_out( self, ingrediente, cantidad ):
        """ funcion q va nos servir para dsiminuir
            la cantidad de un ingrediente
            sea porque se acabo, sea porque se vencio """
        """ Primera version, basada en la cantidad y no en la fecha """

        if ingrediente in self.stock:
            if self.stock[ingrediente] >= cantidad:
                self.stock[ingrediente] -= cantidad
                print("despues de disminuir, tenemos... ", self.stock)
                self.salvar_stock()
            else:
                print("ATENCION: cantidad insuficiente de: ", ingrediente )
        else:
            print("ATENCION: no tenemos: ", ingrediente )


    def verificar_ingrediente( self, ingrediente, cantidad ):
        """ funcion q va nos servir para saber
            si tenemos un ingrediente y si tenemos
            la cantidad necesaria para el pedido realizado """

        if ingrediente in self.stock:
            if self.stock[ingrediente] >= cantidad:
                return True
            else:
                return False
        else:
            return False

    def salvar_stock(self):
        """ funcion q va nos servir para grabar el stock en un fichero """

        with open( NOMBRE_FIC_GRABADO, 'wb' ) as ficherow:
            saumure.dump( self, ficherow )

    def cargar(self):
        """ funcion que nos va ayudar a cargar la clase/objeto """

        if camino.exists(NOMBRE_FIC_GRABADO):
            with open( NOMBRE_FIC_GRABADO, 'rb' ) as ficor:
                self.ingrediente = saumure.load(ficor)
                print("el stockage contiene... ", self.stock)

        else:
            return None

    def gestion_del_menu(self):
        "Vamos a leer cada instrucion y segun ella vamos a una parte del codigo """

        MENSAJE = "Con los ingredientes, que desea hacer: (a)gregar, (c)onfirmar, (d)isminuir, (S)alir, (V)olver: \n"

        escoja = input(MENSAJE)
        
        while True:
            if escoja == "A" or escoja == "a":
                self.agregar_ingrediente()
            elif escoja == "L" or escoja == "l":
                self.verificar_stock()
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
    

class Kontrolador(object):
    """ clase q nos sirve a reutilisar cada vez q queramos nuestro stockage,
        y a salvarlo si lo modificamos """

    """ vamos a gestionar el almacenamiento de datos en nuestro stockage,
        para ello vamos a poner un menu """

    def __init__(self):
        """ Si nuestro stockage no existe, creamos una instancia del stockage,
            que sera un atributo de Kontrolador,
            pero si existe, lo cargamos """

        self.ingrediente = self.cargar()

        if self.ingrediente is None:
            self.ingrediente = {}

        self.gestion_del_menu()

        #ficha_individual_1 = FichaIndividual("Wilson", "Mosquera", "1964/04/14", "wilsonmemo@hotmail.com" )
        #print("el contacto agregado es: ", ficha_individual_1)
        #self.anuario.agregar_ficha(ficha_individual_1)

    def cargar(self):
        """ funcion que nos va ayudar a cargar la clase/objeto """

        if camino.exists(NOMBRE_FIC_GRABADO):
            with open( NOMBRE_FIC_GRABADO, 'rb' ) as ficor:
                self.ingrediente = saumure.load(ficor)
                print("el stockage contiene... ", self.ingrediente)

        else:
            return None

    def gestion_del_menu(self):
        "Vamos a leer cada instrucion y segun ella vamos a una parte del codigo """

        MENSAJE = "Con los ingredientes, que desea hacer: (a)gregar, (l)istar, (d)isminuir, (S)alir, (V)olver: \n"

        escoja = input(MENSAJE)
        
        while True:
            if escoja == "A" or escoja == "a":
                self.aumento_ingrediente()
            elif escoja == "L" or escoja == "l":
                self.afichar_stock()
            elif escoja == "V" or escoja == "v":
                print(INSTRUCIONES)
            elif escoja == "D" or escoja == "d":
                self.disminucion_stock()
            elif escoja == "S" or escoja == "s":
                if confirmar_salir():
                    print("grabacion del anuario")
                    self.anuario.grabar()
                    print("Final del programa")
                    break
            else:
                modelo = "Tecla enviada desconocida, %s "
                print(modelo%MENSAJE)

    def aumento_ingrediente(self):
        """ funcion q nos va a servir para agregar un nuevo contacto"""
        
        print("agregar ingrediente y la cantidad")
        ingrediente = input("El nombre, por favor? ")
        if ingrediente == "q":
            print("Abandonamos")
            return
        cantidad = input("La cantidad, por favor? ")
        if cantidad == "q":
            print("Abandonamos")
            return

        self.ingrediente.agregar_ingrediente( ingrediente, cantidad )

        fecha_de_vencimiento = input("La fecha de vencimiento en el formato aaaa/mm/jj, por favor? ")
        if fecha_de_vencimiento == "q":
            print("Abandonamos")
            return


### Session principal
if __name__ == "__main__" :
    #controlando = Kontrolador()
    probando = ingrediente()
    probando.gestion_del_menu()
    
