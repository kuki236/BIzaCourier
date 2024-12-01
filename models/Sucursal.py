from database.conection import create_connection
from mysql.connector import Error
def create_sucursal(nombre, direccion, horario_apertura, horario_cierre):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """INSERT INTO Sucursal (nombre_Sucursal, direccion, horario_apertura, horario_cierre)
                       VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (nombre, direccion, horario_apertura, horario_cierre))
            connection.commit()
            print("Sucursal creada con éxito.")
        except Error as e:
            print(f"Error al crear sucursal: {e}")
        finally:
            cursor.close()
            connection.close()

def read_sucursal():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM Sucursal"
            cursor.execute(query)
            sucursales = cursor.fetchall()
            for sucursal in sucursales:
                print(sucursal)
        except Error as e:
            print(f"Error al leer sucursales: {e}")
        finally:
            cursor.close()
            connection.close()

def update_sucursal(id_sucursal, nombre, direccion, horario_apertura, horario_cierre):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """UPDATE Sucursal
                       SET nombre_Sucursal = %s, direccion = %s, horario_apertura = %s, horario_cierre = %s
                       WHERE idSucursal = %s"""
            cursor.execute(query, (nombre, direccion, horario_apertura, horario_cierre, id_sucursal))
            connection.commit()
            print("Sucursal actualizada con éxito.")
        except Error as e:
            print(f"Error al actualizar sucursal: {e}")
        finally:
            cursor.close()
            connection.close()

def delete_sucursal(id_sucursal):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM Sucursal WHERE idSucursal = %s"
            cursor.execute(query, (id_sucursal,))
            connection.commit()
            print("Sucursal eliminada con éxito.")
        except Error as e:
            print(f"Error al eliminar sucursal: {e}")
        finally:
            cursor.close()
            connection.close()