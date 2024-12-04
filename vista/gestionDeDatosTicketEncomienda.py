import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Gestion de datos pedido
class gestionDeDatosTicketEncomienda(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de datos Pedido")
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


        self.lblTitulo = ttk.Label(self.Frame1, text="Gestion de datos del Pedido", anchor="center")
        self.lblTitulo.grid(row=0,column=0, sticky="nsew", pady=5)
        self.lblSubTitulo = ttk.Label(self.Frame1, text="Administra tu información facilmente", anchor="center")
        self.lblSubTitulo.grid(row=1,column=0, sticky="nsew",pady=5)

        # Creacion del frame2 (para el ingreso de datos)
        self.Frame2 = ttk.Frame(self)
        self.Frame2.grid(row=1,column=0,sticky="nsew", padx=5,pady=5)

        # 12 filas y 3 columnas
        for i in range(0,12):
            self.Frame2.rowconfigure(i, weight=1)
        for i in range(0,3):
            self.Frame2.columnconfigure(i,weight=1)


        self.lblDatos = ttk.Label(self.Frame2, text= "Datos")
        self.lblDatos.grid(row=0,column=0, sticky="w")
        self.lblEstado = ttk.Label(self.Frame2, text="Estado de transferencia:")
        self.lblEstado.grid(row=1, column=0, sticky="w")
        opciones = ["Creado", "En camino", "Llegó al destino"]
        self.comboEstado = ttk.Combobox(self.Frame2, values=opciones, state="readonly")
        self.comboEstado.set(opciones[1])
        self.comboEstado.grid(row=2, column=1)
        self.lblFechaIn = ttk.Label(self.Frame2, text="Fecha inicio:")
        self.lblFechaIn.grid(row=3, column=0, sticky="w")
        self.entradaFechaIn = ttk.Entry(self.Frame2, width=50)
        self.entradaFechaIn.grid(row=4, column=0, columnspan=3, sticky="w")
        self.lblCargo = ttk.Label(self.Frame2, text="Fecha recepcion:")
        self.lblCargo.grid(row=5, column=0, sticky="w")
        self.entradaFechaRe = ttk.Entry(self.Frame2, width=50)
        self.entradaFechaRe.grid(row=6, column=0, columnspan=3, sticky="w")


        self.lblSucOri = ttk.Label(self.Frame2, text="Id sucursal de origen:")
        self.lblSucOri.grid(row=7, column=0, sticky="w", columnspan=3)
        self.entradaSucOri = ttk.Entry(self.Frame2, width=50)
        self.entradaSucOri.grid(row=8, column=0, columnspan=3, sticky="w")

        self.lblIdPedido = ttk.Label(self.Frame2, text="Id del pedido:")
        self.lblIdPedido.grid(row=9, column=0, sticky="w", columnspan=3)
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
        columnas_tabla = ("ID_ticket_encomienda", "Estado", "Fecha_inicio", "Fecha_recepcion", "Fecha_estimada", "id_sucursal_origen", "id_pedido")
        self.tabla = ttk.Treeview(self.Frame3, columns=columnas_tabla, show="headings")
        self.tabla.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")

        # Configuración de las columnas de la tabla
        for item_columna in columnas_tabla:
            self.tabla.heading(item_columna, text=item_columna)

        # Configuración del ancho de las columnas
        self.tabla.column("ID_ticket_encomienda", width=50, anchor="center")
        self.tabla.column("Estado", width=150, anchor="w")
        self.tabla.column("Fecha_inicio", width=100, anchor="w")
        self.tabla.column("Fecha_recepcion", width=100, anchor="w")
        self.tabla.column("Fecha_estimada", width=100, anchor="w")
        self.tabla.column("id_sucursal_origen", width=100, anchor="w")
        self.tabla.column("id_pedido", width=100, anchor="w")

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
        from models.ticketEncomienda import read_ticket_encomienda
        self.datos_ticket = read_ticket_encomienda()
        print(self.datos_ticket)
        for ide,estado, fechaIn, fechaRe, fechaEsEn, idOrig, idDesti, idPedido in self.datos_ticket:
            self.tabla.insert("", "end", values=(ide, estado, fechaIn, fechaRe, fechaEsEn, idOrig, idDesti, idPedido))

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
            self.comboEstado.insert(0, valores[1])  # Nombre
            self.entradaFechaIn.insert(0, valores[2])
            self.entradaFechaRe.insert(0,valores[3])
            self.entradaSucOri.insert(0, valores[5])
            self.entradaIdPedido.insert((0, valores[6]))




    def limpiar_entradas(self):
        self.comboEstado.set("")
        self.entradaFechaRe.delete(0, tk.END)
        self.entradaFechaIn.delete(0, tk.END)
        self.entradaSucOri.delete(0, tk.END)
        self.entradaIdPedido.delete(0, tk.END)









    # COMPLETAR DESDE AQUI
    def crearEmpleado(self):
        from models.ticketEncomienda import create_ticket_encomienda
        estado = self.comboEstado.get()
        fechaIn = self.entradaFechaIn.get()
        fechaRe = self.entradaFechaRe.get()
        sucOrigin = self.entradaSucOri.get()
        idPedido = self.entradaIdPedido.get()

        if estado and fechaIn and fechaRe and sucOrigin and idPedido:
            create_ticket_encomienda(estado, sucOrigin, idPedido, fechaRe)
            messagebox.showinfo("Ticket encomienda", f"Se creó correctamente el ticket")
            self.actualizarTabla()
            self.limpiar_entradas()
        else:
            messagebox.showerror("Error", "Hubo un problema al crear ticket de encomienda")
    def actualizarEmpleado(self):
        from models.ticketEncomienda import update_ticket_encomienda
        seleccion = self.tabla.focus()  # Obtiene la clave del elemento seleccionado
        if seleccion:
            valores = self.tabla.item(seleccion, "values")
            ide = valores[0]
            estado = self.comboEstado.get()
            fechaRe = self.entradaFechaRe.get()

            if ide and estado and fechaRe:
                update_ticket_encomienda(ide, estado, fechaRe)
                messagebox.showinfo("Ticket encomienda", f"Se actualizo los campos de ticket encomienda")
                self.actualizarTabla()
                self.limpiar_entradas()
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar el ticket")




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
                    messagebox.showinfo("Empleado", f"Se elimino los campos del ticket")
                    self.actualizarTabla()
                    self.limpiar_entradas()
                else:
                    return

            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar empleado")


if __name__ == "__main__":
    gDatos = gestionDeDatosTicketEncomienda()
    gDatos.mainloop()
