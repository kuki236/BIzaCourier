import tkinter as tk
from tkinter import ttk


class vistaEmpleado(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Pedidos")
        self.geometry("600x400")
        self.centrar_ventana()
        self.config(bg="white")
        self.agregar_widgets()

    def agregar_widgets(self):
        # Configuración de la ventana principal (2 filas, 1 columna)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.columnconfigure(0, weight=1)

        # Frame superior para el título
        self.Frame1 = ttk.Frame(self)
        self.Frame1.grid(row=0, column=0, sticky="nsew")
        self.Frame1.rowconfigure(0, weight=1)
        self.Frame1.columnconfigure(0, weight=1)

        # Título y subtítulo
        self.lblTitulo = ttk.Label(self.Frame1, text="Gestión de Pedidos", anchor="center", font=("Arial", 16, "bold"))
        self.lblTitulo.grid(row=0, column=0, sticky="nsew")
        self.lblSubTitulo = ttk.Label(self.Frame1, text="Organiza y gestiona tus pedidos fácilmente", anchor="center")
        self.lblSubTitulo.grid(row=1, column=0, sticky="nsew")

        # Frame inferior para los botones
        self.Frame2 = ttk.Frame(self)
        self.Frame2.grid(row=1, column=0, sticky="nsew", padx=150, pady=50)

        # Configuración del frame inferior (3 filas, 1 columna)
        self.Frame2.rowconfigure(0, weight=1)
        self.Frame2.rowconfigure(1, weight=1)
        self.Frame2.rowconfigure(2, weight=1)
        self.Frame2.columnconfigure(0, weight=1)

        # Botones
        self.btnCrearPedido = ttk.Button(self.Frame2, text="Crear Pedido", command=self.crear_pedido)
        self.btnCrearPedido.grid(row=0, column=0, sticky="nsew", pady=10)

        self.btnCambiarEstado = ttk.Button(self.Frame2, text="Cambiar Estado Pedido", command=self.cambiar_estado_pedido)
        self.btnCambiarEstado.grid(row=1, column=0, sticky="nsew", pady=10)

    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    # Funciones para los botones
    def crear_pedido(self):
        from vista.gestionDeDatosPedido import gestionDeDatosPedido
        self.destroy()
        gPedido = gestionDeDatosPedido()
        gPedido.mainloop()
        # Aquí podrías llamar a otra Sclase o ventana si es necesario

    def cambiar_estado_pedido(self):
        from vista.gestionDeDatosTicketEncomienda import ca
        print("Función Cambiar Estado Pedido llamada.")
        # Aquí podrías llamar a otra clase o ventana si es necesario


if __name__ == "__main__":
    iniciar_menu = vistaEmpleado()
    iniciar_menu.mainloop()
