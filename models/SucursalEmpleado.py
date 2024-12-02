from database.conection import create_connection
from mysql.connector import Error

# Validar si un empleado existe
def validar_existencia_empleado(id_empleado):
    query = "SELECT COUNT(*) FROM Empleado WHERE idEmpleado = %s"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, (id_empleado,))
        count = cursor.fetchone()[0]
        return count > 0
    except Error as e:
        print(f"Error al validar empleado: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Validar si una sucursal existe
def validar_existencia_sucursal(id_sucursal):
    query = "SELECT COUNT(*) FROM Sucursal WHERE idSucursal = %s"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query, (id_sucursal,))
        count = cursor.fetchone()[0]
        return count > 0
    except Error as e:
        print(f"Error al validar sucursal: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Asignar un empleado a una sucursal con validación
def asignar_empleado_a_sucursal(id_empleado, id_sucursal):
    if not validar_existencia_empleado(id_empleado):
        print(f"El empleado con ID {id_empleado} no existe.")
        return
    if not validar_existencia_sucursal(id_sucursal):
        print(f"La sucursal con ID {id_sucursal} no existe.")
        return
    
    # Verificar si la relación ya existe
    query_verificar = "SELECT COUNT(*) FROM EmpleadoSucursal WHERE idEmpleado = %s AND idSucursal = %s"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query_verificar, (id_empleado, id_sucursal))
        existe = cursor.fetchone()[0] > 0
        if existe:
            print(f"El empleado con ID {id_empleado} ya está asignado a la sucursal con ID {id_sucursal}.")
            return
    except Error as e:
        print(f"Error al verificar relación existente: {e}")
        return
    finally:
        cursor.close()
        conn.close()

    # Asignar al empleado a la sucursal
    query_asignar = "INSERT INTO EmpleadoSucursal (idEmpleado, idSucursal) VALUES (%s, %s)"
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(query_asignar, (id_empleado, id_sucursal))
        conn.commit()
        print(f"Empleado con ID {id_empleado} asignado a la sucursal con ID {id_sucursal}.")
    except Error as e:
        print(f"Error al asignar empleado a sucursal: {e}")
    finally:
        cursor.close()
        conn.close()
