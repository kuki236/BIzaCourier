import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import sys
sys.path.append('C:\\Users\\Usuario\\Desktop\\yo\\BIzaCourier')


class GestionDeDatosSucursalEmpleado(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Sucursal y Empleado")
        self.geometry("1000x600")
        self.centrar_ventana()
        self.config(bg="white")
        self.agregar_widgets()

    def agregar_widgets(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("frame1.TFrame", background="#5286ee")

        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=1)
        for i in range(2):
            self.columnconfigure(i, weight=1)

        # Frame 1: Título
        self.Frame1 = ttk.Frame(self, style="frame1.TFrame")
        self.Frame1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.Frame1.rowconfigure(0, weight=1)
        self.Frame1.columnconfigure(0, weight=1)
        
        self.lblTitulo = ttk.Label(self.Frame1, text="Gestión de Sucursales y Empleados", anchor="center")
        self.lblTitulo.grid(row=0, column=0, sticky="nsew", pady=5)
        self.lblSubTitulo = ttk.Label(self.Frame1, text="Administra asignaciones fácilmente", anchor="center")
        self.lblSubTitulo.grid(row=1, column=0, sticky="nsew", pady=5)

        # Frame 2: Entrada de datos
        self.Frame2 = ttk.Frame(self)
        self.Frame2.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        for i in range(11):
            self.Frame2.rowconfigure(i, weight=1)
        for i in range(3):
            self.Frame2.columnconfigure(i, weight=1)

        self.lblDatos = ttk.Label(self.Frame2, text="Datos")
        self.lblDatos.grid(row=0, column=0, sticky="w")
        
        self.lblEmpleadoID = ttk.Label(self.Frame2, text="ID Empleado:")
        self.lblEmpleadoID.grid(row=1, column=0, sticky="w")
        self.entradaEmpleadoID = ttk.Entry(self.Frame2, width=50)
        self.entradaEmpleadoID.grid(row=2, column=0, columnspan=3, sticky="w")

        self.lblSucursalID = ttk.Label(self.Frame2, text="ID Sucursal:")
        self.lblSucursalID.grid(row=3, column=0, sticky="w")
        self.entradaSucursalID = ttk.Entry(self.Frame2, width=50)
        self.entradaSucursalID.grid(row=4, column=0, columnspan=3, sticky="w")

        # Botones
        self.botonAsignar = ttk.Button(self.Frame2, text="Asignar", command=self.asignar_empleado)
        self.botonAsignar.grid(row=10, column=0)
        self.botonActualizar = ttk.Button(self.Frame2, text="Actualizar", command=self.actualizar_asignacion)
        self.botonActualizar.grid(row=10, column=1)
        self.botonEliminar = ttk.Button(self.Frame2, text="Eliminar", command=self.eliminar_asignacion)
        self.botonEliminar.grid(row=10, column=2)

        # Frame 3: Tabla
        self.Frame3 = ttk.Frame(self)
        self.Frame3.grid(row=1, column=1, sticky="nsew", padx=10)
        self.Frame3.rowconfigure(0, weight=1)
        self.Frame3.rowconfigure(1, weight=3)
        self.Frame3.columnconfigure(0, weight=1)

        self.lblRegistros = ttk.Label(self.Frame3, text="Registros")
        self.lblRegistros.grid(row=0, column=0, sticky="w", padx=5)

        columnas_tabla = ("Nombre Empleado", "Nombre Sucursal")
        self.tabla = ttk.Treeview(self.Frame3, columns=columnas_tabla, show="headings")
        self.tabla.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Configura los encabezados de las columnas de la tabla.
        for item_columna in columnas_tabla:
            self.tabla.heading(item_columna, text=item_columna)

        # Ajusta las columnas de la tabla para que se vean de manera adecuada.
        self.tabla.column("Nombre Empleado", width=200, anchor="center")
        self.tabla.column("Nombre Sucursal", width=200, anchor="center")

        self.cargar_tabla()
        self.tabla.bind("<ButtonRelease-1>", self.obtener_fila_seleccionada)

    def centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

# Modifica la función cargar_tabla para que pase los datos correctamente.
    def cargar_tabla(self):
        from models.SucursalEmpleado import read_asignaciones
        self.datos_asignaciones = read_asignaciones()
        for nombre_empleado, nombre_sucursal in self.datos_asignaciones:
            self.tabla.insert("", "end", values=(nombre_empleado, nombre_sucursal))

    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        self.cargar_tabla()

    def obtener_fila_seleccionada(self, event):
        seleccion = self.tabla.focus()
        if seleccion:
            valores = self.tabla.item(seleccion, "values")
            self.limpiar_entradas()
            self.entradaEmpleadoID.insert(0, valores[0])
            self.entradaSucursalID.insert(0, valores[1])

    def limpiar_entradas(self):
        self.entradaEmpleadoID.delete(0, tk.END)
        self.entradaSucursalID.delete(0, tk.END)

    def asignar_empleado(self):
        from models.SucursalEmpleado import asignar_empleado_a_sucursal
        empleado_id = self.entradaEmpleadoID.get()
        sucursal_id = self.entradaSucursalID.get()
        if empleado_id and sucursal_id:
            asignar_empleado_a_sucursal(empleado_id, sucursal_id)
            messagebox.showinfo("Asignación", "Empleado asignado correctamente")
            self.actualizar_tabla()
            self.limpiar_entradas()
        else:
            messagebox.showerror("Error", "Complete todos los campos")

    def actualizar_asignacion(self):
        from models.SucursalEmpleado import update_asignacion
        seleccion = self.tabla.focus()
        if seleccion:
            valores = self.tabla.item(seleccion, "values")
            empleado_id_anterior = valores[0]
            sucursal_id_anterior = valores[1]
            empleado_id = self.entradaEmpleadoID.get()
            sucursal_id = self.entradaSucursalID.get()
            if empleado_id and sucursal_id:
                update_asignacion(empleado_id_anterior, sucursal_id_anterior, empleado_id, sucursal_id)
                messagebox.showinfo("Asignación", "Asignación actualizada correctamente")
                self.actualizar_tabla()
                self.limpiar_entradas()
            else:
                messagebox.showerror("Error", "Complete todos los campos")

    def eliminar_asignacion(self):
        from models.SucursalEmpleado import delete_asignacion
        seleccion = self.tabla.focus()
        if seleccion:
            valores = self.tabla.item(seleccion, "values")
            empleado_id = valores[0]
            sucursal_id = valores[1]
            if empleado_id and sucursal_id:
                respuesta = messagebox.askyesno("Confirmar", "¿Desea eliminar esta asignación?")
                if respuesta:
                    delete_asignacion(empleado_id, sucursal_id)
                    messagebox.showinfo("Asignación", "Asignación eliminada correctamente")
                    self.actualizar_tabla()
                    self.limpiar_entradas()

if __name__ == "__main__":
    app = GestionDeDatosSucursalEmpleado()
    app.mainloop()
