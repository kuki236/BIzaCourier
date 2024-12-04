import tkinter as tk
from tkinter import ttk


class inicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de datos")
        self.geometry("1000x600")
        self.centrar_ventana()
        self.config(bg="white")
        self.agregar_widgets()


    def agregar_widgets(self):
        # Aqui van los estilos


        # Configuracion de la ventana ( Seran 2 filas y 1 columna )
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.columnconfigure(0, weight=1)
        # Aqui van la creacion de los widgets
        self.Frame1 = ttk.Frame(self)
        self.Frame1.grid(row=0, column=0, sticky="nsew")
        # Configurar el frame1
        self.Frame1.rowconfigure(0, weight=1)
        self.Frame1.rowconfigure(1,weight=1)
        self.Frame1.columnconfigure(0, weight=1)

        # Crear los titulos en el frame1
        self.lblTitulo = ttk.Label(self.Frame1, text="bizaCourier", anchor="center")
        self.lblTitulo.grid(row=0, column=0, sticky="nsew")
        self.lblSubTitulo = ttk.Label(self.Frame1, text="Envios rapidos y seguros", anchor="center")
        self.lblSubTitulo.grid(row=1,column=0,sticky="nsew")

        # Crear el frame2 ----------------------------
        self.Frame2 = ttk.Frame(self)
        self.Frame2.grid(row=1,column=0,sticky="nsew",padx=375, pady=50)

        # Configurar el frame2 (6 filas y 1 columna)
        for i in range(0,6):
            self.Frame2.rowconfigure(i, weight=1)
        self.Frame2.columnconfigure(0,weight=1)

        self.lblOpciones = ttk.Label(self.Frame2, text="Opciones")
        self.lblOpciones.grid(row=0,column=0)

        nombre_botones = ["CRUD empleados","CRUD Sucursales", "CRUD Pedido","Asignar Empleado a Sucursal", "Buscar pedido por nombre"]
        comandos_botones = [self.crudEmpleados, self.crudSucursales, self.crudPedido, self.asignarEmpleado, self.buscarPedido]

        # Creamos los botones
        for i, nombre, comando in zip(range(1,6), nombre_botones, comandos_botones):
            self.boton = ttk.Button(self.Frame2, text=nombre, command=comando)
            self.boton.grid(row=i, column=0, sticky="nsew")


    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    # Estas son las funciones para las botones al hacer click
    def crudEmpleados(self):
        pass
    def crudSucursales(self):
        pass
    def crudPedido(self):
        pass
    def asignarEmpleado(self):
        pass
    def buscarPedido(self):
        pass

if __name__ == "__main__":
    iniciarMenu = inicio()
    iniciarMenu.mainloop()