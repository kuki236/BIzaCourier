from database.conection import create_connection, close_connection

class Sucursal:
    @staticmethod
    def create(nombre, direccion, apertura, cierre):
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """
                    INSERT INTO Sucursal (nombre_Sucursal, direccion, horario_apertura, horario_cierre)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (nombre, direccion, apertura, cierre))
                connection.commit()
                print("Sucursal creada exitosamente")
            except Exception as e:
                print(f"Error al crear sucursal: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def read_all():
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM Sucursal")
                sucursales = cursor.fetchall()
                return sucursales
            except Exception as e:
                print(f"Error al leer sucursales: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def update(id_sucursal, nombre, direccion, apertura, cierre):
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """
                    UPDATE Sucursal
                    SET nombre_Sucursal = %s, direccion = %s, horario_apertura = %s, horario_cierre = %s
                    WHERE idSucursal = %s
                """
                cursor.execute(query, (nombre, direccion, apertura, cierre, id_sucursal))
                connection.commit()
                print("Sucursal actualizada exitosamente")
            except Exception as e:
                print(f"Error al actualizar sucursal: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def delete(id_sucursal):
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM Sucursal WHERE idSucursal = %s"
                cursor.execute(query, (id_sucursal,))
                connection.commit()
                print("Sucursal eliminada exitosamente")
            except Exception as e:
                print(f"Error al eliminar sucursal: {e}")
            finally:
                close_connection(connection)