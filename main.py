from models.Pedido import read_pedidos, create_pedido, update_pedido, delete_pedido
from models.Cliente import read_clientes, create_cliente, update_cliente, delete_cliente
from models.ticketEncomienda import create_ticket_encomienda,delete_ticket_encomienda,read_ticket_encomienda,update_ticket_encomienda
from models.Empleado import read_empleados, create_empleado, update_empleado, delete_empleado
from models.Sucursal import read_sucursal, create_sucursal, update_sucursal, delete_sucursal


def show_menu():
    """Muestra el menú de opciones."""
    print("\n--- Menú Principal ---")
    print("1. Gestión de Pedidos")
    print("2. Gestión de Clientes")
    print("3. Gestión de Empleados")
    print("4. Gestión de Sucursales")
    print("5. Transferir Pedido")
    print("6. Salir")

"""""
def main():
    """"""""Función principal que muestra el menú y gestiona la interacción del usuario."""
"""""
    while True:
        show_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            print("\n--- Gestión de Pedidos ---")
            print("1. Ver pedidos")
            print("2. Crear pedido")# Buggggg no debe pedir la sucursal
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
"""