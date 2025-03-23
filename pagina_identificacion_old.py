""" Pagina de identificacion """
""" Version 3, 09-04 a 11h """
""" nombre unico del fichero """
""" Agregamos el cadre de la pagina principal """

# coding: utf-8

import tkinter as tk
import random as rd
import gestion_bdd as mibase
import gestion_cocina as micocina
import enchainment_pages
#import gestion_admin as admin

# CONSTANTES

class identificacion(tk.Tk):
    """ Clase que va crear los componentes de mi ventana """
    def __init__(self):         # contructor
        tk.Tk.__init__(self)       # contructor de la clase madre

        # Somos una instancia de la cocina
        self.bdd = mibase.mi_base()
        self.cocina = micocina.cocina()
        #self.admin = admin.admin()

        #self.grid()

        self.crear_componentes()

    def crear_componentes(self):
        """ Crear y posicionar botones """
    
        # Crear y posicionar los widgets
        self.label = tk.Label( self, text = 'Bienvenido a la Boutique - Pagina de Identificacion')
        self.label.pack()

        self.label = tk.Label( self, text = 'Por favor escribe tu usuario')
        self.label.pack()

        self.display1 = tk.Entry(self, font=("Arial", 24), bg='darkblue', fg='red', borderwidth=0)
        self.display1.pack()

        self.label2 = tk.Label( self, text = 'Por favor escribe tu clave')
        self.label2.pack()

        self.display2 = tk.Entry(self, font=("Arial", 24), bg='darkred', fg='red', borderwidth=0)
        self.display2.pack()

        self.boton_busqueda = tk.Button( self, text = 'Valider', command = self.celula_de_identificacion)
        self.boton_busqueda.pack()

        # Boton para salir de la aplicacion
        self.bouton_salir = tk.Button( self, text = "Salir", command = self.quit )
        self.bouton_salir.pack(side=tk.BOTTOM)

    def celula_de_identificacion(self):
        """ recuperamos el valor escrito y lo enviamos a la funcion """

        usuario = self.display1.get()

        contrasena  = self.display2.get()

        print("el valor a enviar ahora mismo es: ",usuario," y ", contrasena)

        requete = "select * from usuarios where nombre_usuario = '%s' and contrasena = '%s'"%(usuario,contrasena)
        
        print("******************************************")

        print("recibimos: ", self.bdd.consultacion_madre(requete))

        print("******************************************")

        #  Verificamos si el usuario existe
        if self.bdd.consultacion_madre(requete) == 'Admin':
            """ Administrador """
            self.admin()
        elif self.bdd.consultacion_madre(requete) == 'Cocinero':
            """ Concinero """
            self.cocina.crear_componentes()
        elif self.bdd.consultacion_madre(requete) == 'Mesero':
            """ Mesero """
        elif self.bdd.consultacion_madre(requete) == 'Jardinero':
            """ Jardinero """
        elif self.bdd.consultacion_madre(requete) == 'Responsable':
            """ Responsable """
        else:
            print("la pareja 'usuario, clave' no existe")
    
if __name__ == "__main__":
    app = identificacion()
    app.title("Boutique, gestion de los productos de la cocina")
    app.mainloop()   