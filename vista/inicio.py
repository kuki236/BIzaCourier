import tkinter as tk
from tkinter import ttk


class inicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de datos")
        self.geometry("1000x600")
        self.centrar_ventana()
        self.config(bg="white")
        self.estilo_moderno()
        self.agregar_widgets()

    def estilo_moderno(self):
        """Define un estilo moderno para los widgets."""
        estilo = ttk.Style()
        estilo.theme_use("clam")

        # Fondo de la ventana principal
        self.config(bg="#f5f5f5")

        # Estilo para títulos
        estilo.configure(
            "Titulo.TLabel",
            font=("Arial", 24, "bold"),
            foreground="#333333",
            background="#f5f5f5",
        )
        estilo.configure(
            "SubTitulo.TLabel",
            font=("Arial", 16),
            foreground="#555555",
            background="#f5f5f5",
        )

        # Estilo para botones
        estilo.configure(
            "Boton.TButton",
            font=("Arial", 12),
            foreground="white",
            background="#0078D7",
            borderwidth=1,
            focuscolor="#005A9E",
        )
        estilo.map(
            "Boton.TButton",
            background=[("active", "#005A9E"), ("disabled", "#cccccc")],
        )

        # Estilo para etiquetas simples
        estilo.configure(
            "Etiqueta.TLabel",
            font=("Arial", 12),
            foreground="#333333",
            background="#f5f5f5",
        )
    def agregar_widgets(self):
        # Aqui van los estilos


        # Configuracion de la ventana ( Seran 2 filas y 1 columna )
        """Agrega widgets a la ventana."""
        # Configuración de la ventana
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.columnconfigure(0, weight=1)

        # Frame 1
        self.Frame1 = ttk.Frame(self, style="Titulo.TFrame")
        self.Frame1.grid(row=0, column=0, sticky="nsew")

        self.Frame1.rowconfigure(0, weight=1)
        self.Frame1.rowconfigure(1, weight=1)
        self.Frame1.columnconfigure(0, weight=1)

        # Crear títulos en Frame 1
        self.lblTitulo = ttk.Label(
            self.Frame1, text="bizaCourier", anchor="center", style="Titulo.TLabel"
        )
        self.lblTitulo.grid(row=0, column=0, sticky="nsew")

        self.lblSubTitulo = ttk.Label(
            self.Frame1,
            text="Envíos rápidos y seguros",
            anchor="center",
            style="SubTitulo.TLabel",
        )
        self.lblSubTitulo.grid(row=1, column=0, sticky="nsew")

        # Frame 2
        self.Frame2 = ttk.Frame(self, style="Etiqueta.TFrame")
        self.Frame2.grid(row=1, column=0, sticky="nsew", padx=375, pady=50)

        for i in range(0, 6):
            self.Frame2.rowconfigure(i, weight=1)
        self.Frame2.columnconfigure(0, weight=1)

        self.lblOpciones = ttk.Label(
            self.Frame2, text="Opciones", anchor="center", style="SubTitulo.TLabel"
        )
        self.lblOpciones.grid(row=0, column=0, pady=(0, 10))

        # Botones
        nombre_botones = [
            "CRUD Empleados",
            "CRUD Sucursales",
            "CRUD Cliente",
            "Asignar Empleado a Sucursal",
            "Buscar Pedido por Nombre",
        ]
        comandos_botones = [
            self.crudEmpleados,
            self.crudSucursales,
            self.crudCliente,
            self.asignarEmpleado,
            self.buscarPedido,
        ]

        for i, nombre, comando in zip(range(1, 6), nombre_botones, comandos_botones):
            boton = ttk.Button(
                self.Frame2, text=nombre, command=comando, style="Boton.TButton"
            )
            boton.grid(row=i, column=0, sticky="nsew", pady=5)


    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    # Estas son las funciones para las botones al hacer click
    def crudEmpleados(self):
        from vista.gestionDeDatosEmpleado import gestionDeDatosEmpleado
        self.destroy()
        gDatos = gestionDeDatosEmpleado()
        gDatos.mainloop()

    def crudSucursales(self):
        from vista.gestionDeDatosSucursal import gestionDeDatosSucursal
        self.destroy()
        gDatos = gestionDeDatosSucursal()
        gDatos.mainloop()
    def crudCliente(self):
        from vista.gestionDeDatosCliente import gestionDeDatosCliente
        self.destroy()
        gDatos = gestionDeDatosCliente()
        gDatos.mainloop()
    def asignarEmpleado(self):
        from vista.sucursalEmpleado import GestionDeDatosSucursalEmpleado
        self.destroy()
        gSucursalEmpleado = GestionDeDatosSucursalEmpleado()
        gSucursalEmpleado.mainloop()
        pass
    def buscarPedido(self):
        from vista.buscarPedido import buscarPedido
        self.destroy()
        gDatos = buscarPedido()
        gDatos.mainloop()

if __name__ == "__main__":
    iniciarMenu = inicio()
    iniciarMenu.mainloop()