import tkinter as tk
from tkinter import scrolledtext


# Respuestas básicas del chatbot
def responder(mensaje):
    if "hola" in mensaje.lower():
        return "¡Hola! ¿En qué puedo ayudarte?"
    elif "cómo estás" in mensaje.lower():
        return "Estoy funcionando perfectamente, ¿y tú?"
    elif "adiós" in mensaje.lower() or "bye" in mensaje.lower():
        return "¡Adiós! Espero verte pronto."
    else:
        return "Lo siento, no entiendo eso. Intenta con otra pregunta."


# Manejar el envío de mensajes
def enviar_mensaje():
    mensaje = entrada.get()
    if mensaje.strip() == "":
        return

    # Mostrar el mensaje del usuario en el área de chat
    chatbox.insert(tk.END, f"Tú: {mensaje}\n")

    # Obtener y mostrar la respuesta del chatbot
    respuesta = responder(mensaje)
    chatbox.insert(tk.END, f"Chatbot: {respuesta}\n")

    # Limpiar la entrada
    entrada.delete(0, tk.END)


# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Chatbot Simulado")
ventana.geometry("400x500")

# Área de chat (desplazable)
chatbox = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, state="normal", bg="lightyellow", fg="black")
chatbox.place(x=10, y=10, width=380, height=400)

# Entrada de texto
entrada = tk.Entry(ventana, font=("Arial", 14))
entrada.place(x=10, y=420, width=300, height=30)
entrada.bind("<Return>", lambda event: enviar_mensaje())


# Botón para enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje, bg="lightblue", font=("Arial", 12))
boton_enviar.place(x=320, y=420, width=70, height=30)

# Iniciar el loop principal
ventana.mainloop()
