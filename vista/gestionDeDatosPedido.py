import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Pedido
class gestionDeDatosPedido(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de datos del pedido")
        self.geometry("1000x600")
        self.centrar_ventana()
        self.config(bg="white")
        self.agregar_widgets()


    def agregar_widgets(self):
        estilo = ttk.Style()

        # Establecer un tema base
        estilo.theme_use("clam")

        # Estilo del frame del título
        estilo.configure("frame1.TFrame", background="#5286ee")
        estilo.configure("frame2.TFrame", background="#f5f5f5")
        estilo.configure("frame3.TFrame", background="#f5f5f5")

        # Estilo para etiquetas
        estilo.configure("TLabel", font=("Arial", 12), background="#f5f5f5", foreground="#333")
        estilo.configure("Titulo.TLabel", font=("Arial", 20, "bold"), background="#5286ee", foreground="white")
        estilo.configure("Subtitulo.TLabel", font=("Arial", 14), background="#5286ee", foreground="white")

        # Estilo para entradas de texto
        estilo.configure("TEntry", padding=5, relief="flat", font=("Arial", 12))

        # Estilo para botones
        estilo.configure("TButton", font=("Arial", 12, "bold"), padding=5, background="#5286ee", foreground="white")
        estilo.map("TButton",
                   background=[("active", "#4169e1"), ("disabled", "#cccccc")],
                   foreground=[("active", "white")])

        # Estilo para la tabla
        estilo.configure("Treeview", font=("Arial", 10), rowheight=25, background="#ffffff", foreground="#333")
        estilo.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#5286ee", foreground="white")
        estilo.map("Treeview",
                   background=[("selected", "#5286ee")],
                   foreground=[("selected", "white")])

        # Bordes y márgenes
        estilo.configure("frame1.TFrame", relief="flat", padding=10)
        estilo.configure("TEntry", relief="flat", padding=5)


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


        self.lblTitulo = ttk.Label(self.Frame1, text="Gestion de datos del Pedido", anchor="center")
        self.lblTitulo.grid(row=0,column=0, sticky="nsew", pady=5)
        self.lblSubTitulo = ttk.Label(self.Frame1, text="Administra tu información facilmente", anchor="center")
        self.lblSubTitulo.grid(row=1,column=0, sticky="nsew",pady=5)

        # Creacion del frame2 (para el ingreso de datos)
        self.Frame2 = ttk.Frame(self)
        self.Frame2.grid(row=1,column=0,sticky="nsew", padx=5,pady=5)

        # 11 filas y 3 columnas
        for i in range(0,12):
            self.Frame2.rowconfigure(i, weight=1)
        for i in range(0,3):
            self.Frame2.columnconfigure(i,weight=1)


        self.lblDatos = ttk.Label(self.Frame2, text= "Datos")
        self.lblDatos.grid(row=0,column=0, sticky="w")
        self.lblDirec = ttk.Label(self.Frame2, text="Direccion:")
        self.lblDirec.grid(row=1, column=0, sticky="w")
        self.entradaDirec = ttk.Entry(self.Frame2, width=50)
        self.entradaDirec.grid(row=2,column=0,columnspan=3, sticky="w")
        self.lblCodPos = ttk.Label(self.Frame2, text="Codigo postal:")
        self.lblCodPos.grid(row=3, column=0, sticky="w")
        self.entradaCodPos = ttk.Entry(self.Frame2, width=50)
        self.entradaCodPos.grid(row=4, column=0, columnspan=3, sticky="w")
        self.lblIdCli = ttk.Label(self.Frame2, text="ID cliente:")
        self.lblIdCli.grid(row=5, column=0, sticky="w")
        self.entradaIdCli = ttk.Entry(self.Frame2, width=50)
        self.entradaIdCli.grid(row=6, column=0, columnspan=3, sticky="w")

        self.lblIdEnc = ttk.Label(self.Frame2, text="ID encargado:")
        self.lblIdEnc.grid(row=7, column=0, sticky="w")
        self.entradaIdEnc = ttk.Entry(self.Frame2, width=50)
        self.entradaIdEnc.grid(row=8, column=0, columnspan=3, sticky="w")

        self.lblIdPedido = ttk.Label(self.Frame2, text="ID pedido: ")
        self.lblIdPedido.grid(row=9, column=0,sticky="w")
        self.entradaIdPedido = ttk.Entry(self.Frame2, width=50)
        self.entradaIdPedido.grid(row=10, column=0, columnspan=3, sticky="w")

        # Creacion de botones
        self.botonCrear = ttk.Button(self.Frame2, text="Crear", command=self.crearEmpleado)
        self.botonCrear.grid(row=11,column=0)
        self.botonActualizar = ttk.Button(self.Frame2, text= "Actualizar",command=self.actualizarEmpleado)
        self.botonActualizar.grid(row=11, column=1)
        self.botonEliminar = ttk.Button(self.Frame2, text="Eliminar", command=self.eliminarEmpleado)
        self.botonEliminar.grid(row=11,column=2)


        # Creacion del frame3 para la tabla

        self.Frame3 = ttk.Frame(self)
        self.Frame3.grid(row=1,column=1, sticky="nsew", padx=10)

        # El frame3 tendra 2 filas y 1 columna
        self.Frame3.rowconfigure(0,weight=1)
        self.Frame3.rowconfigure(1,weight=3)
        self.Frame3.columnconfigure(0,weight=1)

        self.lblRegistros = ttk.Label(self.Frame3, text="Registros")
        self.lblRegistros.grid(row=0,column=0,sticky="w", padx=5)

        # Creacion de la tabla
        columnas_tabla = ("ID", "Nombre", "Direccion_entrega", "Codigo_postal", "ID_cliente", "Encargado")
        self.tabla = ttk.Treeview(self.Frame3, columns=columnas_tabla, show="headings")
        self.tabla.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")

        # Configuración de las columnas de la tabla
        for item_columna in columnas_tabla:
            self.tabla.heading(item_columna, text=item_columna)

        # Configuración del ancho de las columnas
        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Nombre", width=150, anchor="w")
        self.tabla.column("Direccion_entrega", width=100, anchor="w")
        self.tabla.column("Codigo_postal", width=100, anchor="w")
        self.tabla.column("ID_cliente", width=100, anchor="center")
        self.tabla.column("Encargado", width=100, anchor="center")

        # Cargar los datos de la tabla
        self.cargarTabla()

        # Vincular evento para seleccionar una fila
        self.tabla.bind("<ButtonRelease-1>", self.obtener_fila_seleccionada)





    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def cargarTabla(self):
        from models.Pedido import read_pedidos
        self.datos_pedidos = read_pedidos()
        for ide,nombre,direc,cod,idCli,idCreador in self.datos_pedidos:
            self.tabla.insert("", "end", values=(ide, nombre, direc, cod, idCli, idCreador))

    def actualizarTabla(self):
        for item in self.tabla.get_children():  # Obtener todos los elementos de la tabla
            self.tabla.delete(item)  # Eliminar cada elemento
        self.cargarTabla()

    def obtener_fila_seleccionada(self,event):
        # Obtiene la fila seleccionada en la tabla
        seleccion = self.tabla.focus()  # Obtiene la clave del elemento seleccionado
        if seleccion:
            valores = self.tabla.item(seleccion, "values")  # Obtiene los valores de la fila seleccionada
            # Limpia las entradas antes de llenarlas
            self.limpiar_entradas()

            # Rellena las entradas con los valores de la fila seleccionada
            self.entradaDirec.insert(0, valores[2])
            self.entradaCodPos.insert(0, valores[3])
            self.entradaIdCli.insert(0, valores[4])
            self.entradaIdEnc.insert(0, valores[5])
            self.entradaIdPedido.insert(0, valores[0])



    def limpiar_entradas(self):

        self.entradaIdPedido.delete(0, tk.END)
        self.entradaDirec.delete(0, tk.END)
        self.entradaCodPos.delete(0, tk.END)
        self.entradaIdEnc.delete(0, tk.END)
        self.entradaIdCli.delete(0, tk.END)

    def crearEmpleado(self):
        from models.Pedido import create_pedido
        ide = self.entradaIdPedido.get()
        direc = self.entradaDirec.get()
        codPos = self.entradaCodPos.get()
        idCliente = self.entradaIdCli.get()
        idEncargado = self.entradaIdEnc.get()

        if ide and direc and codPos and idCliente and idEncargado:
            create_pedido(ide, direc, codPos, idCliente, idEncargado)
            messagebox.showinfo("Pedido", f"El pedido se agregó correctamente")
            self.actualizarTabla()
            self.limpiar_entradas()
        else:
            messagebox.showerror("Pedido", "Hubo un problema al agregar pedido")
    def actualizarEmpleado(self):
        from models.Pedido import update_pedido

        seleccion = self.tabla.focus()  # Obtiene la clave del elemento seleccionado
        if seleccion:

            ide = self.entradaIdPedido.get()
            direc = self.entradaDirec.get()
            codPos = self.entradaCodPos.get()

            if ide and direc and codPos:
                update_pedido(ide, direc, codPos)
                messagebox.showinfo("Pedido", f"Se actualizo los campos del pedido")
                self.actualizarTabla()
                self.limpiar_entradas()
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar el pedido")




    def eliminarEmpleado(self):
        from models.Empleado import delete_empleado
        seleccion = self.tabla.focus()  # Obtiene la clave del elemento seleccionado
        if seleccion:
            valores = self.tabla.item(seleccion, "values")
            ide = valores[0]

            if ide:
                delete_empleado(ide)
                rpta = messagebox.askyesno("Aviso", "¿Esta seguro de continuar?")
                if rpta:
                    messagebox.showinfo("Pedido", f"Se elimino los campos del pedido")
                    self.actualizarTabla()
                    self.limpiar_entradas()
                else:
                    messagebox.showerror("Empleado", "Se eliminó los campos del empleado")

            else:
                messagebox.showerror("Error", "Hubo un problema al eliminar el pedido")


if __name__ == "__main__":
    gDatos = gestionDeDatosPedido()
    gDatos.mainloop()