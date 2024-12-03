import tkinter as tk
from tkinter import ttk


class gestionDeDatos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de datos")
        self.geometry("1000x600")
        self.centrar_ventana()
        self.config(bg="white")
        self.agregar_widgets()


    def agregar_widgets(self):
        # Aqui van los estilos
        estilo = ttk.Style()
        estilo.theme_use("clam")
        # Cambiar el fondo del frame utilizando ttk.Style
        estilo.configure("frame1.TFrame", background="#5286ee")


        # Configurar la ventana (3 filas y 2 columnas)
        self.rowconfigure(0,weight=2)
        self.rowconfigure(1,weight=5)
        self.rowconfigure(2,weight=1)

        for i in range(0,2):
            self.columnconfigure(i,weight=1)

        # Creacion del frame1 para el titulo
        self.Frame1 = ttk.Frame(self, style="frame1.TFrame")
        self.Frame1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.Frame1.rowconfigure(0, weight=1)
        self.Frame1.rowconfigure(0,weight=1)
        self.Frame1.columnconfigure(0,weight=1)


        self.lblTitulo = ttk.Label(self.Frame1, text="Gestion de datos", anchor="center")
        self.lblTitulo.grid(row=0,column=0, sticky="nsew", pady=5)
        self.lblSubTitulo = ttk.Label(self.Frame1, text="Administra tu información facilmente", anchor="center")
        self.lblSubTitulo.grid(row=1,column=0, sticky="nsew",pady=5)

        # Creacion del frame2 (para el ingreso de datos)
        self.Frame2 = ttk.Frame(self)
        self.Frame2.grid(row=1,column=0,sticky="nsew", padx=5,pady=5)

        # 10 filas y 3 columnas
        for i in range(0,10):
            self.Frame2.rowconfigure(i, weight=1)
        for i in range(0,3):
            self.Frame2.columnconfigure(i,weight=1)


        self.lblDatos = ttk.Label(self.Frame2, text= "Datos")
        self.lblDatos.grid(row=0,column=0, sticky="w")
        self.lblNombre = ttk.Label(self.Frame2, text="Nombre:")
        self.lblNombre.grid(row=1, column=0, sticky="w")
        self.entradaNombre = ttk.Entry(self.Frame2, width=50)
        self.entradaNombre.grid(row=2,column=0,columnspan=3, sticky="w")
        self.lblApellido = ttk.Label(self.Frame2, text="Apellido:")
        self.lblApellido.grid(row=3, column=0, sticky="w")
        self.entradaApellido = ttk.Entry(self.Frame2, width=50)
        self.entradaApellido.grid(row=4, column=0, columnspan=3, sticky="w")
        self.lblCorreo = ttk.Label(self.Frame2, text="Correo:")
        self.lblCorreo.grid(row=5, column=0, sticky="w")
        self.entradaCorreo = ttk.Entry(self.Frame2, width=50)
        self.entradaCorreo.grid(row=6, column=0, columnspan=3, sticky="w")
        self.lblTelefono = ttk.Label(self.Frame2, text="Telefono:")
        self.lblTelefono.grid(row=7, column=0, sticky="w")
        self.entradaTelefono = ttk.Entry(self.Frame2, width=50)
        self.entradaTelefono.grid(row=8, column=0, columnspan=3, sticky="w")

        # Creacion de botones
        self.botonCrear = ttk.Button(self.Frame2, text="Crear")
        self.botonCrear.grid(row=9,column=0)
        self.botonActualizar = ttk.Button(self.Frame2, text= "Actualizar")
        self.botonActualizar.grid(row=9, column=1)
        self.botonEliminar = ttk.Button(self.Frame2, text="Eliminar")
        self.botonEliminar.grid(row=9,column=2)


        # Creacion del frame3 para la tabla

        self.Frame3 = ttk.Frame(self)
        self.Frame3.grid(row=1,column=1, sticky="nsew")

        # El frame3 tendra 2 filas y 1 columna
        self.Frame3.rowconfigure(0,weight=1)
        self.Frame3.rowconfigure(1,weight=3)
        self.Frame3.columnconfigure(0,weight=1)

        self.lblRegistros = ttk.Label(self.Frame3, text="Registros")
        self.lblRegistros.grid(row=0,column=0,sticky="w", padx=5)

        # Creacion de la tabla
        columnas_tabla = ("ID", "Nombre", "Apellido", "Correo", "Telefono")
        self.tabla = ttk.Treeview(self.Frame3, columns=columnas_tabla, show="headings")
        self.tabla.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")

        # Configuración de las columnas de la tabla
        for item_columna in columnas_tabla:
            self.tabla.heading(item_columna, text=item_columna)

        # Configuración del ancho de las columnas
        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Nombre", width=150, anchor="w")
        self.tabla.column("Apellido", width=100, anchor="w")
        self.tabla.column("Correo", width=100, anchor="w")
        self.tabla.column("Telefono", width=100, anchor="w")

        # Cargar los datos de la tabla
        self.cargarTabla()





    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def cargarTabla(self):
        pass

if __name__ == "__main__":
    gDatos = gestionDeDatos()
    gDatos.mainloop()