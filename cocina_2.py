""" Modulo Cocina """
""" Version 2, proyecto ANYEA """
""" WgMg Python ChatPT """
""" Vamos a salvar el stock """

### Session de imports
import pickle as saumure
import os.path as camino

### Session de constantes
NOMBRE_FIC_GRABADO = "stockage.pickle"

class ingrediente(object):
    """ definicion del annuario """

    def __init__(self):
        """ Gestion del stock de ingredientes """

        #self.stock = { 'harina': 100, 'huevos': 50, 'leche': 30, 'mantequilla': 32 }
        self.stock = self.cargar()

        if self.stock is None:
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
                self.stock = saumure.load(ficor)

        else:
            return None


### Session principal
if __name__ == "__main__" :
    probando = ingrediente()
    probando.agregar_ingrediente("Yuca", 15)
    
