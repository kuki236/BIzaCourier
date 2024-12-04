import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Cliente
class gestionDeDatosCliente(tk.Tk):
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


        self.lblTitulo = ttk.Label(self.Frame1, text="Gestion de datos del Cliente", anchor="center")
        self.lblTitulo.grid(row=0,column=0, sticky="nsew", pady=5)
        self.lblSubTitulo = ttk.Label(self.Frame1, text="Administra tu información facilmente", anchor="center")
        self.lblSubTitulo.grid(row=1,column=0, sticky="nsew",pady=5)

        # Creacion del frame2 (para el ingreso de datos)
        self.Frame2 = ttk.Frame(self)
        self.Frame2.grid(row=1,column=0,sticky="nsew", padx=5,pady=5)

        # 11 filas y 3 columnas
        for i in range(0,11):
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

        self.lblTelefono = ttk.Label(self.Frame2, text="Telefono:")
        self.lblTelefono.grid(row=5, column=0, sticky="w")
        self.entradaTelefono = ttk.Entry(self.Frame2, width=50)
        self.entradaTelefono.grid(row=6, column=0, columnspan=3, sticky="w")



        # Creacion de botones
        self.botonCrear = ttk.Button(self.Frame2, text="Crear", command=self.crearEmpleado)
        self.botonCrear.grid(row=10,column=0)
        self.botonActualizar = ttk.Button(self.Frame2, text= "Actualizar",command=self.actualizarEmpleado)
        self.botonActualizar.grid(row=10, column=1)
        self.botonEliminar = ttk.Button(self.Frame2, text="Eliminar", command=self.eliminarEmpleado)
        self.botonEliminar.grid(row=10,column=2)


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
        columnas_tabla = ("ID", "Nombre", "Apellido", "Telefono")
        self.tabla = ttk.Treeview(self.Frame3, columns=columnas_tabla, show="headings")
        self.tabla.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")

        # Configuración de las columnas de la tabla
        for item_columna in columnas_tabla:
            self.tabla.heading(item_columna, text=item_columna)

        # Configuración del ancho de las columnas
        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Nombre", width=150, anchor="w")
        self.tabla.column("Apellido", width=100, anchor="w")
        self.tabla.column("Telefono", width=100, anchor="w")

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
        from models.Cliente import read_clientes
        self.datos_clientes = read_clientes()
        for ide,nombre,apellido,telefono in self.datos_clientes:
            self.tabla.insert("", "end", values=(ide, nombre, apellido, telefono))

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
            self.entradaNombre.insert(0, valores[1])  # Nombre
            self.entradaApellido.insert(0, valores[2])  # Apellido
            self.entradaTelefono.insert(0, valores[3]) # telefono


    def limpiar_entradas(self):
        self.entradaNombre.delete(0, tk.END)
        self.entradaApellido.delete(0, tk.END)
        self.entradaTelefono.delete(0, tk.END)

    def crearEmpleado(self):
        from models.Cliente import create_cliente
        nombre = self.entradaNombre.get()
        apellido = self.entradaApellido.get()
        telefono = self.entradaTelefono.get()
        if nombre and apellido and telefono:
            create_cliente(nombre, apellido,telefono)
            messagebox.showinfo("Cliente", f"El cliente {nombre} {apellido} se agregó correctamente")
            self.actualizarTabla()
            self.limpiar_entradas()
        else:
            messagebox.showerror("Error", "Hubo un problema al agregar cliente")
    def actualizarEmpleado(self):
        from models.Cliente import update_cliente
        seleccion = self.tabla.focus()  # Obtiene la clave del elemento seleccionado
        if seleccion:
            valores = self.tabla.item(seleccion, "values")
            ide = valores[0]
            nombre = self.entradaNombre.get()
            apellido = self.entradaApellido.get()
            telefono = self.entradaTelefono.get()
            if nombre and apellido and telefono:
                update_cliente(ide, nombre, apellido, telefono)
                messagebox.showinfo("Cliente", f"Se actualizó los campos del cliente")
                self.actualizarTabla()
                self.limpiar_entradas()
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar cliente")




    def eliminarEmpleado(self):
        from models.Cliente import delete_cliente
        seleccion = self.tabla.focus()  # Obtiene la clave del elemento seleccionado
        if seleccion:
            valores = self.tabla.item(seleccion, "values")
            ide = valores[0]

            if ide:
                delete_cliente(ide)
                rpta = messagebox.askyesno("Aviso", "¿Esta seguro de continuar?")
                if rpta:
                    messagebox.showinfo("Cliente", f"Se eliminó los campos del cliente correctamente")
                    self.actualizarTabla()
                    self.limpiar_entradas()
                else:
                    return

            else:
                messagebox.showerror("Error", "Hubo un problema al eliminar cliente")


if __name__ == "__main__":
    gDatos = gestionDeDatosCliente()
    gDatos.mainloop()