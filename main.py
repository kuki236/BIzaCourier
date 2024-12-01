from models.Pedido import read_pedidos, create_pedido, update_pedido, delete_pedido
from models.Cliente import read_clientes, create_cliente, update_cliente, delete_cliente
from models.TransferenciaPedido import transferir_pedido
from models.Empleado import read_empleados, create_empleado, update_empleado, delete_empleado
from models.Sucursal import read_sucursales, create_sucursal, update_sucursal, delete_sucursal


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
                create_pedido()
            elif sub_opcion == '3':
                update_pedido()
            elif sub_opcion == '4':
                delete_pedido()
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
                create_cliente()
            elif sub_opcion == '3':
                update_cliente()
            elif sub_opcion == '4':
                delete_cliente()
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
                create_empleado()
            elif sub_opcion == '3':
                update_empleado()
            elif sub_opcion == '4':
                delete_empleado()
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
                read_sucursales()
            elif sub_opcion == '2':
                create_sucursal()
            elif sub_opcion == '3':
                update_sucursal()
            elif sub_opcion == '4':
                delete_sucursal()
            else:
                print("Opción inválida.")
        
        elif opcion == '5':
            print("\n--- Transferencia de Pedido ---")
            transferir_pedido()
        
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()