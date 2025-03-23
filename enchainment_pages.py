import tkinter as tk 
import pagina_identificacion
import gestion_cocina
#import gestion_admin

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pintando Ando")
        self.geometry("1080x720")
        self.minsize(420,300)

        #self.cocinero = gestion_cocina.cocina()
        #self.admin = gestion_admin.admin()


        self.login_page = LoginPage(self)
        self.page1 = Page1(self)
        self.page2 = Page2(self)

        self.show_login_page()

    def show_login_page(self):
        self.login_page.pack()
        self.page1.pack_forget()
        self.page2.pack_forget()

    def show_page1(self):
        self.login_page.pack_forget()
        self.page1.pack()
        self.page2.pack_forget()

    def show_page2(self):
        self.login_page.pack_forget()
        self.page1.pack_forget()
        self.page2.pack()

class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # Configuración de widgets para el inicio de sesión
        self.identidad = pagina_identificacion.identificacion()
        self.crear_widgets()

    def crear_widgets(self):
        # Llamo la pagina de identificacion
        self.identidad.crear_componentes()

    def cerrar_frame(self):
        # Cerrar la caja

        self.destroy

class Page1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Configuración de widgets para la página 1

        self.cocinero = gestion_cocina.cocina()

        self.crear_widgets()

    def crear_widgets(self):
        # Llamo la pagina de gestion de la cocina
        self.cocinero.crear_componentes()


class Page2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Configuración de widgets para la página 2
        #self.admin()

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
