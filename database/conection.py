import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",  # Cambia esto por tu usuario
            password="LamineYamal728",  # Cambia esto por tu contraseña
            database="bizaCourier",
            port=3307  # Especifica el puerto aquí
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Conexión cerrada")
create_connection()