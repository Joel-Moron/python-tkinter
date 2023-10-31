import tkinter as tk

# Función para manejar el evento del botón "Enviar"
def enviar():
    nombre = nombre_entry.get()
    print("Nombre ingresado:", nombre)

# Crear una instancia de Tk
root = tk.Tk()

# Obtener la resolución de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular el ancho y alto de la ventana
window_width = 400  # Ancho de la ventana en píxeles
window_height = 300  # Alto de la ventana en píxeles

# Calcular las coordenadas X e Y para centrar la ventana
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Configurar la geometría de la ventana para centrarla
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Etiqueta
label = tk.Label(root, text="Nombre:")
label.grid(row=0, column=0)

# Campo de entrada
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1)

# Botón "Enviar"
enviar_button = tk.Button(root, text="Enviar", command=enviar)
enviar_button.grid(row=1, column=0, columnspan=2)

# Iniciar el bucle principal
root.mainloop()