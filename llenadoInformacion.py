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
# Crear sucursales con direcciones reales en Perú
    create_sucursal(
        nombre_sucursal="Sucursal Lima",
        direccion="Avenida Javier Prado Este 1234, San Isidro, Lima, Perú",
        codigo_postal= 15046,
        horario_apertura="08:00",
        horario_cierre="18:00"
    )

    create_sucursal(
        nombre_sucursal="Sucursal Arequipa",
        direccion="Calle Mercaderes 207, Arequipa, Arequipa, Perú",
        codigo_postal= 40012,
        horario_apertura="08:00",
        horario_cierre="18:00"
    )

    create_sucursal(
        nombre_sucursal="Sucursal Cusco",
        direccion="Avenida El Sol 1010, Cusco, Cusco, Perú",
        codigo_postal= 80025,
        horario_apertura="08:00",
        horario_cierre="18:00"
    )

    create_sucursal(
        nombre_sucursal="Sucursal Piura",
        direccion="Avenida Sánchez Cerro 345, Piura, Piura, Perú",
        codigo_postal= 20001,
        horario_apertura="08:00",
        horario_cierre="18:00"
    )

    # Insertar ejemplos en la tabla Pedido
    # Crear pedidos con direcciones de entrega reales y cercanas a las sucursales
    create_pedido(
        idPedido=1,
        direccion_entrega="Calle Las Begonias 345, San Isidro, Lima, Perú",  # Cerca de Sucursal Lima
        codigo_postal_entrega=15046,
        idCliente=random.randint(1, 5),  # Cliente aleatorio
        created_by=random.randint(1, 5)  # Empleado aleatorio
    )

    create_pedido(
        idPedido=2,
        direccion_entrega="Calle San Francisco 512, Cercado, Arequipa, Perú",  # Cerca de Sucursal Arequipa
        codigo_postal_entrega=40011,
        idCliente=random.randint(1, 5),
        created_by=random.randint(1, 5)
    )

    create_pedido(
        idPedido=3,
        direccion_entrega="Av. Cusco, Cusco Peru",  # Cerca de Sucursal Cusco
        codigo_postal_entrega= 80021,
        idCliente=random.randint(1, 5),
        created_by=random.randint(1, 5)
    )

    create_pedido(
        idPedido=4,
        direccion_entrega="Av. Sánchez Cerro, Piura 20001",  # Cerca de Sucursal Piura
        codigo_postal_entrega=20001,
        idCliente=random.randint(1, 5),
        created_by=random.randint(1, 5)
    )

    create_pedido(
        idPedido=5,
        direccion_entrega="Avenida República de Panamá 1650, Surquillo, Lima, Perú",  # Cerca de Sucursal Lima
        codigo_postal_entrega= 15047,
        idCliente=random.randint(1, 5),
        created_by=random.randint(1, 5)
    )

    # Insertar ejemplos en la tabla TicketEncomienda
    for i in range(1, 6):
        create_ticket_encomienda(
            idSucursalOrigen=random.randint(1, 5),
            idPedido=i,
            fecha_recepcion=None,  # Siempre None
            fecha_estimada_entrega=None  # Siempre None
        )

    print("Datos de ejemplo insertados correctamente.")
insertar_datos_ejemplo()