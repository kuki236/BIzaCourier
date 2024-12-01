from database.conection import create_connection
from mysql.connector import Error

def create_pedido(direccion_entrega, estado, fecha_estimadada_entrega, fecha_creacion, id_sucursal_origen, id_cliente, created_by):
    """Crea un nuevo pedido en la base de datos con validación de claves foráneas."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            # Verificar que la sucursal y el cliente existen
            cursor.execute("SELECT idSucursal FROM Sucursal WHERE idSucursal = %s", (id_sucursal_origen,))
            if not cursor.fetchone():
                print("Error: La sucursal especificada no existe.")
                return

            cursor.execute("SELECT idCliente FROM Cliente WHERE idCliente = %s", (id_cliente,))
            if not cursor.fetchone():
                print("Error: El cliente especificado no existe.")
                return

            # Insertar el pedido
            query = """
            INSERT INTO Pedido (direccion_entrega, estado, fecha_estimadada_entrega, fecha_creacion, idSucursalOrigen, idCliente, created_by)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (direccion_entrega, estado, fecha_estimadada_entrega, fecha_creacion, id_sucursal_origen, id_cliente, created_by))
            connection.commit()
            print("Pedido creado con éxito.")
        except Error as e:
            print("Error al crear el pedido:", e)
        finally:
            cursor.close()
            connection.close()
def read_pedidos():
    """Obtiene todos los pedidos con los nombres de la sucursal y del cliente."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            # Usamos LEFT JOIN para obtener los nombres de la sucursal y del cliente
            query = """
            SELECT 
                p.idPedido,
                p.direccion_entrega,
                p.estado,
                p.fecha_estimadada_entrega,
                p.fecha_creacion,
                p.idSucursalOrigen,
                s.nombre AS nombre_sucursal,
                p.idCliente,
                c.nombre_Cliente AS nombre_cliente,
                p.created_by
            FROM 
                Pedido p
            LEFT JOIN 
                Sucursal s ON p.idSucursalOrigen = s.idSucursal
            LEFT JOIN 
                Cliente c ON p.idCliente = c.idCliente
            """
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print("Error al leer los pedidos:", e)
        finally:
            cursor.close()
            connection.close()

def update_pedido(id_pedido, direccion_entrega, estado, fecha_estimadada_entrega, fecha_creacion, id_sucursal_origen, id_cliente, created_by):
    """Actualiza la información de un pedido existente."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = """
            UPDATE Pedido
            SET direccion_entrega = %s, estado = %s, fecha_estimadada_entrega = %s, fecha_creacion = %s, idSucursalOrigen = %s, idCliente = %s, created_by = %s
            WHERE idPedido = %s
            """
            cursor.execute(query, (direccion_entrega, estado, fecha_estimadada_entrega, fecha_creacion, id_sucursal_origen, id_cliente, created_by, id_pedido))
            connection.commit()
            print("Pedido actualizado con éxito.")
        except Error as e:
            print("Error al actualizar el pedido:", e)
        finally:
            cursor.close()
            connection.close()

def delete_pedido(id_pedido):
    """Elimina un pedido de la base de datos."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = "DELETE FROM Pedido WHERE idPedido = %s"
            cursor.execute(query, (id_pedido,))
            connection.commit()
            print("Pedido eliminado con éxito.")
        except Error as e:
            print("Error al eliminar el pedido:", e)
        finally:
            cursor.close()
            connection.close()