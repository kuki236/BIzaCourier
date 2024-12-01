from database.conection import create_connection
from mysql.connector import Error

def create_cliente(nombre_cliente, telefono, apellido_cliente):
    """Crea un nuevo cliente en la base de datos."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO Cliente (nombre_Cliente,apellido_cliente,telefono) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre_cliente,apellido_cliente,telefono))
            connection.commit()
            print("Cliente creado con éxito.")
        except Error as e:
            print("Error al crear el cliente:", e)
        finally:
            cursor.close()
            connection.close()

def read_clientes():
    """Obtiene todos los clientes de la base de datos."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM Cliente"
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print("Error al leer los clientes:", e)
        finally:
            cursor.close()
            connection.close()

def update_cliente(id_cliente, nombre_cliente, telefono, apellido_cliente):
    """Actualiza la información de un cliente existente."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = """
            UPDATE Cliente
            SET nombre_Cliente = %s, telefono = %s, apellido_cliente = %s
            WHERE idCliente = %s
            """
            cursor.execute(query, (nombre_cliente, telefono, apellido_cliente, id_cliente))
            connection.commit()
            print("Cliente actualizado con éxito.")
        except Error as e:
            print("Error al actualizar el cliente:", e)
        finally:
            cursor.close()
            connection.close()

def delete_cliente(id_cliente):
    """Elimina un cliente de la base de datos."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = "DELETE FROM Cliente WHERE idCliente = %s"
            cursor.execute(query, (id_cliente,))
            connection.commit()
            print("Cliente eliminado con éxito.")
        except Error as e:
            print("Error al eliminar el cliente:", e)
        finally:
            cursor.close()
            connection.close()