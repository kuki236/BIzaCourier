import tkinter as tk
from tkinter import ttk, messagebox
import folium
import os
import webbrowser
from models.ticketEncomienda import obtener_latitud_longitud, read_ticket_encomienda
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DetallesPedido(tk.Tk):
    def __init__(self, nombre_pedido):
        super().__init__()
        self.title("Gestión de datos")
        self.geometry("800x700")
        self.config(bg="white")
        self.nombre_pedido = nombre_pedido

        # Inicialización de variables
        self.direccion_entrega = "Información no disponible"
        self.sucursal_origen = "Información no disponible"
        self.sucursal_destino = "Información no disponible"
        self.estado_transferencia = "Información no disponible"
        self.fecha_estimada_entrega = "Información no disponible"

        # Obtener datos y cargar widgets
        self.obtener_datos()
        self.agregar_widgets()

    def obtener_datos(self):
        try:
            datos = read_ticket_encomienda()

            if datos:
                for dato in datos:
                    if dato.get('nombre_pedido') == self.nombre_pedido:
                        self.direccion_entrega = dato.get('direccion_entrega', 'Información no disponible')
                        self.sucursal_origen = dato.get('nombre_sucursal_origen', 'Información no disponible')
                        self.sucursal_destino = dato.get('nombre_sucursal_destino', 'Información no disponible')
                        self.estado_transferencia = dato.get('estado_transferencia', 'Información no disponible')
                        self.fecha_estimada_entrega = dato.get('fecha_estimada_entrega', 'Información no disponible')
                        break
                else:
                    messagebox.showerror("Error", f"No se encontró un pedido con el nombre '{self.nombre_pedido}'.")
            else:
                messagebox.showerror("Error", "No se encontraron datos en la base de datos.")

        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener datos: {e}")

    def agregar_widgets(self):
        # Estilos
        # Aquí van los estilos -----------------------------------------
        estilo = ttk.Style()
        estilo.theme_use("clam")

        # Estilo para los Labels
        estilo.configure("TLabel", font=("Helvetica", 10), background="white", foreground="black")

        # Estilo para los Labels con títulos (resaltados)
        estilo.configure("Titulo.TLabel", font=("Helvetica", 10, "bold"), background="white", foreground="black")

        # Estilo para los Labels de encabezado principal
        estilo.configure("Encabezado.TLabel", font=("Helvetica", 16, "bold"), background="white", foreground="black")

        # Estilo para los Botones
        estilo.configure("TButton", font=("Helvetica", 12, "bold"), background="#d4f4ff", foreground="black")
        estilo.map("TButton",
                   background=[("active", "#a3d7ff"), ("pressed", "#8cbce0")],
                   foreground=[("disabled", "gray")])

        # Título de la ventana
        ttk.Label(self, text=f"Gestión de Encomienda: {self.nombre_pedido}", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Mostrar detalles del pedido
        self.mostrar_detalle("Dirección de entrega:", self.direccion_entrega, 1)
        self.mostrar_detalle("Sucursal de origen:", self.sucursal_origen, 2)
        self.mostrar_detalle("Sucursal de destino:", self.sucursal_destino, 3)
        self.mostrar_detalle("Estado de transferencia:", self.estado_transferencia, 4)
        self.mostrar_detalle("Fecha estimada de entrega:", self.fecha_estimada_entrega, 5)

        # Botón para ver en mapa
        ttk.Button(self, text="Ver en Mapa", command=self.mostrar_mapa).grid(row=6, column=0, columnspan=2, pady=20)

    def mostrar_detalle(self, titulo, detalle, fila):
        ttk.Label(self, text=titulo, font=("Helvetica", 10, "bold")).grid(row=fila, column=0, sticky="w", padx=10, pady=2)
        ttk.Label(self, text=detalle, wraplength=700).grid(row=fila, column=1, sticky="w", padx=10, pady=2)

    def mostrar_mapa(self):
        if not self.direccion_entrega or not self.sucursal_origen or not self.sucursal_destino:
            messagebox.showerror("Error", "No se han cargado todas las direcciones necesarias.")
            return

        try:
            # Crear el mapa
            m = folium.Map(location=[0, 0], zoom_start=13)

            # Coordenadas de entrega
            lat_entrega, lon_entrega = obtener_latitud_longitud(self.direccion_entrega)
            if lat_entrega and lon_entrega:
                folium.Marker(
                    location=[lat_entrega, lon_entrega],
                    popup=f"Dirección de entrega: {self.direccion_entrega}",
                    icon=folium.Icon(color="green")
                ).add_to(m)

            # Coordenadas de sucursal de origen
            lat_origen, lon_origen = obtener_latitud_longitud(self.sucursal_origen)
            if lat_origen and lon_origen:
                folium.Marker(
                    location=[lat_origen, lon_origen],
                    popup=f"Sucursal de origen: {self.sucursal_origen}",
                    icon=folium.Icon(color="blue")
                ).add_to(m)

            # Coordenadas de sucursal de destino
            lat_destino, lon_destino = obtener_latitud_longitud(self.sucursal_destino)
            if lat_destino and lon_destino:
                folium.Marker(
                    location=[lat_destino, lon_destino],
                    popup=f"Sucursal de destino: {self.sucursal_destino}",
                    icon=folium.Icon(color="red")
                ).add_to(m)

            # Guardar y abrir el mapa
            mapa_path = "mapa_encomienda.html"
            m.save(mapa_path)
            webbrowser.open(f'file://{os.path.abspath(mapa_path)}')

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al generar el mapa: {e}")


if __name__ == "__main__":
    nombre_pedido = input("Ingrese el nombre del pedido: ").strip()
    if nombre_pedido:
        app = DetallesPedido(nombre_pedido)
        app.mainloop()
    else:
        print("El nombre del pedido no puede estar vacío.")
