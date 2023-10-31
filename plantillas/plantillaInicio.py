import tkinter as tk

class InicioView(tk.Frame):
    def __init__(self, parent, mostrar_detalles):
        super().__init__(parent)
        label = tk.Label(self, text="Esta es la vista de inicio")
        label.pack()
        boton = tk.Button(self, text="Mostrar Detalles", command=mostrar_detalles)
        boton.pack()