import tkinter as tk 
import pagina_identificacion
import gestion_cocina
#import gestion_admin

class principal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pintando Ando")
        self.geometry("1080x720")
        self.minsize(420,300)

        #self.cocinero = gestion_cocina.cocina()
        #self.admin = gestion_admin.admin()


        self.loginpage()
        #self.page1 = Page1(self)
        #self.page2 = Page2(self)

        #self.show_login_page()

    def loginpage(self):
        
        # Configuración de widgets para el inicio de sesión
        self.identidad = pagina_identificacion.identificacion()
        
        # Llamo la pagina de identificacion
        self.identidad.crear_componentes_identificacion()

    def cerrar_frame(self):
        # Cerrar la caja
        self.destroy


if __name__ == "__main__":
    app = principal()
    app.mainloop()
