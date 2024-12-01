from database.conection import create_connection
from mysql.connector import Error

from database.conection import create_connection
from mysql.connector import Error
from datetime import datetime  

# Create (Insert)
def create_ticket_encomienda(estado_transferencia="Creado", idSucursalOrigen=None, idSucursalDestino=None, idPedido=None, fecha_recepcion=None, fecha_estimada_entrega=None):
    try:
        conn = create_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            # Obtener la fecha y hora actual
            fecha_inicio = datetime.now()
            query = """
            INSERT INTO bizaCourier.TicketEncomienda (estado_transferencia, fecha_inicio, fecha_recepcion, fecha_estimada_entrega, idSucursalOrigen, idSucursalDestino, idPedido)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (estado_transferencia, fecha_inicio, fecha_recepcion, fecha_estimada_entrega, idSucursalOrigen, idSucursalDestino, idPedido))
            conn.commit()
            print("TicketEncomienda creado exitosamente")
    except Error as e:
        print(f"Error al insertar en la base de datos: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
# Read (Select)
def read_ticket_encomienda():
    try:
        conn = create_connection()
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            query = """
            SELECT 
                te.idTicketEncomienda,
                te.estado_transferencia,
                te.fecha_inicio,
                te.fecha_recepcion,
                te.fecha_estimada_entrega,
                so.nombre_sucursal AS nombre_sucursal_origen,
                sd.nombre_sucursal AS nombre_sucursal_destino,
                p.nombre_pedido AS nombre_pedido
            FROM 
                bizaCourier.TicketEncomienda te
            LEFT JOIN 
                bizaCourier.Sucursal so ON te.idSucursalOrigen = so.idSucursal
            LEFT JOIN 
                bizaCourier.Sucursal sd ON te.idSucursalDestino = sd.idSucursal
            LEFT JOIN 
                bizaCourier.Pedido p ON te.idPedido = p.idPedido;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
    except Error as e:
        print(f"Error al leer de la base de datos: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Update (Update)
def update_ticket_encomienda(idTicketEncomienda, estado_transferencia=None, fecha_recepcion=None, fecha_estimada_entrega=None):
    try:
        conn = create_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            update_values = []
            set_clause = []
            
            if estado_transferencia is not None:
                set_clause.append("estado_transferencia = %s")
                update_values.append(estado_transferencia)
            if fecha_recepcion is not None:
                set_clause.append("fecha_recepcion = %s")
                update_values.append(fecha_recepcion)
            if fecha_estimada_entrega is not None:
                set_clause.append("fecha_estimada_entrega = %s")
                update_values.append(fecha_estimada_entrega)

            # Adding the ID condition at the end
            set_clause_str = ", ".join(set_clause)
            query = f"""
            UPDATE bizaCourier.TicketEncomienda
            SET {set_clause_str}
            WHERE idTicketEncomienda = %s;
            """
            update_values.append(idTicketEncomienda)
            cursor.execute(query, tuple(update_values))
            conn.commit()
            print("TicketEncomienda actualizado exitosamente")
    except Error as e:
        print(f"Error al actualizar en la base de datos: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Delete (Delete)
def delete_ticket_encomienda(idTicketEncomienda):
    try:
        conn = create_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            query = """
            DELETE FROM bizaCourier.TicketEncomienda
            WHERE idTicketEncomienda = %s;
            """
            cursor.execute(query, (idTicketEncomienda,))
            conn.commit()
            print("TicketEncomienda eliminado exitosamente")
    except Error as e:
        print(f"Error al eliminar de la base de datos: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
