from models.Pedido import read_pedidos, create_pedido, update_pedido, delete_pedido
from models.Cliente import read_clientes, create_cliente, update_cliente, delete_cliente
from models.TransferenciaPedido import transferir_pedido
from models.Empleado import read_empleados, create_empleado, update_empleado, delete_empleado
from models.Sucursal import read_sucursal, create_sucursal, update_sucursal, delete_sucursal

def insertar_datos_ejemplo1():
    # Insertar 5 empleados de ejemplo
 
    empleados_ejemplo = [
        {"nombre": "Juan Perez", "cargo": "Gerente", "username": "jperez","contraseña":"jperez+1234"},
        {"nombre": "Ana Gómez", "cargo": "Gerente", "username": "agomez","contraseña":"agomez+1234"},
        {"nombre": "Carlos Díaz", "cargo": "Empleado", "username": "cdiaz","contraseña":"jcdiaz+1234"},
        {"nombre": "Luisa Tama", "cargo": "Empleado", "username": "ltama","contraseña":"ltama+1234"},
        {"nombre": "Pedro Martínez", "cargo": "Empleado", "username": "pmartinez","contraseña":"pmartinez+1234"},
    ]
    for empleado in empleados_ejemplo:
        create_empleado(empleado["nombre"], empleado["cargo"], empleado["username"], empleado["contraseña"])
    
    # Insertar 5 clientes de ejemplo
    clientes_ejemplo = [
        {"nombre": "Pedro ", "telefono": "123456789", "apellido": "López"},
        {"nombre": "Maria ", "telefono": "987654321", "apellido": "Castillo"},
        {"nombre": "Luis ", "telefono": "112233445", "apellido": "Ramírez"},
        {"nombre": "Sofía ", "telefono": "667788990", "apellido": "Torres"},
        {"nombre": "Jorge ", "telefono": "223344556", "apellido": "Sánchez"},
    ]
    for cliente in clientes_ejemplo:
        create_cliente(cliente["nombre"], cliente["apellido"], cliente ["telefono"])
   
 # Insertar 5 sucursales de ejemplo
    sucursales_ejemplo = [
            {"nombre_Sucursal": "Sucursal Centro", "direccion": "Calle Mayor 123", "horario_apertura": "08:00", "horario_cierre": "18:00"},
            {"nombre_Sucursal": "Sucursal Norte", "direccion": "Avenida del Sol 456", "horario_apertura": "09:00", "horario_cierre": "17:00"},
            {"nombre_Sucursal": "Sucursal Sur", "direccion": "Calle Luna 789", "horario_apertura": "10:00", "horario_cierre": "19:00"},
            {"nombre_Sucursal": "Sucursal Este", "direccion": "Boulevard de la Paz 101", "horario_apertura": "07:30", "horario_cierre": "16:30"},
            {"nombre_Sucursal": "Sucursal Oeste", "direccion": "Calle de la Esperanza 202", "horario_apertura": "08:30", "horario_cierre": "20:00"}
    ]
    for sucursal in sucursales_ejemplo:
        create_sucursal(sucursal["nombre_Sucursal"], sucursal["direccion"], sucursal["horario_apertura"], sucursal["horario_cierre"])
    
def insertar_datos_ejemplo2():
       # Insertar 5 pedidos de ejemplo
         pedidos_ejemplo = [
        {"direccion_entrega": "av san juan","estado": "En preparación","fecha estimada entrega": "2025-03-12","idSOrigen":1,"idCliente":1,"created_by":1},
        {"direccion_entrega": "calle 45, sector 3", "estado": "En preparación", "fecha estimada entrega": "2025-03-15",  "idSOrigen": 2, "idCliente": 2,"created_by":2},
        {"direccion_entrega": "av principal, bloque 7", "estado": "En preparación", "fecha estimada entrega": "2025-03-20", "idSOrigen": 3, "idCliente": 3,"created_by":3},
         {"direccion_entrega": "av central, zona 5", "estado": "En preparación", "fecha estimada entrega": "2024-05-28", "idSOrigen": 5, "idCliente": 4,"created_by":4},
        {"direccion_entrega": "av central, zona 5", "estado": "En preparación", "fecha estimada entrega": "2024-05-28", "idSOrigen": 5, "idCliente": 5,"created_by":5}
         ]
         for pedido in pedidos_ejemplo:
             create_pedido(pedido["direccion_entrega"], pedido["estado"], pedido["fecha estimada entrega"],pedido["idSOrigen"],pedido["idCliente"],pedido["created_by"])
    # Insertar 5 transferencias de pedido de ejemplo
         transferencias_ejemplo = [
        {"id_pedido": 1, "id_sucursal_origen": 1, "id_sucursal_destino": 2},
        {"id_pedido": 2, "id_sucursal_origen": 2, "id_sucursal_destino": 3},
        {"id_pedido": 3, "id_sucursal_origen": 3, "id_sucursal_destino": 4},
        {"id_pedido": 4, "id_sucursal_origen": 4, "id_sucursal_destino": 5},
        {"id_pedido": 5, "id_sucursal_origen": 5, "id_sucursal_destino": 1},
    ]
         for transferencia in transferencias_ejemplo:
                transferir_pedido(transferencia["id_pedido"], transferencia["id_sucursal_origen"], transferencia["id_sucursal_destino"])
 # aolo insertar una vez sino bug


insertar_datos_ejemplo1()
insertar_datos_ejemplo2()

def show_menu():
    """Muestra el menú de opciones."""
    print("\n--- Menú Principal ---")
    print("1. Gestión de Pedidos")
    print("2. Gestión de Clientes")
    print("3. Gestión de Empleados")
    print("4. Gestión de Sucursales")
    print("5. Transferir Pedido")
    print("6. Salir")


def main():
    """Función principal que muestra el menú y gestiona la interacción del usuario."""
    while True:
        show_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            print("\n--- Gestión de Pedidos ---")
            print("1. Ver pedidos")
            print("2. Crear pedido")
            print("3. Actualizar pedido")
            print("4. Eliminar pedido")
            sub_opcion = input("Seleccione una opción (1-4): ")
            if sub_opcion == '1':
                read_pedidos()
            elif sub_opcion == '2':
                # Solicitar datos para la creación de un pedido
                direccion_entrega = input("Ingrese la dirección de entrega: ")
                estado = input("Ingrese el estado del pedido: ")
                fecha_estimadada_entrega = input("Ingrese la fecha estimada de entrega (YYYY-MM-DD): ")
                fecha_creacion = input("Ingrese la fecha de creación (YYYY-MM-DD): ")
                id_sucursal_origen = input("Ingrese el ID de la sucursal de origen: ")
                id_cliente = input("Ingrese el ID del cliente: ")
                created_by = input("Ingrese el nombre del creador: ")
                create_pedido(direccion_entrega, estado, fecha_estimadada_entrega, fecha_creacion, id_sucursal_origen, id_cliente, created_by)
            elif sub_opcion == '3':
                # Solicitar el ID y los datos para actualizar un pedido
                id_pedido = input("Ingrese el ID del pedido a actualizar: ")
                direccion_entrega = input("Ingrese la nueva dirección de entrega: ")
                estado = input("Ingrese el nuevo estado del pedido: ")
                fecha_estimadada_entrega = input("Ingrese la nueva fecha estimada de entrega (YYYY-MM-DD): ")
                fecha_creacion = input("Ingrese la nueva fecha de creación (YYYY-MM-DD): ")
                id_sucursal_origen = input("Ingrese el nuevo ID de la sucursal de origen: ")
                id_cliente = input("Ingrese el nuevo ID del cliente: ")
                created_by = input("Ingrese el nuevo nombre del creador: ")
                update_pedido(id_pedido, direccion_entrega, estado, fecha_estimadada_entrega, fecha_creacion, id_sucursal_origen, id_cliente, created_by)
            elif sub_opcion == '4':
                # Solicitar el ID del pedido a eliminar
                id_pedido = input("Ingrese el ID del pedido a eliminar: ")
                delete_pedido(id_pedido)
            else:
                print("Opción inválida.")
        
        elif opcion == '2':
            print("\n--- Gestión de Clientes ---")
            print("1. Ver clientes")
            print("2. Crear cliente")
            print("3. Actualizar cliente")
            print("4. Eliminar cliente")
            sub_opcion = input("Seleccione una opción (1-4): ")
            if sub_opcion == '1':
                read_clientes()
            elif sub_opcion == '2':
                # Solicitar datos para la creación de un cliente
                nombre = input("Ingrese el nombre del cliente: ")
                direccion = input("Ingrese la dirección del cliente: ")
                telefono = input("Ingrese el teléfono del cliente: ")
                email = input("Ingrese el email del cliente: ")
                create_cliente(nombre, direccion, telefono, email)
            elif sub_opcion == '3':
                # Solicitar el ID y los datos para actualizar un cliente
                id_cliente = input("Ingrese el ID del cliente a actualizar: ")
                nombre = input("Ingrese el nuevo nombre del cliente: ")
                direccion = input("Ingrese la nueva dirección del cliente: ")
                telefono = input("Ingrese el nuevo teléfono del cliente: ")
                email = input("Ingrese el nuevo email del cliente: ")
                update_cliente(id_cliente, nombre, direccion, telefono, email)
            elif sub_opcion == '4':
                # Solicitar el ID del cliente a eliminar
                id_cliente = input("Ingrese el ID del cliente a eliminar: ")
                delete_cliente(id_cliente)
            else:
                print("Opción inválida.")
        
        elif opcion == '3':
            print("\n--- Gestión de Empleados ---")
            print("1. Ver empleados")
            print("2. Crear empleado")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            sub_opcion = input("Seleccione una opción (1-4): ")
            if sub_opcion == '1':
                read_empleados()
            elif sub_opcion == '2':
                # Solicitar datos para la creación de un empleado
                nombre = input("Ingrese el nombre del empleado: ")
                cargo = input("Ingrese el cargo del empleado: ")
                salario = input("Ingrese el salario del empleado: ")
                id_sucursal = input("Ingrese el ID de la sucursal: ")
                create_empleado(nombre, cargo, salario, id_sucursal)
            elif sub_opcion == '3':
                # Solicitar el ID y los datos para actualizar un empleado
                id_empleado = input("Ingrese el ID del empleado a actualizar: ")
                nombre = input("Ingrese el nuevo nombre del empleado: ")
                cargo = input("Ingrese el nuevo cargo del empleado: ")
                salario = input("Ingrese el nuevo salario del empleado: ")
                id_sucursal = input("Ingrese el nuevo ID de la sucursal: ")
                update_empleado(id_empleado, nombre, cargo, salario, id_sucursal)
            elif sub_opcion == '4':
                # Solicitar el ID del empleado a eliminar
                id_empleado = input("Ingrese el ID del empleado a eliminar: ")
                delete_empleado(id_empleado)
            else:
                print("Opción inválida.")
        
        elif opcion == '4':
            print("\n--- Gestión de Sucursales ---")
            print("1. Ver sucursales")
            print("2. Crear sucursal")
            print("3. Actualizar sucursal")
            print("4. Eliminar sucursal")
            sub_opcion = input("Seleccione una opción (1-4): ")
            if sub_opcion == '1':
                read_sucursal()
            elif sub_opcion == '2':
                # Solicitar datos para la creación de una sucursal
                nombre = input("Ingrese el nombre de la sucursal: ")
                direccion = input("Ingrese la dirección de la sucursal: ")
                telefono = input("Ingrese el teléfono de la sucursal: ")
                create_sucursal(nombre, direccion, telefono)
            elif sub_opcion == '3':
                # Solicitar el ID y los datos para actualizar una sucursal
                id_sucursal = input("Ingrese el ID de la sucursal a actualizar: ")
                nombre = input("Ingrese el nuevo nombre de la sucursal: ")
                direccion = input("Ingrese la nueva dirección de la sucursal: ")
                telefono = input("Ingrese el nuevo teléfono de la sucursal: ")
                update_sucursal(id_sucursal, nombre, direccion, telefono)
            elif sub_opcion == '4':
                # Solicitar el ID de la sucursal a eliminar
                id_sucursal = input("Ingrese el ID de la sucursal a eliminar: ")
                delete_sucursal(id_sucursal)
            else:
                print("Opción inválida.")
        
        elif opcion == '5':
            print("\n--- Transferencia de Pedido ---")
            # Solicitar datos para la transferencia de un pedido
            id_pedido = input("Ingrese el ID del pedido a transferir: ")
            id_sucursal_origen = input("Ingrese el ID de la sucursal de origen: ")
            id_sucursal_destino = input("Ingrese el ID de la sucursal destino: ")
            transferir_pedido(id_pedido, id_sucursal_origen, id_sucursal_destino)
        
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    main()