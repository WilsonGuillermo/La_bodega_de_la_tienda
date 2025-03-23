""" Modulo Cocina """
""" Version 10, proyecto ANYEA """
""" WgMg Python ChatPT """
""" Vamos a salvar el stock """
""" si el stock existe, lo cargamos """
""" Agregamos el menu """
""" nuevo menu affichar la lista """
""" Tenemos cuenta del referencial """
""" El mensaje del menu entra a la boucle"""
""" validacion stock, funcionando """
""" Consultar todo el stock """
""" disminuir la cantidad de un producto """

### Session de imports
import pickle as saumure
import os.path as camino
from gestion_bdd_4 import mi_base


### Session de constantes
class ingrediente(object):
    """ definicion del stockage """

    def __init__(self):
        """ Gestion del stock de ingredientes """

        self.mibase = mi_base()      
        
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
        
        k = input("El nombre del producto, por favor? ")
        if k == "q":
            print("Abandonamos")
            return
        if self.mibase.consultacion_bis(k):
            """ El producto existe, hacemos una actualizacion"""
            v = int(input("La cantidad que necesita, por favor? "))
            if v == "q":
                print("Abandonamos")
                return
            nueva_cantidad = int(self.mibase.consultacion_ter(k)) - v
            if nueva_cantidad < 0:
                print("ATTENCION: No hay suficiente %s, pedido rechazado!!"%k)
                return
            elif nueva_cantidad == 0:
                print("se puede hacer pero no queda mas %s en el stock"%k)
            
            # disminuimos la cantidad del producto
            print("la nueva cantidad  es :",nueva_cantidad)
            producto_al_dia = ( nueva_cantidad, k ) # Enviamos en el otro sentido
            print("el producto al dia: ",producto_al_dia)
            self.mibase.update(producto_al_dia)

    def verificar_ingrediente( self ):
        """ funcion q va nos servir para saber
            si tenemos un ingrediente y si tenemos
            la cantidad necesaria para el pedido realizado """
        
        k = input("El nombre del producto a verificar, por favor? ")
        if k == "q":
            print("Abandonamos")
            return
        if self.mibase.consultacion_bis(k):
            """ si el producto hace parte del stock, recuperamos su cantidad """
            
            v = "Actualmente tenemos %3i %s"
            cantidad = self.mibase.consultacion_ter(k)

            print(v%(cantidad,k))
        else:
            print("el producto pedido no hace parte del stock")

    def afichar_productos(self):
        """ afichar el stock"""
        self.mibase.consultacion()
    
    def gestion_del_menu(self):
        "Vamos a leer cada instrucion y segun ella vamos a una parte del codigo """
        
        while True:
            MENSAJE = "Con los ingredientes, que desea hacer: (a)gregar, (c)onfirmar, (d)isminuir, (S)alir, (l)ista, (V)olver: \n"
            escoja = input(MENSAJE)

            if escoja == "A" or escoja == "a":
                print("agregar ingrediente y la cantidad")

                self.agregar_ingrediente()
                
            elif escoja == "c" or escoja == "C":
                print("ingrediente y cantidad à verificar")
               
                self.verificar_ingrediente()

            elif escoja == "l" or escoja == "L":
                self.afichar_productos()
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
    
