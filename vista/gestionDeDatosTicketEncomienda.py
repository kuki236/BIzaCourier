import tkinter as tk
from tkinter import ttk, messagebox
from models.ticketEncomienda import read_ticket_encomienda, create_ticket_encomienda, update_ticket_encomienda, \
    delete_ticket_encomienda, get_sucursales


# Función para mostrar los registros en la tabla
def actualizar_tabla():
    for row in tree.get_children():
        tree.delete(row)

    registros = read_ticket_encomienda()
    for registro in registros:
        tree.insert('', 'end',
                    values=(registro['idTicketEncomienda'], registro['estado_transferencia'], registro['fecha_inicio'],
                            registro['fecha_recepcion'], registro['fecha_estimada_entrega'],
                            registro['nombre_sucursal_origen'],
                            registro['nombre_sucursal_destino'], registro['nombre_pedido'],
                            registro['direccion_entrega']))


# Función para capturar datos de la fila seleccionada y ponerlos en los inputs
def seleccionar_fila(event):
    seleccionado = tree.selection()
    if not seleccionado:
        return

    item = tree.item(seleccionado)
    datos = item['values']

    entry_id.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_fecha_recepcion.delete(0, tk.END)
    entry_fecha_estimada.delete(0, tk.END)

    entry_id.insert(0, datos[0])
    entry_estado.insert(0, datos[1])
    entry_fecha_recepcion.insert(0, datos[3])
    entry_fecha_estimada.insert(0, datos[4])

    # Seleccionar las sucursales en los Combobox
    combobox_sucursal_origen.set(datos[5])
    combobox_sucursal_destino.set(datos[6])


# Función para crear un nuevo ticket de encomienda
def crear_ticket():
    estado = entry_estado.get()
    fecha_recepcion = entry_fecha_recepcion.get()
    fecha_estimada = entry_fecha_estimada.get()
    sucursal_origen = combobox_sucursal_origen.get()
    sucursal_destino = combobox_sucursal_destino.get()

    if estado and fecha_recepcion and fecha_estimada and sucursal_origen and sucursal_destino:
        try:
            # Llamar a la función para crear el ticket de encomienda
            create_ticket_encomienda(estado_transferencia=estado, idSucursalOrigen=sucursal_origen,
                                     fecha_recepcion=fecha_recepcion,
                                     fecha_estimada_entrega=fecha_estimada, idSucursalDestino=sucursal_destino)
            messagebox.showinfo("Éxito", "Ticket creado correctamente")
            actualizar_tabla()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el ticket: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")


# Función para actualizar un ticket de encomienda
def actualizar_ticket():
    ticket_id = entry_id.get()
    estado = entry_estado.get()
    fecha_recepcion = entry_fecha_recepcion.get()
    fecha_estimada = entry_fecha_estimada.get()
    sucursal_origen = combobox_sucursal_origen.get()
    sucursal_destino = combobox_sucursal_destino.get()

    if ticket_id and (estado or fecha_recepcion or fecha_estimada or sucursal_origen or sucursal_destino):
        try:
            # Llamar a la función para actualizar el ticket de encomienda
            update_ticket_encomienda(ticket_id, estado_transferencia=estado, fecha_recepcion=fecha_recepcion,
                                     fecha_estimada_entrega=fecha_estimada, idSucursalOrigen=sucursal_origen,
                                     idSucursalDestino=sucursal_destino)
            messagebox.showinfo("Éxito", "Ticket actualizado correctamente")
            actualizar_tabla()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el ticket: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete el ID y al menos un campo a actualizar")


# Función para eliminar un ticket de encomienda
def eliminar_ticket():
    ticket_id = entry_id.get()

    if ticket_id:
        try:
            delete_ticket_encomienda(ticket_id)
            messagebox.showinfo("Éxito", "Ticket eliminado correctamente")
            actualizar_tabla()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el ticket: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese el ID del ticket a eliminar")


# Función para obtener la lista de sucursales
def cargar_sucursales():
    sucursales = get_sucursales()
    return [sucursal[1] for sucursal in sucursales]  # Retorna solo los nombres de las sucursales


# Crear la ventana principal
root = tk.Tk()
root.title("CRUD de Tickets de Encomienda")
root.geometry("1000x600")

# Frame para los inputs y botones
frame_inputs = tk.Frame(root)
frame_inputs.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

# Labels y Entradas
tk.Label(frame_inputs, text="ID Ticket").grid(row=0, column=0, sticky="w")
entry_id = tk.Entry(frame_inputs)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Estado de Transferencia").grid(row=1, column=0, sticky="w")
entry_estado = tk.Entry(frame_inputs)
entry_estado.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Fecha de Recepción").grid(row=2, column=0, sticky="w")
entry_fecha_recepcion = tk.Entry(frame_inputs)
entry_fecha_recepcion.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Fecha Estimada de Entrega").grid(row=3, column=0, sticky="w")
entry_fecha_estimada = tk.Entry(frame_inputs)
entry_fecha_estimada.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Sucursal de Origen").grid(row=4, column=0, sticky="w")
combobox_sucursal_origen = ttk.Combobox(frame_inputs, values=cargar_sucursales())
combobox_sucursal_origen.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Sucursal de Destino").grid(row=5, column=0, sticky="w")
combobox_sucursal_destino = ttk.Combobox(frame_inputs, values=cargar_sucursales())
combobox_sucursal_destino.grid(row=5, column=1, padx=5, pady=5)

# Botones
tk.Button(frame_inputs, text="Crear", command=crear_ticket).grid(row=6, column=0, pady=5)
tk.Button(frame_inputs, text="Actualizar", command=actualizar_ticket).grid(row=6, column=1, pady=5)
tk.Button(frame_inputs, text="Eliminar", command=eliminar_ticket).grid(row=6, column=2, pady=5)

# Treeview para mostrar los tickets de encomienda
tree = ttk.Treeview(root, columns=(
"ID", "Estado", "Fecha Inicio", "Fecha Recepción", "Fecha Estimada", "Sucursal Origen", "Sucursal Destino",
"Nombre Pedido", "Dirección Entrega"), show="headings")
tree.heading("ID", text="ID Ticket")
tree.heading("Estado", text="Estado Transferencia")
tree.heading("Fecha Inicio", text="Fecha Inicio")
tree.heading("Fecha Recepción", text="Fecha Recepción")
tree.heading("Fecha Estimada", text="Fecha Estimada")
tree.heading("Sucursal Origen", text="Sucursal Origen")
tree.heading("Sucursal Destino", text="Sucursal Destino")
tree.heading("Nombre Pedido", text="Nombre Pedido")
tree.heading("Dirección Entrega", text="Dirección Entrega")

tree.column("ID", width=60)
tree.column("Estado", width=120)
tree.column("Fecha Inicio", width=100)
tree.column("Fecha Recepción", width=100)
tree.column("Fecha Estimada", width=120)
tree.column("Sucursal Origen", width=100)
tree.column("Sucursal Destino", width=100)
tree.column("Nombre Pedido", width=150)
tree.column("Dirección Entrega", width=200)

tree.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
tree.bind("<ButtonRelease-1>", seleccionar_fila)

# Cargar la tabla al inicio
actualizar_tabla()

# Iniciar la aplicación
root.mainloop()
