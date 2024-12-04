import tkinter as tk
from tkinter import ttk,messagebox


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x500")
        self.centrar_ventana()
        self.config(bg="#d4f4ff")

        self.agregar_widgets()

    def agregar_widgets(self):
        # Aqui van los estilos: ----------------------------------------
        estilo = ttk.Style()
        estilo.theme_use("clam")

        # Cambiar el fondo del frame utilizando ttk.Style
        estilo.configure("TFrame", background="white")

        # Aqui va la configuracion de las filas y columnas de la ventana --------------
        for i in range(0, 3):
            self.rowconfigure(i, weight=1)
        for j in range(0, 3):
            self.columnconfigure(j, weight=1)

        # Creacion del frame para centrar el contenido ----------------
        self.Frame1 = ttk.Frame(self)
        self.Frame1.grid(row=1,column=1,padx=5,pady=5)


        for i in range(0,5):
            self.Frame1.rowconfigure(i, weight=1)
        self.Frame1.columnconfigure(0,weight=1)

        # Aqui van los widgets -------------------------------------
        self.lblInicioSesion = ttk.Label(self.Frame1, text="INICIO SESIÓN",anchor="center")
        self.lblInicioSesion.grid(row=0,column=0,sticky="nsew", padx=5, pady=5)

        self.lblUsuario = ttk.Label(self.Frame1, text="Usuario: ")
        self.lblUsuario.grid(row=1,column=0,sticky="w", padx=5)

        self.lblContrasenia = ttk.Label(self.Frame1, text="Contraseña: ")
        self.lblContrasenia.grid(row=3,column=0,sticky="w", padx=5)

        self.entradaUsuario = ttk.Entry(self.Frame1)
        self.entradaUsuario.grid(row=2,column=0)

        self.entradaContrasenia = ttk.Entry(self.Frame1, show="*")
        self.entradaContrasenia.grid(row=4,column=0)

        self.botonIniciar = ttk.Button(self.Frame1, text="Iniciar sesión", command=self.iniciar)
        self.botonIniciar.grid(row=5,column=0,sticky="nsew", padx=10,pady=10)


    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def iniciar(self):
        from models.Login_Funcion import autenticar_usuario
        from vista.vistaEmpleado import vistaEmpleado
        from vista.inicio import inicio
        nombre = self.entradaUsuario.get()
        password = self.entradaContrasenia.get()

        if nombre and password:
            persona = autenticar_usuario(nombre,password)
            print(persona)
            if persona["cargo"] == "Empleado":
                self.destroy()
                objEmp = vistaEmpleado()
                objEmp.mainloop()
            elif persona["cargo"] == "Gerente":
                self.destroy()
                objInicio = inicio()
                objInicio.mainloop()
            else:
                messagebox.showerror("Error", "El usuario no existe")
        else:
            messagebox.showerror("Error", "Error al iniciar sesion")





if __name__ == "__main__":
    login_app = Login()
    login_app.mainloop()