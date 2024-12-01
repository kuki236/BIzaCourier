from database.conection import create_connection
from mysql.connector import Error
def create_empleado(nombre, cargo, username, contraseña):
    """Crea un nuevo empleado en la base de datos."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO Empleado (nombre, cargo, username, contraseña) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre, cargo, username, contraseña))
            connection.commit()
            print("Empleado creado con éxito.")
        except Error as e:
            print("Error al crear el empleado:", e)
        finally:
            cursor.close()
            connection.close()

def read_empleados():
    """Obtiene todos los empleados de la base de datos."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM Empleado"
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except Error as e:
            print("Error al leer los empleados:", e)
        finally:
            cursor.close()
            connection.close()

def update_empleado(id_empleado, nombre, cargo, username, contraseña):
    """Actualiza la información de un empleado existente."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = """
            UPDATE Empleado
            SET nombre = %s, cargo = %s, username = %s, contraseña = %s
            WHERE idEmpleado = %s
            """
            cursor.execute(query, (nombre, cargo, username, contraseña, id_empleado))
            connection.commit()
            print("Empleado actualizado con éxito.")
        except Error as e:
            print("Error al actualizar el empleado:", e)
        finally:
            cursor.close()
            connection.close()

def delete_empleado(id_empleado):
    """Elimina un empleado de la base de datos."""
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            query = "DELETE FROM Empleado WHERE idEmpleado = %s"
            cursor.execute(query, (id_empleado,))
            connection.commit()
            print("Empleado eliminado con éxito.")
        except Error as e:
            print("Error al eliminar el empleado:", e)
        finally:
            cursor.close()
            connection.close()