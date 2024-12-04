from database.conection import create_connection
from mysql.connector import Error
def create_sucursal(nombre_sucursal, direccion, codigo_postal, horario_apertura, horario_cierre):
    query = "INSERT INTO Sucursal (nombre_sucursal, direccion, codigo_postal, horario_apertura, horario_cierre) VALUES (%s, %s, %s, %s, %s)"
    values = (nombre_sucursal, direccion, codigo_postal, horario_apertura, horario_cierre)
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        print("Sucursal creada correctamente.")
    except Error as e:
        print(f"Error al crear sucursal: {e}")
    finally:
        cursor.close()
        conn.close()

def read_sucursales():
    query = "SELECT * FROM Sucursal"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        sucursales = cursor.fetchall()
        return sucursales
    except Error as e:
        print(f"Error al leer sucursales: {e}")
    finally:
        cursor.close()
        conn.close()

def update_sucursal(id_sucursal, nombre_sucursal, direccion, codigo_postal, horario_apertura, horario_cierre):
    query = "UPDATE Sucursal SET nombre_sucursal = %s, direccion = %s, codigo_postal = %s, horario_apertura = %s, horario_cierre = %s WHERE idSucursal = %s"
    values = (nombre_sucursal, direccion, codigo_postal, horario_apertura, horario_cierre, id_sucursal)
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()  # Asegúrate de guardar los cambios
        print("Sucursal actualizada correctamente.")
    except Error as e:
        print(f"Error al actualizar sucursal: {e}")
    finally:
        cursor.close()  # Cierra el cursor
        conn.close()    # Cierra la conexión

def delete_sucursal(id_sucursal):
    query = "DELETE FROM Sucursal WHERE idSucursal = %s"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, (id_sucursal,))
        conn.commit()
        print("Sucursal eliminada con éxito.")
    except Error as e:
        print(f"Error al eliminar sucursal: {e}")
    finally:
        cursor.close()  
        conn.close()   
        # Buscar una sucursal por ID
def buscar_sucursal_por_id(id_sucursal):
    query = "SELECT * FROM Sucursal WHERE idSucursal = %s"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, (id_sucursal,))
        result = cursor.fetchone()
        if result:
            print(f"Sucursal encontrada: {result}")
        else:
            print(f"No se encontró la sucursal con ID: {id_sucursal}")
    except Error as e:
        print(f"Error al buscar la sucursal: {e}")
    finally:
        cursor.close()  
        conn.close()