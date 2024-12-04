import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Cliente
class gestionDeDatosCliente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de datos")
        self.geometry("700x600")
        self.centrar_ventana()
        self.config(bg="white")
        self.agregar_widgets()

    def agregar_widgets(self):
        # aqui van los estilos

        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)

        # Creacion del frame1 donde estará la informacion

        self.Frame1 = ttk.Frame(self)
        self.Frame1.grid(row=0,column=0,sticky="nsew", padx=15,pady=10)

        for i in range(0,11):
            self.Frame1.rowconfigure(i,weight=1)
        self.Frame1.columnconfigure(0,weight=1)

        # Aqui iran los widgets para el frame1
        self.lblDetallesPed = ttk.Label(self.Frame1,text="Detalles del pedido")
        self.lblDetallesPed.grid(row=0,column=0,sticky="w")
        self.dirEnt = ttk.Label(self.Frame1, text="Dirección de entrega:")
        self.dirEnt.grid(row=1, column=0, sticky="w")
        self.modDirec = ttk.Label(self.Frame1, text="[Direccion]") # por modificar
        self.modDirec.grid(row=2, column=0, sticky="w")
        self.nombreCliente = ttk.Label(self.Frame1, text="Nombre del cliente:")
        self.nombreCliente.grid(row=3, column=0, sticky="w")
        self.modNombreCliente = ttk.Label(self.Frame1, text="[Nombre cliente]")  # por modificar
        self.modDirec.grid(row=4, column=0, sticky="w")
        self.nombreEmpleado = ttk.Label(self.Frame1, text="Nombre del empleado:")
        self.nombreEmpleado.grid(row=5, column=0, sticky="w")
        self.modNombreEmpleado = ttk.Label(self.Frame1, text="[Nombre empleado]")  # por modificar
        self.modNombreEmpleado.grid(row=6, column=0, sticky="w")
        self.sucOrig = ttk.Label(self.Frame1, text="Sucursal de origen:")
        self.sucOrig.grid(row=7, column=0, sticky="w")
        self.modSucOrig = ttk.Label(self.Frame1, text="[Sucursal de origen]")  # por modificar
        self.modSucOrig.grid(row=8, column=0, sticky="w")
        self.sucDest = ttk.Label(self.Frame1, text="Sucursal de Destino:")
        self.sucDest.grid(row=9, column=0, sticky="w")
        self.modSucDest = ttk.Label(self.Frame1, text="[Sucursal de Destino]")  # por modificar
        self.modSucDest.grid(row=10, column=0, sticky="w")




        # creacion del frame2 donde estará el mapa
        self.Frame2 = ttk.Frame(self)
        self.Frame2.grid(row=0,column=1,sticky="nsew", padx=15,pady=10)

    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    gDatos = gestionDeDatosCliente()
    gDatos.mainloop()