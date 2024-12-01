from datetime import datetime

from database.conection import create_connection
from mysql.connector import Error


def transferir_pedido(id_pedido, id_sucursal_origen, id_sucursal_destino):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        fecha_transferencia = datetime.now()

        # Estado de la transferencia (puedes ajustarlo a tus necesidades)
        estado_transferencia = "Pendiente"
        cursor.execute(
            "INSERT INTO TransferenciaPedido (fecha_Transferencia, estado_Transferencia, idPedido, idSucursalOrigen, idSucursalDestino) "
            "VALUES (%s, %s, %s, %s, %s)",
            (fecha_transferencia, estado_transferencia, id_pedido, id_sucursal_origen, id_sucursal_destino)
        )
        conn.commit()
        print("Pedido transferido exitosamente.")
    except Exception as e:
        print(f"Error al transferir el pedido: {e}")
    finally:
        cursor.close()
        conn.close()