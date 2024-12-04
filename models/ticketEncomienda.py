# models/ticketEncomienda.py
from database.conection import create_connection
from mysql.connector import Error
import requests
from math import radians, cos, sin, sqrt, atan2
from datetime import datetime, timedelta
import random
from urllib.parse import quote_plus


def obtener_latitud_longitud(direccion):
    direccion_codificada = quote_plus(direccion)
    url = f'https://nominatim.openstreetmap.org/search?q={direccion_codificada}&format=jsonv2'
    headers = {
        'User-Agent': 'BizaCourier/1.0 (sebasandree729@gmail.com)'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                return float(data[0].get('lat')), float(data[0].get('lon'))
            else:
                return None, None
        except ValueError:
            return None, None
    else:
        return None, None


def calcular_distancia(coord1, coord2):
    R = 6371.0  # Radio de la Tierra en kilómetros
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def calcular_fecha_estimada_entrega(distancia_km):
    horas_por_km = 0.05  # Tiempo base: 20 km/h promedio
    tiempo_base_horas = distancia_km * horas_por_km
    variacion = random.uniform(-0.2, 0.2) * tiempo_base_horas  # Variación de -20% a +20%
    tiempo_total_horas = tiempo_base_horas + variacion
    dias_estimados = tiempo_total_horas / 8  # Jornada de 8 horas
    fecha_estimada = datetime.now() + timedelta(days=dias_estimados)
    return fecha_estimada


def create_ticket_encomienda(estado_transferencia="Creado", idSucursalOrigen=None, idPedido=None, fecha_recepcion=None,
                             fecha_estimada_entrega=None):
    try:
        conn = create_connection()
        if conn.is_connected():
            cursor = conn.cursor()

            # Obtener direccion_entrega del pedido
            cursor.execute("SELECT direccion_entrega FROM bizaCourier.Pedido WHERE idPedido = %s", (idPedido,))
            direccion_entrega = cursor.fetchone()
            if not direccion_entrega:
                print(f"No se encontró el pedido con ID: {idPedido}")
                return
            direccion_entrega = direccion_entrega[0]

            # Obtener latitud y longitud de la direccion_entrega
            coord_entrega = obtener_latitud_longitud(direccion_entrega)
            if not coord_entrega[0]:
                print("No se pudo obtener las coordenadas de la dirección de entrega.")
                return

            # Obtener todas las sucursales y sus direcciones
            cursor.execute("SELECT idSucursal, direccion FROM Sucursal")
            sucursales = cursor.fetchall()
            if not sucursales:
                print("No se encontraron sucursales registradas.")
                return

            # Calcular distancia a cada sucursal
            distancias = []
            for sucursal in sucursales:
                id_sucursal, direccion_sucursal = sucursal
                coord_sucursal = obtener_latitud_longitud(direccion_sucursal)
                if coord_sucursal[0]:
                    distancia = calcular_distancia(coord_entrega, coord_sucursal)
                    distancias.append((distancia, id_sucursal))

            # Obtener la sucursal más cercana
            if distancias:
                distancia_minima, idSucursalDestino = min(distancias, key=lambda x: x[0])

                # Calcular fecha estimada de entrega
                fecha_estimada_entrega = calcular_fecha_estimada_entrega(distancia_minima)

                # Insertar el ticket encomienda
                fecha_inicio = datetime.now()
                query = """
                INSERT INTO bizaCourier.TicketEncomienda (estado_transferencia, fecha_inicio, fecha_recepcion, fecha_estimada_entrega, idSucursalOrigen, idSucursalDestino, idPedido)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(query, (
                estado_transferencia, fecha_inicio, fecha_recepcion, fecha_estimada_entrega, idSucursalOrigen,
                idSucursalDestino, idPedido))
                conn.commit()
                print("TicketEncomienda creado exitosamente.")
    except Error as e:
        print(f"Error al insertar en la base de datos: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def read_ticket_encomienda():
    try:
        conn = create_connection()
        if not conn or not conn.is_connected():
            print("No se pudo establecer una conexión con la base de datos.")
            return []

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
            p.nombre AS nombre_pedido,
            p.direccion_entrega AS direccion_entrega
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
        if not results:
            print("No se encontraron registros en la base de datos.")
            return []

        print("Resultados obtenidos:", results)
        return results

    except Exception as e:
        print(f"Error al leer de la base de datos: {e}")
        return []
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()




def update_ticket_encomienda(idTicketEncomienda, estado_transferencia=None, fecha_recepcion=None,
                             fecha_estimada_entrega=None):
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


def cambiar_estado_transferencia(idTicketEncomienda, nuevo_estado):
    """
    Cambia el estado de transferencia de un TicketEncomienda.
    """
    try:
        conn = create_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            query = """
            UPDATE bizaCourier.TicketEncomienda
            SET estado_transferencia = %s
            WHERE idTicketEncomienda = %s;
            """
            cursor.execute(query, (nuevo_estado, idTicketEncomienda))
            conn.commit()
            print(
                f"Estado de transferencia actualizado exitosamente a '{nuevo_estado}' para TicketEncomienda ID: {idTicketEncomienda}")
    except Error as e:
        print(f"Error al actualizar el estado de transferencia: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
def get_sucursales():
    """
    Devuelve una lista de todas las sucursales registradas en la base de datos.
    """
    try:
        conn = create_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT idSucursal, nombre_sucursal FROM bizaCourier.Sucursal")
            sucursales = cursor.fetchall()
            return sucursales  # Retorna una lista de tuplas (idSucursal, nombre_sucursal)
    except Error as e:
        print(f"Error al obtener las sucursales: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()