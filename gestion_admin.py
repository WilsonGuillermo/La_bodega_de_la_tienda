""" Pagina de Gestion de la cocina """
""" Version 1 """

# coding: utf-8

import tkinter as tk
import random as rd
import gestion_bdd as mibase
import gestion_cocina as cocina

# CONSTANTES

class admin(tk.Tk):
    """ Clase que va crear los componentes de mi ventana """
    def __init__(self):         # contructor
        tk.Tk.__init__(self)       # contructor de la clase madre

        # Somos una instancia de la cocina
        self.bdd = mibase.mi_base()
        #self.admin = admin.admin()

        #self.grid()

        self.crear_componentes()

    def crear_componentes(self):
        """ Crear y posicionar botones """
    
        # Crear y posicionar los widgets
        self.label = tk.Label( self, text = 'Bienvenido a la Boutique - Pagina para gestionar la cocina')
        self.label.pack()

        self.label = tk.Label( self, text = 'Que deseas hacer ?')
        self.label.pack()

        self.boton_busqueda = tk.Button( self, text = 'Modificar la cantidad de stockage de un producto', command = self.ingredientes)
        self.boton_busqueda.pack()

        self.boton_busqueda = tk.Button( self, text = 'Modificar los menus', command = self.menus)
        self.boton_busqueda.pack()

        self.boton_busqueda = tk.Button( self, text = 'Modificar los platos del dia', command = self.platos_del_dia)
        self.boton_busqueda.pack()

        self.boton_busqueda = tk.Button( self, text = 'Modificar los platos informales', command = self.platos_informales)
        self.boton_busqueda.pack()

        self.boton_busqueda = tk.Button( self, text = 'Modificar las bebidas', command = self.bebidas)
        self.boton_busqueda.pack()

        self.boton_busqueda = tk.Button( self, text = 'Modificar los postres', command = self.postres)
        self.boton_busqueda.pack()

        # Boton para salir de la aplicacion
        self.bouton_salir = tk.Button( self, text = "Salir", command = self.quit )
        self.bouton_salir.pack(side=tk.BOTTOM)

if __name__ == "__main__":
    app = admin()
    app.title("Boutique, Pagina del Administrador")
    app.mainloop()