import tkinter as tk

from plantillas.plantillaInicio import InicioView
from plantillas.plantillaFormulario import DetallesView

# Crear una instancia de Tkinter
root = tk.Tk()
root.title("Mi Aplicación Tkinter")

# Resto del código (funciones para cambiar de vista, creación de la ventana principal, etc.)

# Funciones para cambiar de vista
def mostrar_inicio():
    detalles_view.pack_forget()
    inicio_view.pack()

def mostrar_detalles():
    inicio_view.pack_forget()
    detalles_view.pack()

# Crear instancias de las vistas
inicio_view = InicioView(root, mostrar_detalles)
detalles_view = DetallesView(root, mostrar_inicio)

# Mostrar la vista de inicio inicialmente
inicio_view.pack()

# Iniciar el bucle principal
root.mainloop()