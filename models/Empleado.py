from database.conection import create_connection
from mysql.connector import Error
def create_empleado(nombre, apellido, cargo, username, contrasena):
    query = "INSERT INTO Empleado (nombre, apellido, cargo, username, contrase\u00f1a) VALUES (%s, %s, %s, %s, %s)"
    values = (nombre, apellido, cargo, username, contrasena)
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        print("Empleado creado correctamente.")
    except Error as e:
        print(f"Error al crear empleado: {e}")
    finally:
        cursor.close()
        conn.close()

# Leer Empleados
def read_empleados():
    query = "SELECT * FROM Empleado"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        empleados = cursor.fetchall()
        for empleado in empleados:
            print(empleado)
    except Error as e:
        print(f"Error al leer empleados: {e}")
    finally:
        cursor.close()
        conn.close()

# Actualizar Empleado
def update_empleado(id_empleado, nombre, apellido, cargo, username, contrasena):
    query = "UPDATE Empleado SET nombre = %s, apellido = %s, cargo = %s, username = %s, contrase\u00f1a = %s WHERE idEmpleado = %s"
    values = (nombre, apellido, cargo, username, contrasena, id_empleado)
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        print("Empleado actualizado correctamente.")
    except Error as e:
        print(f"Error al actualizar empleado: {e}")
    finally:
        cursor.close()
        conn.close()

# Eliminar Empleado
def delete_empleado(id_empleado):
    query = "DELETE FROM Empleado WHERE idEmpleado = %s"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, (id_empleado,))
        conn.commit()
        print("Empleado eliminado correctamente.")
    except Error as e:
        print(f"Error al eliminar empleado: {e}")
    finally:
        cursor.close()
        conn.close()