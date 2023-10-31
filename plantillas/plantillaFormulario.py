import tkinter as tk

class DetallesView(tk.Frame):
    def __init__(self, parent, mostrar_inicio):
        super().__init__(parent)

        def enviar():
            nombre = nombre_entry.get()
            print("Nombre ingresado:", nombre)

        label = tk.Label(self, text="Nombre:")
        label.grid(row=0, column=0)

        nombre_entry = tk.Entry(self)
        nombre_entry.grid(row=0, column=1)

        enviar_button = tk.Button(self, text="Enviar", command=enviar)
        enviar_button.grid(row=1, column=0, columnspan=2)

        boton = tk.Button(self, text="Volver a Inicio", command=mostrar_inicio)
        boton.grid(row=1, column=2, columnspan=2)