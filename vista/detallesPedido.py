import tkinter as tk
from tkinter import ttk, messagebox
import folium
from folium import IFrame
import os
import webbrowser
from models.ticketEncomienda import obtener_latitud_longitud, read_ticket_encomienda
from PIL import Image, ImageTk
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class gestionDeDatosCliente(tk.Tk):
    def __init__(self, nombre_pedido):
        super().__init__()
        self.title("Gestión de datos")
        self.geometry("800x700")
        self.centrar_ventana()
        self.config(bg="white")
        self.nombre_pedido = nombre_pedido
        self.direccion_entrega = None
        self.sucursal_destino = None
        self.nombre_cliente = None
        self.nombre_empleado = None
        self.obtener_datos()
        self.agregar_widgets()

    def obtener_datos(self):
        # Obtener datos de la base de datos usando las funciones de `ticketEncomienda`
        datos = read_ticket_encomienda()
        for dato in datos:
            if dato['nombre_pedido'] == self.nombre_pedido:
                self.direccion_entrega = dato['direccion_entrega']
                self.sucursal_destino = dato['nombre_sucursal_destino']
                self.nombre_cliente = dato['nombre_cliente']
                self.nombre_empleado = dato['nombre_empleado']
                break

    def agregar_widgets(self):
        # Título de la ventana
        title_label = ttk.Label(self, text=f"Gestión de Encomienda para: {self.nombre_pedido}", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Mostrar la dirección de entrega y la sucursal de destino
        ttk.Label(self, text="Dirección de entrega:").pack(pady=5)
        ttk.Label(self, text=self.direccion_entrega, wraplength=700).pack(pady=5)

        ttk.Label(self, text="Sucursal de destino:").pack(pady=5)
        ttk.Label(self, text=self.sucursal_destino, wraplength=700).pack(pady=5)

        # Botón para ver el mapa
        ver_mapa_btn = ttk.Button(self, text="Ver en Mapa", command=self.mostrar_mapa)
        ver_mapa_btn.pack(pady=10)

    def mostrar_mapa(self):
        # Crear un mapa de folium centrado en la dirección de entrega y la dirección de la sucursal de destino
        if not self.direccion_entrega or not self.sucursal_destino:
            messagebox.showerror("Error", "No se han cargado las direcciones necesarias.")
            return

        # Crear el mapa
        m = folium.Map(location=[0, 0], zoom_start=13)

        # Agregar marcador para la dirección de entrega
        lat_entrega, lon_entrega = obtener_latitud_longitud(self.direccion_entrega)
        if lat_entrega and lon_entrega:
            folium.Marker(
                location=[lat_entrega, lon_entrega],
                popup=f"Dirección de entrega: {self.direccion_entrega}",
                icon=folium.Icon(color="green")
            ).add_to(m)

        # Agregar marcador para la sucursal de destino
        lat_sucursal, lon_sucursal = obtener_latitud_longitud(self.sucursal_destino)
        if lat_sucursal and lon_sucursal:
            folium.Marker(
                location=[lat_sucursal, lon_sucursal],
                popup=f"Sucursal de destino: {self.sucursal_destino}",
                icon=folium.Icon(color="blue")
            ).add_to(m)

        # Guardar el mapa en un archivo temporal y abrirlo en el navegador
        mapa_path = "mapa_encomienda.html"
        m.save(mapa_path)
        webbrowser.open(f'file://{os.path.abspath(mapa_path)}')

    def centrar_ventana(self):
        ventana_ancho = self.winfo_width()
        ventana_alto = self.winfo_height()
        pantalla_ancho = self.winfo_screenwidth()
        pantalla_alto = self.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ventana_ancho // 2)
        y = (pantalla_alto // 2) - (ventana_alto // 2)
        self.geometry(f'{ventana_ancho}x{ventana_alto}+{x}+{y}')

if __name__ == "__main__":
    nombre_pedido = "9BKP0TFZJCZ2"
    app = gestionDeDatosCliente(nombre_pedido)
    app.mainloop()
