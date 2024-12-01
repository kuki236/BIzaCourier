from database.conection import create_connection
from mysql.connector import Error
import random
import string
def generate_random_name(length=12):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Crear un pedido
def create_pedido(idPedido, direccion_entrega, codigo_postal_entrega, idCliente, created_by):
    try:
        connection = create_connection()
        nombre = generate_random_name()  # Generar nombre aleatorio
        query = """
        INSERT INTO bizaCourier.Pedido (idPedido, nombre, direccion_entrega, codigo_postal_entrega, idCliente, created_by)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (idPedido, nombre, direccion_entrega, codigo_postal_entrega, idCliente, created_by)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        print(f"Pedido creado correctamente con nombre: {nombre}")
    except Error as e:
        print(f"Error al crear el pedido: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Leer todos los pedidos
def read_pedidos():
    try:
        connection = create_connection()
        query = "SELECT * FROM bizaCourier.Pedido"
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"Error al leer los pedidos: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Actualizar un pedido
def update_pedido(idPedido, direccion_entrega=None, codigo_postal_entrega=None):
    try:
        connection = create_connection()
        query = "UPDATE bizaCourier.Pedido SET "
        values = []
        if direccion_entrega:
            query += "direccion_entrega = %s, "
            values.append(direccion_entrega)
        if codigo_postal_entrega:
            query += "codigo_postal_entrega = %s, "
            values.append(codigo_postal_entrega)
        query = query.rstrip(", ") + " WHERE idPedido = %s"
        values.append(idPedido)
        cursor = connection.cursor()
        cursor.execute(query, tuple(values))
        connection.commit()
        print(f"Pedido {idPedido} actualizado correctamente.")
    except Error as e:
        print(f"Error al actualizar el pedido: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Eliminar un pedido
def delete_pedido(idPedido):
    try:
        connection = create_connection()
        query = "DELETE FROM bizaCourier.Pedido WHERE idPedido = %s"
        cursor = connection.cursor()
        cursor.execute(query, (idPedido,))
        connection.commit()
        print(f"Pedido {idPedido} eliminado correctamente.")
    except Error as e:
        print(f"Error al eliminar el pedido: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
# Buscar un pedido por ID
def buscar_pedido_por_id(idPedido):
    try:
        connection = create_connection()
        query = "SELECT * FROM bizaCourier.Pedido WHERE idPedido = %s"
        cursor = connection.cursor()
        cursor.execute(query, (idPedido,))
        result = cursor.fetchone()
        if result:
            print(f"Pedido encontrado: {result}")
        else:
            print(f"No se encontró el pedido con ID: {idPedido}")
    except Error as e:
        print(f"Error al buscar el pedido: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def buscar_pedido_por_nombre(nombre):
    try:
        connection = create_connection()
        query = "SELECT * FROM bizaCourier.Pedido WHERE nombre = %s"
        cursor = connection.cursor()
        cursor.execute(query, (nombre,))
        result = cursor.fetchone()
        if result:
            print(f"Pedido encontrado: {result}")
        else:
            print(f"No se encontró ningún pedido con el nombre: {nombre}")
    except Error as e:
        print(f"Error al buscar el pedido: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()