import tkinter as tk
from tkinter import ttk


class buscarPedido(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Buscar pedido")
        self.geometry("400x500")
        self.centrar_ventana()
        self.config(bg="#d4f4ff")
        self.agregar_widgets()

    def agregar_widgets(self):
        # Aqui van los estilos
        estilo = ttk.Style()
        estilo.theme_use("clam")
        # Cambiar el fondo del frame utilizando ttk.Style
        estilo.configure("frame1.TFrame", background="#5286ee")
        # Configurar la ventana
        self.rowconfigure(0,weight=2)
        self.rowconfigure(1,weight=5)
        self.rowconfigure(2,weight=1)

        for i in range(0,3):
            self.columnconfigure(i,weight=1)

        # Creacion del frame1
        self.Frame1 = ttk.Frame(self, style="frame1.TFrame")
        self.Frame1.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        self.Frame1.rowconfigure(0, weight=1)
        self.Frame1.rowconfigure(0,weight=1)
        self.Frame1.columnconfigure(0, weight=1)

        self.lblTitulo = ttk.Label(self.Frame1, text="Seguimiento de Pedido", anchor="center")
        self.lblTitulo.grid(row=0,column=0, sticky="nsew", pady=5)
        self.lblSubTitulo = ttk.Label(self.Frame1, text="Ingrese su código de pedido para buscar el estado", anchor="center")
        self.lblSubTitulo.grid(row=1,column=0, sticky="nsew",pady=5)

        # Creacion del frame2
        self.Frame2 = ttk.Frame(self)
        self.Frame2.grid(row=1,column=1,sticky="nsew", padx=5,pady=5)

        for i in range(0,3):
            self.Frame2.rowconfigure(i, weight=1)
        self.Frame2.columnconfigure(0,weight=1)

        self.lblCodigoPedido = ttk.Label(self.Frame2, text="Codigo de Pedido:")
        self.lblCodigoPedido.grid(row=0, column=0)
        self.entradaPedido = ttk.Entry(self.Frame2)
        self.entradaPedido.grid(row=1,column=0)
        self.botonBuscar = ttk.Button(self.Frame2, text="Buscar")
        self.botonBuscar.grid(row=2,column=0)

    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    pedido = buscarPedido()
    pedido.mainloop()