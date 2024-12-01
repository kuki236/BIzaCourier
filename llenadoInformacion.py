from models.Pedido import create_pedido
from models.Cliente import  create_cliente
from models.ticketEncomienda import create_ticket_encomienda
from models.Empleado import create_empleado
from models.Sucursal import  create_sucursal

import random

def insertar_datos_ejemplo():
    # Lista de nombres y apellidos reales
    nombres_clientes = ["Carlos", "María", "Juan", "Lucía", "Pedro"]
    apellidos_clientes = ["Pérez", "Gómez", "Fernández", "Martínez", "Rodríguez"]
    nombres_empleados = ["Sofía", "Andrés", "Valeria", "Luis", "Gabriel"]
    apellidos_empleados = ["Torres", "Ramírez", "Díaz", "Castillo", "Rojas"]

    # Insertar ejemplos en la tabla Cliente
    for i in range(5):
        create_cliente(
            nombre_cliente=nombres_clientes[i],
            apellido_cliente=apellidos_clientes[i],
            telefono=f"999555{i:03}"
        )

    # Insertar ejemplos en la tabla Empleado
    for i in range(5):
        create_empleado(
            nombre=nombres_empleados[i],
            apellido=apellidos_empleados[i],
            cargo="Empleado" if i % 2 == 0 else "Gerente",
            username=f"user{i}",
            contrasena=f"password{i}"
        )

    # Insertar ejemplos en la tabla Sucursal
    for i in range(1, 6):
        create_sucursal(
            nombre_sucursal=f"Sucursal {i}",
            direccion=f"Avenida Principal {i} Nro. {i * 10}",
            codigo_postal=15000 + i,
            horario_apertura="08:00",
            horario_cierre="18:00"
        )

    # Insertar ejemplos en la tabla Pedido
    for i in range(1, 6):
        create_pedido(
            idPedido=i,
            direccion_entrega=f"Avenida Secundaria {i} Mz {chr(65 + i)}",
            codigo_postal_entrega=15050 + i,
            idCliente=random.randint(1, 5),  # Cliente aleatorio
            created_by=random.randint(1, 5)  # Empleado aleatorio
        )

    # Insertar ejemplos en la tabla TicketEncomienda
    for i in range(1, 6):
        create_ticket_encomienda(
            idSucursalOrigen=random.randint(1, 5),
            idSucursalDestino=random.randint(1, 5),
            idPedido=i,
            fecha_recepcion=None,  # Siempre None
            fecha_estimada_entrega=None  # Siempre None
        )

    print("Datos de ejemplo insertados correctamente.")
insertar_datos_ejemplo()