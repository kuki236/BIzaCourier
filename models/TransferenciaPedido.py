from database.conection import create_connection
from mysql.connector import Error


def transferir_pedido(id_pedido, id_sucursal_origen, id_sucursal_destino):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO TransferenciaPedido (idPedido, idSucursalOrigen, idSucursalDestino) "
            "VALUES (%s, %s, %s)",
            (id_pedido, id_sucursal_origen, id_sucursal_destino)
        )
        conn.commit()
        print("Pedido transferido exitosamente.")
    except Exception as e:
        print(f"Error al transferir el pedido: {e}")
    finally:
        cursor.close()
        conn.close()