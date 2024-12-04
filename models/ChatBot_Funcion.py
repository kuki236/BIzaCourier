from database.conection import create_connection
from mysql.connector import Error

def consultar_estado_pedido():
    print("Hola! Soy tu asistente virtual para consultas de pedidos. 😊")
    print("Puedo ayudarte a conocer el estado de tu pedido.")

    while True:
        nombre_pedido = input("\nPor favor, ingresa el *nombre del pedido* que deseas consultar: ").strip()

        if nombre_pedido.lower() == "salir":
            print("Entendido! Si necesitas más ayuda, no dudes en volver. 👋")
            break

        try:
            connection = create_connection()

            query = """
            SELECT 
                p.idPedido, 
                p.nombre AS nombre_pedido,
                p.direccion_entrega, 
                p.codigo_postal_entrega, 
                te.estado_transferencia, 
                te.fecha_estimada_entrega
            FROM 
                bizaCourier.Pedido p
            LEFT JOIN 
                bizaCourier.TicketEncomienda te ON p.idPedido = te.idPedido
            WHERE 
                p.nombre = %s
            """

            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, (nombre_pedido,))
            pedido = cursor.fetchone()

            if pedido:
                print("\n🎉Aquí está la información de tu pedido!")
                print(f"🔹 **ID del Pedido**: {pedido['idPedido']}")
                print(f"🔹 **Nombre del Pedido**: {pedido['nombre_pedido']}")
                print(f"📍 **Dirección de Entrega**: {pedido['direccion_entrega']}")
                print(f"📫 **Código Postal**: {pedido['codigo_postal_entrega']}")
                print(f"📦 **Estado de Transferencia**: {pedido['estado_transferencia'] or 'Pendiente'}")
                print(f"📅 **Fecha Estimada de Entrega**: {pedido['fecha_estimada_entrega'] or 'No calculada'}")
            else:
                print(f" Lo siento, no encontré ningún pedido con el nombre '{nombre_pedido}'. Por favor, verifica y vuelve a intentarlo.")

        except Error as e:
            print(f" Ocurrió un error al consultar el pedido. Detalles: {e}")

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

        # Confirmar si el usuario desea realizar otra consulta
        continuar = input("\n\u00bfQuieres consultar otro pedido? (sí/no): ").strip().lower()
        if continuar != "sí":
            print("Gracias por usar el asistente de pedidos! Que tengas un excelente día! ")
            break

# Ejecución directa del chatbot para la consulta
if __name__ == "__main__":
    consultar_estado_pedido()
