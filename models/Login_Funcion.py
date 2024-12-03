from database.conection import create_connection
from mysql.connector import Error

# Función de autenticación
def autenticar_usuario(username, contrasena):
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM Empleado WHERE username = %s AND contrasena = %s"
        cursor.execute(query, (username, contrasena))
        empleado = cursor.fetchone()

        if empleado:
            return empleado
        else:
            return None

    except Error as e:
        print(f"Error al autenticar usuario: {e}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


# Función principal para manejar el inicio de sesión
def iniciar_sesion():
    """
    Método para manejar la lógica de inicio de sesión.
    """
    usuario = input("Ingrese su nombre de usuario: ").strip()
    contrasena = input("Ingrese su contraseña: ").strip()

    if not usuario or not contrasena:
        print("Por favor, complete todos los campos.")
        return

    empleado = autenticar_usuario(usuario, contrasena)

    if empleado:
        print(f"Bienvenido, {empleado['nombre']} {empleado['apellido']} ({empleado['cargo']})")
        # Aquí puedes realizar otras acciones como redirigir al menú principal.
    else:
        print("Usuario o contraseña incorrectos.")


if __name__ == "__main__":
    iniciar_sesion()
