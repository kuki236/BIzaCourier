from database.conection import create_connection
from mysql.connector import Error

# Crear Cliente
def create_cliente(nombre_cliente, apellido_cliente, telefono):
    query = "INSERT INTO Cliente (nombre_cliente, apellido_cliente, telefono) VALUES (%s, %s, %s)"
    values = (nombre_cliente, apellido_cliente, telefono)
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        print("Cliente creado correctamente.")
    except Error as e:
        print(f"Error al crear cliente: {e}")
    finally:
        cursor.close()
        conn.close()

# Leer Clientes
def read_clientes():
    query = "SELECT * FROM Cliente"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(cliente)
    except Error as e:
        print(f"Error al leer clientes: {e}")
    finally:
        cursor.close()
        conn.close()

# Actualizar Cliente
def update_cliente(id_cliente, nombre_cliente, apellido_cliente, telefono):
    query = "UPDATE Cliente SET nombre_cliente = %s, apellido_cliente = %s, telefono = %s WHERE idCliente = %s"
    values = (nombre_cliente, apellido_cliente, telefono, id_cliente)
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        print("Cliente actualizado correctamente.")
    except Error as e:
        print(f"Error al actualizar cliente: {e}")
    finally:
        cursor.close()
        conn.close()

# Eliminar Cliente
def delete_cliente(id_cliente):
    query = "DELETE FROM Cliente WHERE idCliente = %s"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, (id_cliente,))
        conn.commit()
        print("Cliente eliminado correctamente.")
    except Error as e:
        print(f"Error al eliminar cliente: {e}")
    finally:
        cursor.close()
        conn.close()