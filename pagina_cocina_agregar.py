""" afichage de la pagina control
    de los productos de la cocina """
""" Version 4 """
""" nombre unico"""

# coding: utf-8

import tkinter as tk
import random as rd
#import cocina_plus_bdd_7 as cocina
import gestion_bdd as mibase

# CONSTANTES
DESCONOCIDO = "producto desconocido"

ser_o_estar = None

class Aplicacion_Agregar_Ingredientes(tk.Tk):
    """ Clase que va crear los componentes de mi ventana """
    def __init__(self):         # contructor
        tk.Tk.__init__(self)       # contructor de la clase madre

        # Somos una instancia de la cocina
        self.bdd = mibase.mi_base()

        #self.grid()

        self.crear_componentes()
    
    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def append(self, text):
        actualText = self.display.get()
        textLength = len(actualText)
        if actualText == "0":
            self.replaceText(text)
        else:
            self.display.insert(textLength, text)

    def mostrar_resultado(self):
        global ser_o_estar

        ser_o_estar = self.verificando_existencia()
    
    def verificando_existencia(self):
        """ recuperamos el valor escrito y lo enviamos a la funcion """
        
        global ser_o_estar

        producto = self.display1.get()

        print("el valor a enviar ahora mismo es: ",producto)
        
        #  Verificamos si el producto hace parte del referente
        if self.bdd.consultacion_referencial(producto):
            # si esta, verificamos si ya hace parte del stock
            if self.bdd.consultacion_bis(producto):
                #ser_o_estar = PUESTA_AL_DIA
                print(producto," a poner al dia")
                """ Intentamos hacer la modification desde aqui """
                self.label = tk.Label( self, text = 'Poner al dia la cantidad, por favor: ')
                self.label.pack(pady=20)

                self.display = tk.Entry(self, font=("Arial", 24), bg='darkblue', fg='red', borderwidth=0)
                self.display.insert(0, "0")
                self.display.pack(pady=20)

                """ Vamos a poner al dia la cantidad """
                print("Solo vamos a poner al dia la cantidad")

                self.boton_cantidad = tk.Button( self, text = 'Agregar cantidad', command = self.poner_al_dia)
                self.boton_cantidad.pack(pady=20)
            else:
                print(producto," es NUEVO")

                self.label = tk.Label( self, text = 'Agregar cantida por favor: ')
                self.label.pack(pady=20)

                self.display = tk.Entry(self, font=("Arial", 24), bg='darkblue', fg='red', borderwidth=0)
                self.display.insert(0, "0")
                self.display.pack(pady=20)

                """ El producto se puede agregar """
                print(" El producto nuevo y se puede agregar en la tabla ingredientes ")
                self.boton_nuevo = tk.Button( self, text = 'Agregar cantidad', command = self.ingresar_nuevo)
                self.boton_nuevo.pack(pady=20)
                
        else:
            print(producto," DESCONOCIDO")
            self.label = tk.Label( self, text = 'El producto no hace parte del stock, consultar con el administrador')
            self.label.pack()
            
    def ingresar_nuevo(self):
        """ recuperamos el valor escrito y lo enviamos a la funcion """

        producto = self.display1.get()
        cantidad = self.display.get()

        requete = (producto,cantidad)
        print("voy a ingresar uno nuevo: ", requete)
        return self.bdd.agregar(requete)

    def poner_al_dia(self):
        """ recuperamos el valor escrito y lo enviamos a la funcion """

        producto = self.display1.get()
        cantidad = int(self.display.get())
        cantidad_vieja = int(self.bdd.consultacion_ter(producto))
        cantidad_nueva = cantidad + cantidad_vieja

        requete = (producto,cantidad_nueva)

        return self.bdd.update(requete)
    
    def evaluate(self):
        try:
            self.replaceText(eval(self.display.get()))
        except (SyntaxError, AttributeError):
            messagebox.showerror("Error", "Syntax Error")
            self.replaceText("0")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot Divide by 0")
            self.replaceText("0")

    def crear_componentes(self):
        """ Crear y posicionar botones """
    
        # Crear y posicionar los widgets
        self.label = tk.Label( self, text = 'Bienvenido a la Boutique - control de la cocina')
        self.label.pack()

        self.label = tk.Label( self, text = 'Vamos a agregar producto o aumentar su stock')
        self.label.pack()

        self.display1 = tk.Entry(self, font=("Arial", 24), bg='darkblue', fg='red', borderwidth=0)
        self.display1.pack()

        self.boton_busqueda = tk.Button( self, text = 'Buscar producto', command = self.verificando_existencia)
        self.boton_busqueda.pack()

        # Boton para salir de la aplicacion
        self.bouton_salir = tk.Button( self, text = "Salir", command = self.quit )
        self.bouton_salir.pack(side=tk.BOTTOM)
        
        #self.boton_salir = tk.Button( self, text = 'Salir', command = self.stop)
        #self.boton_salir.pack()

    def stop(self, esc ):
        """ salir de la aplicacion """
        self.quit()

if __name__ == "__main__":
    app = Aplicacion_Agregar_Ingredientes()
    app.title("Boutique, gestion de los productos de la cocina")
    app.mainloop()

