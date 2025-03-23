""" afichage de CANVAS """
""" Version 1 """

# coding: utf-8

import tkinter as tk
import random as rd
import cocina_plus_bdd_7 as cocina

class AplicacionIngredientes(tk.Tk):
    """ Clase que va crear los componentes de mi ventana """
    def __init__(self):         # contructor
        tk.Tk.__init__(self)       # contructor de la clase madre

        # Somos una instancia de la cocina
        self.cocina = cocina.ingrediente()

        self.crear_componentes(self):
        
        # Crear y posicionar los widgets
        self.label = tk.Label( self, text = 'Bienvenido a la Boutique - control de la cocina')
        self.label.pack()

        self.boton_agregar = tk.Button( self, text = 'Agregar producto', command = self.cocina.agregar_ingrediente())
        self.boton_agregar.pack()

        self.boton_disminuir = tk.Button( self, text = 'Disminuir cantidad producto', command = self.cocina.ingrediente_out())
        self.boton_disminuir.pack()

        self.boton_verificar = tk.Button( self, text = 'Verificar disponibilidad del producto', command = self.cocina.verificar_ingrediente())
        self.boton_verificar.pack()

        self.boton_salir = tk.Button( self, text = 'Salir del control de los productos', command = self.cocina.confirmar_salir())
        self.boton_salir.pack()

    def stop(self, esc ):
        """ salir de la aplicacion """
        self.quit()

if __name__ == "__main__":
    app = AplicacionIngredientes()
    app.title("Boutique, gestion de los productos de la cocina")
    app.mainloop()

